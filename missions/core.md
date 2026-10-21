# Mission: core

> **Purpose:** the required scenario: log in, add two products, check out, finish the order. Has a pass/fail verdict.
> **Used when:** passed to the agent after the charter (`--mission core`). This is the mission for the demo.

**Theme:** the checkout scenario as a normal shopper would do it.
**Expectations to check:** F1–F7 (and C1–C5 on every page you pass through).
**Verdict:** this mission has a pass/fail verdict (see `quality-definition.md`, section 5).

## Steps

1. Log in with the given account.
2. Add **Sauce Labs Backpack** and **Sauce Labs Bike Light** to the cart.
3. Open the cart.
4. Start checkout.
5. Enter valid customer information (First Name `Test`, Last Name `User`, Postal Code `12345`).
6. Continue to the order overview.
7. Finish the order.

## After each step, record

URL, visible key text, cart badge count, field values.

## Free exploration

Budget: 12 actions. Ideas, not a checklist. Choose your own:
- Open a product's detail page and go back. Do name, image, price and description match what the list showed?
- Remove an item from the cart and put it back. Does the badge follow?
- Try the sort dropdown on the products page. Does the order match the label?
- Anything else on the shopping path that a real customer might do.

Budget: 12 actions. An action is one click, one typed input, or one navigation. After 12, the agent stops. Without a limit it could wander and burn tokens or time.
Ideas, not a checklist. The three bullets are suggestions to get it started. The agent doesn't have to do all of them, and it can do others.
"Choose your own". The agent decides what looks worth poking at. This is the part where the AI judges for itself, instead of replaying a script.
Why it's there. The 7 steps only prove the happy path works. Real bugs often sit next to that path. The seeded problem_user bugs include the sort dropdown and product links, which the fixed steps never touch.