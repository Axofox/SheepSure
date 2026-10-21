# Run Protocol — 3 Runs and Comparison

> **Purpose:** how the 3 runs are executed and compared, how disagreements are classified, and how the verdict is reached.
> **Used when:** designing or changing the compare logic in `runner.py`, and when a human triages runs that disagree. The agent does not read it.

## Why 3 runs

AI agents are non-deterministic: the same instructions can produce a different path, different observations, or a different interpretation each time. One run is one opinion. Three runs let us separate **what the app reliably does** from **what the agent happened to notice or misread**.

## Execution

| Setting | Value |
|---|---|
| Runs | 3, each starting from a fresh browser session |
| Instructions | Identical for every run: `agent-charter.md` + `quality-definition.md` + `test-standards.md` + the mission file `missions/<id>.md` |
| Captured per run | Step record for every step (expected vs observed, pass/fail/unsure), outcome screenshot per step, findings, console log, network log |
| Output | `reports/<account>/<mission>/` (accounts: `problem_user`, and `standard_user` as the optional baseline; missions: `core`, `reset-state`, `cart-crud`, `form-errors`) containing `run-1/`, `run-2/`, `run-3/` (each with `run.md`, `steps/`, `console.log`, `network.log`, `findings.yaml`), plus `comparison.md`, `report.md` (for humans) and `report.json` (the same content as structured data, for tools and AI agents). Starting a new batch overwrites the previous results for that account and mission. To run one run at a time instead, use `--add-run`: it adds `run-N+1` and compares all saved runs. |

## Comparison

### Step results across runs

Every check (step + quality_ref) is compared across the 3 runs, including the passes.

| Results across runs | Meaning |
|---|---|
| pass / pass / pass | **Confirmed pass.** Expectation met reproducibly |
| fail / fail / fail | **Confirmed fail.** See reproducible findings |
| Mixed | **Unstable.** The human looks at the screenshots of each run |
| Any "unsure" | **Not verified.** Counts as neither pass nor fail |

A check that was never recorded in a run counts as **not verified** in that run, never as pass.

### Coverage across runs

Each mission ends with a **free exploration** step: the AI picks its own paths inside the mission's theme, within an action budget. Runs will therefore cover different ground, and that is expected. The runner records pages visited, actions taken and the paths the AI says it tried, and lists the runs side by side. A path tried in only one run is a reason to look closer (a new idea, or a hallucination), and it is never counted as a pass or fail.

### Findings across runs

Findings are matched across runs by **step + quality_ref + what was observed** — not by exact wording, because the agent will describe the same thing differently each time. Matching can be done by a separate AI "judge" prompt, with rule-based matching on `step` and `quality_ref` as a first filter.

### AI review of findings

After the runs, a second AI pass (a vision model) reads each finding's description from every run and looks at the screenshots. It adds a **suggested status** (likely real bug / likely intended or spec gap / likely false positive / needs human), a suggested severity, whether the screenshot supports the description, and one question for the human. It only suggests. The human decides, and the suggestion is shown beside the original finding, never instead of it.

### Classification

| Seen in | Label | Meaning | What happens |
|---|---|---|---|
| 3 / 3 | **Reproducible** | Consistent behaviour of the app | Top of the report; strongest candidates for bugs |
| 2 / 3 | **Likely** | Probably real, may depend on path or timing | Reported; human checks evidence |
| 1 / 3 | **Unconfirmed** | Could be real, could be agent error | Reported separately; human triage |

### What a mismatch (1/3 or 2/3) can mean

A mismatch is a signal to **look closer**, not a verdict. Possible causes:

1. **Agent variance** — the agent took a different path or simply didn't notice it in other runs.
2. **App flakiness** — the app behaves differently depending on timing or state (a real, harder-to-catch bug).
3. **Agent error / hallucination** — the agent reported something that didn't happen. Evidence check catches this.
4. **Gap in the quality definition** — the expected behaviour isn't defined, so each run judged differently. This can point to a missing requirement or feature, and is a question for the product owner.

### Important limit

**Agreement is not proof.** If all three runs make the same mistake (for example, because the instructions are unclear), they will all agree and still be wrong. That is why every finding needs evidence (screenshot, field value, DOM), and why a human reviews the reproducible findings too.

## Silent issues

Findings with `technical_signal: none` and `type: suspicious` are grouped into their own section. They are not counted as bugs and do not fail the run. They exist so a human can decide whether "nothing crashed" actually means "everything is fine".

## Possible flow gaps

A **flow gap** is a point where the app works, but a step or option a shopper would reasonably expect is absent, and the quality definition does not say it should exist (rule TS-006). Findings with `type: flow-gap` get their own report section. They are not bugs, do not fail the run, and are a question for the product owner: intended, or a missing requirement? The agent's view of what a shopper "would expect" is an opinion from general knowledge, so a human always decides.

## Overall verdict

| Verdict | Condition |
|---|---|
| **Pass** | All 3 runs completed, and every F1–F7 check is a confirmed pass |
| **Fail** | At least one reproducible or likely failure against F1–F7 |
| **Inconclusive** | Runs disagree on whether the scenario completed — human decides |
