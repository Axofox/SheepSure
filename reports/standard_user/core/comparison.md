# Comparison across 3 run(s)

Rules: `run-protocol.md`. One row per step + expectation.

| Step | Ref | Expected | Run 1 | Run 2 | Run 3 | Across runs |
|---|---|---|---|---|---|---|
| 1 | F1 | Valid credentials (standard_user / secret_sauce) log the user in and land on the products page | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | F3 | The cart badge count equals the number of items in the cart (none yet after login) | [✅ pass](run-1/steps/S01.png) | [➖ not recorded](run-2/steps/S01.png) | [➖ not recorded](run-3/steps/S01.png) | **not verified** |
| 1 | C1 | Each product's name, image, description and price match each other on the products list | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | C5 | No unexpected console errors or failed network requests | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 2 | F2 | Clicking 'Add to cart' on Sauce Labs Backpack and Sauce Labs Bike Light adds those products, and their buttons change to 'Remove' | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | F3 | The cart badge count equals the number of items in the cart (2) | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | C1 | Each product's name, image, description and price match each other on the products page | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 2 | C4 | No broken layout, overlapping elements or unreadable text. | [➖ not recorded](run-1/steps/S02.png) | [⚠️ unsure](run-2/steps/S02.png) | [➖ not recorded](run-3/steps/S02.png) | **not verified** |
| 3 | F3 | Cart badge count equals number of items in the cart (2) | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | F4 | Cart contains exactly Sauce Labs Backpack and Sauce Labs Bike Light with correct names, prices and quantities | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C1 | Each product's name, image, description and price match each other everywhere it appears | [⚠️ unsure](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 3 | C4 | No layout breakage, overlapping elements or unreadable text | [⚠️ unsure](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 3 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C2 | The cart link opens the cart page | [➖ not recorded](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 3 | C3 | No inaccurate error messages | [➖ not recorded](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 4 | C2 | Clicking "Checkout" in the cart opens the checkout information page (checkout-step-one) titled "Checkout: Your Information". | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | F3 | The cart badge still equals the 2 items in the cart (Backpack and Bike Light from step 2), with nothing changed by navigating. | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | F5 | The checkout form shows empty First Name, Last Name and Postal Code fields, ready for input. Whether it accepts and keeps the values is tested in step 5. | [⚠️ unsure](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [➖ not recorded](run-3/steps/S04.png) | **not verified** |
| 4 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | C4 | No layout breakage or unreadable text on the checkout information page | [➖ not recorded](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [➖ not recorded](run-3/steps/S04.png) | **not verified** |
| 4 | C3 | No error message appears when checkout first opens. | [➖ not recorded](run-1/steps/S04.png) | [➖ not recorded](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **not verified** |
| 5 | F5 | First Name, Last Name and Postal Code fields hold exactly what was typed: 'Test', 'User', '12345' (TS-002 read-back), and no error appears for valid input. | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | F3 | The cart badge equals the number of items in the cart (2: Backpack and Bike Light). | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 5 | C4 | No layout breakage, overlapping or unreadable text | [➖ not recorded](run-1/steps/S05.png) | [⚠️ unsure](run-2/steps/S05.png) | [➖ not recorded](run-3/steps/S05.png) | **not verified** |
| 6 | F6 | The overview lists the same items as the cart (Sauce Labs Backpack and Sauce Labs Bike Light, quantity 1 each). Item total equals the sum of the item prices, and Total equals Item total plus Tax. | [✅ pass](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 6 | C1 | Each product's name, description and price are the same here as everywhere else it appears. | [✅ pass](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 6 | C4 | No broken layout, overlapping elements or unreadable text. | [⚠️ unsure](run-1/steps/S06.png) | [➖ not recorded](run-2/steps/S06.png) | [➖ not recorded](run-3/steps/S06.png) | **not verified** |
| 6 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | F5 | Each checkout field keeps exactly what was typed (Test / User / 12345). | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [➖ not recorded](run-3/steps/S06.png) | **not verified** |
| 6 | F3 | The cart badge count equals the number of items in the cart (2 selected products). | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 7 | F7 | Clicking Finish shows an order confirmation, and the cart is empty afterwards (no badge, no items). | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | C4 | No layout breakage, overlapping elements, or unreadable text in the flow | [➖ not recorded](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [⚠️ unsure](run-3/steps/S07.png) | **not verified** |
| 8 | - | the judge returns checks | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S08.png) | [✅ pass](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **confirmed pass** |

## Coverage: what each run explored

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | 7 | 6 | 7 |
| Browser actions taken | 23 | 19 | 25 |
| Paths tried in free exploration | 4 | 0 | 6 |

**Pages not visited by every run:**

- `/inventory-item.html`: only in run(s) 1, 3

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
