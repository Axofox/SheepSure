# Comparison across 3 run(s)

Rules: `run-protocol.md`. One row per step + expectation.

| Step | Ref | Expected | Run 1 | Run 2 | Run 3 | Across runs |
|---|---|---|---|---|---|---|
| 1 | F1 | Valid credentials log the user in and land on the products page | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | C1 | Each product's name, image, description and price match each other everywhere it appears | [❌ fail](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 1 | C4 | No layout breakage, overlapping elements, or unreadable text in the flow | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [➖ not recorded](run-3/steps/S01.png) | **not verified** |
| 1 | C5 | No unexpected console errors or failed network requests | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 2 | F2 | Clicking 'Add to cart' on Sauce Labs Backpack and Sauce Labs Bike Light adds those products, and each button changes to 'Remove'. Other products are unaffected. | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | F3 | Cart badge count equals the number of items actually in the cart. | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | C1 | Each product's name, image, description and price match each other everywhere they appear. | [❌ fail](run-1/steps/S02.png) | [⚠️ unsure](run-2/steps/S02.png) | [❌ fail](run-3/steps/S02.png) | **not verified** |
| 2 | C5 | No unexpected console errors or failed network requests | [⚠️ unsure](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **not verified** |
| 2 | C4 | No layout breakage or unreadable text on the products page | [➖ not recorded](run-1/steps/S02.png) | [⚠️ unsure](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 3 | F3 | Cart badge count equals the number of items in the cart (2 items, badge 2) | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | F4 | Cart contains exactly the selected products with correct names, prices and quantities (Backpack $29.99, Bike Light $9.99) | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C4 | No layout breakage, overlapping elements, or unreadable text on the cart page | [⚠️ unsure](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 3 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C1 | Product name, description and price in the cart match the same product elsewhere (products page). | [➖ not recorded](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 4 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | F4 | Cart still holds the selected products (names, prices, quantities) when checkout starts | [➖ not recorded](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [➖ not recorded](run-3/steps/S04.png) | **not verified** |
| 4 | F5 | Checkout 'Your Information' page loads with fields ready to accept input | [➖ not recorded](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | C4 | No layout breakage, overlapping elements or unreadable text on the checkout information page | [➖ not recorded](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [➖ not recorded](run-3/steps/S04.png) | **not verified** |
| 4 | F3 | Cart badge count equals the number of items in the cart. | [➖ not recorded](run-1/steps/S04.png) | [➖ not recorded](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 5 | F5 | Checkout accepts valid First Name 'Test', Last Name 'User' and Postal Code '12345', and each field keeps exactly what was typed. | [❌ fail](run-1/steps/S05.png) | [❌ fail](run-2/steps/S05.png) | [❌ fail](run-3/steps/S05.png) | **confirmed fail** |
| 5 | C4 | No layout breakage, overlapping elements, or unreadable text on the checkout information page. | [⚠️ unsure](run-1/steps/S05.png) | [➖ not recorded](run-2/steps/S05.png) | [⚠️ unsure](run-3/steps/S05.png) | **not verified** |
| 5 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | STEP | the agent completes the step | [❌ fail](run-1/steps/S05.png) | [❌ fail](run-2/steps/S05.png) | [❌ fail](run-3/steps/S05.png) | **confirmed fail** |
| 6 | F5 | Checkout accepts valid First Name (Test), Last Name (User) and Postal Code (12345), and each field keeps exactly what was typed; Continue moves to the overview. | [❌ fail](run-1/steps/S06.png) | [❌ fail](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | F6 | Overview reached and shows the cart items, item total and tax. | [⚠️ unsure](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | C3 | Error message describes the real problem. | [✅ pass](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 6 | C4 | No layout breakage, overlapping elements or unreadable text on the checkout page. | [⚠️ unsure](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 7 | F7 | Finishing shows an order confirmation and the cart is empty afterwards. | [⚠️ unsure](run-1/steps/S07.png) | [⚠️ unsure](run-2/steps/S07.png) | [⚠️ unsure](run-3/steps/S07.png) | **not verified** |
| 7 | F5 | Checkout accepts valid First Name, Last Name and Postal Code, and each field keeps exactly what was typed (mission step 5: Test / User / 12345). | [❌ fail](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [➖ not recorded](run-3/steps/S07.png) | **not verified** |
| 7 | C5 | No unexpected console errors or failed network requests | [❌ fail](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **unstable** |
| 7 | STEP | the agent completes the step | [❌ fail](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [➖ not recorded](run-3/steps/S07.png) | **not verified** |
| 8 | F5 | Checkout step one accepts valid First Name, Last Name and Postal Code, and each field keeps exactly what was typed (Last Name should hold the typed text, e.g. "Tester", and Continue should advance to checkout-step-two). | [❌ fail](run-1/steps/S08.png) | [➖ not recorded](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | C3 | If Continue is blocked, any error message shown accurately describes the real problem (for example, that Last Name is missing or invalid). | [⚠️ unsure](run-1/steps/S08.png) | [➖ not recorded](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | C4 | No layout breakage, overlapping elements, or unreadable text on the checkout step one page. | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S08.png) | [✅ pass](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **confirmed pass** |
| 8 | C1 | Product name, image, description and price match each other everywhere they appear (the Bike Light detail page should match the list). | [➖ not recorded](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C2 | Clicking a product name opens that product's detail page, and 'Back to products' returns to the list. | [➖ not recorded](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [❌ fail](run-3/steps/S08.png) | **not verified** |

## Coverage: what each run explored

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | 4 | 5 | 5 |
| Browser actions taken | 47 | 53 | 38 |
| Paths tried in free exploration | 2 | 3 | 8 |

**Pages not visited by every run:**

- `/inventory-item.html`: only in run(s) 2, 3

**Paths each run tried in free exploration** (as reported by the AI; details in `run-<n>/run.md`):

- **Run 1** (2):
  - Checkout step one, Last Name field. I typed "Tester" into [4] "Last Name" several times (actions 2, 4, 6, 8) and once "Lastname" (action 3). Each type reported ok, but the page still shows input:text "Last Name" value="" and the URL stays /checkout-step-one.html. Clicking Continue (action 7) did not advance to checkout-step-two. Clicking "Dismiss error" (action 9) left me on the same page. The First Name ("Tester") and Zip/Postal Code ("12345") fields keep their values. Result: the Last Name field appears not to retain typed input, so a customer cannot finish checkout step one. This looks like a real bug, but I did not capture the exact error text shown on Continue, so the exact message is unknown.
  - Cart badge and checkout header were visible throughout (badge "2", header "Checkout: Your Information"). Not tested further: product detail pages and sort dropdown (outside the actions used here).
- **Run 2** (3):
  - Checkout step one: typed "Tester" into the Last Name field twice (actions 3-4), then clicked "Dismiss error" (action 5), then "Cancel" (action 6). Each action reported ok and I ended on /cart.html. I did not record the exact error text, so I cannot quote it.
  - Product detail page: clicked "Sauce Labs Bike Light" (action 7), landed on /inventory-item.html, then clicked "Back to products" (action 8) and returned to /inventory.html. I did not record the detail page's name, price or description, so I did not verify they match the list ($9.99, description "A red light isn't the desired state in testing but it sure helps when riding your bike at night..."). This comparison is NOT confirmed.
  - Sort dropdown: selected "Price (low to high)" twice (actions 9-10). Both reported ok and the URL stayed /inventory.html, but the dropdown still shows value="az" ("Name (A to Z)") and the list did not change to price order. The visible order is Sauce Labs Backpack $29.99, Sauce Labs Bike Light $9.99, Sauce Labs Bolt T-Shirt $15.99, Sauce Labs Fleece Jacket, Sauce Labs Onesie, Test.allTheThings() T-Shirt (Red). That is alphabetical by name, not low-to-high by price. BUG: the "Price (low to high)" option does not apply its sort on this page (problem_user account). I did not try "Price (high to low)" or "Name (Z to A)", so I cannot say whether those work.
- **Run 3** (8):
  - Checkout step one: typed "Tester" into [4] "Last Name" (action 4). Result: ok, page moved to /checkout-step-one.html. I did not see the field values or any validation message after that.
  - Checkout step one: clicked [2] "2" (action 5). Result: ok, page moved to /cart.html. The label "2" is ambiguous, and I did not check what it was.
  - Cart: clicked "Remove" [6] (action 6), then "Remove" [4] (action 7). Both returned ok, page stayed at /cart.html. I did not read the cart contents or badge after these removals, so I can't confirm the badge followed them.
  - Continue Shopping: clicked [3] "Continue Shopping" (action 8). Result: ok, page went to /inventory.html.
  - Product detail: clicked the "Sauce Labs Backpack" name link [5] (action 9). Result: ok, page went to /inventory-item.html. I did not capture the detail page's name, image, price or description, so I did not compare them with the list.
  - Back to products: clicked [3] "Back to products" (action 10). Result: ok, page returned to /inventory.html.
  - Sort dropdown: selected "Price (low to high)" in [3] (action 11). The action returned ok and the URL stayed /inventory.html. However, the current page shows the dropdown still at value="az" (the Name (A to Z) option), and the listed order is Sauce Labs Backpack $29.99, Sauce Labs Bike Light $9.99, Sauce Labs Bolt T-Shirt $15.99. That is not ascending by price, so the sort either did not apply or applied incorrectly. This is a likely bug to verify.
  - Sort label text: the page text reads "Name (A to Z) Name (A to Z) Name (Z to A) Price (low to high) Price (high to low)", which lists "Name (A to Z)" twice. This may be a rendering artifact, but I did not verify it.
