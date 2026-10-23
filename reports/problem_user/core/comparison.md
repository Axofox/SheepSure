# Comparison across 3 run(s)

Rules: `run-protocol.md`. One row per step + expectation.

**Same checks in every run?** 22 of 35 checks were recorded in all runs. 13 were not (marked 🔀 in the 'Checked in' column).

| Step | Ref | Expected | Checked in | Run 1 | Run 2 | Run 3 | Across runs |
|---|---|---|---|---|---|---|---|
| 1 | F1 | Valid credentials log the user in and land on the products page | all runs | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | C1 | Each product's name, image, description and price match each other everywhere it appears | all runs | [❌ fail](run-1/steps/S01.png) | [❌ fail](run-2/steps/S01.png) | [❌ fail](run-3/steps/S01.png) | **confirmed fail** |
| 1 | C5 | No unexpected console errors or failed network requests | all runs | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 2 | F2 | Clicking 'Add to cart' on Sauce Labs Backpack and Sauce Labs Bike Light adds those products, and each button changes to 'Remove'. | all runs | [⚠️ unsure](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **not verified** |
| 2 | F3 | The cart badge count equals the number of items actually in the cart. | all runs | [⚠️ unsure](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 2 | C1 | A product's name, image, description and price match each other everywhere it appears. | all runs | [❌ fail](run-1/steps/S02.png) | [❌ fail](run-2/steps/S02.png) | [❌ fail](run-3/steps/S02.png) | **confirmed fail** |
| 2 | C4 | No layout breakage, overlapping elements, or unreadable text in the flow. | 🔀 only run 1, 3 | [⚠️ unsure](run-1/steps/S02.png) | [➖ not recorded](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 2 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 3 | F4 | Cart contains exactly the selected products: Sauce Labs Backpack and Sauce Labs Bike Light, with correct names, prices and quantity 1 each | all runs | [❌ fail](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **unstable** |
| 3 | F3 | Cart badge count equals the number of items actually in the cart | all runs | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C2 | The cart link opens the cart page | 🔀 only run 1, 3 | [✅ pass](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 3 | C3 | Any error messages are accurate | 🔀 only run 1 | [✅ pass](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [➖ not recorded](run-3/steps/S03.png) | **not verified** |
| 3 | C4 | No layout breakage or unreadable text | 🔀 only run 1, 2 | [⚠️ unsure](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [➖ not recorded](run-3/steps/S03.png) | **not verified** |
| 3 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C1 | Product name, description and price match everywhere the product appears | 🔀 only run 2, 3 | [➖ not recorded](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 4 | F5 | Clicking Checkout opens the customer information page (checkout-step-one) with empty First Name, Last Name and Postal Code fields ready for input. | all runs | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | F3 | The cart badge shows the number of items actually in the cart. After step 2 that should be 2 (Backpack and Bike Light). | all runs | [⚠️ unsure](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | C2 | Clicking the 'Checkout' button opens the checkout information page. | 🔀 only run 2, 3 | [➖ not recorded](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **not verified** |
| 4 | C4 | No layout breakage or unreadable text. | 🔀 only run 2, 3 | [➖ not recorded](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 5 | F5 | After typing, First Name = "Test", Last Name = "User", Postal Code = "12345". Each field keeps exactly what was typed. | all runs | [❌ fail](run-1/steps/S05.png) | [❌ fail](run-2/steps/S05.png) | [❌ fail](run-3/steps/S05.png) | **confirmed fail** |
| 5 | C4 | No layout breakage, overlapping elements or unreadable text on the checkout information page. | 🔀 only run 1 | [⚠️ unsure](run-1/steps/S05.png) | [➖ not recorded](run-2/steps/S05.png) | [➖ not recorded](run-3/steps/S05.png) | **not verified** |
| 5 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 6 | F5 | Checkout accepts First Name 'Test', Last Name 'User', Postal Code '12345', and each field keeps exactly what was typed; Continue moves on to the overview. | all runs | [❌ fail](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [❌ fail](run-3/steps/S06.png) | **not verified** |
| 6 | F6 | The order overview shows the same items as the cart, with item total = sum of item prices and total = item total + tax. | all runs | [⚠️ unsure](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | C3 | Error messages describe the real problem. | all runs | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | F3 | The cart badge equals the number of items in the cart (2 selected). | 🔀 only run 2, 3 | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 7 | - | the judge returns checks | 🔀 only run 1, 2 | [⚠️ unsure](run-1/steps/S07.png) | [⚠️ unsure](run-2/steps/S07.png) | [➖ not recorded](run-3/steps/S07.png) | **not verified** |
| 7 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | STEP | the agent completes the step | 🔀 only run 2 | [➖ not recorded](run-1/steps/S07.png) | [❌ fail](run-2/steps/S07.png) | [➖ not recorded](run-3/steps/S07.png) | **not verified** |
| 7 | F7 | Clicking Finish shows an order confirmation (checkout-complete page) and the cart is empty afterwards (no badge). | 🔀 only run 3 | [➖ not recorded](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [❌ fail](run-3/steps/S07.png) | **not verified** |
| 7 | F5 | Each checkout field keeps exactly what was typed (First Name 'Test', Last Name 'User', Postal Code '12345'), and valid input is accepted. | 🔀 only run 3 | [➖ not recorded](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [❌ fail](run-3/steps/S07.png) | **not verified** |
| 8 | - | the judge returns checks | all runs | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S08.png) | [✅ pass](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **confirmed pass** |

## Why the AI was unsure

The judge's own words for each check it could not call pass or fail.

- **Step 1 C5, run 1:** 6 console entries, 6 failed requests to events.backtrace.io (third-party only, no visible problem by itself)
- **Step 1 C5, run 2:** 6 console entries, 6 failed requests to events.backtrace.io (third-party only, no visible problem by itself)
- **Step 1 C5, run 3:** 6 console entries, 6 failed requests to events.backtrace.io (third-party only, no visible problem by itself)
- **Step 2 F2, run 1:** The step was not carried out. The agent says its click failed with a tool schema error and was then stopped, so no click reached the page. Page facts show both products with the button still reading 'Add to cart'. Because the app never got the action, these facts cannot show whether Add to cart works.
- **Step 2 F3, run 1:** cart_badge is null and the agent saw the cart link read 'Cart, empty'. Every button reads 'Add to cart', so nothing is in the cart. No badge for an empty cart is consistent. But the step never added anything, so the case this step is meant to check (badge = 2) was not tested.
- **Step 2 F3, run 3:** The badge shows '2', which matches the two items showing 'Remove'. The cart contents have not been read yet, so the facts can't confirm that the badge matches what is really in the cart.
- **Step 2 C4, run 1:** The visible text is complete and readable, with no overlap shown. Product images are probably broken or placeholder images (every one is 'sl-404'), but these facts cannot show how that renders.
- **Step 2 C4, run 3:** The visible text reads normally. The page facts don't show visual layout, so overlap can't be judged. Every product image points to a 404-named asset, which suggests broken images (recorded under C1).
- **Step 3 C4, run 1:** The page facts are text only. They show the expected cart page elements but cannot show layout or overlap problems
- **Step 3 C4, run 2:** The visible text reads in a normal order (header, Your Cart, QTY/Description, the items, Continue Shopping, Checkout, footer). The facts do not cover visual layout or overlap.
- **Step 3 C1, run 2:** In the cart, each name is paired with a matching description (Backpack/Sly Pack text, Bike Light/red light text) and a price. The page facts for this step do not include the products-list values, so the cart cannot be compared with the list. The cart page shows no images (image: null).
- **Step 3 C1, run 3:** Inside the cart, each description fits its product: the Backpack has the 'Sly Pack' text and the Bike Light has the red light text. The prices are the usual catalog prices. The cart page shows no images (image is null), and this step gives no product-list facts to compare against.
- **Step 4 F3, run 1:** cart_badge is null on checkout-step-one. This page lists no items, so these facts can't show whether the cart really holds 2 items (badge display bug) or was emptied (state loss). Earlier step facts aren't available here.
- **Step 4 F3, run 3:** cart_badge is "2". The page facts do not list the cart items on this page, so the badge cannot be checked against the actual contents here. It does match the 2 products selected in the scenario.
- **Step 4 C4, run 2:** The page facts contain no layout information. The visible text reads normally.
- **Step 4 C4, run 3:** The page facts have no layout or visual information (no screenshot facts). The visible text looks normal.
- **Step 5 C4, run 1:** visible_text shows the header, the 'Checkout: Your Information' title, Cancel, and the footer. Input values and the Continue button are not text nodes, so the facts cannot show whether the form looks right. There is no screenshot evidence either way.
- **Step 6 F5, run 2:** Page facts: first-name='Tester', last-name='', postal-code=''. None of the mission values are present. The agent says it typed 'Tester' into Last Name twice and the text ended up in First Name. The page facts match that, but they cannot show which field received the keystrokes. The agent also typed 'Tester' instead of 'User' and never filled Postal Code.
- **Step 6 F6, run 1:** The overview was never reached. URL stayed at https://www.saucedemo.com/checkout-step-one.html, so items and totals could not be checked.
- **Step 6 F6, run 2:** The overview was never reached. URL stays at /checkout-step-one.html, items list is empty, and the error 'Error: Last Name is required' is shown. Cart badge is 2.
- **Step 6 F6, run 3:** The overview was never reached (the URL is still checkout-step-one.html and no items are shown), so the totals could not be checked.
- **Step 7 -, run 1:** the AI judge call failed, so nothing was judged (judge failed: claude failed: {"duration_api_ms":1239,"stop_reason":"stop_sequence","sessio...)
- **Step 7 -, run 2:** the AI judge call failed, so nothing was judged (judge failed: claude failed: {"duration_api_ms":0,"stop_reason":"stop_sequence","session_i...)
- **Step 8 -, run 1:** the AI judge call failed, so nothing was judged (judge failed: claude failed: {"duration_api_ms":0,"stop_reason":"stop_sequence","session_i...)
- **Step 8 -, run 2:** the AI judge call failed, so nothing was judged (judge failed: claude failed: {"duration_api_ms":0,"stop_reason":"stop_sequence","session_i...)
- **Step 8 -, run 3:** the AI judge call failed, so nothing was judged (judge failed: claude failed: {"duration_api_ms":0,"stop_reason":"stop_sequence","session_i...)

## Coverage: what each run explored

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | 4 | 4 | 4 |
| Browser actions taken | 18 | 18 | 20 |
| Paths tried in free exploration | 0 | 0 | 1 |

**Pages not visited by every run:**

- none, all runs visited the same pages

**Actions per step** (element numbers and result pages left out; a step marked ⚠️ was done differently):

| Step | Same in all runs? | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| 1 | ✅ same | 1. type "Username" text="problem_user"<br>2. type "Password" text="secret_sauce"<br>3. click "Login" | 1. type "Username" text="problem_user"<br>2. type "Password" text="secret_sauce"<br>3. click "Login" | 1. type "Username" text="problem_user"<br>2. type "Password" text="secret_sauce"<br>3. click "Login" |
| 2 | ⚠️ **differs** | _no actions_ | 1. click "Add to cart"<br>2. click "Add to cart" | 1. click "Add to cart"<br>2. click "Add to cart" |
| 3 | ⚠️ **differs** | 1. click "Cart, empty" | 1. click "2" | 1. click "2" |
| 4 | ✅ same | 1. click "Checkout" | 1. click "Checkout" | 1. click "Checkout" |
| 5 | ⚠️ **differs** | 1. type "First Name" text="Test"<br>2. type "Last Name" text="User"<br>3. type "Last Name" text="User" | 1. type "First Name" text="Test"<br>2. type "Last Name" text="User" | 1. type "First Name" text="Test"<br>2. type "Last Name" text="User" |
| 6 | ⚠️ **differs** | 1. type "Last Name" text="Tester"<br>2. click "Continue" | 1. type "Last Name" text="Tester"<br>2. click "Continue"<br>3. type "Last Name" text="Tester" | 1. type "Last Name" text="Tester"<br>2. click "Continue" |
| 7 | ⚠️ **differs** | 1. type "Last Name" text="User" | _no actions_ | 1. type "Last Name" text="User" |
| 8 | ⚠️ **differs** | _no actions_ | _no actions_ | 1. type "Last Name" text="Tester" |

**Paths each run tried in free exploration** (as reported by the AI; details in `run-<n>/run.md`):

- **Run 1** (0):
  - none reported
- **Run 2** (0):
  - none reported
- **Run 3** (1):
  - 1. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
