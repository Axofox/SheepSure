"""Stage 3a: run the whole checkout scenario with plain Playwright (no AI).

Purpose: a no-AI baseline that proves screenshots, console and network capture work.
Used when: to check the capture pipeline or the app itself, before or without the AI runner.

Every step is recorded: action, expected vs observed, result, the
screenshot of the outcome, console and network entries. Proves the capture works before the
AI is added. Output: reports/<account>/core/run-1/, overwriting the previous run.

Usage: .venv/bin/python scripted_run.py [standard_user|problem_user]
"""
import re
import shutil
import sys
from pathlib import Path

import yaml
from playwright.sync_api import sync_playwright

ACCOUNT = sys.argv[1] if len(sys.argv) > 1 else "standard_user"
PASSWORD = "secret_sauce"
PRODUCTS = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
ADD_IDS = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light"]
FORM = {"#first-name": "Test", "#last-name": "User", "#postal-code": "12345"}

run_dir = Path("reports") / ACCOUNT / "core" / "run-1"
shutil.rmtree(run_dir, ignore_errors=True)
(run_dir / "steps").mkdir(parents=True)

console_lines = []
network_lines = []
records = []
shop_prices = {}  # name -> price, read from the products page in step 2


def money(text):
    return float(re.search(r"\$([\d.]+)", text).group(1))


def cart_items(page):
    """Names and prices of the items currently listed (cart or overview page)."""
    names = page.locator(".cart_item .inventory_item_name").all_inner_texts()
    prices = [money(t) for t in page.locator(".cart_item .inventory_item_price").all_inner_texts()]
    return names, prices


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()  # new page in a fresh browser = fresh session
    page.set_default_timeout(5000)

    page.on("console", lambda m: console_lines.append(f"[{m.type}] {m.text}"))
    page.on("pageerror", lambda e: console_lines.append(f"[pageerror] {e}"))
    page.on("requestfailed", lambda r: network_lines.append(
        f"FAILED {r.method} {r.url} ({r.failure})"))
    page.on("response", lambda r: network_lines.append(
        f"{r.status} {r.request.method} {r.url}") if r.status >= 400 else None)

    def step(n, action, do, check, fallback_ref):
        """Screenshot, do the action, screenshot, evaluate the checks, record it all."""
        c0, n0 = len(console_lines), len(network_lines)
        problem = None
        try:
            do()
        except Exception as e:
            problem = f"action failed: {str(e).splitlines()[0]}"
        page.screenshot(path=run_dir / "steps" / f"S{n:02d}.png")

        checks = []
        try:
            for ref, expected, observed, ok in check():
                checks.append({"quality_ref": ref, "expected": expected,
                               "observed": observed, "result": "pass" if ok else "fail"})
        except Exception as e:
            problem = problem or f"check failed: {str(e).splitlines()[0]}"
        if problem:
            checks.append({"quality_ref": fallback_ref, "expected": "step completes",
                           "observed": problem, "result": "fail"})

        new_console, new_network = console_lines[c0:], network_lines[n0:]
        checks.append({"quality_ref": "C5", "expected": "No unexpected console errors or failed network requests",
                       "observed": f"{len(new_console)} console entries, {len(new_network)} failed requests",
                       "result": "pass" if not (new_console or new_network) else "unsure"})
        result = "fail" if any(c["result"] == "fail" for c in checks) else (
            "unsure" if any(c["result"] == "unsure" for c in checks) else "pass")
        records.append({
            "step": n, "action": action, "checks": checks,
            "screenshot": f"steps/S{n:02d}.png",
            "console_errors": new_console or "none", "failed_requests": new_network or "none",
            "step_result": result,
        })
        print(f"Step {n}: {action} -> {result.upper()}")
        for c in checks:
            print(f"    {c['result']:6} {c['quality_ref']}: {c['observed']}")

    # 1. Log in
    def login():
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", ACCOUNT)
        page.fill("#password", PASSWORD)
        page.click("#login-button")
        page.wait_for_url("**/inventory.html")

    step(1, f"opened saucedemo.com and logged in as {ACCOUNT}", login, lambda: [
        ("F1", "Valid credentials log the user in and land on the products page",
         f"URL is {page.url}, {page.locator('.inventory_item').count()} products shown",
         page.url.endswith("/inventory.html") and page.locator(".inventory_item").count() > 0)], "F1")

    # 2. Add Backpack and Bike Light
    def add_products():
        for name in PRODUCTS:
            item = page.locator(".inventory_item").filter(has_text=name)
            shop_prices[name] = money(item.locator(".inventory_item_price").inner_text())
        for button_id in ADD_IDS:
            page.click(f"#{button_id}")

    def check_added():
        out = []
        for name in PRODUCTS:
            label = page.locator(".inventory_item").filter(has_text=name).locator("button").inner_text()
            out.append(("F2", f"{name}: button changes to Remove", f"button reads '{label}'", label == "Remove"))
        badge = page.locator(".shopping_cart_badge").all_inner_texts()
        out.append(("F3", "Cart badge shows 2", f"badge reads {badge or 'no badge'}", badge == ["2"]))
        return out

    step(2, "clicked Add to cart on Sauce Labs Backpack and Sauce Labs Bike Light",
         add_products, check_added, "F2")

    # 3. Open the cart
    def check_cart():
        names, prices = cart_items(page)
        expected_prices = [shop_prices[n] for n in names if n in shop_prices]
        return [
            ("F4", f"Cart contains exactly {PRODUCTS}", f"cart lists {names}", sorted(names) == sorted(PRODUCTS)),
            ("F4", "Cart prices match the products page", f"cart prices {prices}, products page {expected_prices}",
             prices == expected_prices and len(prices) == len(names)),
            ("F3", "Cart badge equals number of items in cart",
             f"badge {page.locator('.shopping_cart_badge').all_inner_texts() or 'none'}, {len(names)} items in cart",
             page.locator(".shopping_cart_badge").all_inner_texts() == [str(len(names))]),
        ]

    step(3, "opened the cart", lambda: page.click(".shopping_cart_link"), check_cart, "F4")

    # 4. Checkout
    step(4, "clicked Checkout", lambda: page.click("#checkout"), lambda: [
        ("C2", "Checkout opens the information form (checkout-step-one)", f"URL is {page.url}",
         "checkout-step-one" in page.url)], "C2")

    # 5. Enter customer info
    def fill_form():
        for selector, value in FORM.items():
            page.fill(selector, value)

    def check_form():
        out = []
        for selector, value in FORM.items():
            shown = page.input_value(selector)
            out.append(("F5", f"{selector} keeps '{value}'", f"field shows '{shown}'", shown == value))
        return out

    step(5, "typed first name, last name and postal code", fill_form, check_form, "F5")

    # 6. Continue to the overview
    def continue_to_overview():
        page.click("#continue")
        page.wait_for_url("**/checkout-step-two.html")

    def check_overview():
        names, prices = cart_items(page)
        subtotal = money(page.locator(".summary_subtotal_label").inner_text())
        tax = money(page.locator(".summary_tax_label").inner_text())
        total = money(page.locator(".summary_total_label").inner_text())
        return [
            ("F6", f"Overview lists {PRODUCTS}", f"overview lists {names}", sorted(names) == sorted(PRODUCTS)),
            ("F6", "Item total = sum of item prices", f"item total {subtotal}, items sum to {round(sum(prices), 2)}",
             round(sum(prices), 2) == subtotal),
            ("F6", "Total = item total + tax", f"total {total}, item total {subtotal} + tax {tax} = {round(subtotal + tax, 2)}",
             round(subtotal + tax, 2) == total),
        ]

    step(6, "clicked Continue to reach the order overview", continue_to_overview, check_overview, "F6")

    # 7. Finish
    def finish():
        page.click("#finish")
        page.wait_for_url("**/checkout-complete.html")

    def check_complete():
        header = page.locator(".complete-header").inner_text()
        badge = page.locator(".shopping_cart_badge").all_inner_texts()
        return [
            ("F7", "Order confirmation is shown", f"header reads '{header}'", "thank you" in header.lower()),
            ("F7", "Cart is empty afterwards", f"badge {badge or 'none'}", badge == []),
        ]

    step(7, "clicked Finish", finish, check_complete, "F7")

    browser.close()

# An empty log is written as "none captured": that is evidence, not a missing file.
(run_dir / "console.log").write_text("\n".join(console_lines) or "none captured")
(run_dir / "network.log").write_text("\n".join(network_lines) or "none captured")
(run_dir / "run.yaml").write_text(
    yaml.safe_dump(records, sort_keys=False, allow_unicode=True, width=120))

# run.md: the human-readable version. Every step has an anchor, so the summary
# table can jump to it, and the screenshots are shown inline and linked.
ICON = {"pass": "✅", "fail": "❌", "unsure": "⚠️"}
md = ['<a id="top"></a>', f"# Run 1 - {ACCOUNT} (scripted, no AI)\n",
      "| Step | Action | Result | Screenshot |", "|---|---|---|---|"]
for r in records:
    md.append(f"| [{r['step']}](#step-{r['step']}) | {r['action']} | {ICON[r['step_result']]} {r['step_result']} "
              f"| [screenshot]({r['screenshot']}) |")
for r in records:
    md.append(f"\n---\n\n<a id=\"step-{r['step']}\"></a>\n## Step {r['step']}: {r['action']}  {ICON[r['step_result']]}\n")
    md.append(f"[↑ back to summary](#top) · jump to [screenshot](#step-{r['step']}-shot)\n")
    md += ["| Check | Expected | Observed | Result |", "|---|---|---|---|"]
    for c in r["checks"]:
        md.append(f"| {c['quality_ref']} | {c['expected']} | {c['observed']} | {ICON[c['result']]} {c['result']} |")
    if r["console_errors"] != "none" or r["failed_requests"] != "none":
        md.append(f"\nConsole: {r['console_errors']}  \nFailed requests: {r['failed_requests']}")
    md.append(f"\n<a id=\"step-{r['step']}-shot\"></a>**Outcome** - [{r['screenshot']}]({r['screenshot']})\n\n![step {r['step']} outcome]({r['screenshot']})")
(run_dir / "run.md").write_text("\n".join(md) + "\n")

print("Saved to:", run_dir)
