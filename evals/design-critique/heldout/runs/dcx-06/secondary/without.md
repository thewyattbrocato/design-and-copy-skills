The thing the manager is sensing is probably this: **the cancellation policy shows up only after the customer has entered card details, and nothing in the flow lets them act on it.** Each page can pass QA on its own, but the problems show up across the sequence.

**1. The cancellation policy is disclosed too late, and only in small print.**
The only mention of the 24-hour rule is under the "Complete purchase" button on Page 3. Customers see the court price and the total before that, and nothing before payment says the booking is non-refundable inside 24 hours. Clicking "Complete purchase" is the only acceptance step, with no checkbox or explicit agreement.

**2. The flow has no way to cancel.**
The policy tells customers to cancel at least 24 hours ahead, but Page 4 offers only "Back to home." There's no link to view or cancel the booking, and the confirmation doesn't mention the policy. A customer who wants to cancel has to guess how, or call the club.

**3. A booking made within 24 hours is non-refundable the moment it's made.**
Nothing says this. A customer booking tomorrow at 6 PM can't cancel in time, and the page doesn't tell them so.

**4. "Late cancellation" is undefined.**
"At least 24 hours before your slot" leaves open which time zone applies, whether the cutoff is the slot start, and whether a no-show or partial cancellation counts as "late."

**5. The price shown before payment isn't the price charged.**
Page 1 shows $24. Page 3 charges $25.92 after $1.92 tax. The tax is revealed only at the last step, which is classic drip pricing and a common source of complaints. The tax may be correct; the problem is when the customer sees it.

**6. The confirmation doesn't confirm the booking.**
Page 4 says nothing about the court, date, time, sport, or guest count. It says the reservation is "on its way to your inbox," so the customer has nothing to check on screen if the email is slow or lands in spam. It also says "purchase" and "order," which is odd for a court slot.

**7. Sport and guests disappear after Page 2.**
- The sport filter on Page 1 isn't clearly marked as selected, and the result "Court 3" doesn't name a sport. Page 3's summary doesn't show the sport either, so a customer who wanted pickleball could pay for a tennis court without noticing.
- Guests are collected (0–3) but never appear again. I can't tell from the text whether guests cost extra, need to be registered, or are recorded at all. If the club charges per guest or limits guests, that's a gap.

**What I'd change, in order of importance:**
1. Show the cancellation terms before payment, with a required checkbox, and repeat them on the confirmation.
2. Add a cancel/manage-booking link to the confirmation and to the confirmation email, and make the cutoff explicit (for example, "cancel by 6:00 PM Friday for a Saturday 6:00 PM slot, America/New_York").
3. Show the total with tax on the court results page, or label the $24 as "plus tax."
4. Put the booking details on the confirmation page: sport, court, date, time, guest count, and reservation number.
5. Change "purchase/order" to "booking/reservation," and label the selected sport on every page.

I worked only from the text you pasted, so I haven't checked the live app, and I'm inferring the guest-fee and time-zone questions from what's missing. The club should confirm those with whoever owns the pricing and policy.
