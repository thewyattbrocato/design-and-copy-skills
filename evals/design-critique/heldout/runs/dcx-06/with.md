**The flow reads as a generic online-shop checkout, not a booking at a neighborhood club. Each page is fine alone, but the whole thing never tells the player what they're committing to until after they've committed.** That's most likely the "off" feeling. Page 2 sounds like a club ("Who's playing?"). Pages 3 and 4 sound like a retailer: "Complete purchase," "Order confirmed," "Thanks for your purchase!"

I only had the text, so I couldn't check layout, visual hierarchy, contrast, progress indicators or error states.

## Findings, in fix order

1. **Blocker-ish: the cancellation rule shows up after the decision.**
   - It first appears as small print under the pay button on page 3.
   - A no-refund rule is a cost, and it appears after the player has picked a slot, entered details and reached the card fields.
   - Fix: show the rule on page 1, next to the result (for example, "Free cancellation until Fri 13 Nov, 18:00"). Keep it on page 3 as normal-size text above the button, and repeat it on the confirmation.
   - Bookings made within 24 hours are non-refundable from the moment of purchase, and nothing says so.

2. **Major: the price changes between page 1 and page 3.**
   - Page 1 says $24 and page 3 says $25.92, because $1.92 of tax appears for the first time at payment. That's 8%, computed from the page 3 line items.
   - The amount is small, but a surprise at the card form costs trust.
   - Fix: show "$24 + tax" on page 1, or show the all-in $25.92.

3. **Major: the confirmation page doesn't confirm the booking.**
   - It gives a reservation number and says an email is coming. It doesn't restate court, sport, date, time or amount paid.
   - It doesn't echo the email address typed on page 2, so a typo goes unnoticed.
   - It offers no way to cancel, change or add the slot to a calendar. Its only action is "Back to home."
   - Someone checking at 17:45 on the day has nothing to look at.
   - Fix: repeat the booking summary and email address, add a "Manage or cancel" link and "Add to calendar," and change the heading to something like "You're booked: Court 3, Sat 14 Nov, 6 PM."

4. **Moderate: the guest count goes nowhere.**
   - Page 2 asks for "Number of guests" (0–3). It doesn't change the price, appear on the payment summary or show on the confirmation.
   - The player can't tell why it's asked. It also takes no guest names.
   - Fix: if it feeds capacity, check-in or insurance, say so in a line of helper text and carry it through. If nothing uses it, remove the field.

5. **Moderate: the booking details change shape and drop information between pages.**
   - Page 1 says "Sat 14 Nov" and "18:00–19:00." Page 3 says "Sat 14 November" and "6:00 PM to 7:00 PM." The date is abbreviated on one page and spelled out on the other, and the time moves from 24-hour to 12-hour. People double-check at payment, so a format change makes them wonder if something changed.
   - The sport the player filtered on (tennis or pickleball) never appears on the payment summary or the confirmation.
   - Page 2 has no summary at all.
   - Fix: pick one date and time format for the whole flow. Show one persistent summary line on pages 2–4 with sport, court, date, time and price.

6. **Minor, voice: the copy doesn't match the club.**
   - "Order," "purchase" and "Thanks for your purchase!" treat a court as a product.
   - Fix: "Confirm and pay $25.92," "You're booked," and "See you on Court 3." This is partly taste, but it's likely what the manager is reacting to.

## What works and should stay

- **Page 1 narrows to one clear result.** The player sees court, time and price and one Select action.
- **Page 2 is short.** There are three fields and a button whose label ("Continue to payment") says what comes next.
- **Page 3 itemizes the charge and repeats the booking in a summary box.** The total is explicit and sits before the card fields.
- **The reservation number is on the confirmation.** That gives the player and the front desk something to refer to.

## Not checked
- I haven't seen the visual layout, so how prominent the cancellation text is on screen is unchecked.
- The page text doesn't show a slot-hold timer, a step indicator or any error states, so I haven't judged them.
