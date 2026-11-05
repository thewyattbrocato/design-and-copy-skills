**The flow fails as a whole because it never states one consistent promise: the price, the policy, and what you're booking all change from page to page.** Each page is fine alone. Together they read like a generic store checkout bolted onto a club, which is probably what the manager is sensing.

## Findings, ranked

**1. Major: the price changes at the last step.**
- Page 1 says **$24**. Page 3 says **$25.92** after $1.92 tax, which is 8% of $24.
- The math is right, but the person only sees the real price after entering their details and arriving at the card fields.
- **Fix:** show the tax-inclusive total ($25.92) on page 1, or at least "$24 + tax".

**2. Major: the cancellation rule shows up after the decision.**
- It appears only as small print under "Complete purchase", after the person has started typing card details. It reads as a trap even if no one meant it that way.
- It's also the highest-stakes line in the flow, because late cancellations aren't refunded.
- **Fix:** put the rule on page 1 beside the Select button, and repeat it in the page 3 summary box with the actual deadline. For this slot that's Fri 13 Nov, 6:00 PM, which you can compute and show.
- Repeat the deadline on the confirmation page. It's currently missing there.

**3. Major: the confirmation page tells people almost nothing.**
- It gives a reservation number and "on its way to your inbox". It omits the court, date, time, the email address it was sent to, the cancellation deadline, and any way to manage or cancel the booking.
- This is the page people screenshot or return to. "Back to home" is the only action.
- **Fix:** repeat the booking summary, name the email address, show the deadline, and add a "Manage booking" link.

**4. Moderate: the vocabulary drifts.**
- The same thing is called a *reservation* (page 1 heading, page 4 body), a *booking* (page 3 heading), a *purchase* (page 3 button, page 4 body), and an *order* (page 4 heading).
- "Order confirmed" and "Thanks for your purchase!" sound like a retailer. The rest of the flow sounds like a club.
- **Fix:** pick "reservation" and use it everywhere. Suggested wording: "Pay and reserve", "Reservation confirmed".

**5. Moderate: guest count is collected and then dropped.**
- Page 2 asks for the number of guests (0–3). That number never appears in the page 3 summary or on the confirmation, and it doesn't change the price.
- People will wonder whether it was saved.
- **Fix:** show it in the summary and confirmation ("You + 2 guests"). If it doesn't matter to the club, remove the field.
- Related: the page 3 summary omits the sport, so "Court 3" is ambiguous.

**6. Minor: three date and time formats.**
- Page 1 uses "Sat 14 Nov" and "18:00-19:00". Page 3 uses "Sat 14 November" and "6:00 PM to 7:00 PM". Dollars and AM/PM suggest a US audience that likely doesn't read 24-hour time.
- **Fix:** use the 12-hour format from page 3 everywhere, with one date format.

## What works and should stay
- **The flow is short.** Four steps with plain headings.
- **"Who's playing?"** is friendlier and more specific than "Your details".
- **The page 3 line items add up and are itemized.** Rental, tax, and total are clear. They just need to appear earlier.

## Not checked
I only had the text, so I couldn't judge visual hierarchy, contrast, the size of the small print, error states, or mobile layout. I also assumed the guest count has no pricing effect, since nothing shows one.
