**Yes, there's a problem, and it's a significant one. The review step is mostly nominal.**

## How bad is it

- At 4,000 claims a week, a 9% model error rate is about **360 wrong categories a week**.
- Reviewers changed about **80 a week** (2%). Even if every change was a correct fix, they caught at most about 22% of the model's errors.
- That leaves **at least 280 wrong claims a week** (about 7%) saved as if a human had verified them. That's roughly 14,000 a year.
- The true catch rate is probably lower, because some of the 80 changes are likely reviewer disagreements or mistakes rather than real fixes.

Compare that with what a real review would produce. If reviewers were actually checking, the change rate should be near the error rate, so around 9%, not 2%. A 2% change rate suggests most claims get a glance at best.

The design explains this:

- **The default is the model's answer.** Doing nothing means approving.
- **"Next claim" saves the selection.** Approving takes no deliberate action, and there is no "confirm" step to skip.
- **There's no rationale.** The reviewer must read the claim and independently work out the right category to disagree. Agreeing is much cheaper than disagreeing, and at 4,000 claims a week that pressure compounds.

This is a standard automation-bias and anchoring setup. The risk is also worse than a plain error rate, because the human sign-off makes the data look verified. If saved categories feed retraining, reporting, or payout routing, the errors become trusted labels. Retraining on those labels would also weaken the audit signal you rely on.

**Caveats on the numbers:**

- I'd check that the 9% and the 2% are comparable. If the audit measured the final saved category rather than the model's raw pick, the model's raw error is higher, around 11%.
- The errors are probably not uniform. They likely cluster in ambiguous categories, which makes the problem worse where it matters most.
- Severity depends on what the category drives, such as routing, payout, or fraud flags. I don't know that from what you've given me.

## What I'd do

1. **Measure before redesigning.**
   - Join the audit sample to the review logs. Of the audited errors, how many did reviewers change? Break that down by category, reviewer, time on screen, and model confidence.
   - Seed a small share of the queue with known-wrong suggestions to get a direct catch rate.

2. **Remove the implicit approval.** Replace "Next claim" with an explicit action, like "Confirm: *Water damage*" alongside "Change category". This is cheap and removes the "do nothing" path. It adds a click, so watch the throughput impact.

3. **Give reviewers something to check against.** Show the model's confidence and its runner-up categories. Highlight the claim text that drove the pick. Be aware that explanations can increase over-trust, so test this rather than assume it helps.

4. **Spend attention where errors are.** Send low-confidence or historically error-prone categories to a slower, blind-first review (the reviewer picks before seeing the model's answer). For high-confidence categories, drop the pretense of review: auto-accept them and audit a random sample instead.

5. **Track the right metric.** Use catch rate on audited or seeded items, not speed or approval rate. Give reviewers periodic feedback on what they missed. Keep reviewer-corrected labels separate from unverified approvals if they feed training.

6. **Validate with an A/B test.** Compare the new design against the current one on the same audited ground truth before rolling it out. Success means the change rate rises toward the true error rate and the post-review error rate falls.

I'd start with steps 1 and 2, since the first quantifies the problem and the second costs almost nothing.
