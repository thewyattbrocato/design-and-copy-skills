**Yes, there's a real problem. The review step is catching very little, so it gives much less protection than it appears to.**

**The numbers**
- Of 4,000 claims a week, about 360 (9%) have a wrong model category.
- Reviewers changed about 80 (2%). Even if every change was a correct fix, they caught at most 80 of 360, or about 22% of errors.
- So at least 280 wrong categories a week, roughly 14,000 a year, get approved and saved with a human sign-off on them.
- That's a floor. Some of the 80 changes may be disagreements over ambiguous claims or mistaken edits, which would make the catch rate lower.

**Why it's happening**
This design predicts rubber-stamping:
- The pre-selected answer anchors the reviewer, and agreeing takes zero effort.
- "Next claim" records approval as a side effect of moving on. Nothing separates "I checked this" from "I skipped it."
- The model gives no reasoning, so the reviewer must read the claim and decide independently to catch an error. At 4,000 claims a week, that takes more time than most reviewers have.
- Rejecting costs a click and a decision, and accepting costs nothing.

This is mostly a design problem, not a reviewer problem.

**Caveats**
- I don't know what's at stake in a wrong category. If it drives payout, denial, fraud flags, or regulatory reporting, this is serious. If it only affects reporting, it's less so.
- The 9% and 2% may come from different samples or periods, and I don't know how the audit set ground truth. Check that before quoting the numbers externally.
- Errors are probably concentrated in certain categories or claim types. The average hides that.

**What I'd do**
1. **Measure reviewer detection directly.** Seed the queue with claims whose correct category is known, including some where the model is wrong. Also log time per claim. This gives the real catch rate, instead of one inferred from the 2%.
2. **Change the interaction.**
   - Replace "Next claim" with an explicit action like "Confirm: [category]", or start with the dropdown empty for a subset.
   - Log "confirmed" and "changed" as separate events.
3. **Add context.** Show the model's confidence and top 2–3 alternatives. If feasible, highlight the text spans that drove the choice. Test this before rolling it out, because a wrong rationale can increase over-trust.
4. **Route by confidence.**
   - Send low-confidence or historically error-prone categories to a forced-choice or blind review.
   - If high-confidence categories prove highly accurate on audit, lighten review there so reviewer attention goes where errors cluster.
5. **Keep auditing.** Blind-label a weekly random sample and track the model's error rate, reviewer catch rate, and error rate after review.
6. **Protect the data.** Don't use saved categories as training labels or ground truth without accounting for this. Unchanged model picks are mostly the model's own output, so training on them reinforces its mistakes.

I'd start with step 1, because it's cheap and tells you how much the other steps need to change.

If you can share the consequences of a wrong category and the per-category error breakdown, I can put a firmer severity on this and say which of these steps matter most.
