Your QA notes describe three separate problems, and the markup shows more. In order of what I'd fix first:

**1. Wiping the form after a decline (fix first).**
- **What happens:** Someone who just had a card declined has to retype everything. Many will leave instead. This is the point where you lose people who were ready to pay.
- **Fix:** Keep what they typed and show a message at the top of the form, such as "Your bank declined this card. Try another card or contact your bank." Keep the fields filled in. Never store or re-show the CVV from the server, but the page shouldn't reload at all. Submit in the background and update the page in place.

**2. The Pay button is grey, and nothing says why.**
- **What happens:** A disabled button gives no reason, and it's often unreachable by keyboard or screen reader. Someone with an autofill glitch or one typo sees a dead button and doesn't know what to do.
- **Fix:** Keep the button always clickable and labeled with the amount, like "Pay $24.00". When it's pressed with problems, show a short summary at the top listing each problem. Each item should link to its field. Each field also gets its own message saying how to fix it, such as "Enter the 3 or 4 digits on the back of your card".

**3. "Invalid input" appears after the first digit.**
- **What happens:** It tells people they're wrong while they're still typing a correct number. It's also vague.
- **Fix:** Don't show errors while someone is still typing their first attempt. Check when they press Pay. After a field has shown an error, re-check it as they edit so the message disappears as soon as it's fixed.

**Smaller problems visible in the markup (second pass):**
- **No labels:** The fields have placeholders but no visible labels. The name disappears once someone types, which hurts anyone checking their entry.
- **Wrong keyboards:** Fields are plain text, so phones show a full keyboard. Card, expiry, CVV and zip should bring up the numeric keypad. Add the standard autofill hints (`cc-number`, `cc-exp`, `cc-csc`, `postal-code`, `country`) so the browser and wallets can fill them in. Autofill is a big conversion lever on mobile.
- **Card formatting:** Accept spaces and dashes in the card number and clean them up in code, rather than rejecting them.
- **Country list:** A 195-item dropdown starting at Afghanistan is slow on a phone. Preselect the country from the person's location or past orders, and make it type-to-search.
- **Order and review:** Zip and country usually come before card details. Show an order summary with the total near the button so people see what they're paying.

**To confirm the cause:** Since you're comparing before and after the redesign, check drop-off by field and see how often declined cards lead to a retry versus an exit. I'd expect the first fix to show up there. I can't see your analytics, so that's a guess from the form alone. The server must also re-check everything, regardless of what the page does.

If you give this to your engineers, the ask is: "Keep values after a decline, never disable Pay, and only show errors after the first press of Pay." I can write that up as a ticket, or draft the corrected form code, if you'd like.
