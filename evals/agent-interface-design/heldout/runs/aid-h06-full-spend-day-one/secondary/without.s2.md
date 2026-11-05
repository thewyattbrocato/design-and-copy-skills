You don't need to argue against what customers asked for. You can agree with it and disagree about sequencing. Customers want their ads to work without their time. That doesn't require the assistant to spend money unsupervised on day one, and the numbers make that case.

**1. The value of full control over approve-with-one-click is small; the tail risk is large.**
Ask what full autonomy buys the customer beyond "review and approve a recommendation in 30 seconds." Usually it's a few minutes a week. Now ask what one bad autonomous week costs a $2–5k/month shop: a bug, a bad conversion signal, or a bid strategy that overspends can burn a meaningful share of a month's budget before anyone notices. Small shops have thin margins and no buffer, so one such event can be existential for them. Your expected loss is roughly P(bad event) × size of loss, and for small accounts the loss side is large relative to their budget while the gain side is minutes.

**2. Small accounts are the worst place to learn optimization.**
Small shops have few conversions, so their performance data is noisy. An optimizer given budget control on a few dozen conversions will mostly fit noise: it will shift money toward whatever got lucky last week. Show him the confidence intervals on the account's conversion rate. If the interval is ±40%, the "optimal" decision is mostly random. Full control on that data is spending real money to chase variance.

**3. The optimizer's objective is probably not the customer's profit.**
Platforms and most internal models optimize for ROAS or conversions, not contribution margin after COGS, returns, and fees. An autonomous system that maximizes the wrong metric with full budget authority will confidently and efficiently lose money for the customer. Ask him which metric the assistant would optimize and whether it's tied to profit. If the answer is "ROAS," that's a concrete, numbers-based reason to gate spend changes.

**4. Churn math favors staging.**
A customer who gets one "the AI spent $800 on the wrong thing" story will leave and tell other shops. Customer acquisition for this segment is presumably expensive. Compare: LTV of a retained small-shop customer × churn probability increase from one bad autonomous incident, versus the upside from autonomy at the margin. Fill in your own numbers. Even rough ones usually settle it.

**5. Propose a staged path with exit criteria, not a no.**
- **Stage 0 (shadow):** The assistant recommends spend changes and logs what it would have done. Measure its decisions against what the human actually did and against outcomes.
- **Stage 1 (bounded autonomy):** It can act within hard guardrails: daily and monthly spend caps, max % change per day, no new campaigns, automatic rollback on anomaly. Cap losses by construction.
- **Stage 2 (expanded autonomy):** Unlock per account once it beats a holdout or human baseline on a pre-agreed metric over a set period.

This gives the CTO the thing he's looking for: a clear, measurable path to "full control," with the metric and threshold decided in advance. It also means you ship full autonomy as the destination, which answers the customer request directly.

**How to frame it for him:** "I'm not arguing against autonomy. I'm arguing we should be able to prove it beats the baseline before we let it spend a customer's money, and that the bounded version is the fastest way to get there." Then propose the metric and the pass/fail threshold, so the decision rests on numbers rather than opinion.

If you share rough data (typical monthly spend per account, conversions per account per month, and the margin profile), I can help you build the expected-loss comparison and a sample size calculation for the shadow-mode test. Those are the two numbers that will matter most in that conversation.
