# Report Template

> **Purpose:** the structure of the final human-readable report (`report.md`).
> **Used when:** as the reference for what `runner.py` writes at the end of a batch, and when reviewing a report. The agent does not read it.

> Goal: a human can understand the result in 1 minute and make decisions in 5.
> Placeholders are in `<angle brackets>`. No result is written until the runs have actually happened.

---

# QA Report — SauceDemo Checkout — `<date>`

## 1. Verdict

**`<Pass | Fail | Inconclusive>`** — `<one sentence: what happened>`

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Scenario outcome | `<completed / blocked at step N>` | | |
| Steps passed | `<x/7>` | | |
| Findings | `<n>` | | |

## 2. Step results — expectations vs. what happened

Every expectation checked, including the passes. Screenshot links go to the outcome screenshot of that step in each run.

| Step | Ref | Expected | Observed (run 1 / 2 / 3) | Run 1 | Run 2 | Run 3 | Across runs | Screenshots |
|---|---|---|---|---|---|---|---|---|
| 1 | F1 | `<…>` | `<…>` | `<pass/fail/unsure>` | | | `<confirmed pass / confirmed fail / unstable / not verified>` | `<R1 · R2 · R3>` |
| 2 | F2 | `<…>` | `<…>` | | | | | |
| 2 | F3 | `<…>` | `<…>` | | | | | |
| … | | | | | | | | |

## 2b. Coverage — what each run explored

How much ground each run covered and where the runs went in different directions. The runner fills the counts. The paths are the AI's own descriptions, so a human checks them against the screenshots.

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | `<n>` | | |
| Browser actions taken | `<n>` | | |
| Paths tried in free exploration | `<n>` | | |

Pages not visited by every run, and the paths each run tried, are listed under the table.

## 3. Needs your decision

The short list a human must look at. Each item has one question.

| # | Finding | Seen in | AI suggestion | Question for you |
|---|---|---|---|---|
| 1 | `<short title>` | `<3/3>` | `<likely real bug / intended or spec gap / false positive / needs human>` | Bug, or intended? |
| 2 | `<short title>` | `<1/3>` | `<…>` | Real, or agent error? Evidence attached. |

## 4. Reproducible findings (3/3)

### `<id>` — `<short title>`
- **Step:** `<n>` · **Expectation:** `<F/C ref>` · **Suggested severity:** `<…>`
- **Expected:** `<…>`
- **Observed:** `<…>`
- **Technical signal:** `<console / network / none>`
- **Evidence:** `<screenshots from each run>`
- **AI review (a suggestion, a human decides):** `<suggested status, severity, does the screenshot support the description, reasoning>`
- **Steps to reproduce:** `<numbered, copy-paste ready for a ticket>`

## 5. Likely findings (2/3)

`<same structure, plus: what was different in the run where it did not appear>`

## 6. Unconfirmed findings (1/3)

`<same structure, plus: possible explanation — agent variance / flakiness / agent error / spec gap>`

## 7. Silent observations (no error signal)

Things that looked off with no console or network error. **Not classified as bugs.**

| Observation | Seen in | Why it looked suspicious |
|---|---|---|
| `<…>` | `<x/3>` | `<…>` |

## 8. Known / excluded

Items matched against rules in `test-standards.md` and therefore not reported as findings.

| Rule ID | What was seen |
|---|---|
| `<TS-xxx>` | `<…>` |

## 9. Not covered in this run

Honest list of what the agent did **not** check (e.g. other products, other browsers, accessibility, error paths).

## 10. Raw data

Relative links, from the mission folder, to `run-<n>/run.md`, the screenshot folders `run-<n>/steps/`, `run-<n>/console.log`, `run-<n>/network.log` and `comparison.md`.
