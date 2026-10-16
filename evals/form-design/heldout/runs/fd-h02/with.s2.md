The form has four problems. I've ranked them by how likely each is to be costing you sales.

**1. The form wipes everything after a decline (fix first).**
A declined card is the most common failure at payment, and it's the moment a customer is most likely to give up. If they have to retype the card, expiry, CVV and zip, many won't. The fix is to keep every value the customer entered after a decline. Show the reason at the top in plain words, for example "Your bank declined this card. Try another card or contact your bank." Don't reload the page. Clearing the card number and CVV is the only reasonable exception, and even then, keep the rest.

**2. The Pay button is grey and doesn't say why.**
Customers who are ready to pay hit a dead button and can't tell what's missing. On some devices the button can't be reached by keyboard at all. Keep the button active at all times. If they press it with problems, show a message next to each problem field saying what to fix, such as "Enter the 16 digits on the front of your card." If several fields have problems, add a summary at the top. Only disable the button while the payment is actually being processed, so nobody double-charges themselves.

**3. The red "Invalid input" appears after the first digit.**
The form tells customers they're wrong while they are still typing correctly. It looks like an error on their side and erodes trust at the worst moment. Check fields when they press Pay. After a field has shown an error, re-check it as they edit, so the message disappears the moment it's fixed. Replace "Invalid input" with a message that says how to fix it.

**4. Smaller issues that add friction:**
- **Placeholders are the only labels.** "Card number" disappears when the customer starts typing. Add visible labels above each field.
- **The card, expiry, CVV and zip fields are plain text inputs.** That means phones show the full letter keyboard. Set them to show the number pad and turn on autofill, so saved cards fill in one tap. This is likely a big factor on mobile.
- **The country list has 195 entries starting at Afghanistan.** Preselect the customer's country, or let them type to search.
- **Spaces in the card number.** Accept spaces and dashes (customers type "4242 4242...") and clean them up in code rather than rejecting them.
- **The button says "Pay now".** Better to show the amount, for example "Pay $24.00".

**How to confirm the cause:** if your analytics can track field-level drop-off, check where people leave. I'd expect spikes at the card field (problem 3), on the Pay button (problem 2), and right after a decline (problem 1). Comparing mobile against desktop would also show whether the keyboard issue matters.

I'd hand your engineer items 1–3 as one ticket, since they're the same area of code. The label, keyboard and country list changes are small and can follow in the same release.

If you'd like, I can write the ticket text or a corrected version of the form for your engineer.
