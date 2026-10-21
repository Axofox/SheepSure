# Test Standards — Learned Rules

> **Purpose:** the rules the agent must follow (TS-001…): what to exclude, how to interpret things, and how to behave while testing.
> **Used when:** read by the agent and the judge before every run. A human adds a rule here after reviewing a report and deciding the agent needs correcting.

> **Owner: Human approves, AI reads before every run.**
> This is how the agent learns. When a human notices a recurring mistake in reports, it is written here so the next iterations avoid it.
> Rules here override the agent's own judgement.

## How to add a rule

1. A human spots a pattern in a report (false positive, missed check, wrong severity, wrong interpretation).
2. The human writes a rule below — or the agent proposes one in the report and the human approves it.
3. The rule gets an ID, a reason, and a date. It is never added without a human approving it.
4. Rules are reviewed regularly. A rule that hides a real problem gets removed.

## Rule types

| Type | Use when |
|---|---|
| **Exclude** | Something is reported repeatedly but is known, accepted or intentional |
| **Always check** | The agent keeps missing something important |
| **Interpret** | The agent misunderstands what something means |
| **Severity** | The agent consistently rates something too high or too low |
| **Behaviour** | The agent does something unhelpful while testing (e.g. too many retries) |

## Rule format

```yaml
- id: TS-001
  type: <exclude | always-check | interpret | severity | behaviour>
  rule: <one clear sentence the agent can follow>
  reason: <why — what went wrong before>
  scope: <which steps / pages>
  added_by: <name>
  date: <YYYY-MM-DD>
  review_by: <date — so exclusions don't become permanent blind spots>
```

## Active rules

<!-- Starting rules. These shape how the agent works, they are not results. -->

```yaml
- id: TS-001
  type: behaviour
  rule: Verify the outcome of every action by reading the page state afterwards, never assume an action succeeded because the click happened.
  reason: Agents tend to report a step as passed because they performed it.
  scope: all steps
  added_by: Tina
  date: 2026-10-20
  review_by: —

- id: TS-002
  type: always-check
  rule: After typing into any form field, read the field value back and compare it to what was typed.
  reason: Input problems are often silent — no error until a later step.
  scope: step 5
  added_by: Tina
  date: 2026-10-20
  review_by: —

- id: TS-003
  type: behaviour
  rule: Retry a failed step at most once, then stop and report. Do not invent workarounds.
  reason: Workarounds hide the real user experience and can make a blocked flow look passed.
  scope: all steps
  added_by: Tina
  date: 2026-10-20
  review_by: —

- id: TS-004
  type: interpret
  rule: An issue with no console or network error is "suspicious", not a "failure", unless it breaks an F1–F7 expectation.
  reason: Keeps silent observations visible without inflating the bug count.
  scope: all steps
  added_by: Tina
  date: 2026-10-20
  review_by: —
```

```yaml
- id: TS-005
  type: always-check
  rule: Record every step with its expected vs observed values and an outcome screenshot, including steps that pass.
  reason: An unrecorded pass cannot be verified or compared across runs.
  scope: all steps
  added_by: Tina
  date: 2026-10-20
  review_by: —
```

```yaml
- id: TS-006
  type: interpret
  rule: If something works but a step or option a shopper would reasonably expect is absent, and quality-definition.md does not say it should exist, report type "flow-gap" (a possible flow gap / possible unconfirmed bug). Name what is missing and what the shopper would expect. Never call it a bug and never fail a check for it.
  reason: Without an expected behaviour there is nothing to compare against. A human (product owner) decides if it is intended or a missing requirement.
  scope: all steps
  added_by: Tina
  date: 2026-10-21
  review_by: —
```
