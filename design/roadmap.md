# Roadmap — Next Steps and Evolution

> **Purpose:** what to improve next in this solution, and how the approach grows across QA (requirements, tickets, incidents).
> **Used when:** preparing the review discussion and planning the next iteration. Add an item when a run or pilot exposes a weakness.

## Improve next (this solution)

1. **Promote reproducible findings to regression checks.** Once a human confirms a 3/3 finding as a bug, generate a deterministic test (Playwright) for it. Exploration finds; scripts guard.
2. **Measure the agent, and use the results to tune the rules.** The model itself learns nothing between runs; only the text we give it changes. Track false positives and missed issues per batch against a human-confirmed answer key, then decide where each mistake belongs:
   - **The record of mistakes** (counts, which finding was wrong and why) goes in a separate results file, outside `reports/` so a new batch cannot overwrite it. The agent does not read it.
   - **A rule that prevents a repeated agent mistake** goes in `instructions/test-standards.md` as a short, human-approved rule.
   - **A gap in what "correct" means** goes in `instructions/quality-definition.md`.
   - **A tool problem** (for example the extension's dead clicks) changes neither file.
   - **Check that it worked:** run again after one rule change and compare the counts. Keep the rule only if false positives drop without missed bugs rising.
   - **Today:** nothing records this automatically. The mistakes are written up by hand in `pilots/comparison.md`, and the `human_decision` field in `report.json` is empty for a human to fill in.
3. **Auto-draft tickets** from confirmed findings, with steps to reproduce and evidence attached — human approves before filing.
4. **Screenshot evidence for every step.** The Chrome-extension pilots (`pilots/`) produced no screenshots: run 1 claimed files that did not exist, and in run 2 the extension's screenshot tool failed. The pilots accepted this as a known limitation. The fix is to capture outcome screenshots from the runner itself (Playwright), so evidence no longer depends on what the agent says it saved.
5. **Clean, isolated browser state per run.** A shared Chrome profile carries cart state between runs (see `pilots/comparison.md`). Each run should start from clean site data, or a fresh Playwright context.
6. **Automate the exploratory runs.** The three extension pilots were started by hand: open a chat, paste the prompt, copy the result out. Let `runner.py` start the runs itself, with the same instructions each time, so they need no manual steps and can be repeated on every release.
7. **Separate exploring from judging, with saved evidence in between.** Today the judge already runs as a separate AI call, but right after each step. Make the split stricter, with one job and a small prompt per stage:
   - **Explorer** gets the test style (`agent-charter.md` + the mission) and a short list of facts to capture. It writes only evidence to a file: actions, URL, DOM values, console, network, screenshots. It gives no verdicts.
   - **Judge** runs afterwards on that saved evidence only, with the quality rules (`quality-definition.md` + `test-standards.md`). For each item it suggests bug / not a bug / unsure, a priority, and the reason, naming the rule it used. A human decides.
   - **Why:** each agent has less to hold in mind, so fewer checks are missed (a hypothesis to test); the explorer no longer grades its own work; and after a rule change only the judge needs re-running, with no re-browsing.
   - **How to test it:** run the same mission both ways and compare missed known bugs and false positives (see item 2).
8. **Replay what the AI did as a deterministic test, then compare.** After the runs are compared, turn each run into a test script (Playwright, or manual steps) that repeats **exactly what the AI did**: the same actions, in the same order, with the same typed values, whatever the AI concluded. Include the passed, failed and suspicious checks.
   - **Compare:** run the script and put its results next to the AI's. If they match, the AI's observation is reproducible. If they differ, the AI misread the page, or the path was unstable. This separates AI error from app behaviour. A human decides in the unclear cases.
   - **What it needs:** the runner must record a stable selector for every action (visible label, role or test id), because the element numbers the agent sees change on every page.
   - **What it does not show:** a replay only covers what the AI did. To find what the AI missed, compare against an independent baseline too: `scripted_run.py` (no AI, fixed F1–F7 checks) and a human exploratory pass.
   - **Review:** a human checks each test against `quality-definition.md` before it counts, since a test with the wrong expectation proves nothing.

## Toward less repetitive manual QA

| Today (manual) | With this approach |
|---|---|
| Tester walks the flow every release | Agent walks it 3× and reports |
| Tester writes bug reports | Agent drafts them with evidence |
| Knowledge lives in people's heads | Knowledge lives in `quality-definition.md` and `test-standards.md` |
| Regression suite written by hand | Confirmed findings become regression tests |
| Tester's time spent executing | Tester's time spent defining quality and judging results |

## Broader use across QA

| Source | How AI can use it | Human role |
|---|---|---|
| **Product requirements** | Turn acceptance criteria into charters and quality expectations; flag missing or contradictory criteria | Confirm what "done" means |
| **Development changes** | Read the diff / PR and decide which flows to explore first (risk-based) | Confirm risk priorities |
| **Support tickets** | Cluster recurring complaints into patterns; add them as "always check" rules | Decide which patterns matter |
| **Customer-reported defects** | Reproduce the report automatically from its description; attach evidence. Idea: a simple one-button browser extension for customers that records their exact steps (element selectors), plus console and network errors, which become a replay script for the runner. Privacy by default: record which elements were used, not what was typed; anything that is not ours, including inputs, is blurred or masked (Sentry-style), and passwords and tokens are never captured. Not built: it is a project of its own. | Confirm and prioritise |
| **Existing automated tests** | Find gaps: which flows/expectations have no coverage; spot flaky tests | Decide what to cover |
| **Production incidents** | Turn each incident into a new expectation and a regression check | Approve the lesson learned |

## The direction

The same three building blocks scale to all of these:

1. **Quality definition** — what good looks like (human-owned)
2. **Agent charter** — how to explore and report (shared)
3. **Test standards** — what the team has learned (human-approved, growing over time)

