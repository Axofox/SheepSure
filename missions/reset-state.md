# Mission: reset-state

> **Purpose:** an optional exploration of whether state that should clear (cart, fields, session) really clears. No verdict.
> **Used when:** passed to the agent after the charter (`--mission reset-state`), once `core` works.

**Theme:** does something that should go away actually go away, everywhere?
**Expectations to check:** R1–R4 (and C5 on every step).
**Verdict:** none. Findings are classified by reproducibility.

## Steps

1. Log in with the given account.
2. Add **Sauce Labs Backpack** and **Sauce Labs Bike Light**. Record the badge count and the button label on all six products.
3. Open the burger menu and choose **Reset App State**. Do **not** reload the page. Record the badge count, all six button labels, and the cart contents. (R2)
4. Add the Backpack, open the cart, start checkout and click **Continue** with all fields empty. Record the error text. Type a first name only, and record whether the error is still shown. Click the **X** on the error and record the result. (R1)
5. Fill in valid information, continue, and finish the order. Record the cart badge and the cart contents afterwards. (R3)
6. Log out from the burger menu and log in again. Record any error text or leftover field values on the pages you reach. (R4)

## Notes

- If the error stays after typing, do not call it a bug on your own. Check `test-standards.md`, and report it as an observation. The baseline account may behave the same way.

## Free exploration

Budget: 12 actions. Ideas, not a checklist. Choose your own:
- Trigger the checkout error in a different way (only one field missing) and see how and when it goes away.
- Use Reset App State at a different moment (with an item in the cart, on the cart page, in the middle of checkout).
- Go back with the browser Back button after finishing an order. What state is shown?
- Anything else where something should disappear, empty or reset.
