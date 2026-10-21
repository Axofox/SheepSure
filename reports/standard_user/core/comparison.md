# Comparison across 3 run(s)

Rules: `run-protocol.md`. One row per step + expectation.

| Step | Ref | Expected | Run 1 | Run 2 | Run 3 | Across runs |
|---|---|---|---|---|---|---|
| 1 | F1 | Valid credentials log the user in and land on the products page | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | C5 | No unexpected console errors or failed network requests | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 2 | F2 | Clicking 'Add to cart' on Sauce Labs Backpack and Sauce Labs Bike Light adds those products and their buttons change to 'Remove'. | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | F3 | Cart badge count equals the number of items actually in the cart (2 items selected). | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | C5 | No unexpected console errors or failed network requests | [⚠️ unsure](run-1/steps/S02.png) | [⚠️ unsure](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 2 | C1 | Product names, images and prices on the products list match each other for the two added products. | [➖ not recorded](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **not verified** |
| 2 | C4 | No layout breakage, overlapping elements, or unreadable text on the products page | [➖ not recorded](run-1/steps/S02.png) | [➖ not recorded](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 3 | F3 | Cart badge count equals the number of items in the cart (2 items selected, badge shows 2) | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | F4 | Cart contains exactly the selected products: Sauce Labs Backpack ($29.99) and Sauce Labs Bike Light ($9.99), with correct quantities | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C1 | Product name, image, description and price match across the flow | [⚠️ unsure](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [➖ not recorded](run-3/steps/S03.png) | **not verified** |
| 3 | C4 | No layout breakage, overlapping elements or unreadable text on the cart page | [⚠️ unsure](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [➖ not recorded](run-3/steps/S03.png) | **not verified** |
| 3 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 4 | C4 | No layout breakage, overlapping elements, or unreadable text on the checkout step-one page | [⚠️ unsure](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | C2 | Clicking the Checkout button opens the checkout page that the label describes (Checkout: Your Information). | [➖ not recorded](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [➖ not recorded](run-3/steps/S04.png) | **not verified** |
| 4 | F3 | Cart badge count equals the number of items actually in the cart. | [➖ not recorded](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | F5 | Checkout information form loads with First Name, Last Name and Postal Code fields present for input. | [➖ not recorded](run-1/steps/S04.png) | [➖ not recorded](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | C1 | Product name, image, description and price match wherever a product appears. | [➖ not recorded](run-1/steps/S04.png) | [➖ not recorded](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 5 | F5 | Checkout accepts valid First Name (Test), Last Name (User) and Postal Code (12345), and each field keeps exactly what was typed. | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 6 | F6 | Overview shows the same items as the cart; item total = sum of item prices; total = item total + tax | [⚠️ unsure](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 6 | C1 | Product name and price match each other everywhere they appear | [⚠️ unsure](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | C4 | No layout breakage, overlapping elements, or unreadable text in the flow | [⚠️ unsure](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | C2 | Navigation goes where the label says | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [➖ not recorded](run-3/steps/S06.png) | **not verified** |
| 6 | C3 | Error messages are accurate; no false error when none is expected | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [➖ not recorded](run-3/steps/S06.png) | **not verified** |
| 7 | F7 | Finishing shows an order confirmation, and the cart is empty afterwards | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | C4 | No layout breakage, overlapping elements, or unreadable text on the confirmation page | [➖ not recorded](run-1/steps/S07.png) | [⚠️ unsure](run-2/steps/S07.png) | [⚠️ unsure](run-3/steps/S07.png) | **not verified** |
| 8 | F2 | Clicking "Add to cart" on a product adds that product and its button changes to "Remove" | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | F3 | Cart badge count equals the number of items actually in the cart | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | C1 | A product's name, image, description and price match each other everywhere it appears | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C2 | Navigation goes where the label says (e.g. clicking a product opens that product) | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [❌ fail](run-3/steps/S08.png) | **not verified** |
| 8 | C4 | No layout breakage, overlapping elements, or unreadable text in the flow | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S08.png) | [✅ pass](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **confirmed pass** |

## Coverage: what each run explored

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | 7 | 7 | 7 |
| Browser actions taken | 32 | 31 | 31 |
| Paths tried in free exploration | 8 | 5 | 7 |

**Pages not visited by every run:**

- none, all runs visited the same pages

**Paths each run tried in free exploration** (as reported by the AI; details in `run-<n>/run.md`):

- **Run 1** (8):
  - Logged step 4 "click [4] 'Remove'" -> ok, landed on /inventory-item.html. Element [4] in the current list is "View details for Sauce Labs Onesie", a link, not a Remove button. The log label and element don't match, so I can't confirm which element was clicked. I did not verify the removal.
  - Logged step 5 "Back to products" -> ok, now at /inventory.html.
  - Sort dropdown set to "Price (low to high)" (step 6, ok). Visible order on /inventory.html: Sauce Labs Onesie $7.99, Sauce Labs Bike Light $9.99, Sauce Labs Bolt T-Shirt $15.99. Ascending, as the label says. Items after the Bolt T-Shirt are cut off in the page text, so the full order is unverified.
  - Logged step 7 "click [6] 'Add to cart'" -> ok. Current page shows the Sauce Labs Onesie with a "Remove" button and the cart badge at 1. This suggests the Onesie is in the cart, but the log label and element [6] (which is now "Remove") don't match, so this is unconfirmed.
  - Clicked cart badge "1" (step 8) -> ok, now at /cart.html. I did not read the cart contents.
  - Clicked "Sauce Labs Onesie" product name link (step 9) -> ok, now at /inventory-item.html. I did not read the detail page's name, price, or description, so I could not compare them with the list ($7.99, "Rib snap infant onesie for the junior automation engineer in development...").
  - "Back to products" (step 10) -> ok, now at /inventory.html.
  - Sort set to "Price (low to high)" again (step 11) -> ok. Visible order is unchanged: Onesie $7.99, Bike Light $9.99, Bolt T-Shirt $15.99.
- **Run 2** (5):
  - Opened the Sauce Labs Backpack detail page from the product list (click on "Sauce Labs Backpack"), then used "Back to products". Landed on /inventory.html. Did not compare name, image, price or description to the list, so no match check was done for this path.
  - Sort dropdown set to "Price (low to high)" on /inventory.html (ok, still on /inventory.html). I did not read the resulting product order or prices from the page, so I cannot confirm the order matches the label.
  - Sort dropdown changed to "Price (high to low)" on /inventory.html (ok, still on /inventory.html). I did not read the resulting product order, so I cannot confirm the order matches the label.
  - Opened the Sauce Labs Fleece Jacket detail page (/inventory-item.html?id=5). Page text shows: "Sauce Labs Fleece Jacket", description "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.", price "$49.99", button "Add to cart". Cart badge shows 1. I did not compare these against the product list, and I did not check the image.
  - Earlier steps in the log: clicked "Remove" (4) and "Add to cart" (5) on /inventory-item.html, then clicked the cart badge "1" (6), which went to /cart.html. The log says these were ok, but I did not record the badge count or cart contents at each step, so I cannot confirm whether the badge followed each change.
- **Run 3** (7):
  - Product detail "Remove" then cart check: clicked Remove on the product (action 4), the page moved to /inventory-item.html, then I clicked the cart link (action 5), which landed on /cart.html. I did not record the exact cart contents text, so I can't confirm the cart state beyond the URL.
  - Cart -> "Continue Shopping": clicked "Continue Shopping" (action 6) and landed on /inventory.html as expected.
  - Sort dropdown, Price (low to high): selected "Price (low to high)" (action 7). The page stayed at /inventory.html. I did not capture the list order right after this step.
  - Sort dropdown, Price (high to low): selected "Price (high to low)" (action 8). The page stayed at /inventory.html. BUT the current page shows the sort select still reads value="az" (its label is "Name (A to Z)"), and the list text begins "Sauce Labs Backpack $29.99", "Sauce Labs Bike Light $9.99", "Sauce Labs Bolt T-Shirt $15.99", "Sauce Labs Fleece Jacket". That order is A-Z by name, not high-to-low by price. This looks like a bug: the Price (high to low) selection did not reorder the products, or the dropdown reverted. Worth re-checking.
  - Product detail, Fleece Jacket: opened "Sauce Labs Fleece Jacket" from the list (action 9), landed on /inventory-item.html. I did not record the title, price or description text from that page, so I did not compare them with the list.
  - Add to cart on detail page: clicked "Add to cart" (action 10), page stayed on /inventory-item.html. On the later list page, the Fleece Jacket entry shows a "Remove" button (element 15), which suggests the item was added. The cart badge on the current page reads "1".
  - "Back to products" from detail page: clicked "Back to products" (action 11), landed on /inventory.html. The cart badge still reads 1.
