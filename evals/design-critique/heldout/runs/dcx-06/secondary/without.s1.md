The thing most likely bugging her is the **cancellation policy**. It only appears once the customer is about to pay, in small print under the button, and nothing asks them to acknowledge it. Each page passes QA alone because the policy is technically shown, but as a whole flow the customer is asked to commit to a non-refundable charge with little notice:

- **Page 1 (select a court)** says nothing about cancellation or refunds.
- **Page 3 (payment)** has the policy in the smallest text on the page, directly under the action button. There's no checkbox or "I understand" step.
- **Page 4 (confirmation)** doesn't repeat the policy, shows no court, time, or amount, and gives no way to cancel. It only says the confirmation is "on its way to your inbox."

So a customer who books, pays, and later wants out has no visible path to cancel and may not have understood that a late cancellation forfeits $25.92. That's a complaints and chargeback risk, and it's the kind of thing a manager senses without being able to name it.

Smaller issues that compound it:

1. **The confirmation page is thin.** It lacks the booking details, the policy, and a cancel link. Once the email is delayed or lands in spam, the customer has only "#HC-2231" to go on.
2. **Guests don't appear to affect the price.** Page 2 asks for 0–3 guests, but the Page 3 summary shows only the court rental and tax. Either guests are free (and that should be stated) or the total is wrong.
3. **The sport choice doesn't carry through.** A customer filters by Tennis or Pickleball on Page 1, but the Page 3 summary ("Court 3, Sat 14 November, 6:00 PM to 7:00 PM") doesn't name the sport. A pickleball booking could be paid for as a tennis court, or the reverse, if Court 3 is shared or the sport filter is changed mid-flow.
4. **"Complete purchase" describes a reservation as a purchase.** The button and the "Thanks for your purchase!" line frame it as a retail sale, which reinforces the feeling that the policy is a fine print add-on.
5. **No time zone is shown** on the slot times. That matters for the 24-hour cutoff.

I only had the page text, not the code, so I can't confirm whether any of these happen in the actual system. The first things to check are:

- Does a cancel path exist anywhere in the product? If not, that's the biggest gap.
- Does the guest count change the charge?
- Does the sport selection get saved to the booking record?
- Does the confirmation email include the court, time, sport, and policy?

If you want, I can draft a revised Page 3 with an explicit acknowledgment checkbox and a Page 4 that restates the booking details and policy.
