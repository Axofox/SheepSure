# Human in the Loop

> **Purpose:** where humans decide and where the AI works alone, plus the feedback loop into `test-standards.md`.
> **Used when:** when reviewing a report, and to explain the human/AI split in the walkthrough.

The AI does the repetitive work. Humans keep the judgement. This file defines where that line is.

## Where humans are required

| Moment | Human decision | Why it can't be fully automated |
|---|---|---|
| **Before** | Write and update `quality-definition.md` | Quality is a product decision, not a technical one |
| **After the runs** | Triage the "Needs your decision" list | Bug vs. intended behaviour depends on business intent |
| **Unconfirmed findings** | Real issue or agent error? | The agent can't reliably judge its own mistakes |
| **Silent observations** | Worth a ticket or not? | No technical signal — needs context |
| **Learning** | Approve or reject new rules in `test-standards.md` | Unchecked rules can teach the agent to ignore real bugs |
| **Release** | Is this blocking? | Risk acceptance is a human responsibility |

## Feedback loop

```
Report ──► Human reviews ──► Pattern noticed?
                                  │
                       yes ───────┴─────── no
                        │                   │
          Write / approve rule        Decide findings,
          in test-standards.md        file tickets
                        │
          Next run reads the rule
                        │
          Next report: was the rule effective?
```

## Reviewer checklist

- [ ] Is the verdict supported by evidence (screenshots / values)?
- [ ] For each reproducible finding: bug, intended, or spec gap?
- [ ] For each unconfirmed finding: does the evidence show it happened?
- [ ] Any silent observation worth investigating?
- [ ] Any pattern of agent mistakes → new rule for `test-standards.md`?
- [ ] Any gap in `quality-definition.md` exposed by disagreement between runs?
- [ ] Does "Not covered" contain anything that matters for this release?

## Principle

The report should make the human's decision **easy**, not make it **for** them.
