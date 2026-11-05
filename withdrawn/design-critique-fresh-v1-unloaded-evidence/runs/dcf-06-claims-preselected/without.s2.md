**Yes, there's a problem, and it's probably serious.** The review step looks like a human check but works mostly as a rubber stamp.

## What the numbers say

- The model is wrong on 9% of 4,000 claims, which is about **360 claims a week**.
- Reviewers change the category on 2%, which is about **80 a week**.
- So reviewers catch **at most 22%** of the model's errors, and that assumes every change was a correct fix.
- At least **280 wrong categories a week (~7% of all claims)** get saved with a human "approval" on them. If some of the 80 changes were wrong, or reviewers changed correct picks, it's worse.

The audit measured the model's pick, not the saved label. Last quarter's final error rate was therefore probably around 7% or higher. Please confirm that with the audit data.

## Why it happens

The design pushes reviewers toward accepting:

- The answer is **pre-selected**, so doing nothing means approving.
- **"Next claim" saves** whatever is selected, so approval and not looking are the same click.
- There is **no rationale**, so a reviewer has to re-do the classification to disagree. That's slow, and agreeing is cheap.
- At 4,000 claims a week, there's pressure to move fast. This is classic automation bias.
- Nothing records whether a reviewer actually confirmed a claim, so the logs can't tell you who checked.

## How bad is it?

The data doesn't show the cost of a wrong category. That depends on what it drives: routing, payout, denial, or fraud flags. If categories affect payment or regulatory handling, ~280 weekly errors are a real exposure. There's also an organizational risk, because the process is documented as human-reviewed when it mostly isn't.

One caveat is that a 2% change rate doesn't prove reviewers aren't looking. The errors may be hard to spot from the claim text alone. The first step below separates those two explanations.

## What I'd do

**1. Measure (about 1–2 weeks, no UI change)**
- Look at time-on-claim distributions. Many claims saved in a few seconds suggests no real review.
- Break down change rate by category and model confidence, and see where the audit's 9% errors concentrate.
- Seed known-answer claims, including some with deliberately wrong suggestions, to get the true catch rate per reviewer.

**2. Fix the interaction**
- **Don't pre-select** when confidence is low or the category is high-stakes. Show the suggestion beside an empty dropdown, or show the top 2–3 candidates.
- Replace "Next claim" with an explicit **"Confirm category"** action. Changing a category should be no harder than confirming one. Log confirm and change separately.
- Show **why**: highlight the claim text spans that drove the prediction, and show confidence. Test this before rolling it out, because a wrong explanation can increase trust in a wrong answer.

**3. Spend reviewer time where it matters**
- Route low-confidence and high-stakes claims to full review.
- For high-confidence claims, use sampled review rather than 100% nominal review. This is more honest and frees capacity.

**4. Keep monitoring**
- Keep a steady trickle of seeded gold claims in the queue and track catch rate over time.
- The headline metric is the **final saved-label error rate** from audits, not the model's accuracy. A reasonable target is a catch rate well above 22%, but I'd set it after the measurement step.
- Stop treating rubber-stamped labels as ground truth. If the labels feed retraining, they're contaminated with the model's own errors.

If you share the review logs or the audit export, I can run the breakdowns in step 1.
