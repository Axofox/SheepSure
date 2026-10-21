# Quality Definition — SauceDemo Checkout

> **Purpose:** the human-owned definition of what "good" means: expectations F1–F7, C1–C5, oracles and severity.
> **Used when:** read by the agent before every run and by the judge when it decides pass/fail. Changed only by a human, never by the agent.

> **Owner: Human.** The agent reads this before every run. It does not change it.
> This is the reference ("oracle") the AI compares what it sees against.

## 1. Product context

- An online shop. A logged-in user selects products, reviews a cart, enters customer information and places an order.
- The checkout is the money path. Anything that stops, misleads or silently changes an order is high impact.

## 2. What "quality" means for this flow

### Must be true (functional)

| # | Expectation |
|---|---|
| F1 | Valid credentials log the user in and land on the products page |
| F2 | Clicking "Add to cart" on a product adds **that** product, and the button changes to "Remove" |
| F3 | The cart badge count equals the number of items actually in the cart |
| F4 | The cart contains exactly the selected products — correct names, prices, quantities |
| F5 | Checkout accepts valid First Name, Last Name, Postal Code, and each field keeps exactly what was typed |
| F6 | The overview shows the same items as the cart; item total = sum of item prices; total = item total + tax |
| F7 | Finishing shows an order confirmation, and the cart is empty afterwards |

### Should be true (consistency and trust)

| # | Expectation |
|---|---|
| C1 | A product's name, image, description and price match each other everywhere it appears |
| C2 | Navigation goes where the label says (e.g. clicking a product opens *that* product) |
| C3 | Error messages are accurate — they describe the real problem |
| C4 | No layout breakage, overlapping elements, or unreadable text in the flow |
| C5 | No unexpected console errors or failed network requests during the flow |

### Exploration themes (PROPOSED: drafted by the AI assistant, not yet approved by the owner)

Each theme is one mission in `missions/`. Same rule as C1–C5: reported, and a human decides.

**Reset state: does something that should go away actually go away, everywhere?**

| # | Expectation |
|---|---|
| R1 | A validation error clears once the user corrects the field (or dismisses it, and it stays gone) |
| R2 | "Reset App State" empties the cart, removes the badge, and every button reads "Add to cart" again, without a reload |
| R3 | After a completed order, the cart and badge are empty and a new order can start clean |
| R4 | After logout and login, there are no stale errors or leftover form values |

**Cart data (create, read, delete) and persistence**

| # | Expectation |
|---|---|
| D1 | Removing an item (on the products page or in the cart) updates the badge, the button and the cart list consistently |
| D2 | The same item cannot be added twice; adding all products gives badge 6; removing all gives an empty cart |
| D3 | The cart survives a page reload, the Back button, and logout/login, as in a normal shop |
| D4 | Cancelling checkout keeps the cart intact |

**Form input and validation**

| # | Expectation |
|---|---|
| V1 | Each "required" error names the field that is actually missing |
| V2 | Fields keep what was typed after an error (nothing lost, swapped or changed) |
| V3 | Unusual input (spaces only, 200 characters, special characters, letters in the postal code) is either accepted and kept exactly, or rejected with a clear message. It is never silently altered |

### Out of scope for this exercise

- Performance benchmarks, security testing, full accessibility audit, cross-browser coverage.
- Products not involved in the scenario — unless an issue with them is noticed in passing (then: observation only).

## 3. Perspectives (oracles) the agent must use

Based on FEW HICCUPPS — the agent checks what it sees against:

| Oracle | Question the agent asks |
|---|---|
| **Claims** | Does the app do what its labels, buttons and messages say? |
| **User expectations** | Would a normal shopper be surprised or confused here? |
| **Product consistency** | Is the same thing shown the same way on every page? |
| **History** | Does the result match what happened in previous runs? |
| **Comparable products** | Does this behave like a normal online checkout? |
| **Purpose** | Can the user actually complete their goal: buy these two items? |
| **Statutes / standards** | Prices, totals and tax add up correctly |

## 4. Severity scale

| Severity | Meaning | Example type |
|---|---|---|
| **Blocker** | The user cannot complete the order | Checkout cannot continue |
| **Major** | Order completes but is wrong, or user is misled | Wrong item or price in overview |
| **Minor** | Inconsistent, confusing, but not order-changing | Wrong product image |
| **Observation** | Looks suspicious; not confirmed as a problem | Unusual behaviour with no error signal |

## 5. Definition of done for a run

A **core** run is **passed** only if F1–F7 all hold. Anything in C1–C5 and in the exploration themes R, D and V is reported but does not by itself fail the run: a human decides.

The exploration missions have no pass/fail verdict. They produce confirmed, likely and unconfirmed findings (see `run-protocol.md`).
