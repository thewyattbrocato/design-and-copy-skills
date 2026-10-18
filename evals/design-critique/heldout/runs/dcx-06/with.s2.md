**Verdict:** Each page works alone. Across the four pages, the things the customer commits to (the real price, the cancellation terms, the details they entered) show up late or get dropped. That is probably the "off" feeling.

Assumed audience: neighborhood members booking on the web. I only had page text, so layout, contrast, error states, a progress indicator and back/edit behavior are not checked.

## Findings, in priority order

**1. Major: the cancellation policy first appears after the card fields, as small print under the pay button.**
- The 24-hour no-refund rule is a condition of the purchase. It is not on page 1, where someone picks a slot, and it is not on the confirmation.
- Someone booking Saturday's 18:00 slot on Friday evening is non-refundable from the moment they pay. Nothing tells them that.
- **Fix:** Show the rule on page 1 next to the slot, in plain type. Repeat it on page 3 as a visible line above the button, with the actual deadline for this booking (for this slot, Fri 13 Nov, 18:00). Repeat the deadline on the confirmation.

**2. Major: the price changes at the last step.**
- Page 1 shows "$24". Page 3 shows $25.92 after $1.92 tax (8% of $24).
- The member decided at $24 and sees $25.92 only after entering details. It is small money, but it reads as a surprise.
- **Fix:** On page 1 show "$24 + tax" or "$25.92 total". Use one money format throughout ($24 vs $24.00).

**3. Major: details the customer gave are dropped.**
- Sport is chosen on page 1 and never appears again.
- Guest count is collected on page 2, but it isn't in the page 3 summary or the confirmation. It also changes nothing visible, so it's unclear why it's asked.
- **Fix:** Carry sport, court, date, time and guest count into the page 3 summary and the confirmation. If guests don't affect price or capacity, say why you collect them (for example, "so we can set up the court"). If they do, show how.

**4. Moderate: the confirmation says almost nothing.**
- It has a reservation number and "on its way to your inbox". It doesn't show court, date, time, amount paid, the email address used, or the cancellation deadline.
- "Back to home" is the only action. There's no add-to-calendar and no way to view or cancel the booking.
- If the email is delayed, the member has nothing to show at the court.
- **Fix:** Repeat the booking summary and cancellation deadline on the page. Echo the email address. Offer "Add to calendar" and "Manage booking" as the actions. Make "Back to home" secondary.

**5. Moderate: the wording and formats drift, and the tone is retail.**
- The same thing is called Reserve, Select, booking, purchase, order and reservation.
- "Order confirmed" and "Thanks for your purchase!" sound like a shop, not a club.
- Times change format: "Sat 14 Nov, 18:00" on page 1, "Sat 14 November, 6:00 PM to 7:00 PM" on page 3.
- **Fix:** Pick one noun, "booking" or "reservation". Use "Booking confirmed" and "Confirm and pay". Use one date and time format. 12-hour is likely friendlier for a US club, since your prices are in dollars.

**6. Minor: no stated slot hold.**
- Nothing says the court is held while the member fills in details and pays. They may worry someone else will take it.
- **Fix:** If you hold it, say so, for example "We're holding Court 3 for 10 minutes". If you don't, tell them what happens when the slot is taken.

## What to keep
- **Page 3 line items:** Rental, tax and total are each on their own line, so the math is easy to check.
- **"Continue to payment":** The button tells people what comes next. "Who's playing?" is a friendly, human heading.
- **Page 1 result row:** Court, time and price are visible before selecting.
- **Reservation number:** It's already on the confirmation, so it just needs company.

## Fastest check
Watch three or four members book a slot for the next day. Ask them, without prompting, what they paid and what happens if they can't make it. I expect most will miss the cancellation rule and be surprised by the total.
