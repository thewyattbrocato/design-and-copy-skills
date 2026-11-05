Your QA notes describe three problems. The third is the most likely cause of the drop in conversion.

**What's wrong, ranked by likely revenue impact**

1. **A declined card wipes the whole form.** Declines are common (typos, bank fraud checks, insufficient funds), and this is the moment a customer is most likely to quit. Right now they have to retype the card, expiry, CVV, zip and country, and many won't. The page also gives no sign of what went wrong. **This is what I'd fix first.** The fix is to keep everything they typed after a decline, and to show a plain message at the top, such as "Your bank declined this card. Try another card or contact your bank." For safety, card number and CVV are often cleared on purpose. If your payment provider requires that, keep the other fields and put the cursor in the card field.

2. **The Pay button is grey with no explanation.** A customer who is ready to pay can't tell why they can't, and a disabled button usually can't be reached by keyboard or screen reader. Keep the button clickable at all times. When they press it, list what's missing or wrong, next to each field and in a summary at the top. Name the fix, for example "Enter the 3-digit code on the back of your card". Don't use "Invalid input".

3. **"Invalid input" appears after the first digit.** Every customer sees an error while typing a correct card number. That reads as "you did something wrong" and costs trust at the worst moment. Only show errors after they press Pay. Once a field has shown an error, clear it as soon as the value becomes valid.

**Smaller issues that add friction**

- **Placeholders are the only labels.** "Card number" disappears when someone starts typing, so they can't check what a field was for. Add visible labels above the fields.
- **Card fields are `type="text"` with no hints.** Add autofill attributes (`autocomplete="cc-number"`, `cc-exp`, `cc-csc`, `postal-code`, `country`) and a numeric keypad for phones. Autofill and saved cards can then fill the form in a second.
- **The 195-country dropdown starts at Afghanistan.** Default it to the customer's country, or make it type-to-search, so most people don't scroll.
- **The button just says "Pay now".** Showing the amount ("Pay $39.00") reassures people. Disable it only while a payment is actually being processed, to prevent double charges.

**Two checks I'd run before shipping fixes**

- Look at your analytics for where people leave. If drop-off after a failed payment is high, that confirms #1. If it's at the first field, it's #3.
- Compare mobile and desktop. Missing numeric keypads and unnecessary scrolling hurt mobile the most.

I haven't seen the real page or your funnel data, so this ranking comes from the markup and QA notes alone. Hand the list to your engineers as is. Items 1–3 are small changes, and I'd expect them to fit in a sprint.
