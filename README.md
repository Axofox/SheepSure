# AI-Driven QA — SauceDemo Checkout

> **Purpose:** the overview of the solution: the idea, the folder layout, the flow, and what is automated vs. human.
> **Used when:** first thing to read, and the starting point for the walkthrough.

An AI agent explores the SauceDemo checkout flow **three times**, the results are compared, and a human reviews one consolidated report. Humans own the definition of quality; the AI does the repetitive exploring, observing and documenting.

## Core idea

1. **Humans define quality first** — what "good" means for this product, before any test runs.
2. **The AI explores, it does not just replay a script** — it follows the scenario, but observes the whole experience through defined perspectives (oracles).
3. **Run it 3 times, then compare** — AI is non-deterministic, so one run is one opinion. Agreement across runs = reproducible. Disagreement = needs a human look.
4. **Silent issues are reported, not judged** — things that look wrong with no console or network error are recorded as *observations*, not bugs.
5. **The report is built for fast human decisions** — evidence first, grouped by confidence, with a clear "decide here" section.
6. **The agent learns from human feedback** — repeated mistakes are written into `test-standards.md`, and every future run reads it.

## Folders and files

| Path | Purpose | Owner |
|---|---|---|
| `instructions/quality-definition.md` | What quality means for this product and flow | Human |
| `instructions/agent-charter.md` | The agent's instructions: scenario, perspectives, how to record findings | Human writes, AI follows |
| `instructions/test-standards.md` | Rules the agent must follow: exclusions, interpretations, behaviour limits | Human approves, AI reads every run |
| `missions/` | One file per mission (`core` for the demo; three optional explorations) | Human |
| `design/run-protocol.md` | How the 3 runs are executed and compared | System |
| `design/report-template.md` | The structure of the final human-readable report | System |
| `design/human-in-the-loop.md` | Where humans decide, and the feedback loop | Human |
| `design/roadmap.md` | What to improve next and how this scales across QA | — |
| `runner.py` | The AI runner: drives the browser, judges, compares runs, writes the report | Code |
| `reports/` | Output of `runner.py`, per account and mission (overwritten per batch) | Generated |
| `pilots/` | Three manual runs through the Chrome extension, kept as evidence, plus their comparison | History |

## Flow

```
quality-definition.md ─┐
agent-charter.md ──────┼──► Run 1 ─┐
test-standards.md ─────┘   Run 2 ─┼──► Compare ──► Report ──► Human review
                           Run 3 ─┘                              │
                                                                 ▼
                                              Feedback written to test-standards.md
                                                                 │
                                                  (read by the next iteration)
```

## Environment

- Application: https://www.saucedemo.com/
- User: `problem_user` / `secret_sauce`
- Tooling: Playwright drives the browser and captures screenshots, console and network logs. A small agent loop in `runner.py` lets an LLM choose the actions. Browser Use supplies the model wrappers. The model is your choice (local via Ollama, or hosted), set with `--model` or `LLM_MODEL` in `.env`.

## How to run the test

Run from the project folder. Each command starts a fresh batch of 3 runs and overwrites the previous batch for that account and mission.

**Standard run (3 runs at the same time, hosted model):**

```bash
.venv/bin/python runner.py --account standard_user --mission core --model claude-haiku-5-5 --parallel --max-agent-steps 12
```

| Option | What it does |
|---|---|
| `--account` | `standard_user` (baseline) or `problem_user` (seeded bugs) |
| `--mission` | `core` (the demo), or `reset-state`, `cart-crud`, `form-errors` |
| `--model` | The model for browsing, judging and review. Names starting with `claude` or `gemini` use a hosted model; anything else is a local Ollama model. Can also be set as `LLM_MODEL` in `.env` |
| `--parallel` | Runs all 3 runs at the same time instead of one after another. Use it with a hosted model, **not** with a local Ollama model. A batch takes about 5 minutes instead of about 15 |
| `--max-agent-steps` | How many actions the agent may take per mission step (one click, one typed input or one navigation). Default is 12. Raise it for longer flows. A higher limit costs more time and tokens |
| `--runs` | Number of runs (default 3) |
| `--headed` | Show the browser window |
| `--add-run` | Add one more run to the existing folder, then compare all runs |
| `--review-only` | Redo comparison and report from the saved runs, no browsing |

The free-exploration step has its own action limit, set by `Budget:` in the mission file (for example `missions/core.md`).

**Both accounts, so you can compare them:**

```bash
.venv/bin/python runner.py --account problem_user --mission core --model claude-haiku-5-5 --parallel --max-agent-steps 12
.venv/bin/python runner.py --account standard_user --mission core --model claude-haiku-5-5 --parallel --max-agent-steps 12
```

The report is written to `reports/<account>/<mission>/report.md`. Observed values come from the page. Pass/fail judgements come from the AI and need a human review.

## What is automated vs. human

| Automated (AI) | Human |
|---|---|
| Driving the browser through the scenario | Defining quality and acceptance |
| Observing UI, console, network, state | Deciding: bug, intended behaviour, or spec gap |
| Recording findings with evidence | Approving rules into `test-standards.md` |
| Running 3 times and comparing | Deciding what is release-blocking |
| Producing the report | Filing tickets (or approving auto-filed ones) |
