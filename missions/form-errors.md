# Mission: form-errors

> **Purpose:** an optional exploration of the checkout form: validation messages and unusual input. No verdict.
> **Used when:** passed to the agent after the charter (`--mission form-errors`), once `core` works.

**Theme:** the checkout information form, validation messages and unusual input.
**Expectations to check:** V1–V3, C3 (and C5 on every step).
**Verdict:** none. Findings are classified by reproducibility.

## Steps

1. Log in with the given account, add the Backpack, open the cart and start checkout.
2. Click **Continue** with all fields empty. Record the exact error text and which field it names. (V1)
3. Type only a Last Name and click Continue. Record the error and the value in each field. (V1, V2)
4. Type First and Last Name, leave the Postal Code empty, click Continue. Record the error and the field values. (V1, V2)
5. Enter spaces only in all three fields and click Continue. Record whether it is accepted or rejected, the message, and the field values. (V3)
6. Enter a 200-character First Name, Last Name `O'Brien-Müller`, and Postal Code `ABC-9`. Record what is kept in each field and whether it continues. (V3)
7. Enter `<b>Test</b> & "Co"` as First Name, valid other fields. Record what is kept and what happens on Continue. (V3)

## Notes

- Report what the app actually does. If the message is unclear or the behavior is a judgment call, label it an observation, not a bug.

## Free exploration

Budget: 12 actions. Ideas, not a checklist. Choose your own:
- Try other unusual input: only digits in the names, a very long postal code, leading and trailing spaces, an emoji.
- Fix one field after an error and see what happens to the other fields and to the message.
- Submit the form twice in a row. Does anything change or duplicate?
- Anything else that tests the information form and its messages.
