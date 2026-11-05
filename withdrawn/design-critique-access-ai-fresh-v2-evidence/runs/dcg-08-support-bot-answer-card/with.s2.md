**The card states a policy as settled fact and puts the doubt where nobody reads it.** Customers act on the paragraph, and the "may be inaccurate" footer is the only sign that the answer could be wrong. I'm assuming a generated answer, shown to customers deciding whether to request or skip a refund, at high fidelity. I haven't seen the real card, so contrast and sizes are not checked.

**Findings, highest severity first**

1. **Blocker: the answer has no visible source.**
   - The paragraph reads as authoritative, but nothing says which policy it came from or when that policy was current.
   - The links go to generic pages ("billing basics", "our terms"). They don't point to the refund clause the answer relies on.
   - Change: attach a citation to the claim itself, for example "Source: Refund policy, §3, updated [date]". Link to that exact section, and quote the sentence it rests on.

2. **Blocker: the answer ignores the facts that decide the outcome.**
   - "Within 30 days of purchase" depends on the customer's purchase date, and the card doesn't use it. It also ignores whether the plan was bought directly or through a reseller or app store, and whether it was a renewal.
   - The customer has to work out which case they are in. Wrong guesses are probably where the bad actions come from.
   - Change: if the bot can see the account, state the result: "You bought on 12 Oct, so you're inside the 30-day window until 11 Nov." If it can't, ask one question first, or list the conditions that change the answer.

3. **Major: the caveat is in the wrong place and has no content.**
   - It sits at the very bottom, in pale grey small type, and says nothing about what to check. It will be skipped, and even if read it gives no action.
   - Change: remove the generic footer. Put a specific line directly under the money claims: "Refund eligibility depends on your purchase date. Check it in [Billing → Orders] before cancelling."

4. **Major: no safe next step at the point of decision.**
   - The card answers "can I?" but offers no way to do it, and no way to reach a person when the stakes are money.
   - Change: add one primary action, "Request a refund" (or "Check my eligibility"), and a secondary "Ask a person to confirm". Show the human option more prominently on any answer that involves money or cancellation.

5. **Moderate: one dense paragraph hides the two outcomes.**
   - It holds a refund path (full refund, 5–7 working days) and a non-refund path (cancel, keep access to term end). A skimmer can merge them.
   - Change: split into two short labeled lines, "Within 30 days" and "After 30 days". Bold the deadline.

6. **Moderate: the feedback controls can't correct the harm.**
   - Thumbs up/down give you a signal after the customer has already acted. They also don't say what was wrong.
   - Change: on thumbs-down, ask "What was wrong?" with options such as wrong date, wrong policy, doesn't apply to me, or other. Send these to whoever owns the policy text. Use them to find which answers keep failing.

7. **Minor: link labels are vague.** "Billing basics" and "our terms" don't say what the customer will find. Rename them to the content, for example "Refund policy" and "How to cancel", and make them as large as body text.

**Keep**
- The refund window, the payout time and the post-window behavior are all stated in plain, concrete terms.
- The cancel-and-keep-access line stops customers from assuming cancelling loses their access.
- The links to cancellation and terms are the right destinations. They should just point to specific sections.

**Fix order:** 2 and 1 first. They change whether the answer is right, and everything else only helps customers notice when it isn't. Then 3 and 4. Items 5 to 7 are cheap and can follow.

**Cheapest test:** give five people a past refund question with their own purchase date and watch what they do after reading the card. Count how many request or skip a refund wrongly before and after the changes.

**Not checked:** contrast and type sizes, and whether the bot has account access. That second point decides which version of fix 2 you can build.
