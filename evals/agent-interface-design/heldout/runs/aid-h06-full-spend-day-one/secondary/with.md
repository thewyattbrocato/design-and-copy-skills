Lead with the data problem, not the values argument. A numbers person will accept "we can't measure this well enough yet," and that is the real reason to stage the rollout.

**1. Small shops don't generate enough conversions for autonomous optimization to be reliable.**
A shop with 30 conversions a month has a CPA estimate with a 95% interval of roughly ±35–45%. The system would be making spend decisions on noise: it would cut campaigns that were fine and scale ones that got lucky. Your CTO can check this with a Poisson calculation. The fix is to earn autonomy by showing the system is accurate, which takes data you don't have yet on most accounts.

**2. The loss is asymmetric for the customer.**
Take an illustrative shop with a $1,500/month budget. A bad bid multiplier or a runaway campaign that runs at 10× for three days before anyone notices spends the entire month's budget. For a big advertiser that's a rounding error. For a small shop it's the business's ad line for the month, and they will blame you, not the algorithm. Expected loss = probability of failure × size of loss as a share of their budget, and the second term is far larger for your customers.

**3. "Full control from day one" removes your ability to measure.**
With no holdout group, you can't tell whether the assistant beats doing nothing. Without a reversible, bounded mode, you can't tell whether a bad outcome came from the model or from the market. You won't have the data to justify expanding autonomy later.

**4. Customers asked for less work, not zero oversight.**
"Handle everything" describes an outcome: they want to stop managing ads. You can deliver that outcome with bounded authority. Ask the interviewees directly: "What would have to be true for you to let it spend without checking?" Their answers will likely be specific caps, alerts, and a track record. That's a spec.

**A staged plan he can sign off on:**

- **Phase 1 (recommendations):** The assistant proposes changes with predicted impact. The customer approves with one tap. You log accepted vs. rejected recommendations and predicted vs. realized results.
- **Phase 2 (bounded autonomy):** The assistant executes only within hard limits: daily spend cap, maximum % change per day, no new campaigns, automatic pause on anomalies (for example, spend more than 1.5× the trailing average), and one-click undo. Run it against a holdout group of accounts so you can compare it with manual management.
- **Phase 3 (expansion):** Widen limits per account only when that account's holdout data shows the assistant beats manual management, with a predefined threshold.

**Gate metrics he can track:** realized vs. predicted ROAS on the holdout, overspend incidents per 1,000 account-days, recommendation acceptance rate, and refund/churn tied to spend events.

**The one-line version for him:** "We're not saying no to autonomy. We're saying we can't yet prove the model beats a human on a $1,500 budget with 30 conversions a month, and if it's wrong, our customers lose their month. Phase 2 gets us to full autonomy with the data to back it up, and Phase 1 gets us the data."
