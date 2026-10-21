"""AI runner: an AI agent drives the browser through a mission, N times, and compares the runs.

Purpose: the main program. It is the automated, repeatable version of the test.
Used when: to produce real results, one batch per account + mission, written to reports/.
Reads instructions/ (charter, quality definition, test standards) and missions/<id>.md.

How one run works:
  1. Playwright starts a fresh Chromium (new profile = fresh session) and listens for
     console and network errors.
  2. For every mission step, the AI agent (our own small loop on a local Ollama model) does the step and reports what it saw.
  3. The runner takes the outcome screenshot and reads real facts from the page
     (URL, badge, fields, products, error text), so "observed" is never invented.
  4. A second AI call, the "judge", compares those facts against quality-definition.md
     and test-standards.md and writes the checks (pass/fail/unsure) and findings.
After all runs: comparison.md and report.md are written from the step records (plain code, no AI).

Usage:
  .venv/bin/python runner.py --account standard_user --mission core --runs 1
  .venv/bin/python runner.py --account problem_user --mission reset-state
  .venv/bin/python runner.py --account problem_user --mission core --add-run   (one more run, keeps the saved ones)
  .venv/bin/python runner.py --account problem_user --mission core --model claude-haiku-5-5 --parallel   (3 runs at once)

The model is one setting: --model or LLM_MODEL in .env. A name starting with "claude" (e.g. claude-haiku-5-5,
claude-sonnet-5-5) runs through the `claude` command on your Claude plan, no API key; "gemini..." uses Google
(needs GOOGLE_API_KEY); anything else is a local Ollama model (the default is qwen2.5:7b).
  .venv/bin/python runner.py --account standard_user --mission core --runs 1 --first 1   (timing test: step 1 only)
"""
import argparse
import asyncio
import base64
import json
import os
import re
import shutil
import tempfile
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Literal
from urllib.parse import urlparse

os.environ.setdefault("ANONYMIZED_TELEMETRY", "false")  # Browser Use: no usage reporting
os.environ.setdefault("BROWSER_USE_CLOUD_SYNC", "false")

import yaml
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from pydantic import BaseModel

from browser_use import ChatGoogle, ChatOllama
from google import genai
from google.genai import types as genai_types
from ollama import AsyncClient
from browser_use.llm.messages import (ContentPartImageParam, ContentPartTextParam, ImageURL,
                                      SystemMessage, UserMessage)

ROOT = Path(__file__).parent
START_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"
ICON = {"pass": "✅", "fail": "❌", "unsure": "⚠️", "not recorded": "➖"}


# ---------- What the judge must answer (the model is forced into this shape) ----------

class Check(BaseModel):
    quality_ref: str  # e.g. F5, R2, C5
    expected: str
    observed: str
    result: Literal["pass", "fail", "unsure"]


class Finding(BaseModel):
    quality_ref: str
    title: str
    type: Literal["failure", "unexpected", "suspicious"]
    oracle: str
    expected: str
    observed: str
    confidence: Literal["high", "medium", "low"]
    suggested_severity: Literal["blocker", "major", "minor", "observation"]


class StepJudgement(BaseModel):
    checks: list[Check]
    findings: list[Finding]


# ---------- Setup helpers ----------

def make_llm(model):
    """The model for browsing, judge and reviewer. A name starting with "gemini" uses Google (needs GOOGLE_API_KEY in .env);
    anything else is a local Ollama model, which uses the same num_ctx everywhere so Ollama keeps one model loaded."""
    if model and model.startswith("claude"):
        return ClaudeCLI(model)
    if model and model.startswith("gemini"):
        return ChatGoogle(model=model)
    return ChatOllama(model=model or "qwen2.5:7b", timeout=1800, ollama_options={"num_ctx": 8192})


# ---------- Claude through the `claude` command (uses your Claude plan, no API key) ----------

CLAUDE_WORKDIR = tempfile.mkdtemp(prefix="qa-claude-")  # an empty folder, so the command finds no CLAUDE.md or memory to load


async def claude_json(model, system, user, schema, timeout=300):
    """One call to `claude -p` (print mode). The answer is forced into `schema` and returned as a Python dict."""
    command = ["claude", "-p", "--model", model, "--tools", "", "--no-session-persistence", "--disable-slash-commands",
               "--system-prompt", system, "--output-format", "json", "--json-schema", json.dumps(schema)]
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}  # a key here would bill the API, not your plan
    process = await asyncio.create_subprocess_exec(
        *command, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
        cwd=CLAUDE_WORKDIR, env=env)
    try:
        out, err = await asyncio.wait_for(process.communicate(user.encode()), timeout)  # the prompt goes in through stdin
    except asyncio.TimeoutError:
        process.kill()
        raise RuntimeError(f"claude did not answer within {timeout}s")
    if process.returncode != 0:
        raise RuntimeError(f"claude failed: {short_error(err.decode() or out.decode())}")
    data = json.loads(out)
    if data.get("is_error") or data.get("structured_output") is None:
        raise RuntimeError(f"claude gave no structured answer: {str(data.get('result'))[:200]}")
    return data["structured_output"]


def message_text(message):
    """The text of a browser_use message. Images are skipped: the Claude option is text-only."""
    content = message.content
    if isinstance(content, str):
        return content
    return "\n".join(part.text for part in content if getattr(part, "text", None))


class ClaudeCLI:
    """Looks like the browser_use model objects, so the judge and the reviewer can call it the same way."""

    def __init__(self, model):
        self.model = model

    async def ainvoke(self, messages, output_format):
        system = "\n".join(message_text(m) for m in messages if isinstance(m, SystemMessage))
        user = "\n".join(message_text(m) for m in messages if isinstance(m, UserMessage))
        data = await claude_json(self.model, system, user, output_format.model_json_schema())
        return SimpleNamespace(completion=output_format.model_validate(data))


def load_mission(mission_id):
    """Returns the mission text, its numbered steps, and the optional free-exploration section."""
    path = ROOT / "missions" / f"{mission_id}.md"
    if not path.exists():
        raise SystemExit(f"No mission file {path}")
    text = path.read_text()
    steps_section = text.split("## Steps", 1)[1].split("\n## ", 1)[0]
    steps = [m.group(1).strip() for m in re.finditer(r"^\d+\.\s+(.*)$", steps_section, re.M)]
    explore = None
    if "## Free exploration" in text:
        body = text.split("## Free exploration", 1)[1].split("\n## ", 1)[0].strip()
        budget = re.search(r"Budget:\s*(\d+)", body)
        explore = {"budget": int(budget.group(1)) if budget else 12, "ideas": body}
    return text, steps, explore


def url_path(url):
    p = urlparse(url or "").path
    return p if p else None


# Facts the runner reads from the page itself after every step (SauceDemo selectors).
PAGE_FACTS_JS = """() => {
  const visible = el => !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
  const inputs = {};
  document.querySelectorAll('input').forEach(i => {
    if (visible(i) && i.type !== 'hidden' && i.type !== 'submit')
      inputs[i.id || i.name || i.placeholder] = i.type === 'password' ? '(hidden)' : i.value;
  });
  const badge = document.querySelector('.shopping_cart_badge');
  const error = document.querySelector('[data-test="error"]');
  const items = [...document.querySelectorAll('.inventory_item, .cart_item')].map(el => ({
    name: el.querySelector('.inventory_item_name')?.innerText,
    price: el.querySelector('.inventory_item_price')?.innerText,
    button: el.querySelector('button')?.innerText,
    image: el.querySelector('img')?.getAttribute('src'),
  }));
  return {url: location.href, cart_badge: badge ? badge.innerText : null,
          error_message: error ? error.innerText : null, inputs, items,
          visible_text: document.body.innerText.slice(0, 3000)};
}"""


def active_page(context):
    """The tab the agent is working in: the last open tab showing a web page."""
    pages = [p for p in context.pages if not p.is_closed()]
    web = [p for p in pages if p.url.startswith("http")]
    return (web or pages)[-1]


def short_error(e):
    return (str(e).strip().splitlines() or [repr(e)])[0][:300]


# ---------- One run ----------

async def judge_step(llm, use_vision, docs, mission_text, n, step_text, agent_report, facts, console, network, shot):
    """The judge: compares real page facts against the quality definition."""
    system = (
        "You are the QA judge. You compare FACTS read from a web page against the expectations below. "
        "Rules: use only the facts given (page facts, console, network, agent report). The agent report can be "
        "wrong; when it disagrees with the page facts, trust the page facts and note it. If the facts do not show "
        "something, the result is 'unsure'. Never guess. Write one check per expectation this step touches "
        "(the refs in brackets in the step, plus C5 for console/network, plus C1/C4 if you notice something). "
        "Judge each expectation from the page facts that concern it. Do NOT write a C5 check (console and network): the runner does that. "
        "Only use expectation refs that the mission lists. "
        "Findings only for failed checks or things that look wrong. Rules in test-standards.md override your judgement.\n\n"
        + docs)
    text = (
        f"MISSION:\n{mission_text}\n\nSTEP {n}: {step_text}\n\n"
        f"AGENT REPORT (what the browsing agent says it did and saw):\n{agent_report}\n\n"
        f"PAGE FACTS (read by the runner after the step, reliable):\n{json.dumps(facts, indent=1, ensure_ascii=False)}\n\n"
        f"CONSOLE ENTRIES DURING THIS STEP: {console or 'none'}\n"
        f"FAILED NETWORK REQUESTS DURING THIS STEP: {network or 'none'}\n")
    content = [ContentPartTextParam(text=text)]
    if use_vision:
        data = base64.b64encode(shot.read_bytes()).decode()
        content.append(ContentPartImageParam(image_url=ImageURL(url=f"data:image/png;base64,{data}", media_type="image/png")))
    response = await llm.ainvoke([SystemMessage(content=system), UserMessage(content=content)],
                                 output_format=StepJudgement)
    return response.completion


# ---------- The browsing agent: a small loop of our own ----------
# Browser Use sends very long prompts, and a 7B model on a CPU got lost in them (it never typed the login).
# Here the model gets a short numbered list of the clickable things on the page and picks ONE action per turn.

class Action(BaseModel):
    thought: str  # one short sentence: why this action
    action: Literal["click", "type", "select", "goto", "back", "wait", "done"]
    id: int | None = None      # element number from the page list (click, type, select)
    text: str | None = None    # text to type, option to select, or URL for goto
    report: str | None = None  # only for done: the factual report


AGENT_SYSTEM = (
    "You are a QA tester controlling a web browser on saucedemo.com. Each turn you see the current page as a numbered list "
    "of elements and you answer with exactly ONE action as JSON.\n"
    "Actions: click (id), type (id, text: types into an input), select (id, text: option label), goto (text: a saucedemo.com URL), "
    "back, wait, done (report).\n"
    "Rules: Do only the task and click nothing that is not part of it (no footer, social or menu links unless the task needs them). "
    "click, type and select ALWAYS need an id from the Elements list. "
    "As soon as the page shows that the task is complete, use done right away. Use the element numbers from the CURRENT PAGE list; numbers change on every page. "
    "To fill a form, use one type action per field, then click the button. Read results from the page, not from your own actions: "
    "an action only happened if ACTIONS SO FAR says ok. Never claim something you did not see on the page. "
    "When the task is finished, or you are blocked, use done and put a short factual report in report: what you did and what you saw "
    "(exact texts, numbers, field values, button labels). If something looks wrong or you are unsure, say so.")

OBSERVE_JS = """() => {
  document.querySelectorAll('[data-qa-id]').forEach(e => e.removeAttribute('data-qa-id'));
  const shown = el => {
    const r = el.getBoundingClientRect(), s = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && r.right > 0 && r.left < innerWidth;
  };
  const clean = (t, n = 60) => (t || '').replace(/\\s+/g, ' ').trim().slice(0, n);
  const out = [];
  document.querySelectorAll('a[href], button, input:not([type=hidden]), select, textarea, [role=button]').forEach(el => {
    if (!shown(el) || out.length >= 45) return;
    const tag = el.tagName.toLowerCase(), type = el.type || '';
    const isField = tag === 'textarea' || (tag === 'input' && !['submit', 'button'].includes(type));
    const label = isField ? clean(el.placeholder || el.getAttribute('aria-label') || el.name || el.id)
      : clean(el.innerText || el.getAttribute('aria-label') || el.value || el.querySelector('img')?.alt || el.id);
    const item = el.closest('.inventory_item, .cart_item');
    const id = out.length + 1;
    el.setAttribute('data-qa-id', id);
    out.push({id, kind: tag === 'input' ? 'input:' + (type || 'text') : tag, label,
              item: item ? clean(item.querySelector('.inventory_item_name')?.innerText) : '',
              value: (isField || tag === 'select') ? (type === 'password' ? (el.value ? '(filled)' : '') : clean(el.value)) : null});
  });
  const error = document.querySelector('[data-test="error"]'), badge = document.querySelector('.shopping_cart_badge');
  return {url: location.href, elements: out, error: error ? clean(error.innerText, 200) : null,
          badge: badge ? clean(badge.innerText) : null, text: clean(document.body.innerText, 700)};
}"""


def format_observation(obs):
    lines = [f"URL: {obs['url']}", f"Cart badge: {obs['badge'] or 'none'}"]
    if obs["error"]:
        lines.append(f"Error message shown: {obs['error']}")
    lines.append(f"Page text: {obs['text']}")
    lines.append("Elements:")
    for e in obs["elements"]:
        item = f" (item: {e['item']})" if e["item"] else ""
        value = f' value="{e["value"]}"' if e["value"] is not None else ""
        lines.append(f'[{e["id"]}] {e["kind"]} "{e["label"]}"{item}{value}')
    return "\n".join(lines)


def make_client(model):
    """The raw client the browsing loop talks to: Google for gemini* models, otherwise local Ollama.
    Claude needs no client object: each call starts the `claude` command."""
    if model and model.startswith("claude"):
        return None
    if model and model.startswith("gemini"):
        return genai.Client()  # reads GOOGLE_API_KEY from the environment
    return AsyncClient(timeout=1800)


async def ask_action(client, model, system, user, temperature):
    """Sends one turn to the model and returns its answer as JSON text in the Action format."""
    if model.startswith("claude"):  # no temperature setting here: the command does not offer one
        return json.dumps(await claude_json(model, system, user, Action.model_json_schema()))
    if model.startswith("gemini"):
        resp = await client.aio.models.generate_content(
            model=model, contents=user,
            config=genai_types.GenerateContentConfig(system_instruction=system, temperature=temperature,
                                                     response_mime_type="application/json", response_schema=Action))
        return resp.text
    resp = await client.chat(model=model, messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                             format=Action.model_json_schema(), keep_alive="30m",
                             options={"temperature": temperature, "num_ctx": 8192})
    return resp.message.content


async def agent_loop(page, client, model, task, budget, temperature):
    """One mission step. Returns done / report / errors / urls / actions / log."""
    result = {"done": False, "report": "", "errors": [], "urls": [], "actions": [], "log": []}
    history, bad_answers = [], 0
    for turn in range(1, budget + 1):
        try:
            obs = await page.evaluate(OBSERVE_JS)
        except Exception as e:
            result["errors"].append(f"could not read the page: {short_error(e)}")
            await asyncio.sleep(1)
            continue
        recent = history[-8:]
        warning = ""
        if len(history) >= 3 and len({h["sig"] for h in history[-3:]}) == 1:
            warning = ("\nWARNING: you repeated the same action 3 times. Do something different, or use done and "
                       "report that you are blocked.\n")
        user = (f"TASK:\n{task}\n\nACTIONS SO FAR:\n{chr(10).join(h['line'] for h in recent) or '(none yet)'}\n\n"
                f"CURRENT PAGE:\n{format_observation(obs)}\n{warning}\nYour next action (turn {turn} of {budget}):")
        try:
            act = Action.model_validate_json(await ask_action(client, model, AGENT_SYSTEM, user, temperature))
        except Exception as e:
            bad_answers += 1
            result["errors"].append(f"unusable model answer: {short_error(e)}")
            history.append({"sig": "bad", "line": f"{turn}. (your answer was not valid JSON for the action format)"})
            if bad_answers >= 3:
                break
            continue

        if act.action == "done":
            result["done"], result["report"] = True, (act.report or act.thought)
            result["actions"].append("done")
            break

        label = next((e["label"] for e in obs["elements"] if e["id"] == act.id), "?")
        sel, outcome = f'[data-qa-id="{act.id}"]', "ok"
        try:
            if act.action in ("click", "type", "select") and act.id is None:
                raise ValueError("this action needs an id")
            if act.action == "click":
                await page.click(sel, timeout=5000)
            elif act.action == "type":
                await page.fill(sel, act.text or "", timeout=5000)
            elif act.action == "select":
                await page.select_option(sel, label=act.text, timeout=5000)
            elif act.action == "goto":
                if not (act.text or "").startswith("https://www.saucedemo.com"):
                    raise ValueError("only https://www.saucedemo.com URLs are allowed")
                await page.goto(act.text)
            elif act.action == "back":
                await page.go_back()
            elif act.action == "wait":
                await asyncio.sleep(1)
        except Exception as e:
            outcome = f"ERROR: {short_error(e)}"
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
        except Exception:
            pass
        await asyncio.sleep(0.4)
        for other in [p for p in page.context.pages if p is not page]:  # e.g. a footer social link opens a new tab
            outcome += f" (it opened another tab, {other.url}; the runner closed it)"
            await other.close()
        target = f' [{act.id}] "{label}"' if act.id is not None else ""
        typed = f' text="{act.text}"' if act.text else ""
        line = f"{turn}. {act.action}{target}{typed} -> {outcome}; now at {urlparse(page.url).path or '/'}"
        history.append({"sig": (act.action, act.id, act.text), "line": line})
        result["log"].append(line)
        result["actions"].append(act.action)
        result["urls"].append(page.url)

    if not result["done"]:
        result["report"] = ("(no final report: the agent ran out of actions or could not continue) Last actions: "
                            + " | ".join(h["line"] for h in history[-4:]))
    return result


async def run_once(run_no, args, llm, run_dir, mission_text, steps, explore, docs):
    steps_dir = run_dir / "steps"
    steps_dir.mkdir(parents=True)
    console_log, network_log, records = [], [], []
    profile = tempfile.mkdtemp(prefix="qa-run-")
    run_start = time.time()

    async with async_playwright() as pw:
        context = await pw.chromium.launch_persistent_context(
            profile, headless=not args.headed, viewport={"width": 1280, "height": 900})
        context.on("console", lambda m: console_log.append(f"[{m.type}] {m.text}") if m.type in ("error", "warning") else None)
        context.on("weberror", lambda e: console_log.append(f"[pageerror] {e.error}"))
        context.on("requestfailed", lambda r: network_log.append(f"FAILED {r.method} {r.url} ({r.failure})"))
        context.on("response", lambda r: network_log.append(f"{r.status} {r.request.method} {r.url}") if r.status >= 400 else None)
        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto(START_URL)

        model = args.model or "qwen2.5:7b"
        client = make_client(model)

        for n, step_text in enumerate(steps, start=1):
            is_explore = bool(explore) and n == len(steps)
            budget = explore["budget"] if is_explore else args.max_agent_steps
            print(f"  Run {run_no}, step {n}/{len(steps)}: {step_text[:70]}...", flush=True)
            c0, n0, t0 = len(console_log), len(network_log), time.time()
            home = f"Account: {args.account}, password: {PASSWORD}. The browser is already open on saucedemo.com (log in first if you are on the login page).\n"
            if is_explore:
                task = (home + f"FREE EXPLORATION. You have at most {budget} actions.\nMission theme and ideas:\n{explore['ideas']}\n\n"
                        "The numbered mission steps are already done. Now try OTHER things inside this theme that those steps did not "
                        "cover. Choose what to try yourself. When you finish (use done before you run out of actions), put every attempt "
                        "in the report as its own line starting with 'PATH: ' followed by what you did and exactly what you saw. "
                        "Quote real texts, numbers and labels. Do not invent anything.")
            else:
                task = (home + f"Mission step {n} of {len(steps)}. Do ONLY this step:\n{step_text}\n\n"
                        "Do not do later steps. When the step is done, or you are blocked, use done with a short factual report.")
            page = active_page(context)
            res = await agent_loop(page, client, model, task, budget, 0.8 if is_explore else 0.2)
            agent_done, agent_report, agent_errors = res["done"], res["report"], res["errors"]
            agent_urls, agent_actions = res["urls"], res["actions"]
            print(f"    run {run_no}, step {n}: agent made {len(agent_actions)} actions, {'finished' if agent_done else 'did not finish'}", flush=True)

            page = active_page(context)
            try:
                await page.wait_for_load_state(timeout=5000)
            except Exception:
                pass
            await asyncio.sleep(0.5)
            shot = steps_dir / f"S{n:02d}.png"
            await page.screenshot(path=shot)
            try:
                facts = await page.evaluate(PAGE_FACTS_JS)
            except Exception as e:
                facts = {"url": page.url, "error": f"could not read page: {short_error(e)}"}
            new_console, new_network = console_log[c0:], network_log[n0:]

            try:
                verdict = await judge_step(llm, args.vision, docs["judge"], mission_text, n, step_text,
                                           agent_report, facts, new_console, new_network, shot)
                checks = [c.model_dump() for c in verdict.checks]
                findings = [f.model_dump() for f in verdict.findings]
            except Exception as e:
                checks = [{"quality_ref": "-", "expected": "the judge returns checks",
                           "observed": f"judge failed: {short_error(e)}", "result": "unsure"}]
                findings = []
            for c in checks + findings:
                c["quality_ref"] = normalize_ref(c["quality_ref"])
            allowed = allowed_refs(mission_text) - {"C5"}  # keep only expectations this mission is about
            checks = [c for c in checks if c["quality_ref"] in allowed or c["quality_ref"] in ("-", "STEP")]
            findings = [f for f in findings if f["quality_ref"] in allowed]
            checks.append(c5_check(new_console, new_network))
            if not agent_done and not is_explore:  # exploration may simply use up its budget
                checks.append({"quality_ref": "STEP", "expected": "the agent completes the step",
                               "observed": f"agent did not finish. {'; '.join(agent_errors)[:300]}", "result": "fail"})
            for k, f in enumerate(findings, start=1):
                f.update({"id": f"S{n}-{f['quality_ref']}-{k}", "step": n, "evidence": f"steps/S{n:02d}.png",
                          "technical_signal": "console/network entries in this step" if (new_console or new_network) else "none"})

            results = [c["result"] for c in checks]
            step_result = "fail" if "fail" in results else ("unsure" if "unsure" in results or not results else "pass")
            records.append({
                "step": n, "action": step_text, "exploration": is_explore, "agent_finished": agent_done,
                "agent_report": agent_report, "agent_urls": agent_urls, "agent_actions": agent_actions,
                "agent_log": res["log"],
                "paths": (re.findall(r"^\s*PATH:\s*(.+)$", agent_report, re.M) or res["log"]) if is_explore else [],
                "checks": checks, "findings": findings, "screenshot": f"steps/S{n:02d}.png", "page_url": facts.get("url"),
                "console_errors": new_console or "none", "failed_requests": new_network or "none",
                "step_result": step_result, "seconds": round(time.time() - t0),
            })
            print(f"    run {run_no}, step {n}: {step_result.upper()} in {round(time.time() - t0)}s", flush=True)

        await context.close()
    shutil.rmtree(profile, ignore_errors=True)

    blocked = next((r["step"] for r in records if not r["agent_finished"] and not r["exploration"]), None)
    outcome = f"blocked at step {blocked}" if blocked else (
        "completed with issues" if any(r["step_result"] == "fail" for r in records) else "completed")
    run = {"run": run_no, "outcome": outcome, "seconds": round(time.time() - run_start), "records": records}
    write_run_files(run_dir, run, args, console_log, network_log)
    return run


def allowed_refs(mission_text):
    """Expectation refs named on the mission's 'Expectations to check' line, e.g. 'F1–F7' becomes F1..F7."""
    line = next((l for l in mission_text.splitlines() if "Expectations to check" in l), "")
    refs = set(re.findall(r"[A-Z]\d+", line))
    for m in re.finditer(r"([A-Z])(\d+)\s*[–-]\s*[A-Z]?(\d+)", line):
        refs |= {f"{m.group(1)}{i}" for i in range(int(m.group(2)), int(m.group(3)) + 1)}
    return refs


def c5_check(console, network):
    """C5 is mechanical, so code decides it, not the model. Failures on the app's own domain fail; third-party noise is 'unsure'."""
    expected = "No unexpected console errors or failed network requests"
    if not console and not network:
        return {"quality_ref": "C5", "expected": expected, "observed": "0 console entries, 0 failed requests", "result": "pass"}
    hosts = sorted({urlparse(line.split()[2]).netloc for line in network if len(line.split()) > 2})
    first_party = any(h.endswith("saucedemo.com") for h in hosts)
    observed = (f"{len(console)} console entries, {len(network)} failed requests"
                + (f" to {', '.join(hosts)}" if hosts else "")
                + ("" if first_party else " (third-party only, no visible problem by itself)"))
    return {"quality_ref": "C5", "expected": expected, "observed": observed, "result": "fail" if first_party else "unsure"}


def normalize_ref(ref):
    m = re.search(r"[A-Z]+\d*", str(ref).upper())
    return m.group(0) if m else str(ref)


# ---------- AI review: reads each finding and its screenshots, suggests a status ----------

class FindingReview(BaseModel):
    suggested_status: Literal["likely real bug", "likely intended or spec gap", "likely false positive", "needs human"]
    suggested_severity: Literal["blocker", "major", "minor", "observation"]
    screenshot_supports_description: Literal["yes", "no", "unclear"]
    reasoning: str  # 1-3 sentences
    question_for_human: str


REVIEW_SYSTEM = (
    "You review findings written by a QA agent after a test run. For each finding you get the agent's description from "
    "every run where it appeared, how many runs saw it, and the screenshots from those runs when attached. Decide: "
    "(1) does the screenshot show what the description claims; (2) is it likely a real bug, intended behaviour or a gap in "
    "the quality definition, or a false positive (the agent misread something); (3) a suggested severity. "
    "Use only what the description and the screenshots show. If they do not decide it, say 'needs human'. "
    "Behaviour that a normal user account would show too is not a seeded bug. You only SUGGEST: a human decides.\n\n")


async def review_findings(groups, runs, mission_dir, quality_docs, llm, total_runs):
    """Adds g['review'] to every finding group. A failure never stops the report."""
    for g in groups:
        lines, images = [], []
        for run_no, f in g["by_run"].items():
            record = next(r for r in runs if r["run"] == run_no)["records"][f["step"] - 1]
            lines.append(f"Run {run_no}: {f['title']}. type={f['type']}, confidence={f['confidence']}. "
                         f"Expected: {f['expected']}. Observed: {f['observed']}. "
                         f"Agent report for the step: {str(record['agent_report'])[:600]}")
            shot = mission_dir / f"run-{run_no}" / f["evidence"]
            if shot.exists() and len(images) < 3:
                images.append(shot)
        text = (f"Finding at step {g['step']}, expectation {g['ref']}. Seen in {g['seen']} of {total_runs} run(s) "
                f"({g['label']}).\n" + "\n".join(lines))
        for with_images in (True, False):  # a text-only model cannot take images: retry without them
            content = [ContentPartTextParam(text=text)]
            if with_images:
                for shot in images:
                    data = base64.b64encode(shot.read_bytes()).decode()
                    content.append(ContentPartImageParam(image_url=ImageURL(url=f"data:image/png;base64,{data}", media_type="image/png")))
            try:
                response = await llm.ainvoke([SystemMessage(content=REVIEW_SYSTEM + quality_docs), UserMessage(content=content)],
                                             output_format=FindingReview)
                g["review"] = response.completion.model_dump()
                g["review"]["saw_images"] = with_images and bool(images)
                break
            except Exception as e:
                g["review"] = {"error": short_error(e)}


def review_line(g):
    r = g.get("review")
    if not r:
        return "not reviewed"
    if "error" in r:
        return f"review failed ({r['error']})"
    return (f"**{r['suggested_status']}** (severity {r['suggested_severity']}, screenshot supports description: "
            f"{r['screenshot_supports_description']}{'' if r['saw_images'] else ', screenshot not seen by the reviewer'}). "
            f"{r['reasoning']}")


# ---------- Writing files ----------

def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def write_run_files(run_dir, run, args, console_log, network_log):
    records = run["records"]
    (run_dir / "console.log").write_text("\n".join(console_log) or "none captured")
    (run_dir / "network.log").write_text("\n".join(network_log) or "none captured")
    (run_dir / "run.yaml").write_text(yaml.safe_dump(run, sort_keys=False, allow_unicode=True, width=120))
    all_findings = [f for r in records for f in r["findings"]]
    (run_dir / "findings.yaml").write_text(
        yaml.safe_dump(all_findings, sort_keys=False, allow_unicode=True, width=120) if all_findings else "[]\n")

    md = ['<a id="top"></a>', f"# Run {run['run']} - {args.account} - mission {args.mission}\n",
          f"Model: `{args.provider} / {args.model or 'default'}` · Outcome: **{run['outcome']}** · "
          f"Duration: {run['seconds']}s · Findings: {len(all_findings)}\n",
          "| Step | Action | Result | Screenshot |", "|---|---|---|---|"]
    for r in records:
        md.append(f"| [{r['step']}](#step-{r['step']}) | {cell(r['action'][:90])} | "
                  f"{ICON[r['step_result']]} {r['step_result']} | [screenshot]({r['screenshot']}) |")
    for r in records:
        md += [f"\n---\n\n<a id=\"step-{r['step']}\"></a>\n## Step {r['step']} {ICON[r['step_result']]}\n",
               f"[↑ back to summary](#top) · jump to [screenshot](#step-{r['step']}-shot)\n",
               f"**Action:** {r['action']}\n", f"**Agent report:** {r['agent_report']}\n",
               f"**Agent actions ({len(r['agent_actions'])}):**\n\n" + "\n".join(f"- {l}" for l in r.get("agent_log", [])) + "\n\n"
               f"**Pages visited:** {', '.join(dict.fromkeys(p for p in map(url_path, r['agent_urls'] + [r['page_url']]) if p)) or 'none'}\n",
               "| Check | Expected | Observed | Result |", "|---|---|---|---|"]
        for c in r["checks"]:
            md.append(f"| {c['quality_ref']} | {cell(c['expected'])} | {cell(c['observed'])} | {ICON[c['result']]} {c['result']} |")
        for f in r["findings"]:
            md.append(f"\n- **Finding {f['id']}** ({f['type']}, {f['suggested_severity']}): {f['title']}. Observed: {f['observed']}")
        if r["console_errors"] != "none" or r["failed_requests"] != "none":
            md.append(f"\nConsole: {r['console_errors']}  \nFailed requests: {r['failed_requests']}")
        md.append(f"\n<a id=\"step-{r['step']}-shot\"></a>**Outcome** - [{r['screenshot']}]({r['screenshot']}) · {r['seconds']}s\n\n"
                  f"![step {r['step']} outcome]({r['screenshot']})")
    (run_dir / "run.md").write_text("\n".join(md) + "\n")


# ---------- Comparing runs (plain code, rules from run-protocol.md) ----------

def check_status(record, ref):
    results = [c["result"] for c in record["checks"] if c["quality_ref"] == ref] if record else []
    if not results:
        return "not recorded"
    return "fail" if "fail" in results else ("unsure" if "unsure" in results else "pass")


def across_runs(statuses):
    if len(statuses) == 1:
        return f"single run: {statuses[0]}"
    if all(s == "pass" for s in statuses):
        return "confirmed pass"
    if all(s == "fail" for s in statuses):
        return "confirmed fail"
    if any(s in ("unsure", "not recorded") for s in statuses):
        return "not verified"
    return "unstable"


def seen_label(seen, total):
    if total == 1:
        return "single run"
    return "reproducible" if seen == total else ("likely" if seen >= 2 else "unconfirmed")


def compare(runs):
    """Check rows: one per (step, quality_ref). Finding groups: matched by step + quality_ref."""
    keys = []
    for run in runs:
        for r in run["records"]:
            for c in r["checks"]:
                if (r["step"], c["quality_ref"]) not in keys:
                    keys.append((r["step"], c["quality_ref"]))
    keys.sort(key=lambda k: k[0])
    rows = []
    for step, ref in keys:
        recs = [next((r for r in run["records"] if r["step"] == step), None) for run in runs]
        statuses = [check_status(rec, ref) for rec in recs]
        first = next(c for rec in recs if rec for c in rec["checks"] if c["quality_ref"] == ref)
        observed = [" / ".join(c["observed"] for c in rec["checks"] if c["quality_ref"] == ref) if rec else "-" for rec in recs]
        rows.append({"step": step, "ref": ref, "expected": first["expected"], "observed": observed,
                     "statuses": statuses, "across": across_runs(statuses)})

    groups = {}
    for run in runs:
        for r in run["records"]:
            for f in r["findings"]:
                groups.setdefault((f["step"], f["quality_ref"]), {}).setdefault(run["run"], f)
    finding_groups = []
    for (step, ref), by_run in sorted(groups.items()):
        first = next(iter(by_run.values()))
        finding_groups.append({"step": step, "ref": ref, "by_run": by_run, "first": first,
                               "seen": len(by_run), "label": seen_label(len(by_run), len(runs))})
    return rows, finding_groups


def coverage(run):
    pages, actions, paths = [], 0, []
    for r in run["records"]:
        for u in r["agent_urls"] + [r["page_url"]]:
            p = url_path(u)
            if p and p not in pages:
                pages.append(p)
        actions += len(r["agent_actions"])
        paths += r["paths"]
    return {"pages": pages, "actions": actions, "paths": paths}


def coverage_markdown(runs):
    """What each run explored. Paths are the AI's own words, so they are listed side by side, not matched."""
    cov = [coverage(run) for run in runs]
    n = len(runs)
    union = list(dict.fromkeys(p for c in cov for p in c["pages"]))
    md = ["| | " + " | ".join(f"Run {run['run']}" for run in runs) + " |", "|---|" + "---|" * n,
          "| Pages (URL paths) visited | " + " | ".join(str(len(c["pages"])) for c in cov) + " |",
          "| Browser actions taken | " + " | ".join(str(c["actions"]) for c in cov) + " |",
          "| Paths tried in free exploration | " + " | ".join(str(len(c["paths"])) for c in cov) + " |"]
    if n > 1:
        md += ["", "**Pages not visited by every run:**\n"]
        partial = [p for p in union if sum(p in c["pages"] for c in cov) < n]
        md += [f"- `{p}`: only in run(s) " + ", ".join(str(runs[i]["run"]) for i, c in enumerate(cov) if p in c["pages"])
               for p in partial] or ["- none, all runs visited the same pages"]
    md += ["", "**Paths each run tried in free exploration** (as reported by the AI; details in `run-<n>/run.md`):\n"]
    for run, c in zip(runs, cov):
        md.append(f"- **Run {run['run']}** ({len(c['paths'])}):")
        md += [f"  - {p}" for p in c["paths"]] or ["  - none reported"]
    return md


def write_comparison(mission_dir, runs, rows):
    n = len(runs)
    md = [f"# Comparison across {n} run(s)\n", "Rules: `run-protocol.md`. One row per step + expectation.\n",
          "| Step | Ref | Expected | " + " | ".join(f"Run {i}" for i in range(1, n + 1)) + " | Across runs |",
          "|---|---|---|" + "---|" * n + "---|"]
    for row in rows:
        md.append(f"| {row['step']} | {row['ref']} | {cell(row['expected'])} | "
                  + " | ".join(f"[{ICON[s]} {s}](run-{i}/steps/S{row['step']:02d}.png)" for i, s in enumerate(row["statuses"], 1))
                  + f" | **{row['across']}** |")
    md += ["\n## Coverage: what each run explored\n"] + coverage_markdown(runs)
    (mission_dir / "comparison.md").write_text("\n".join(md) + "\n")


def write_report(mission_dir, runs, rows, groups, args, mission_text, steps):
    n = len(runs)
    question = {"reproducible": "Bug, or intended?", "likely": "Real? Check the run where it did not appear.",
                "unconfirmed": "Real, or agent error? Evidence attached.", "single run": "Real, or agent error? Only one run."}

    if args.mission == "core":
        f_rows = [r for r in rows if r["ref"].startswith("F")]
        f_fail_runs = [sum(s == "fail" for s in r["statuses"]) for r in f_rows]
        if n > 1 and any(k >= 2 for k in f_fail_runs):
            verdict = "Fail"
        elif n > 1 and f_rows and all(r["across"] == "confirmed pass" for r in f_rows) and all(
                run["outcome"] == "completed" for run in runs):
            verdict = "Pass"
        else:
            verdict = "Inconclusive" + (" (single run: not a real verdict)" if n == 1 else "")
    else:
        verdict = "No verdict (exploration mission: findings only)"

    real_g = [g for g in groups if g["first"]["type"] != "suspicious"]
    count = lambda label: sum(g["label"] == label for g in real_g)
    confirmed_fail = [f"{r['ref']} (step {r['step']})" for r in rows if r["across"] in ("confirmed fail", "single run: fail")]
    not_verified = sum(r["across"] in ("not verified",) or "unsure" in r["statuses"] or "not recorded" in r["statuses"] for r in rows)
    short_lines = [
        f"- **{len(real_g)} finding(s) need a human decision**"
        + (f": {count('reproducible')} reproducible, {count('likely')} likely, {count('unconfirmed')} unconfirmed" if n > 1 else "")
        + (f", {count('single run')} from a single run" if n == 1 and real_g else ""),
        f"- Failing checks: {', '.join(confirmed_fail) or 'none'}",
        f"- {not_verified} of {len(rows)} checks are **not verified** (unsure or not recorded). That is not a pass.",
        "- Observed values come from the page itself. Pass/fail judgements and AI suggestions are marked as such and need a human review.", ""]
    md = [f"# QA Report - SauceDemo - mission `{args.mission}` - `{args.account}` - {time.strftime('%Y-%m-%d')}\n",
          f"> Generated by `runner.py` from {n} AI run(s), model `{args.provider} / {args.model or 'default'}`. "
          "Observed values come from the page; pass/fail judgements come from the AI judge and need human review.\n",
          "## 1. Verdict\n", f"**{verdict}**\n", *short_lines,
          "| | " + " | ".join(f"Run {run['run']}" for run in runs) + " |", "|---|" + "---|" * n,
          "| Outcome | " + " | ".join(run["outcome"] for run in runs) + " |",
          "| Steps passed | " + " | ".join(f"{sum(r['step_result'] == 'pass' for r in run['records'])}/{len(steps)}" for run in runs) + " |",
          "| Findings | " + " | ".join(str(sum(len(r['findings']) for r in run['records'])) for run in runs) + " |",
          "| Duration | " + " | ".join(f"{run['seconds']}s" for run in runs) + " |",
          "\n## 2. Step results - expectations vs. what happened\n",
          "| Step | Ref | Expected | Observed (run 1 / 2 / 3) | " + " | ".join(f"Run {i}" for i in range(1, n + 1)) + " | Across runs | Screenshots |",
          "|---|---|---|---|" + "---|" * n + "---|---|"]
    for row in rows:
        shots = " · ".join(f"[R{i}](run-{i}/steps/S{row['step']:02d}.png)" for i in range(1, n + 1))
        md.append(f"| {row['step']} | {row['ref']} | {cell(row['expected'])} | {cell(' // '.join(row['observed']))} | "
                  + " | ".join(f"{ICON[s]} {s}" for s in row["statuses"]) + f" | **{row['across']}** | {shots} |")

    md += ["\n## 2b. Coverage: what each run explored\n"] + coverage_markdown(runs)
    real = [g for g in groups if g["first"]["type"] != "suspicious"]
    silent = [g for g in groups if g["first"]["type"] == "suspicious"]
    md += ["\n## 3. Needs your decision\n", "| # | Finding | Seen in | AI suggestion | Question for you |", "|---|---|---|---|---|"]
    for i, g in enumerate(real, 1):
        md.append(f"| {i} | S{g['step']} {g['ref']}: {cell(g['first']['title'])} | {g['seen']}/{n} | {cell((g.get('review') or {}).get('suggested_status', 'not reviewed'))} "
                  f"| {cell((g.get('review') or {}).get('question_for_human') or question[g['label']])} |")
    if not real:
        md.append("| - | No findings | | | |")

    sections = [("4. Reproducible findings", "reproducible"), ("5. Likely findings", "likely"),
                ("6. Unconfirmed findings", "unconfirmed"), ("Findings from a single run", "single run")]
    for title, label in sections:
        chosen = [g for g in real if g["label"] == label]
        if label == "single run" and not chosen:
            continue
        md.append(f"\n## {title}\n")
        if not chosen:
            md.append("None.")
        for g in chosen:
            f = g["first"]
            evidence = " · ".join(f"[run {r}](run-{r}/{x['evidence']})" for r, x in g["by_run"].items())
            repro = "\n".join(f"   {i}. {s}" for i, s in enumerate(steps[:g["step"]], 1))
            md += [f"### S{g['step']}-{g['ref']}: {f['title']}",
                   f"- **Step:** {g['step']} · **Expectation:** {g['ref']} · **Suggested severity:** {f['suggested_severity']} · **Confidence:** {f['confidence']}",
                   f"- **Expected:** {f['expected']}", f"- **Observed:** {f['observed']}",
                   f"- **Technical signal:** {f['technical_signal']}", f"- **Evidence:** {evidence}",
                   f"- **AI review (a suggestion, a human decides):** {review_line(g)}",
                   "- **Your decision:** ☐ real bug  ☐ intended / spec gap  ☐ false positive  ☐ needs more info",
                   f"- **Steps to reproduce** (account `{args.account}`):\n{repro}\n"]

    md += ["\n## 7. Silent observations (no error signal)\n", "Not classified as bugs.\n",
           "| Observation | Seen in | Observed |", "|---|---|---|"]
    md += [f"| S{g['step']} {g['ref']}: {cell(g['first']['title'])} | {g['seen']}/{n} | {cell(g['first']['observed'])} |" for g in silent] or ["| None | | |"]
    md += ["\n## 8. Known / excluded\n",
           "Not tracked automatically yet: the judge applies `test-standards.md` while judging. Check `run-<n>/run.md` for details.\n",
           "\n## 9. Not covered in this run\n",
           f"- Only the steps in `missions/{args.mission}.md`, only Chromium, only account `{args.account}`.",
           "- No source-code (component/unit) or API-level tests: SauceDemo is tested as a black box through the UI.",
           "- No performance, security or full accessibility testing.",
           "- Findings are matched across runs by step + expectation only, not by meaning. Two different problems at the same step and expectation count as one.",
           "\n## 10. Raw data\n", "- [comparison.md](comparison.md)",
           "- [report.json](report.json): this report as structured data (for tools and AI agents). `human_decision` is empty for you to fill in."]
    md += [f"- Run {i}: [run.md](run-{i}/run.md) · [screenshots](run-{i}/steps/) · [console.log](run-{i}/console.log) · "
           f"[network.log](run-{i}/network.log) · [findings.yaml](run-{i}/findings.yaml)" for i in range(1, n + 1)]
    (mission_dir / "report.md").write_text("\n".join(md) + "\n")

    # report.json: the same content as report.md for tools and AI agents. Stable keys, one record per check / finding.
    data = {
        "schema_version": 1, "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "account": args.account,
        "mission": args.mission, "model": args.model or "qwen2.5:7b", "runs": n, "verdict": verdict,
        "runs_summary": [{"run": run["run"], "outcome": run["outcome"], "seconds": run["seconds"],
                          "steps_passed": sum(r["step_result"] == "pass" for r in run["records"]), "steps_total": len(steps),
                          "findings": sum(len(r["findings"]) for r in run["records"])} for run in runs],
        "checks": [{"step": r["step"], "ref": r["ref"], "expected": r["expected"], "observed_per_run": r["observed"],
                    "result_per_run": r["statuses"], "across_runs": r["across"],
                    "screenshots": [f"run-{i}/steps/S{r['step']:02d}.png" for i in range(1, n + 1)]} for r in rows],
        "findings": [{"id": f"S{g['step']}-{g['ref']}", "step": g["step"], "quality_ref": g["ref"],
                      "classification": g["label"], "seen_in_runs": list(g["by_run"]), "runs_total": n,
                      "type": g["first"]["type"], "title": g["first"]["title"], "expected": g["first"]["expected"],
                      "observed": g["first"]["observed"], "agent_suggested_severity": g["first"]["suggested_severity"],
                      "confidence": g["first"]["confidence"], "technical_signal": g["first"]["technical_signal"],
                      "evidence": [f"run-{r}/{x['evidence']}" for r, x in g["by_run"].items()],
                      "ai_review": g.get("review"), "human_decision": None} for g in groups],
        "coverage": [{"run": run["run"], **coverage(run)} for run in runs],
        "not_covered": ["steps outside the mission file", "browsers other than Chromium", "component/unit and API level",
                        "performance, security, full accessibility"],
        "files": {"report": "report.md", "comparison": "comparison.md",
                  "runs": [f"run-{i}/run.yaml" for i in range(1, n + 1)]},
    }
    (mission_dir / "report.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


# ---------- Main ----------

async def main():
    load_dotenv(ROOT / ".env")
    parser = argparse.ArgumentParser(description="Run an AI-driven QA mission against SauceDemo.")
    parser.add_argument("--account", default="problem_user")
    parser.add_argument("--mission", default="core")
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--model", default=os.getenv("LLM_MODEL"))
    parser.add_argument("--headed", action="store_true", help="show the browser window")
    parser.add_argument("--vision", action="store_true", help="send the screenshot to the judge too (needs a vision model, e.g. --model qwen2.5vl:7b)")
    parser.add_argument("--first", type=int, help="run only the first N steps, no free exploration (timing test)")
    parser.add_argument("--review-model", default=os.getenv("REVIEW_MODEL"),
                        help="model that reviews the findings after the runs. Default: the --model if it is a Claude model, "
                             "otherwise qwen2.5vl:7b (a vision model that also reads the screenshots)")
    parser.add_argument("--no-review", action="store_true", help="skip the AI review of findings")
    parser.add_argument("--add-run", action="store_true",
                        help="add ONE more run (run-N+1) to the existing folder instead of starting a new batch, then compare all saved runs")
    parser.add_argument("--parallel", action="store_true",
                        help="run all runs of the batch at the same time (use with Claude or Gemini, not with a local Ollama model)")
    parser.add_argument("--review-only", action="store_true", help="redo comparison, AI review and report from the saved runs, no browsing")
    parser.add_argument("--max-agent-steps", type=int, default=12, help="agent actions allowed per mission step")
    args = parser.parse_args()
    is_claude = (args.model or "").startswith("claude")
    args.provider = "claude (your plan)" if is_claude else ("google" if (args.model or "").startswith("gemini") else "ollama")
    args.review_model = args.review_model or (args.model if is_claude else "qwen2.5vl:7b")
    if is_claude and args.vision:
        print("Note: the Claude option is text-only, so --vision is ignored.")
        args.vision = False

    mission_text, steps, explore = load_mission(args.mission)
    if args.first:
        steps, explore = steps[:args.first], None
    if explore:
        steps = steps + ["Free exploration: try other paths inside this mission's theme (the AI chooses)"]
    docs = {name: (ROOT / "instructions" / name).read_text() for name in ("agent-charter.md", "quality-definition.md", "test-standards.md")}
    docs["judge"] = "\n\n".join(f"=== {name} ===\n{docs[name]}" for name in ("quality-definition.md", "test-standards.md"))
    mission_dir = ROOT / "reports" / args.account / args.mission

    if args.review_only:
        runs = [yaml.safe_load(p.read_text()) for p in sorted(mission_dir.glob("run-*/run.yaml"), key=lambda p: int(p.parent.name.split("-")[1]))]
        if not runs:
            raise SystemExit(f"No saved runs in {mission_dir}")
        print(f"Review only: {len(runs)} saved run(s) in {mission_dir}")
    else:
        llm = make_llm(args.model)
        if args.add_run:  # keep the saved runs, number the new one after them
            mission_dir.mkdir(parents=True, exist_ok=True)
            saved = [int(p.name.split("-")[1]) for p in mission_dir.glob("run-*") if p.name.split("-")[1].isdigit()]
            numbers = [max(saved, default=0) + 1]
        else:  # a new batch replaces the old one
            shutil.rmtree(mission_dir, ignore_errors=True)
            numbers = list(range(1, args.runs + 1))
        print(f"Mission '{args.mission}' ({len(steps)} steps), account {args.account}, "
              f"{'adding run ' + str(numbers[0]) if args.add_run else str(args.runs) + ' run(s)'}, model {args.model or 'qwen2.5:7b'}")
        if args.parallel and len(numbers) > 1:
            # All runs start together. Each has its own browser profile and writes only into its own run-N folder.
            print(f"Starting runs {numbers} in parallel...", flush=True)
            results = await asyncio.gather(
                *(run_once(n, args, llm, mission_dir / f"run-{n}", mission_text, steps, explore, docs) for n in numbers),
                return_exceptions=True)  # one run crashing must not throw away the others
            for run_no, run in zip(numbers, results):
                if isinstance(run, Exception):
                    print(f"Run {run_no}: CRASHED, no result saved ({short_error(run)})", flush=True)
                else:
                    print(f"Run {run_no}: {run['outcome']} in {run['seconds']}s", flush=True)
        else:
            for run_no in numbers:
                print(f"Run {run_no}", flush=True)
                run = await run_once(run_no, args, llm, mission_dir / f"run-{run_no}", mission_text, steps, explore, docs)
                print(f"Run {run_no}: {run['outcome']} in {run['seconds']}s", flush=True)
        # always compare what is saved on disk: that includes runs from earlier commands
        runs = [yaml.safe_load(p.read_text()) for p in sorted(mission_dir.glob("run-*/run.yaml"), key=lambda p: int(p.parent.name.split("-")[1]))]

    rows, groups = compare(runs)
    if groups and not args.no_review:
        print(f"AI review of {len(groups)} finding(s) with {args.review_model} (reads descriptions and screenshots)...", flush=True)
        await review_findings(groups, runs, mission_dir, docs["judge"], make_llm(args.review_model), len(runs))
    write_comparison(mission_dir, runs, rows)
    write_report(mission_dir, runs, rows, groups, args, mission_text, steps)
    print(f"Done. Report: {mission_dir / 'report.md'}")


if __name__ == "__main__":
    asyncio.run(main())
