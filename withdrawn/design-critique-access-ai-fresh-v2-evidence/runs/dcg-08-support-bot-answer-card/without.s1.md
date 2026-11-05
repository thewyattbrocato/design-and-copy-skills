The card states a money-and-deadline answer with full confidence. It backs that up with generic links and a disclaimer nobody will read. I haven't seen your actual policy, so I can't say whether the paragraph is wrong. The card gives a customer no way to check it either.

**1. Make the answer verifiable**
- Replace "billing basics / cancelling your plan / our terms" with a link to the exact refund-policy clause the answer came from. Label it with what it is, for example "Refund policy, section 4.2 (updated 12 Mar 2026)".
- For high-stakes topics like refunds, pricing, cancellation and deadlines, don't let the model paraphrase freely. Either pull the approved policy text verbatim or check the generated answer against it before showing it. Free-form generation is the likeliest source of the wrong answers.

**2. Tighten the wording**
- The paragraph leaves out the things that usually decide eligibility: first purchase vs. renewal, promo or discounted plans, region, and whether the 30 days is calendar days. Add those conditions, or say "eligibility depends on X".
- "Money returns in 5 to 7 working days" is probably the processor's timing, and banks vary. Say "typically", or drop it unless it's guaranteed.
- The customer asked about money back, but the after-30-days sentence never says whether a refund is possible. It only says they can cancel. If the policy is "no refund after 30 days", say that directly.
- Lead with the direct answer and split the two cases into short lines instead of one paragraph.

**3. Personalize the deadline**
- If the bot knows the customer's account, show "You purchased on 3 Oct, so the refund window closes 2 Nov." That's more useful and less error-prone than a generic rule.

**4. Give a next step**
- Add a "Request a refund" button or a link to the exact page. Without one, customers act on the text alone and guess at the rest.
- For anything involving money, add "Not sure? Talk to a person", visible on the card.

**5. Fix the disclaimer**
- Pale grey tiny "answers may be inaccurate" does nothing, because it's generic and easy to miss. Delete it as the main safeguard.
- Put a short, readable note next to the claim instead, such as "Based on our refund policy. Final decisions are made by Support." Only add it where it applies.

**6. Make feedback do something**
- A thumbs-down should ask why and offer a human handoff, and it should flag the answer for review. A bare vote tells you little.
- Log every refund-related answer. Regularly sample them against the current policy and keep a test set of refund questions you run before each prompt or model change.

If you do only three things, make them these: ground and verify policy answers, add the specific source and the next-step button, and replace the footer with an inline note.

If you share the policy text or the card's code or template, I can draft the revised copy or the change itself.
