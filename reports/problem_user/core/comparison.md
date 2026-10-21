# Comparison across 3 run(s)

Rules: `run-protocol.md`. One row per step + expectation.

| Step | Ref | Expected | Run 1 | Run 2 | Run 3 | Across runs |
|---|---|---|---|---|---|---|
| 1 | F1 | Valid credentials log the user in and land on the products page | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | C1 | Each product's name, image, description and price match each other everywhere they appear | [❌ fail](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 1 | C4 | No layout breakage, overlapping elements, or unreadable text on the products page | [⚠️ unsure](run-1/steps/S01.png) | [➖ not recorded](run-2/steps/S01.png) | [➖ not recorded](run-3/steps/S01.png) | **not verified** |
| 1 | C5 | No unexpected console errors or failed network requests | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 2 | F2 | Add to cart on Sauce Labs Backpack and Sauce Labs Bike Light adds those products and their buttons change to Remove; other products are untouched. | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | F3 | Cart badge count equals the number of items in the cart. | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 2 | C1 | Each product's name, image, description and price match each other. | [❌ fail](run-1/steps/S02.png) | [⚠️ unsure](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 2 | C4 | No layout breakage, overlapping elements, or unreadable text on the products page. | [⚠️ unsure](run-1/steps/S02.png) | [➖ not recorded](run-2/steps/S02.png) | [➖ not recorded](run-3/steps/S02.png) | **not verified** |
| 2 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 3 | F3 | Cart badge count equals the number of items actually in the cart (2 items, so badge 2) | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | F4 | Cart contains exactly the selected products (Sauce Labs Backpack and Sauce Labs Bike Light) with correct names, prices and quantities | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C1 | Product name, image, description and price match each other everywhere they appear | [➖ not recorded](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 3 | C2 | Clicking the cart icon navigates to the cart | [➖ not recorded](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 3 | C4 | No layout breakage, overlapping elements or unreadable text on the cart page | [➖ not recorded](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 4 | F5 | Checkout page opens with First Name, Last Name and Postal Code fields present and ready for input | [✅ pass](run-1/steps/S04.png) | [➖ not recorded](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | F3 | Cart badge count equals the number of items in the cart, as shown on this page | [⚠️ unsure](run-1/steps/S04.png) | [➖ not recorded](run-2/steps/S04.png) | [➖ not recorded](run-3/steps/S04.png) | **not verified** |
| 4 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 5 | F5 | Checkout accepts First Name 'Test', Last Name 'User', Postal Code '12345', and each field keeps exactly what was typed. | [❌ fail](run-1/steps/S05.png) | [❌ fail](run-2/steps/S05.png) | [❌ fail](run-3/steps/S05.png) | **confirmed fail** |
| 5 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | STEP | the agent completes the step | [❌ fail](run-1/steps/S05.png) | [❌ fail](run-2/steps/S05.png) | [❌ fail](run-3/steps/S05.png) | **confirmed fail** |
| 5 | C4 | No layout breakage, overlapping elements or unreadable text on the checkout information page | [➖ not recorded](run-1/steps/S05.png) | [⚠️ unsure](run-2/steps/S05.png) | [➖ not recorded](run-3/steps/S05.png) | **not verified** |
| 6 | F5 | Checkout accepts valid First Name, Last Name and Postal Code, and each field keeps exactly what was typed (First Name Test, Last Name User, Postal Code 12345). | [⚠️ unsure](run-1/steps/S06.png) | [❌ fail](run-2/steps/S06.png) | [❌ fail](run-3/steps/S06.png) | **not verified** |
| 6 | F6 | The overview shows the same items as the cart, with item total equal to the sum of item prices and total equal to item total plus tax. | [⚠️ unsure](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | STEP | the agent completes the step | [❌ fail](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [➖ not recorded](run-3/steps/S06.png) | **not verified** |
| 6 | C3 | Error messages are accurate and describe the real problem | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 7 | F7 | Finishing the order shows an order confirmation, and the cart is empty afterwards. | [⚠️ unsure](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [➖ not recorded](run-3/steps/S07.png) | **not verified** |
| 7 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | F5 | Checkout accepts valid First Name 'Test', Last Name 'User', Postal Code '12345', and each field keeps exactly what was typed. | [➖ not recorded](run-1/steps/S07.png) | [⚠️ unsure](run-2/steps/S07.png) | [❌ fail](run-3/steps/S07.png) | **not verified** |
| 7 | C3 | Error messages are accurate and describe the real problem. | [➖ not recorded](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [⚠️ unsure](run-3/steps/S07.png) | **not verified** |
| 7 | STEP | the agent completes the step | [➖ not recorded](run-1/steps/S07.png) | [❌ fail](run-2/steps/S07.png) | [❌ fail](run-3/steps/S07.png) | **not verified** |
| 8 | C1 | Product name, image, description and price match across the list and the detail page (here: Sauce Labs Backpack, from the Backpack detail page vs the products list). | [⚠️ unsure](run-1/steps/S08.png) | [➖ not recorded](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C4 | No layout breakage, overlapping elements or unreadable text on the pages passed through in this step. | [⚠️ unsure](run-1/steps/S08.png) | [➖ not recorded](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S08.png) | [✅ pass](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **confirmed pass** |
| 8 | F5 | Checkout Step One accepts valid First Name, Last Name and Postal Code, and each field keeps exactly what was typed | [➖ not recorded](run-1/steps/S08.png) | [❌ fail](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | C3 | The error message describes the real problem | [➖ not recorded](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | F3 | Cart badge count equals the number of items actually in the cart | [➖ not recorded](run-1/steps/S08.png) | [➖ not recorded](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **not verified** |
| 8 | C2 | Navigation and labelled controls do what their label says: the product link opens that product, 'Back to products' returns to the list, and the sort option produces the order its label names | [➖ not recorded](run-1/steps/S08.png) | [➖ not recorded](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |

## Coverage: what each run explored

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | 5 | 4 | 5 |
| Browser actions taken | 49 | 48 | 56 |
| Paths tried in free exploration | 5 | 5 | 4 |

**Pages not visited by every run:**

- `/inventory-item.html`: only in run(s) 1, 3

**Paths each run tried in free exploration** (as reported by the AI; details in `run-<n>/run.md`):

- **Run 1** (5):
  - Cart page, clicked "Cancel" (action 4), then "Remove" (actions 5 and 6). Result: stayed on /cart.html. I did not read the cart contents or badge after each removal in my log, so I can't quote them.
  - From the cart, clicked "Continue Shopping" (action 7). Result: landed on /inventory.html.
  - On the products page, selected "Price (low to high)" in the sort dropdown (action 8), then waited (action 9). Result: the page stayed on /inventory.html. I did not read the product order or prices afterward, so I cannot confirm whether the order matches the label. This is NOT VERIFIED.
  - Opened the product detail page for "Sauce Labs Backpack" via "View details" (action 10). Result: URL /inventory-item.html. I did not record the name, price or description on that page versus the list, so this is NOT VERIFIED for those fields.
  - On the Backpack detail page, clicked "Add to cart" (action 11). Result: the action was logged as ok, but the next page I observed is /inventory-item.html?id=5, titled "Sauce Labs Fleece Jacket" ($49.99, "Add to cart" button still shown), with the cart link reading "Cart, empty" and no cart badge. This is UNCLEAR and suspicious: I expected the Backpack page (id=4) and a badge showing 1 after adding it. Either the page changed to a different product (id=5) unexpectedly, or the cart did not update. I could not check which, since I ran out of actions.
- **Run 2** (5):
  - Checkout Step One, Last Name typed "Tester" (action 4). Tool reported ok, but the page did not keep a value for it.
  - Checkout Step One, Last Name typed "Customer" three times (actions 5, 6, 7). Each reported ok. On the current page the field value is still "" (empty).
  - Checkout Step One, clicked "Dismiss error" (action 8). Page stayed on /checkout-step-one.html.
  - Checkout Step One, Last Name typed "Tester" again (action 9), then clicked "Continue" (action 10). Page stayed on /checkout-step-one.html and showed "Error: Last Name is required". Field value is "".
  - First Name shows value "Tester", Zip/Postal Code shows value "12345", so those two fields do keep input. Only Last Name fails.
- **Run 3** (4):
  - Sort dropdown, "Price (low to high)". I selected "Price (low to high)" in the sort select (element [3]) twice. Both selects returned ok and the page stayed at /inventory.html. The select's current value in the element list is value="az". The product order on the page is Sauce Labs Backpack $29.99, Sauce Labs Bike Light $9.99, Sauce Labs Bolt T-Shirt $15.99, Sauce Labs Fleece Jacket, Sauce Labs Onesie, Test.allTheThings() T-Shirt (Red). That is alphabetical (A to Z) order, not price ascending, which would start with $9.99. Likely bug: the price sort is not applied.
  - Product detail page and back navigation, Sauce Labs Backpack. I clicked the "Sauce Labs Backpack" product link (element [3]) and landed on /inventory-item.html. I clicked "Add to cart" (element [4]), which returned ok, then clicked "Back to products" (element [3]) and landed on /inventory.html. I did not capture the detail page's name, price or description text in my action log, so I cannot confirm them against the list entry ("Sauce Labs Backpack", $29.99, "carry.allTheThings() with the sleek, streamlined Sly Pack...").
  - Cart badge after add-to-cart. After the Backpack add-to-cart and return to the list, the cart badge reads "2". The list shows "Remove" buttons for Sauce Labs Backpack and Sauce Labs Bike Light, which matches two items. I did not record the badge value before the add, so I cannot say whether it incremented by exactly 1.
  - Checkout step one, then cancel. On /checkout-step-one.html I typed "Tester" into the Last Name field (element [4]), clicked "Dismiss error" (element [6]), which returned ok and kept me on the same page, and then clicked "Cancel" (element [6]), which took me to /cart.html. I did not capture the error text itself, so I cannot quote what the error said.
