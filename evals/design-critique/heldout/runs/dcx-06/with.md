**The flow reads as a club on pages 1–2 and an online shop on pages 3–4, and the money and policy details show up later than the decision they affect.** Each page passes alone, so QA found nothing. The problems only show when you read the pages in order.

## Findings, in priority order

**1. The cancellation policy appears only after the decision is made. (Major)**
- It is small print under "Complete purchase" on page 3.
- It is not on page 1, where the player picks a slot. It is not on page 4 either, where they would look when plans change.
- The rule is strict: 24 hours' notice, and late cancellations are not refunded.
- Anyone booking a slot less than 24 hours away is non-refundable from the moment they pay, and nothing says so.
- **Fix:**
  - Show a one-line policy on the page 1 result card.
  - Give it a plain line above the pay button on page 3.
  - Repeat it on page 4 with a cancel or change link.
  - For slots inside 24 hours, say "not refundable" outright.

**2. The price changes between page 1 and page 3. (Major)**
- Page 1 shows $24. Page 3 shows $25.92 after $1.92 tax, which works out to 8% of $24.
- The arithmetic is correct. But the player sees the total only after entering their details, on the third page.
- **Fix:** show "$24 + tax" on page 1, or the all-in $25.92. Keep a running summary on page 2.

**3. The booking has five names, and the tone shifts. (Moderate, on every page)**
- The same thing is called "reserve" (p1), "booking" (p3), "purchase" (p3, p4), "order" (p4) and "reservation" (p4).
- "Who's playing?" sounds like the club. "Complete purchase", "Order confirmed" and "Thanks for your purchase!" sound like a generic checkout template.
- A neighborhood club's manager would likely notice this even if she can't name it.
- **Fix:** pick one noun, "reservation" or "booking". Then rewrite the p3 button and the p4 heading and body in the club's voice. For example: "Pay and reserve Court 3" and "You're booked: Court 3, Sat 14 Nov, 6–7 PM."

**4. Guests are collected but never used. (Moderate)**
- Page 2 asks for 0–3 guests. The number never appears in the page 3 summary, the pricing or the confirmation.
- The player can't tell whether guests change the price, the court or the capacity.
- **Fix:** if guests affect nothing, say why you ask ("so we know how many to expect"). Otherwise show the count in the summary. If it truly isn't needed, drop the field.

**5. The confirmation doesn't confirm the booking. (Moderate)**
- Page 4 gives only a number (#HC-2231) and says the details are "on their way to your inbox."
- It repeats none of the court, date, time, total paid or email address used. It has no calendar add and no cancel link.
- The only record is an email that may be late or end up in spam. "Back to home" is a dead end.
- **Fix:** repeat the page 3 summary and the email address. Add "Add to calendar" and "Manage reservation". Make "Back to home" a secondary action.

**6. The same facts are formatted differently on each page. (Minor, on 3 of 4 pages)**
- Time is "18:00-19:00" on page 1 and "6:00 PM to 7:00 PM" on page 3.
- Date is "Sat 14 Nov" on page 1 and "Sat 14 November" on page 3.
- Price is "$24" on page 1 and "$24.00" on page 3.
- Players may briefly wonder whether it's the same slot. Pick one format. Use 12-hour time if your members do.

**7. The sport is chosen and then disappears. (Minor)**
- Pages 3 and 4 say "Court 3" but not tennis or pickleball.
- Add the sport to the summary and the confirmation.

## What works and should stay
- **The price breakdown on page 3.** It lists rental, tax and total, and the numbers add up. That's honest, and it only needs to be shown earlier.
- **The page 2 form.** Three short fields and a button that says what comes next ("Continue to payment") keep it quick.
- **The summary box on page 3.** It lets the player check the slot before paying. Carry it back to page 2.
- **The filter-then-select start.** One result and one action is clear.

## Not checked
I only had the text, so layout, visual hierarchy, contrast, error states and mobile behavior are not covered. I also don't know whether guests affect capacity or whether the policy has exceptions. Those could change the severity of findings 1 and 4.
