# Comparison across 3 run(s)

Rules: `run-protocol.md`. One row per step + expectation.

| Step | Ref | Expected | Run 1 | Run 2 | Run 3 | Across runs |
|---|---|---|---|---|---|---|
| 1 | F1 | Valid credentials log the user in and land on the products page | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | C1 | A product's name, image, description and price match each other everywhere it appears | [⚠️ unsure](run-1/steps/S01.png) | [➖ not recorded](run-2/steps/S01.png) | [➖ not recorded](run-3/steps/S01.png) | **not verified** |
| 1 | C5 | No unexpected console errors or failed network requests | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 2 | F2 | Add to cart on Sauce Labs Backpack and Sauce Labs Bike Light adds those products and their buttons change to Remove | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | F3 | Cart badge count equals the number of items actually in the cart | [⚠️ unsure](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **not verified** |
| 2 | C1 | Product name, image, description and price match each other where the product appears | [⚠️ unsure](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [➖ not recorded](run-3/steps/S02.png) | **not verified** |
| 2 | C4 | No layout breakage, overlapping elements or unreadable text on the inventory page | [⚠️ unsure](run-1/steps/S02.png) | [➖ not recorded](run-2/steps/S02.png) | [➖ not recorded](run-3/steps/S02.png) | **not verified** |
| 2 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 3 | F3 | Cart badge count equals the number of items actually in the cart (2 items, badge 2) | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | F4 | Cart contains exactly the selected products (Sauce Labs Backpack and Sauce Labs Bike Light) with correct names, prices and quantities | [⚠️ unsure](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 3 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C4 | No layout breakage, overlapping elements, or unreadable text on the cart page | [➖ not recorded](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 3 | C1 | Product name, image, description and price match wherever the product appears | [➖ not recorded](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 4 | C4 | No layout breakage, overlapping elements, or unreadable text on the checkout step-one page | [⚠️ unsure](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | F3 | Cart badge count equals the number of items actually in the cart | [➖ not recorded](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | C1 | Product names, images, descriptions and prices match each other wherever they appear. | [➖ not recorded](run-1/steps/S04.png) | [➖ not recorded](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 5 | F5 | Checkout accepts valid First Name, Last Name, Postal Code, and each field keeps exactly what was typed. Page is on checkout-step-one with no error. | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 6 | F6 | Overview shows the same items as the cart; item total equals the sum of item prices; total equals item total plus tax. | [⚠️ unsure](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 6 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | C1 | Product name and price match wherever the product appears. | [➖ not recorded](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | C4 | No layout breakage, overlapping elements, or unreadable text on the overview. | [➖ not recorded](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 7 | F7 | Finishing shows an order confirmation, and the cart is empty afterwards | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | C4 | No layout breakage, overlapping elements, or unreadable text on the confirmation page | [➖ not recorded](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [⚠️ unsure](run-3/steps/S07.png) | **not verified** |
| 8 | C1 | Fleece Jacket name, description and price on the detail page match the same product's entry on the products list | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C2 | 'Back to products' returns to the products page | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [➖ not recorded](run-3/steps/S08.png) | **not verified** |
| 8 | C4 | No layout breakage, overlapping elements or unreadable text on the detail page | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S08.png) | [✅ pass](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **confirmed pass** |
| 8 | F2 | Add to cart on a product adds that product and the button changes to Remove | [➖ not recorded](run-1/steps/S08.png) | [➖ not recorded](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **not verified** |
| 8 | F3 | Cart badge count equals the number of items actually in the cart | [➖ not recorded](run-1/steps/S08.png) | [➖ not recorded](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |

## Coverage: what each run explored

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | 7 | 7 | 7 |
| Browser actions taken | 31 | 31 | 31 |
| Paths tried in free exploration | 5 | 6 | 3 |

**Pages not visited by every run:**

- none, all runs visited the same pages

**Paths each run tried in free exploration** (as reported by the AI; details in `run-<n>/run.md`):

- **Run 1** (5):
  - Opened "Sauce Labs Onesie" detail page (inventory-item.html), then clicked "Back to products" and landed on /inventory.html. I did not capture the Onesie detail page's name, price or description text in what I observed, so I cannot confirm they match the list.
  - On the products page, clicked "Remove" (action 6), returned to /inventory.html. I did not capture the cart badge value after this step.
  - Used the sort dropdown three times in sequence: "Price (low to high)", then "Name (Z to A)", then "Price (high to low)". Each select was logged as ok and the page stayed on /inventory.html. I did not capture the resulting product order after any of these, so I cannot confirm the order matched each label.
  - Opened "Sauce Labs Fleece Jacket" detail page (inventory-item.html?id=5). Page text shows the name "Sauce Labs Fleece Jacket", the description "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.", and the price "$49.99". The button shows "Remove" and the cart badge shows 1.
  - On the Fleece Jacket detail page, clicked "Add to cart" (action 11), logged ok. The page now shows "Remove" and cart badge 1. This is consistent with the cart holding only the jacket after the earlier Remove.
- **Run 2** (6):
  - Opened the "Sauce Labs Backpack" detail page (click on product link, now at /inventory-item.html), then clicked "Add to cart" on that page (action ok, still at /inventory-item.html). Cart badge afterwards showed 1 on the current page. I did not check the detail page's name, price or description against the list.
  - Clicked "Back to products" from the Backpack detail page; returned to /inventory.html. Did not verify that the list was unchanged or that the Backpack still showed "Remove" rather than "Add to cart".
  - Used the sort dropdown and selected "Price (low to high)"; action ok, page at /inventory.html. I did NOT read the resulting product order, so I cannot say whether the order matches the label. This is a required check still open.
  - Opened the "Sauce Labs Bike Light" detail page (/inventory-item.html) and then clicked "Back to products" (/inventory.html). I did not add the Bike Light to the cart and did not compare its detail-page name, price or description with the list.
  - Clicked the cart badge link "1" from the products page; landed on /cart.html. I did not read the cart contents, so I cannot confirm that the item and its price match.
  - From /cart.html clicked "Checkout"; landed on /checkout-step-one.html titled "Checkout: Your Information". Fields First Name, Last Name and Zip/Postal Code are empty (value=""), with "Cancel" and "Continue" buttons.
- **Run 3** (3):
  - Actions 4-6: on an inventory-item (product detail) page, clicked "Add to cart" (ok), then "Remove" (ok), then "Back to products" (ok, now /inventory.html). I did not record the product name on that detail page or the cart badge after each step, so I cannot confirm the badge followed the add and remove.
  - Action 7: set the products sort dropdown to "Price (low to high)" (ok). The dropdown shows value "lohi". The visible order is Sauce Labs Onesie $7.99, Sauce Labs Bike Light $9.99, Sauce Labs Bolt T-Shirt $15.99, which is ascending. The remaining items' prices are cut off in the page text, so the full order is not verified.
  - Actions 8-11: opened "View details for Sauce Labs Onesie" (ok, now /inventory-item.html), clicked "Add to cart" (ok), clicked "Back to products" (ok), then re-selected "Price (low to high)" (ok). On the final list, Sauce Labs Onesie shows a "Remove" button and the cart badge reads 1. I did not capture the detail page's name, price or description, so I could not compare them with the list values ($7.99; "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.").
