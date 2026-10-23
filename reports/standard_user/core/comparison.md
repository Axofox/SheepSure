# Comparison across 3 run(s)

Rules: `run-protocol.md`. One row per step + expectation.

**Same checks in every run?** 24 of 37 checks were recorded in all runs. 13 were not (marked 🔀 in the 'Checked in' column).

| Step | Ref | Expected | Checked in | Run 1 | Run 2 | Run 3 | Across runs |
|---|---|---|---|---|---|---|---|
| 1 | F1 | Valid credentials (standard_user / secret_sauce) log the user in and land on the products page | all runs | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | F3 | The cart badge count equals the number of items in the cart (none yet after login) | 🔀 only run 1 | [✅ pass](run-1/steps/S01.png) | [➖ not recorded](run-2/steps/S01.png) | [➖ not recorded](run-3/steps/S01.png) | **not verified** |
| 1 | C1 | Each product's name, image, description and price match each other on the products list | all runs | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | C5 | No unexpected console errors or failed network requests | all runs | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 2 | F2 | Clicking 'Add to cart' on Sauce Labs Backpack and Sauce Labs Bike Light adds those products, and their buttons change to 'Remove' | all runs | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | F3 | The cart badge count equals the number of items in the cart (2) | all runs | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | C1 | Each product's name, image, description and price match each other on the products page | all runs | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | C4 | No broken layout, overlapping elements or unreadable text. | 🔀 only run 2 | [➖ not recorded](run-1/steps/S02.png) | [⚠️ unsure](run-2/steps/S02.png) | [➖ not recorded](run-3/steps/S02.png) | **not verified** |
| 3 | F3 | Cart badge count equals number of items in the cart (2) | all runs | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | F4 | Cart contains exactly Sauce Labs Backpack and Sauce Labs Bike Light with correct names, prices and quantities | all runs | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C1 | Each product's name, image, description and price match each other everywhere it appears | all runs | [⚠️ unsure](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 3 | C4 | No layout breakage, overlapping elements or unreadable text | all runs | [⚠️ unsure](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 3 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C2 | The cart link opens the cart page | 🔀 only run 2, 3 | [➖ not recorded](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 3 | C3 | No inaccurate error messages | 🔀 only run 3 | [➖ not recorded](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 4 | C2 | Clicking "Checkout" in the cart opens the checkout information page (checkout-step-one) titled "Checkout: Your Information". | all runs | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | F3 | The cart badge still equals the 2 items in the cart (Backpack and Bike Light from step 2), with nothing changed by navigating. | all runs | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | F5 | The checkout form shows empty First Name, Last Name and Postal Code fields, ready for input. Whether it accepts and keeps the values is tested in step 5. | 🔀 only run 1, 2 | [⚠️ unsure](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [➖ not recorded](run-3/steps/S04.png) | **not verified** |
| 4 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | C4 | No layout breakage or unreadable text on the checkout information page | 🔀 only run 2 | [➖ not recorded](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [➖ not recorded](run-3/steps/S04.png) | **not verified** |
| 4 | C3 | No error message appears when checkout first opens. | 🔀 only run 3 | [➖ not recorded](run-1/steps/S04.png) | [➖ not recorded](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **not verified** |
| 5 | F5 | First Name, Last Name and Postal Code fields hold exactly what was typed: 'Test', 'User', '12345' (TS-002 read-back), and no error appears for valid input. | all runs | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | F3 | The cart badge equals the number of items in the cart (2: Backpack and Bike Light). | all runs | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | C4 | No layout breakage, overlapping or unreadable text | 🔀 only run 2 | [➖ not recorded](run-1/steps/S05.png) | [⚠️ unsure](run-2/steps/S05.png) | [➖ not recorded](run-3/steps/S05.png) | **not verified** |
| 6 | F6 | The overview lists the same items as the cart (Sauce Labs Backpack and Sauce Labs Bike Light, quantity 1 each). Item total equals the sum of the item prices, and Total equals Item total plus Tax. | all runs | [✅ pass](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 6 | C1 | Each product's name, description and price are the same here as everywhere else it appears. | 🔀 only run 1, 3 | [✅ pass](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 6 | C4 | No broken layout, overlapping elements or unreadable text. | 🔀 only run 1 | [⚠️ unsure](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [➖ not recorded](run-3/steps/S06.png) | **not verified** |
| 6 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | F5 | Each checkout field keeps exactly what was typed (Test / User / 12345). | 🔀 only run 2 | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [➖ not recorded](run-3/steps/S06.png) | **not verified** |
| 6 | F3 | The cart badge count equals the number of items in the cart (2 selected products). | 🔀 only run 2, 3 | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 7 | F7 | Clicking Finish shows an order confirmation, and the cart is empty afterwards (no badge, no items). | all runs | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | C4 | No layout breakage, overlapping elements, or unreadable text in the flow | 🔀 only run 3 | [➖ not recorded](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [⚠️ unsure](run-3/steps/S07.png) | **not verified** |
| 8 | - | the judge returns checks | all runs | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C5 | No unexpected console errors or failed network requests | all runs | [✅ pass](run-1/steps/S08.png) | [✅ pass](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **confirmed pass** |

## Why the AI was unsure

The judge's own words for each check it could not call pass or fail.

- **Step 1 C5, run 1:** 6 console entries, 6 failed requests to events.backtrace.io (third-party only, no visible problem by itself)
- **Step 1 C5, run 2:** 6 console entries, 6 failed requests to events.backtrace.io (third-party only, no visible problem by itself)
- **Step 1 C5, run 3:** 6 console entries, 6 failed requests to events.backtrace.io (third-party only, no visible problem by itself)
- **Step 2 C4, run 2:** The page facts contain no layout or rendering information (no screenshot data), so layout cannot be judged from them.
- **Step 3 C1, run 1:** Names, descriptions and prices fit each other (Backpack: Sly Pack description, $29.99; Bike Light: red light description, $9.99). Image is null for both items in the page facts, and this step has no product-list facts to compare against, so image consistency can't be judged
- **Step 3 C1, run 2:** Names, descriptions and prices on the cart page belong together: Backpack 'carry.allTheThings()… Sly Pack' $29.99; Bike Light 'A red light…' $9.99. The cart page shows no images (image null). The page facts for this step do not include the products-list values, so there is nothing here to compare against.
- **Step 3 C4, run 1:** Page facts contain only text and data, no layout or visual information; the visible text is complete and in order
- **Step 3 C4, run 2:** The page facts have no layout or visual information. The visible text looks complete and in order.
- **Step 3 C4, run 3:** The page facts are text only and include no screenshot or layout information
- **Step 4 F5, run 1:** The inputs first-name, last-name and postal-code are present and all empty (""), with no error message. The page facts do not show whether the "Continue" button exists: it is likely an input element, so it does not appear in visible_text. That claim comes only from the agent report. Accepting and keeping the values has not been tested yet.
- **Step 4 C4, run 2:** The page facts show the title, Cancel, the footer and the three inputs. The 'Continue' button the agent mentions does not appear in visible_text, but it is probably a submit input whose label is not part of innerText. The facts cannot confirm the layout visually
- **Step 5 C4, run 2:** Page facts contain only visible text and field values. Layout and rendering cannot be checked from these facts.
- **Step 6 F6, run 2:** The page is still https://www.saucedemo.com/checkout-step-one.html ('Checkout: Your Information'). The overview was not reached, no items are listed and no totals are shown. The agent reports that Continue was never clicked because its own safety check stopped the action. The app did not reject anything: there is no error message, console entry or failed request.
- **Step 6 C4, run 1:** The page facts include only text and DOM data, with no visual or screenshot evidence. Layout cannot be judged.
- **Step 7 C4, run 3:** The page facts contain only text and no layout or screenshot data. The visible text reads cleanly in a logical order, but layout cannot be checked from these facts.
- **Step 8 -, run 1:** the AI judge call failed, so nothing was judged (judge failed: claude failed: {"duration_api_ms":0,"stop_reason":"stop_sequence","session_i...)
- **Step 8 -, run 2:** the AI judge call failed, so nothing was judged (judge failed: claude failed: {"duration_api_ms":0,"stop_reason":"stop_sequence","session_i...)
- **Step 8 -, run 3:** the AI judge call failed, so nothing was judged (judge failed: claude failed: {"duration_api_ms":0,"stop_reason":"stop_sequence","session_i...)

## Coverage: what each run explored

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | 7 | 6 | 7 |
| Browser actions taken | 23 | 19 | 25 |
| Paths tried in free exploration | 4 | 0 | 6 |

**Pages not visited by every run:**

- `/inventory-item.html`: only in run(s) 1, 3

**Actions per step** (element numbers and result pages left out; a step marked ⚠️ was done differently):

| Step | Same in all runs? | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| 1 | ✅ same | 1. type "Username" text="standard_user"<br>2. type "Password" text="secret_sauce"<br>3. click "Login" | 1. type "Username" text="standard_user"<br>2. type "Password" text="secret_sauce"<br>3. click "Login" | 1. type "Username" text="standard_user"<br>2. type "Password" text="secret_sauce"<br>3. click "Login" |
| 2 | ✅ same | 1. click "Add to cart"<br>2. click "Add to cart" | 1. click "Add to cart"<br>2. click "Add to cart" | 1. click "Add to cart"<br>2. click "Add to cart" |
| 3 | ✅ same | 1. click "2" | 1. click "2" | 1. click "2" |
| 4 | ✅ same | 1. click "Checkout" | 1. click "Checkout" | 1. click "Checkout" |
| 5 | ✅ same | 1. type "First Name" text="Test"<br>2. type "Last Name" text="User"<br>3. type "Zip/Postal Code" text="12345" | 1. type "First Name" text="Test"<br>2. type "Last Name" text="User"<br>3. type "Zip/Postal Code" text="12345" | 1. type "First Name" text="Test"<br>2. type "Last Name" text="User"<br>3. type "Zip/Postal Code" text="12345" |
| 6 | ⚠️ **differs** | 1. click "Continue" | _no actions_ | 1. click "Continue" |
| 7 | ⚠️ **differs** | 1. click "Finish" | 1. click "Continue"<br>2. click "Finish" | 1. click "Finish" |
| 8 | ⚠️ **differs** | 1. click "Back Home"<br>2. select "Name (A to Z) Name (Z to A) Price (low to high) Price (high " text="Price (low to high)"<br>3. click "Sauce Labs Bike Light"<br>4. click "Add to cart" | _no actions_ | 1. click "Back Home"<br>2. select "Name (A to Z) Name (Z to A) Price (low to high) Price (high " text="Price (low to high)"<br>3. select "Name (A to Z) Name (Z to A) Price (low to high) Price (high " text="Price (high to low)"<br>4. click "Sauce Labs Backpack"<br>5. click "Add to cart"<br>6. click "Remove" |

**Paths each run tried in free exploration** (as reported by the AI; details in `run-<n>/run.md`):

- **Run 1** (4):
  - 1. click [3] "Back Home" -> ok; now at /inventory.html
  - 2. select [3] "Name (A to Z) Name (Z to A) Price (low to high) Price (high " text="Price (low to high)" -> ok; now at /inventory.html
  - 3. click [8] "Sauce Labs Bike Light" -> ok; now at /inventory-item.html
  - 4. click [4] "Add to cart" -> ok; now at /inventory-item.html
- **Run 2** (0):
  - none reported
- **Run 3** (6):
  - 1. click [3] "Back Home" -> ok; now at /inventory.html
  - 2. select [3] "Name (A to Z) Name (Z to A) Price (low to high) Price (high " text="Price (low to high)" -> ok; now at /inventory.html
  - 3. select [3] "Name (A to Z) Name (Z to A) Price (low to high) Price (high " text="Price (high to low)" -> ok; now at /inventory.html
  - 4. click [8] "Sauce Labs Backpack" -> ok; now at /inventory-item.html
  - 5. click [4] "Add to cart" -> ok; now at /inventory-item.html
  - 6. click [4] "Remove" -> ok; now at /inventory-item.html
