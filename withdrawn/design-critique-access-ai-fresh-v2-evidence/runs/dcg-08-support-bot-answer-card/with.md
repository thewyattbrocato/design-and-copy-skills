**The main problem is that the card states policy as settled fact, and its only warning is in the one place customers don't look.** The paragraph reads as authoritative, so people act on it. The "may be inaccurate" footer is pale grey, small, and below the feedback buttons. It's also generic, so it doesn't say what to double-check. I'd make six changes, ranked below.

1. **Tie the claim to its source, next to the claim (blocker).**
   - The three links are generic ("billing basics", "our terms") and aren't tied to any sentence. A customer can't tell which link backs the 30-day rule.
   - Put a line directly under the paragraph, such as "Source: Refund policy, §3, updated [date]", linking to the exact clause. Generate it from the document the bot actually retrieved. If the bot can't cite a source, it shouldn't state a refund rule as fact.

2. **Take the guess out of money answers (blocker).**
   - The bot says "within 30 days of purchase" without knowing this customer's purchase date.
   - If the bot can see the account, show "You bought on [date]; you're inside the window until [date]" and add a "Request refund" button.
   - If it can't, end with "Refund decisions are confirmed by support" and a "Check with a person" button. Refunds are high-stakes, so they should hand off.

3. **Put the conditions in the answer (major).**
   - Everything is in one paragraph. The conditions that usually make refund answers wrong are missing: first purchase versus renewal, which date the 30 days starts from, and whether discounts, region or payment method change anything. I don't know your actual policy, so check which of these apply.
   - Lead with "Yes, if you're within 30 days of purchase." Follow with two or three short lines for what applies, what doesn't, and what happens after day 30.

4. **Say what is out of the bot's hands (major).**
   - "Returns to your card in 5 to 7 working days" promises something the bank controls. Say what you do ("we issue it within X days") and what you don't ("your bank may take longer").

5. **Replace the footer with a specific, readable notice (moderate).**
   - Move it up to sit with the source line, at body size and normal contrast. I haven't measured the contrast of the current grey, but pale grey small type is the usual failure here.
   - Use something like "Check the policy above before you cancel or buy again". Boilerplate in a bigger font would still be ignored.

6. **Make thumbs-down useful (minor).**
   - A thumbs-down should ask "What was wrong?" and offer a person. It's also how you'll find out which answers are failing.

**Keep:**
- It answers the question first.
- It covers both the inside-30-days and after-30-days cases.
- The wording is plain, with no jargon.
- Feedback is on the card.

**Not checked:** your real refund policy, the contrast values, and which sentence customers act on wrongly. To find that last one, read 20 or so logged thumbs-down or follow-up tickets on this topic before settling on the wording in point 3.
