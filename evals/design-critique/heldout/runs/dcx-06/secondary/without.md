I think the problem is less in any single page and more in what carries from one page to the next, and what the user sees before paying. I'm working from the text only, so I can't see layout, font size, or whether the policy is a link or a checkbox.

**Most likely culprits, in rough order of concern:**

1. **The cancellation policy appears only after the payment fields, in small print, and the flow has no way to cancel.** The 24-hour rule and "late cancellations are not refunded" show up under the Complete purchase button, so the user agrees to it by paying. Page 4 offers only "Back to home," with no link to manage or cancel the booking. Someone who wants to cancel has no visible path, and the rule could be hard to enforce or to defend if disputed. This is worth a check with the club's policy owner, and possibly a lawyer, about whether the disclosure is clear and placed before the purchase commitment.

2. **The sport disappears after page 1.** The user picks Tennis or Pickleball, but the result reads only "Court 3," and the payment summary doesn't name a sport either. Someone could easily pay for a court that isn't the sport they meant, and nothing before payment would catch it.

3. **There's no real review step.** Page 2 collects name, email, and guest count, but page 3 summarizes only court, date, and time. The user pays without seeing who the booking is under, which email the confirmation goes to, or how many guests are coming. A mistyped email would send the confirmation to the wrong person, and the flow gives no chance to catch it.

4. **Guests are collected but go nowhere.** The guest count doesn't change the price, doesn't appear in the summary, and doesn't appear on the confirmation. If guests carry a fee or a club policy, the price is wrong. If they don't, the field does nothing downstream. Either way, someone should confirm what it's for.

5. **The confirmation is thin and depends on email.** Page 4 shows a reservation number and says the details are "on its way to your inbox," but it doesn't restate the court, date, time, or amount. If the email is delayed or misaddressed, the user has nothing on screen to check. The copy also mixes "purchase," "order," and "reservation," which may confuse people about what they bought.

**Ruled out:** The math checks out. $24.00 plus 8% tax is $1.92, for a total of $25.92. Sat 14 November 2026 is a Saturday, which is correct for today's date.

**To settle it, I'd want to know:**
- Is there a guest fee or guest policy?
- Is a court tied to one sport, or can Court 3 be either?
- Does the policy show as a link or checkbox on a real screen, or only as plain text?
- Can staff cancel bookings, and if so, how does a member ask?

If you can share the code or a screenshot of page 3, I can check the policy placement and the sport and guest handling against the actual implementation.
