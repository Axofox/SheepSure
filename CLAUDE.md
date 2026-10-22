# Project context — AI-Driven QA Assessment (zvoove)

> **Purpose:** the project brief for Claude: the assignment, the decided design, the status of the runner, and how to work with Tina.
> **Used when:** loaded automatically at the start of every Claude Code session in this folder. Edit it when the project's status or rules change.

## The assignment
Build a small, working AI-driven QA solution that tests the SauceDemo checkout flow. Time-box: ~2 hours. The working solution is demonstrated live in a review.

- App: https://www.saucedemo.com/
- User: `problem_user` / `secret_sauce` (the account with seeded bugs)
- Baseline: `standard_user` (the account without seeded bugs), used for comparison
- Scenario: log in → add Sauce Labs Backpack + Sauce Labs Bike Light → open cart → checkout → enter valid info → continue → finish order
- The AI must take part in the testing itself, not just generate test code once.

## Design (already decided — see the .md files in this folder)
| File | Role |
|---|---|
| `README.md` | Overview and flow |
| `instructions/quality-definition.md` | Human-owned definition of quality (expectations F1–F7, C1–C5, oracles, severity) |
| `instructions/agent-charter.md` | Instructions given to the browsing agent; step record + finding YAML formats |
| `instructions/test-standards.md` | Learned rules (TS-001…), approved by a human, read before every run |
| `design/run-protocol.md` | 3 runs, comparison logic, classification, verdict |
| `design/report-template.md` | Structure of the final report |
| `design/human-in-the-loop.md` | Where humans decide; feedback loop |
| `design/roadmap.md` | Next steps and broader QA vision |
| `missions/` | One file per mission: `core` (the demo) plus three optional explorations |
| `runner.py` | The AI runner (see "Runner status" below) |
| `scripted_run.py` | No-AI reference run: the same checkout in plain Playwright with real assertions (F1–F7, prices, totals), same output format as the AI runner. Usage: `.venv/bin/python scripted_run.py [standard_user\|problem_user]`. It overwrites `reports/<account>/core/run-1/`, so it also overwrites an AI run-1 |
| `reports/` | Output of `runner.py` per account and mission (overwritten per batch). Currently holds the batches of 2026-10-21 (see "Runner status") |
| `pilots/` | Three manual Chrome-extension runs and their comparison, kept as the agents produced them (screenshot mentions removed). Not in the git repository; it may exist only on Tina's machine |

Key principles:
- Run the agent **3 times** with identical instructions; compare per check (step + quality_ref).
- **Every step is recorded**, including passes: expected vs observed, pass/fail/unsure, plus **one screenshot of the outcome** (`reports/<account>/<mission>/run-<n>/steps/S<step>.png`).
- An unrecorded check = "not verified", never "pass".
- Silent issues (no console or network error) are "suspicious" observations, not bugs.
- Run disagreement = needs human triage (agent variance, app flakiness, agent error, or spec gap).
- Agreement across runs is not proof; findings need evidence.
- Never invent results. Quote only what is in `reports/`; report templates contain placeholders until real runs happen.
- The word "baseline" has two meanings here: the `standard_user` account (comparison for false positives) and `scripted_run.py` (deterministic no-AI reference). Say which one you mean.

## Runner status: built and run once per account, results not yet triaged
`runner.py` exists. An earlier attempt stopped at step 3 when the hosted model's quota ran out, and those results were deleted. Since then, full batches of 3 runs on the `core` mission were committed (2026-10-21, model `claude-haiku-5-5`, hosted). The model is one setting (`--model` or `LLM_MODEL` in `.env`); local Ollama is the alternative.

Results so far (AI judgements, not yet reviewed by a human):
- `problem_user`: all 3 runs blocked at step 5. The Last Name field read back empty (in run 2 the value landed in First Name). Verdict "Fail", 27 of 39 checks not verified. It is **not established** whether this is an app bug or an agent element-targeting error. The report asks for a manual reproduction. Running `scripted_run.py problem_user` is the quick way to separate the two (it types with fixed selectors and reads each field back).
- `problem_user` silent observations: all six products use the same image `/assets/sl-404-...jpg` (3/3 runs, rendering not captured); "Price (low to high)" sort left the A–Z order (1/3 runs).
- `standard_user`: all 3 runs completed, verdict "Inconclusive" (20 of 32 checks not verified), no findings that need a decision.

`runner.py` is a Python script that:
1. Loads `instructions/quality-definition.md`, `instructions/agent-charter.md`, `instructions/test-standards.md` as the agent's instructions
2. Drives the browser through the scenario with **Playwright** and its own small agent loop (Browser Use is used for its model wrappers, `ChatOllama` and `ChatGoogle`)
3. Saves per-step records (YAML/MD) and an outcome screenshot per step, plus console and network logs
4. Repeats 3 times in fresh browser sessions → `reports/<account>/<mission>/run-1..3` (a new batch overwrites the previous one for that account and mission). Missions live in `missions/` (core, reset-state, cart-crud, form-errors)
5. Compares runs and fills `design/report-template.md` → `report.md`
6. Optional: same run on `standard_user` as a baseline

## How to work with the developer (Tina)
- QA engineer, strong in Playwright/Cypress/TypeScript; Python is not her daily language, so keep the Python simple and explain it.
- Plain language first, explain jargon when it appears, one topic at a time, short answers, ask before moving on.
- Be honest about what was and wasn't tested. Never invent results.
- No flattery; correct her directly if something is wrong.
- She edits project files in her editor between turns. Re-read a file before editing it, and do not undo her changes.
- Ask before moving, deleting or restructuring files.
