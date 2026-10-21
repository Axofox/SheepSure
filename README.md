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
| `scripted_run.py` | No-AI baseline run that proves screenshot and log capture work | Code |
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

## What is automated vs. human

| Automated (AI) | Human |
|---|---|
| Driving the browser through the scenario | Defining quality and acceptance |
| Observing UI, console, network, state | Deciding: bug, intended behaviour, or spec gap |
| Recording findings with evidence | Approving rules into `test-standards.md` |
| Running 3 times and comparing | Deciding what is release-blocking |
| Producing the report | Filing tickets (or approving auto-filed ones) |
