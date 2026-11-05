The 3% override rate doesn't tell you the model is accurate. The design makes it close to impossible to learn anything from that number.

**Why the 3% is unreliable**

- **Anchoring.** The model's answer is already selected, so the reviewer's job becomes "spot what's wrong" instead of "decide the category." People accept defaults far more often than they would choose the same answer independently.
- **The task is shallow.** The reviewer sees only two lines of claim text. Many miscategorizations can't be caught from that, so reviewers can't disagree even when they would want to.
- **Enter is the fastest path.** Approving takes one keystroke. Changing a category means opening a dropdown, picking a value and confirming. The cheapest action is always "agree."
- **"Approve all on this page" is a green button.** It styles bulk agreement as the normal path. Every row approved that way counts as a review, whether or not anyone read it.
- **The counter and target bar reward speed.** Throughput is the only thing measured, and nothing measures quality. Reviewers are pushed to approve fast, which pushes the override rate down regardless of model quality.
- **Nothing tests the reviewers.** There are no seeded known-wrong suggestions, no second reviewer on a sample, and no record of time spent per row. You can't tell a careful reviewer from a rubber-stamper.

**What the metric actually measures**

The 3% is the rate at which reviewers disagreed under conditions that discourage disagreement. It's an upper bound on how often they noticed an error. It isn't a lower bound on the model's accuracy. If reviewers catch only a third of the real errors, a true error rate of 9% would still show up as 3%.

Errors can also be concentrated in rare or costly categories, where the average hides them. And a rejected suggestion may show up only as a different dropdown value, with no record of why.

**What to change**

1. **Measure accuracy independently.** Draw a random sample, have two reviewers categorize it blind (no preselected value), and compare both to the model and to each other. Also seed known-wrong suggestions into the live queue to measure the catch rate.
2. **Instrument the queue.** Log time per row, bulk approvals versus individual ones, and override rate by reviewer, category, model confidence and time of day. A flat 0% from someone who spends 1 second per row is informative.
3. **Remove or demote "approve all."** At minimum, put it behind a confirmation and exclude it from the reviewed count. Better, drop it entirely and send high-confidence rows to a sampled audit path instead.
4. **Fix the incentives.** Replace "claims reviewed" with a quality-adjusted measure, such as seeded-error catch rate. Don't set the target on volume alone.
5. **Show more context.** Give reviewers the full claim text on demand, plus the model's confidence and its top alternatives. Make a rejection quick, and capture a reason code.
6. **Use confidence to route work.** Spend human time on low-confidence rows. Sample the high-confidence ones.

For management, I'd say this: the 3% is how often staff changed the model's answer. It says nothing yet about how often the model is right. A blind-labeled sample of a few hundred claims would answer that.
