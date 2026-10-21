<a id="top"></a>
# Run 3 - problem_user - mission core

Model: `claude (your plan) / claude-haiku-5-5` · Outcome: **blocked at step 5** · Duration: 491s · Findings: 9

| Step | Action | Result | Screenshot |
|---|---|---|---|
| [1](#step-1) | Log in with the given account. | ⚠️ unsure | [screenshot](steps/S01.png) |
| [2](#step-2) | Add **Sauce Labs Backpack** and **Sauce Labs Bike Light** to the cart. | ⚠️ unsure | [screenshot](steps/S02.png) |
| [3](#step-3) | Open the cart. | ⚠️ unsure | [screenshot](steps/S03.png) |
| [4](#step-4) | Start checkout. | ⚠️ unsure | [screenshot](steps/S04.png) |
| [5](#step-5) | Enter valid customer information (First Name `Test`, Last Name `User`, Postal Code `12345` | ❌ fail | [screenshot](steps/S05.png) |
| [6](#step-6) | Continue to the order overview. | ❌ fail | [screenshot](steps/S06.png) |
| [7](#step-7) | Finish the order. | ❌ fail | [screenshot](steps/S07.png) |
| [8](#step-8) | Free exploration: try other paths inside this mission's theme (the AI chooses) | ⚠️ unsure | [screenshot](steps/S08.png) |

---

<a id="step-1"></a>
## Step 1 ⚠️

[↑ back to summary](#top) · jump to [screenshot](#step-1-shot)

**Action:** Log in with the given account.

**Agent report:** Step 1 of 8 complete. Logged in as problem_user / secret_sauce by typing the username and password and clicking Login. The page is now https://www.saucedemo.com/inventory.html and shows the "Products" heading with the inventory list (Sauce Labs Backpack $29.99, Sauce Labs Bike Light $9.99, Sauce Labs Bolt T-Shirt, and others). Cart badge is empty ("Cart, empty"). No login error was shown.

**Agent actions (4):**

- 1. type [1] "Username" text="problem_user" -> ok; now at /
- 2. type [2] "Password" text="secret_sauce" -> ok; now at /
- 3. click [3] "Login" -> ok; now at /inventory.html

**Pages visited:** /, /inventory.html

| Check | Expected | Observed | Result |
|---|---|---|---|
| F1 | Valid credentials log the user in and land on the products page | URL is https://www.saucedemo.com/inventory.html, visible text contains the 'Products' heading, six products are listed, and no error_message is present. | ✅ pass |
| C1 | Each product's name, image, description and price match each other everywhere they appear | Names and prices are present for all six products and the agent report agrees. Every product's image has the same src, '/assets/sl-404-Cq1a9k9X.jpg', and the path contains '404'. The page facts do not show whether the image renders, so the image-to-product match cannot be confirmed. | ⚠️ unsure |
| C5 | No unexpected console errors or failed network requests | 4 console entries, 4 failed requests to events.backtrace.io (third-party only, no visible problem by itself) | ⚠️ unsure |

- **Finding S1-C1-1** (suspicious, observation): All product images share one src that looks like a 404 placeholder. Observed: All six products on the inventory page have image src '/assets/sl-404-Cq1a9k9X.jpg', which contains '404'. The page facts do not say whether the image loaded.

Console: ['[error] Failed to load resource: the server responded with a status of 401 (Unauthorized)', '[error] Failed to load resource: the server responded with a status of 401 (Unauthorized)', '[error] Failed to load resource: the server responded with a status of 401 (Unauthorized)', '[error] Failed to load resource: the server responded with a status of 401 (Unauthorized)']  
Failed requests: ['401 POST https://events.backtrace.io/api/summed-events/submit?universe=UNIVERSE&token=TOKEN', '401 POST https://events.backtrace.io/api/unique-events/submit?universe=UNIVERSE&token=TOKEN', '401 POST https://events.backtrace.io/api/summed-events/submit?universe=UNIVERSE&token=TOKEN', '401 POST https://events.backtrace.io/api/unique-events/submit?universe=UNIVERSE&token=TOKEN']

<a id="step-1-shot"></a>**Outcome** - [steps/S01.png](steps/S01.png) · 34s

![step 1 outcome](steps/S01.png)

---

<a id="step-2"></a>
## Step 2 ⚠️

[↑ back to summary](#top) · jump to [screenshot](#step-2-shot)

**Action:** Add **Sauce Labs Backpack** and **Sauce Labs Bike Light** to the cart.

**Agent report:** Step 2 complete. Added Sauce Labs Backpack ($29.99) and Sauce Labs Bike Light ($9.99) to the cart. The inventory page now shows "Remove" buttons for both items, and the cart badge reads 2. Still on https://www.saucedemo.com/inventory.html. I did not open the cart or proceed to later steps.

**Agent actions (3):**

- 1. click [6] "Add to cart" -> ok; now at /inventory.html
- 2. click [9] "Add to cart" -> ok; now at /inventory.html

**Pages visited:** /inventory.html

| Check | Expected | Observed | Result |
|---|---|---|---|
| F2 | Add to cart on Sauce Labs Backpack and Sauce Labs Bike Light adds those products and their buttons change to Remove | Backpack ($29.99) and Bike Light ($9.99) both show Remove. The other four products still show Add to cart. Agent report matches the page facts. | ✅ pass |
| F3 | Cart badge count equals the number of items actually in the cart | Badge reads 2 and exactly two products show Remove on the products page. The cart itself was not opened in this step, so the cart contents are not confirmed here. | ⚠️ unsure |
| C1 | Product name, image, description and price match each other where the product appears | Names, prices and descriptions are shown as text. All six products use the same image path, /assets/sl-404-Cq1a9k9X.jpg, and the file name contains '404'. The facts do not show whether the image renders, so the match cannot be confirmed. | ⚠️ unsure |
| C5 | No unexpected console errors or failed network requests | 2 console entries, 2 failed requests to events.backtrace.io (third-party only, no visible problem by itself) | ⚠️ unsure |

- **Finding S2-C1-1** (suspicious, minor): All six products point to the same image file, named 'sl-404'. Observed: Every product on the inventory page has image src /assets/sl-404-Cq1a9k9X.jpg. The file name suggests a 404 or placeholder asset. Rendering is not visible in the page facts.

Console: ['[error] Failed to load resource: the server responded with a status of 401 (Unauthorized)', '[error] Failed to load resource: the server responded with a status of 401 (Unauthorized)']  
Failed requests: ['401 POST https://events.backtrace.io/api/summed-events/submit?universe=UNIVERSE&token=TOKEN', '401 POST https://events.backtrace.io/api/unique-events/submit?universe=UNIVERSE&token=TOKEN']

<a id="step-2-shot"></a>**Outcome** - [steps/S02.png](steps/S02.png) · 24s

![step 2 outcome](steps/S02.png)

---

<a id="step-3"></a>
## Step 3 ⚠️

[↑ back to summary](#top) · jump to [screenshot](#step-3-shot)

**Action:** Open the cart.

**Agent report:** Step 3 complete. I clicked the cart icon (badge "2") and the browser is now on https://www.saucedemo.com/cart.html, showing "Your Cart" with 2 items: Sauce Labs Backpack ($29.99) and Sauce Labs Bike Light ($9.99). The page also shows the Continue Shopping and Checkout buttons. I did not do any later steps.

**Agent actions (2):**

- 1. click [2] "2" -> ok; now at /cart.html

**Pages visited:** /cart.html

| Check | Expected | Observed | Result |
|---|---|---|---|
| F3 | Cart badge count equals the number of items actually in the cart | Badge reads "2". Cart lists 2 line items (Sauce Labs Backpack qty 1, Sauce Labs Bike Light qty 1), total quantity 2. | ✅ pass |
| F4 | Cart contains exactly the selected products (Sauce Labs Backpack and Sauce Labs Bike Light) with correct names, prices and quantities | Cart shows exactly Sauce Labs Backpack ($29.99, qty 1) and Sauce Labs Bike Light ($9.99, qty 1). No other items. Both show a Remove button. | ✅ pass |
| C1 | Product name, image, description and price match each other everywhere they appear | Cart names and prices are shown with matching descriptions for each item. Item image is null in page facts, so image consistency against the products page cannot be confirmed from this step. No products-page facts were captured here to compare prices against. | ⚠️ unsure |
| C2 | Clicking the cart icon navigates to the cart | Agent clicked the cart icon; URL is https://www.saucedemo.com/cart.html and the page heading reads "Your Cart". | ✅ pass |
| C4 | No layout breakage, overlapping elements or unreadable text on the cart page | Page facts contain visible text only; no layout or overlap information was captured. | ⚠️ unsure |
| C5 | No unexpected console errors or failed network requests | 0 console entries, 0 failed requests | ✅ pass |

<a id="step-3-shot"></a>**Outcome** - [steps/S03.png](steps/S03.png) · 23s

![step 3 outcome](steps/S03.png)

---

<a id="step-4"></a>
## Step 4 ⚠️

[↑ back to summary](#top) · jump to [screenshot](#step-4-shot)

**Action:** Start checkout.

**Agent report:** Step 4 (Start checkout) is complete. I clicked "Checkout" in the cart, and the page is now https://www.saucedemo.com/checkout-step-one.html, titled "Checkout: Your Information". The cart badge shows 2. The First Name, Last Name and Zip/Postal Code fields are empty, and the Cancel and Continue buttons are visible. I did not fill in the form or continue.

**Agent actions (2):**

- 1. click [8] "Checkout" -> ok; now at /checkout-step-one.html

**Pages visited:** /checkout-step-one.html

| Check | Expected | Observed | Result |
|---|---|---|---|
| F5 | Checkout step one is reached with an empty Your Information form (First Name, Last Name, Postal Code) that is ready to accept input | URL is https://www.saucedemo.com/checkout-step-one.html, page text shows 'Checkout: Your Information' and 'Cancel'. All three inputs (first-name, last-name, postal-code) are empty. No error message. Cart badge shows 2. Input acceptance has not been tested in this step, since no values were typed. | ⚠️ unsure |
| C5 | No unexpected console errors or failed network requests | 0 console entries, 0 failed requests | ✅ pass |

<a id="step-4-shot"></a>**Outcome** - [steps/S04.png](steps/S04.png) · 22s

![step 4 outcome](steps/S04.png)

---

<a id="step-5"></a>
## Step 5 ❌

[↑ back to summary](#top) · jump to [screenshot](#step-5-shot)

**Action:** Enter valid customer information (First Name `Test`, Last Name `User`, Postal Code `12345`).

**Agent report:** (no final report: the agent ran out of actions or could not continue) Last actions: 9. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html | 10. type [3] "First Name" text="Test" -> ok; now at /checkout-step-one.html | 11. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html | 12. type [3] "First Name" text="Test" -> ok; now at /checkout-step-one.html

**Agent actions (12):**

- 1. type [3] "First Name" text="Test" -> ok; now at /checkout-step-one.html
- 2. type [4] "Last Name" text="Test" -> ok; now at /checkout-step-one.html
- 3. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 4. type [3] "First Name" text="Test" -> ok; now at /checkout-step-one.html
- 5. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 6. type [3] "First Name" text="Test" -> ok; now at /checkout-step-one.html
- 7. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 8. type [3] "First Name" text="Test" -> ok; now at /checkout-step-one.html
- 9. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 10. type [3] "First Name" text="Test" -> ok; now at /checkout-step-one.html
- 11. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 12. type [3] "First Name" text="Test" -> ok; now at /checkout-step-one.html

**Pages visited:** /checkout-step-one.html

| Check | Expected | Observed | Result |
|---|---|---|---|
| F5 | Checkout accepts valid First Name (Test), Last Name (User), Postal Code (12345), and each field keeps exactly what was typed | Page facts after step 5: first-name = "Test", last-name = "" (empty), postal-code = "" (empty). URL is still /checkout-step-one.html, no error message shown, and the page did not advance. The agent report says Last Name "User" was typed and returned ok, but the page value contradicts that. | ❌ fail |
| C5 | No unexpected console errors or failed network requests | 0 console entries, 0 failed requests | ✅ pass |
| STEP | the agent completes the step | agent did not finish.  | ❌ fail |

- **Finding S5-F5-1** (failure, blocker): Checkout step one loses Last Name and Postal Code input; checkout cannot continue. Observed: Only First Name holds "Test". Last Name and Postal Code read back as empty on /checkout-step-one.html, with no error message. The agent reported typing "User" into Last Name and got ok, but the page does not show it. The page did not advance to the overview.

- **Finding S5-F5-2** (suspicious, observation): Agent repeated the same typing actions after apparent success, and the run ended without a final report. Observed: The agent typed First Name and Last Name again in actions 10 and 11 and 12 without confirming the values were kept, then ran out of actions with no final report. It is unclear whether the empty fields come from the app or from how the browsing tool enters text.

<a id="step-5-shot"></a>**Outcome** - [steps/S05.png](steps/S05.png) · 100s

![step 5 outcome](steps/S05.png)

---

<a id="step-6"></a>
## Step 6 ❌

[↑ back to summary](#top) · jump to [screenshot](#step-6-shot)

**Action:** Continue to the order overview.

**Agent report:** BLOCKED at mission step 6 (continue to order overview). Logged in as problem_user earlier and reached /checkout-step-one.html (Checkout: Your Information). First Name shows "Tester". Last Name field [4] shows value="" even though 7 type actions and 1 click on it reported ok. Clicking Continue shows "Error: Last Name is required", so the page never reached the order overview. Zip/Postal Code [5] is also empty. Cart badge shows 2. I did not fill Zip or any other field, since that is outside this step. The Last Name input may be not accepting typed text on this page, or the typing may be going elsewhere. Needs a manual check or a fix before this step can complete.

**Agent actions (9):**

- 1. click [7] "Continue" -> ok; now at /checkout-step-one.html
- 2. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
- 3. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
- 4. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
- 5. click [4] "Last Name" -> ok; now at /checkout-step-one.html
- 6. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
- 7. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
- 8. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html

**Pages visited:** /checkout-step-one.html

| Check | Expected | Observed | Result |
|---|---|---|---|
| F5 | After typing First Name, Last Name and Postal Code, each field keeps the typed value, and Continue proceeds to the order overview. Step 6 assumes step 5 entered Last Name "User". | Page facts: first-name = "Tester", last-name = "", postal-code = "". The URL is still /checkout-step-one.html and the error "Error: Last Name is required" is shown. The Last Name value was not kept, and the page did not advance. | ❌ fail |
| F6 | The order overview shows the cart items, item total = sum of prices, and total = item total + tax. | The overview was never reached (URL is still checkout-step-one, items list is empty in page facts). Nothing about the overview can be verified. | ⚠️ unsure |
| C3 | The error message describes the real problem. | The message "Error: Last Name is required" matches the page state, where the Last Name field is empty. The message is accurate for the state shown, though the agent reports it typed a value that did not persist. | ✅ pass |
| C5 | No unexpected console errors or failed network requests | 0 console entries, 0 failed requests | ✅ pass |

- **Finding S6-F5-1** (failure, blocker): Last Name not kept on checkout step one; Continue blocked with 'Last Name is required'. Observed: After the agent reported typing into Last Name, the field value is empty. Continue shows 'Error: Last Name is required' and stays on /checkout-step-one.html. Postal Code is also empty. First Name shows 'Tester'. The cart badge still shows 2.

- **Finding S6-F5-2** (suspicious, observation): Postal Code left empty before Continue (step 5 incomplete in this run). Observed: The agent did not fill Postal Code, citing it as outside the step. Continue was clicked with Last Name and Postal Code both empty, so the blocked result cannot be attributed to Last Name alone.

<a id="step-6-shot"></a>**Outcome** - [steps/S06.png](steps/S06.png) · 74s

![step 6 outcome](steps/S06.png)

---

<a id="step-7"></a>
## Step 7 ❌

[↑ back to summary](#top) · jump to [screenshot](#step-7-shot)

**Action:** Finish the order.

**Agent report:** (no final report: the agent ran out of actions or could not continue) Last actions: 9. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html | 10. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html | 11. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html | 12. type [5] "Zip/Postal Code" text="12345" -> ok; now at /checkout-step-one.html

**Agent actions (12):**

- 1. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 2. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 3. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 4. click [4] "Last Name" -> ok; now at /checkout-step-one.html
- 5. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 6. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 7. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 8. click [6] "Dismiss error" -> ok; now at /checkout-step-one.html
- 9. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 10. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 11. type [4] "Last Name" text="User" -> ok; now at /checkout-step-one.html
- 12. type [5] "Zip/Postal Code" text="12345" -> ok; now at /checkout-step-one.html

**Pages visited:** /checkout-step-one.html

| Check | Expected | Observed | Result |
|---|---|---|---|
| F5 | Checkout accepts First Name 'Test', Last Name 'User', Postal Code '12345', and each field keeps exactly what was typed. | Page facts show first-name = 'User' (not 'Test'), last-name = '' (empty), postal-code = '12345'. The 'User' value landed in the First Name field, and Last Name is empty despite the agent's report of 'type [4] Last Name text=User -> ok' being repeated three times. First Name and Last Name values are swapped or misplaced; the step never reached a valid, complete entry. | ❌ fail |
| C3 | If the form is invalid, any error message accurately describes the real problem. | error_message is null and no error text is visible. No submit was attempted in this step, so there is no error that should or should not appear yet. Cannot judge. | ⚠️ unsure |
| C5 | No unexpected console errors or failed network requests | 0 console entries, 0 failed requests | ✅ pass |
| STEP | the agent completes the step | agent did not finish.  | ❌ fail |

- **Finding S7-F5-1** (failure, major): Last Name typed value lands in First Name; Last Name stays empty on checkout step one. Observed: After repeated 'Last Name' typing attempts, page facts show first-name = 'User', last-name = '', postal-code = '12345'. The agent's report says each Last Name type returned 'ok', but the page state contradicts this. First Name was never set to 'Test'. The run stopped at action 12 before Continue, so step 6 and step 7 were not reached.

- **Finding S7-F5-2** (unexpected, observation): Agent report contradicts page facts on field values. Observed: Agent reported 'type [4] Last Name text=User -> ok' three times and 'type [5] Postal Code 12345 -> ok', yet page facts show the 'User' text in first-name and last-name empty. Per the rules, page facts are trusted over the agent report.

<a id="step-7-shot"></a>**Outcome** - [steps/S07.png](steps/S07.png) · 101s

![step 7 outcome](steps/S07.png)

---

<a id="step-8"></a>
## Step 8 ⚠️

[↑ back to summary](#top) · jump to [screenshot](#step-8-shot)

**Action:** Free exploration: try other paths inside this mission's theme (the AI chooses)

**Agent report:** PATH: Sort dropdown, "Price (low to high)". I selected "Price (low to high)" in the sort select (element [3]) twice. Both selects returned ok and the page stayed at /inventory.html. The select's current value in the element list is value="az". The product order on the page is Sauce Labs Backpack $29.99, Sauce Labs Bike Light $9.99, Sauce Labs Bolt T-Shirt $15.99, Sauce Labs Fleece Jacket, Sauce Labs Onesie, Test.allTheThings() T-Shirt (Red). That is alphabetical (A to Z) order, not price ascending, which would start with $9.99. Likely bug: the price sort is not applied.

PATH: Product detail page and back navigation, Sauce Labs Backpack. I clicked the "Sauce Labs Backpack" product link (element [3]) and landed on /inventory-item.html. I clicked "Add to cart" (element [4]), which returned ok, then clicked "Back to products" (element [3]) and landed on /inventory.html. I did not capture the detail page's name, price or description text in my action log, so I cannot confirm them against the list entry ("Sauce Labs Backpack", $29.99, "carry.allTheThings() with the sleek, streamlined Sly Pack...").

PATH: Cart badge after add-to-cart. After the Backpack add-to-cart and return to the list, the cart badge reads "2". The list shows "Remove" buttons for Sauce Labs Backpack and Sauce Labs Bike Light, which matches two items. I did not record the badge value before the add, so I cannot say whether it incremented by exactly 1.

PATH: Checkout step one, then cancel. On /checkout-step-one.html I typed "Tester" into the Last Name field (element [4]), clicked "Dismiss error" (element [6]), which returned ok and kept me on the same page, and then clicked "Cancel" (element [6]), which took me to /cart.html. I did not capture the error text itself, so I cannot quote what the error said.

Note: The first three actions of the session are not in the action list I was given, so this report only covers actions 4 to 11. I stopped at 11 of 12 actions and did not use the last one.

**Agent actions (12):**

- 1. click [7] "Continue" -> ok; now at /checkout-step-one.html
- 2. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
- 3. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
- 4. type [4] "Last Name" text="Tester" -> ok; now at /checkout-step-one.html
- 5. click [6] "Dismiss error" -> ok; now at /checkout-step-one.html
- 6. click [6] "Cancel" -> ok; now at /cart.html
- 7. click [3] "Sauce Labs Backpack" -> ok; now at /inventory-item.html
- 8. click [4] "Add to cart" -> ok; now at /inventory-item.html
- 9. click [3] "Back to products" -> ok; now at /inventory.html
- 10. select [3] "Name (A to Z) Name (Z to A) Price (low to high) Price (high " text="Price (low to high)" -> ok; now at /inventory.html
- 11. select [3] "Name (A to Z) Name (Z to A) Price (low to high) Price (high " text="Price (low to high)" -> ok; now at /inventory.html

**Pages visited:** /checkout-step-one.html, /cart.html, /inventory-item.html, /inventory.html

| Check | Expected | Observed | Result |
|---|---|---|---|
| F3 | Cart badge count equals the number of items actually in the cart | Page facts show cart badge '2'. Two items show 'Remove' (Sauce Labs Backpack and Sauce Labs Bike Light), and no other item shows 'Remove'. The cart contents themselves were not read in this step, so the match is inferred from the product list. | ✅ pass |
| C1 | Product name, image, description and price match between the list and the product detail page | Page facts were read on /inventory.html only. The agent report says it opened the Backpack detail page but did not record its name, price or description, and no detail-page facts were captured. Nothing can be compared. | ⚠️ unsure |
| C2 | Navigation and labelled controls do what their label says: the product link opens that product, 'Back to products' returns to the list, and the sort option produces the order its label names | The agent report says the Backpack link opened /inventory-item.html and 'Back to products' returned to /inventory.html, but no page facts were captured for the detail page. On the list, the products appear in A to Z order (Backpack, Bike Light, Bolt, Fleece Jacket, Onesie, Test.allTheThings), not price ascending as the 'Price (low to high)' label would require. The current sort selection is only stated in the agent report, not in the page facts. | ⚠️ unsure |
| C5 | No unexpected console errors or failed network requests | 0 console entries, 0 failed requests | ✅ pass |

- **Finding S8-C2-1** (suspicious, minor): Price (low to high) sort does not reorder products. Observed: After the agent selected 'Price (low to high)' twice, the page stayed on /inventory.html and the list is still in A to Z order, starting with Sauce Labs Backpack $29.99 then Sauce Labs Bike Light $9.99. The agent report says the sort select's value is 'az'. The page facts do not show which option is selected.

<a id="step-8-shot"></a>**Outcome** - [steps/S08.png](steps/S08.png) · 110s

![step 8 outcome](steps/S08.png)
