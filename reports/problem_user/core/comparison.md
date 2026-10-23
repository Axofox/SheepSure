# Comparison across 3 run(s)

Rules: `run-protocol.md`. One row per step + expectation.

| Step | Ref | Expected | Run 1 | Run 2 | Run 3 | Across runs |
|---|---|---|---|---|---|---|
| 1 | F1 | Valid credentials log the user in and land on the products page | [✅ pass](run-1/steps/S01.png) | [✅ pass](run-2/steps/S01.png) | [✅ pass](run-3/steps/S01.png) | **confirmed pass** |
| 1 | C1 | Each product's name, image, description and price match each other everywhere it appears | [❌ fail](run-1/steps/S01.png) | [❌ fail](run-2/steps/S01.png) | [❌ fail](run-3/steps/S01.png) | **confirmed fail** |
| 1 | C5 | No unexpected console errors or failed network requests | [⚠️ unsure](run-1/steps/S01.png) | [⚠️ unsure](run-2/steps/S01.png) | [⚠️ unsure](run-3/steps/S01.png) | **not verified** |
| 2 | F2 | Clicking 'Add to cart' on Sauce Labs Backpack and Sauce Labs Bike Light adds those products, and each button changes to 'Remove'. | [⚠️ unsure](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **not verified** |
| 2 | F3 | The cart badge count equals the number of items actually in the cart. | [⚠️ unsure](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 2 | C1 | A product's name, image, description and price match each other everywhere it appears. | [❌ fail](run-1/steps/S02.png) | [❌ fail](run-2/steps/S02.png) | [❌ fail](run-3/steps/S02.png) | **confirmed fail** |
| 2 | C4 | No layout breakage, overlapping elements, or unreadable text in the flow. | [⚠️ unsure](run-1/steps/S02.png) | [➖ not recorded](run-2/steps/S02.png) | [⚠️ unsure](run-3/steps/S02.png) | **not verified** |
| 2 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S02.png) | [✅ pass](run-2/steps/S02.png) | [✅ pass](run-3/steps/S02.png) | **confirmed pass** |
| 3 | F4 | Cart contains exactly the selected products: Sauce Labs Backpack and Sauce Labs Bike Light, with correct names, prices and quantity 1 each | [❌ fail](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **unstable** |
| 3 | F3 | Cart badge count equals the number of items actually in the cart | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C2 | The cart link opens the cart page | [✅ pass](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **not verified** |
| 3 | C3 | Any error messages are accurate | [✅ pass](run-1/steps/S03.png) | [➖ not recorded](run-2/steps/S03.png) | [➖ not recorded](run-3/steps/S03.png) | **not verified** |
| 3 | C4 | No layout breakage or unreadable text | [⚠️ unsure](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [➖ not recorded](run-3/steps/S03.png) | **not verified** |
| 3 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S03.png) | [✅ pass](run-2/steps/S03.png) | [✅ pass](run-3/steps/S03.png) | **confirmed pass** |
| 3 | C1 | Product name, description and price match everywhere the product appears | [➖ not recorded](run-1/steps/S03.png) | [⚠️ unsure](run-2/steps/S03.png) | [⚠️ unsure](run-3/steps/S03.png) | **not verified** |
| 4 | F5 | Clicking Checkout opens the customer information page (checkout-step-one) with empty First Name, Last Name and Postal Code fields ready for input. | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | F3 | The cart badge shows the number of items actually in the cart. After step 2 that should be 2 (Backpack and Bike Light). | [⚠️ unsure](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 4 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **confirmed pass** |
| 4 | C2 | Clicking the 'Checkout' button opens the checkout information page. | [➖ not recorded](run-1/steps/S04.png) | [✅ pass](run-2/steps/S04.png) | [✅ pass](run-3/steps/S04.png) | **not verified** |
| 4 | C4 | No layout breakage or unreadable text. | [➖ not recorded](run-1/steps/S04.png) | [⚠️ unsure](run-2/steps/S04.png) | [⚠️ unsure](run-3/steps/S04.png) | **not verified** |
| 5 | F5 | After typing, First Name = "Test", Last Name = "User", Postal Code = "12345". Each field keeps exactly what was typed. | [❌ fail](run-1/steps/S05.png) | [❌ fail](run-2/steps/S05.png) | [❌ fail](run-3/steps/S05.png) | **confirmed fail** |
| 5 | C4 | No layout breakage, overlapping elements or unreadable text on the checkout information page. | [⚠️ unsure](run-1/steps/S05.png) | [➖ not recorded](run-2/steps/S05.png) | [➖ not recorded](run-3/steps/S05.png) | **not verified** |
| 5 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S05.png) | [✅ pass](run-2/steps/S05.png) | [✅ pass](run-3/steps/S05.png) | **confirmed pass** |
| 6 | F5 | Checkout accepts First Name 'Test', Last Name 'User', Postal Code '12345', and each field keeps exactly what was typed; Continue moves on to the overview. | [❌ fail](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [❌ fail](run-3/steps/S06.png) | **not verified** |
| 6 | F6 | The order overview shows the same items as the cart, with item total = sum of item prices and total = item total + tax. | [⚠️ unsure](run-1/steps/S06.png) | [⚠️ unsure](run-2/steps/S06.png) | [⚠️ unsure](run-3/steps/S06.png) | **not verified** |
| 6 | C3 | Error messages describe the real problem. | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **confirmed pass** |
| 6 | F3 | The cart badge equals the number of items in the cart (2 selected). | [➖ not recorded](run-1/steps/S06.png) | [✅ pass](run-2/steps/S06.png) | [✅ pass](run-3/steps/S06.png) | **not verified** |
| 7 | - | the judge returns checks | [⚠️ unsure](run-1/steps/S07.png) | [⚠️ unsure](run-2/steps/S07.png) | [➖ not recorded](run-3/steps/S07.png) | **not verified** |
| 7 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S07.png) | [✅ pass](run-2/steps/S07.png) | [✅ pass](run-3/steps/S07.png) | **confirmed pass** |
| 7 | STEP | the agent completes the step | [➖ not recorded](run-1/steps/S07.png) | [❌ fail](run-2/steps/S07.png) | [➖ not recorded](run-3/steps/S07.png) | **not verified** |
| 7 | F7 | Clicking Finish shows an order confirmation (checkout-complete page) and the cart is empty afterwards (no badge). | [➖ not recorded](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [❌ fail](run-3/steps/S07.png) | **not verified** |
| 7 | F5 | Each checkout field keeps exactly what was typed (First Name 'Test', Last Name 'User', Postal Code '12345'), and valid input is accepted. | [➖ not recorded](run-1/steps/S07.png) | [➖ not recorded](run-2/steps/S07.png) | [❌ fail](run-3/steps/S07.png) | **not verified** |
| 8 | - | the judge returns checks | [⚠️ unsure](run-1/steps/S08.png) | [⚠️ unsure](run-2/steps/S08.png) | [⚠️ unsure](run-3/steps/S08.png) | **not verified** |
| 8 | C5 | No unexpected console errors or failed network requests | [✅ pass](run-1/steps/S08.png) | [✅ pass](run-2/steps/S08.png) | [✅ pass](run-3/steps/S08.png) | **confirmed pass** |

## Coverage: what each run explored

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Pages (URL paths) visited | 4 | 4 | 4 |
| Browser actions taken | 18 | 18 | 20 |
| Paths tried in free exploration | 0 | 0 | 1 |

**Pages not visited by every run:**

- none, all runs visited the same pages

**Paths each run tried in free exploration** (as reported by the AI; details in `run-<n>/run.md`):

- **Run 1** (0):
  - none reported
- **Run 2** (0):
  - none reported
- **Run 3** (1):
  - 1. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
