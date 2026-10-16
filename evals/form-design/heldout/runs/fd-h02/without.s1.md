**What's wrong:** the form punishes people at the moments they're most likely to give up. There are four problems, roughly in order of damage.

1. **A declined card wipes the whole form.** This is probably your biggest loss. A decline is already a stressful moment, and the customer now has to re-enter everything: card, expiry, CVV, zip, country. Many won't. Browsers also can't help, because the page reload discards what they'd autofilled.

2. **The Pay button is grey and gives no reason.** Someone who thinks they're done sees a dead button with no explanation. They can't tell whether a field is wrong, missing, or the site is broken. People in that state leave.

3. **The error appears on the first digit.** "Invalid input" shows while the customer is still typing, so the form calls them wrong when they aren't. It also says nothing about what a valid entry looks like. This reads as hostile and erodes trust at a payment step.

4. **Smaller friction in the markup:**
   - The fields are plain text inputs. They lack the settings that trigger the numeric keypad on phones and let browsers autofill card details (`inputmode="numeric"`, `autocomplete="cc-number"` and similar). On mobile this is a real tax.
   - The country dropdown is a 195-item list starting at Afghanistan. It should default to the customer's country, or at least be typeable.

**What I'd fix first:** the declined-card reset. Keep the entered values after a failed payment, and show a clear message such as "Your card was declined. Try another card or check the details." It's likely the largest drop-off, and it's usually a small change for engineering. Ask them to submit the form without a full page reload, or to repopulate the fields on the server side. For security reasons, the card number and CVV are often cleared deliberately. Even if those two have to be re-entered, expiry, zip and country should persist.

**Second:** make the Pay button always clickable. When something is missing, show which field and why, for example "Expiry must be MM/YY". Third, validate when the customer leaves a field, not on each keystroke.

**To confirm it's the cause:** your analytics should show where the drop happened. Compare the funnel before and after the redesign, split by:
- Declined-then-abandoned sessions.
- Time spent on the payment step.
- Mobile versus desktop.

If mobile fell much more than desktop, move the missing input types and autofill up the list.

I haven't seen your analytics or the full code, so this is a diagnosis from the form and the QA notes. The funnel data will tell you which of these is actually costing you the most.
