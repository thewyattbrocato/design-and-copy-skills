**Yes, there's a problem. The review step is catching little of what it's there to catch.**

**The numbers**
- At 4,000 claims a week, the model is wrong on about 360 (9%).
- Reviewers change about 80 (2%).
- Even if every change was a correct fix, reviewers catch at most 2/9, about 22%, of the model's errors. At least 7% of claims, about 280 a week or roughly 14,500 a year, go out wrong with a human sign-off on them.
- The true catch rate is probably lower, because some of the 80 changes may be reviewers "fixing" correct picks.

**Why it happens**
- **Default bias:** The model's answer is pre-selected, and "Next claim" saves it. Doing nothing counts as approval, and disagreeing takes extra clicks. People anchor on a visible suggestion.
- **No rationale:** Nothing shows why the model chose its category, so a reviewer has to redo the classification from scratch to disagree. Under volume pressure, they won't.
- **Nothing separates a considered approval from a skim:** The button doesn't ask for a decision, and the logs can't tell the two apart.
- **Oversight in appearance only:** The 2% change rate probably makes the process look healthy. That's a false comfort, since the reviewers' real disagreement rate would be near 9% if they were independently checking.

**How bad it is**
- The error rate is roughly 3.5x what a working review would leave, and the humans add little over the model alone.
- Severity depends on what a wrong category costs. If it only misroutes a claim, that's a nuisance. If it affects payouts, denials, fraud flags, reserves or regulatory reporting, it's serious.
- Two caveats. I'm assuming the 9% was measured against the model's raw picks. If the audit was of final saved categories, the picture changes. I also can't tell from the numbers alone whether reviewers are rubber-stamping or the errors are just hard to spot. Either way the review adds little, but the fix differs.

**What I'd do**
1. **Measure first (a week or two):**
   - Seed known-answer claims into the queue to get the true catch rate.
   - Pull time-per-claim and change rate by reviewer, category and model confidence.
   - Check whether the 9% errors cluster in particular categories.
2. **Change the interaction:**
   - Replace "Next claim" with an explicit confirm, such as "Confirm: Water damage".
   - Show the model's top 2–3 candidates, with confidence if it's calibrated.
   - Highlight the claim text that drove the pick.
3. **Reduce anchoring where it matters:**
   - Route low-confidence or high-stakes claims to a blind decision, where the reviewer picks a category before seeing the model's suggestion.
   - Let high-confidence claims through a lighter review, plus random blind audits.
4. **Keep monitoring:**
   - Keep a small ongoing share of gold claims.
   - Track per-reviewer agreement and time-on-claim.
   - Report the post-review error rate, not just the model's.
5. **Pilot it as an A/B test.** Blind review will be slower, so test whether the accuracy gain justifies the time before rolling it out. At 4,000 claims a week, a few weeks gives enough data.

If you can share the logs or the audit data, I can work out the catch rate and which categories are worst.
