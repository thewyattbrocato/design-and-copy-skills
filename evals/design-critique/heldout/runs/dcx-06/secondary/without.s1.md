Each page is internally correct. The math works (8% tax on $24 is $1.92, so $25.92), and Sat 14 Nov 2026 is a Saturday. The problems show up when the pages are read as one flow.

**1. The price shown isn't the price charged.** Page 1 says $24. Page 3 charges $25.92, because an 8% tax is added at the last step. The tax is disclosed before payment, so this may be legal, but the headline number understates what the user pays. That's the kind of gap drip-pricing rules target, and it's the most likely thing a manager would sense without naming.

**2. The cancellation policy is shown after the card is entered, with no acknowledgment.** It appears as small print under "Complete purchase." There's no checkbox or "I understand," and nothing earlier in the flow mentions it. The user commits to a non-refundable late cancellation without having affirmatively agreed to it. The flow also never says how to cancel, and the confirmation page has no cancel link. The policy is in force but has no working path.

**3. The sport disappears after page 1.** The user picks Tennis or Pickleball, but the result shows only "Court 3, 18:00-19:00." The summary and confirmation never name the sport. A pickleball player can end up booked on a tennis court without noticing. (Whether Court 3 can be either sport is unclear from the text.)

**4. The guest count is collected and then dropped.** Page 2 asks for 0-3 guests, but no price, summary, or confirmation mentions them. Either a guest fee is missing or the field does nothing. Either way, the club's record of the booking won't show the guests.

**5. The slot isn't held.** Court 3 is chosen on page 1, but nothing reserves it through details and payment. If someone else books it in the meantime, no page says what happens after the card is charged.

**6. The confirmation is thin.** It shows only a reservation number and says the details are "on its way to your inbox." It doesn't show the date, court, time, sport, guests, amount paid, or a cancel link. If the email is delayed or lands in spam, the user has a number and one button, "Back to home." Small points: "Thanks for your purchase" is odd for a court booking, and the flow shows times as "18:00" on page 1 and "6:00 PM" on page 3.

Since each page passed QA on its own, the issues fall between pages. The most serious combination is #1 and #2 together: the user pays more than advertised and agrees to a non-refundable policy they only glimpsed at the last step. #3 and #4 are data-loss problems that will cause support tickets.

If you want, I can draft the fixes as a spec or a list of copy changes for the manager, for example a pre-tax/total price on page 1, an explicit policy checkbox before payment, sport and guests carried through to the summary and confirmation, and a confirmation page with full details and a cancel link.
