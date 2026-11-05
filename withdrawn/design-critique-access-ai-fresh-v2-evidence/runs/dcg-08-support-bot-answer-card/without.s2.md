**Short version:** the card states a policy with full confidence but doesn't say where it comes from, doesn't answer the question for this customer, and leaves a gap right where people are most likely to act on it. A pale disclaimer doesn't fix that.

**1. Fix the content**
- **Answer the actual question in the second half.** "After 30 days, you can cancel and keep access" never says whether money comes back. Readers will guess, and some will guess wrong. Say it plainly: "After 30 days, we don't refund the unused portion" (or whatever the real policy is).
- **Lead with the direct answer.** For example: "Yes, if it's within 30 days of purchase." Then give the details.
- **State the conditions.** Say whether the 30 days run from the original purchase or from a renewal. Say whether the refund covers upgrades, add-ons, or discounted or regional purchases. If there are exceptions, name them or route those cases to a person.
- **Soften the timing.** "5 to 7 working days" is really the bank's timing. Write "we issue it right away; your bank usually takes 5 to 7 working days to show it."

**2. Ground it in the real policy instead of generated prose**
- For money, legal and cancellation topics, build the answer from the policy text itself (a template or quoted passage), not free-form generation. Show "Policy last updated: <date>."
- Replace the three generic links with a citation attached to the claim, such as "Source: Refund policy, section 2," linking to that section. "Our terms" as a whole document isn't verifiable.
- Test these answers against the policy in your evals. Refunds should be a regression-tested topic.

**3. Make it specific to the customer when you can**
- If they're logged in, check their plan and purchase date: "You bought this plan on Oct 20, so you're eligible until Nov 19."
- Add an action button, "Request a refund," next to the answer. That's better than text that tells them to go find a form.

**4. Replace the footer with in-context trust signals**
- Remove or demote "answers may be inaccurate." It's unreadable, it's far from the claim, and it shifts blame to the customer without helping them.
- Put a visible line near the money claim: "Check your eligibility before cancelling," or "Not sure? Talk to a person," with a link to human support.
- For high-stakes topics, hand off to a human when the question has any wrinkle (an old purchase, a renewal, a dispute). Don't let the bot guess.

**5. Make the feedback useful**
- Add a reason when someone clicks thumbs down ("Wrong," "Didn't answer my question," "Need a person"). Review the refund-topic downvotes regularly.
- Log which answers were later followed by a support ticket or chargeback. That's a better signal of wrong answers than thumbs.

**Suggested rewrite:**
> **Yes, if it's within 30 days of purchase.** You'll get a full refund, which we issue right away. Your bank usually shows it in 5 to 7 working days.
> **After 30 days, the plan isn't refundable,** but you can cancel anytime and keep access until your term ends.
> Renewed recently or have a special case? [Talk to our team].
> [Request a refund] · Source: Refund policy §2 (updated <date>)

I haven't seen the actual policy. Check the rewrite against it before shipping, especially the "after 30 days" line. If the policy allows exceptions, the card should say so.
