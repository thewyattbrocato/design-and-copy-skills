Lead with the difference between what customers asked for and how you deliver it. Customers want less work and good results. "Full control of spend from day one" is one way to get there, and it's the riskiest one. You can give the CTO the outcome he wants and still stage the autonomy.

**The numbers argument**

1. **The losses are asymmetric.** A small shop's monthly budget is often a few thousand dollars. One bad autonomous day (a bid multiplier bug, a budget set to the wrong currency or period, a runaway campaign, a misread conversion signal) can burn a large share of it. Nobody at a small shop has the margin to absorb that, and they will remember who did it.

2. **You don't know your error rate yet.** Right now the model's spend decisions have no track record on your customers' accounts. Giving it full control means accepting an unmeasured error rate on real money. A numbers person should object to that before anything else.

3. **The upside of skipping approval is small early on.** Approval mode with one-tap "approve all" still saves most of the time customers care about. Full autonomy adds a little more convenience and a lot more tail risk. Compare the expected value of each and the early gain from full autonomy is thin.

4. **Churn is the real cost.** For a small-shop customer, one wasted $800 week can end the relationship. Losing a customer costs more than the spend you were trying to optimize.

**What to propose instead**

Ship with graduated autonomy, and make the graduation rules numeric:

- **Stage 1 (launch):** The assistant recommends, the customer approves. Log every recommendation, approval, rejection, and the outcome.
- **Stage 2:** Auto-apply only low-impact changes, such as ±10–20% budget shifts within a daily cap. Anything bigger still needs approval.
- **Stage 3:** Expand autonomy per account, once that account's recommendations have beaten a baseline (for example, ROAS or CPA versus the customer's own pre-assistant performance) over a set window, with no guardrail breaches.

Non-negotiable guardrails from day one, whatever the stage: hard daily and per-campaign spend caps, a max change per day, a one-click kill switch, and a full audit log of every automated action.

**A line for the CTO**

"The customers asked for the assistant to handle everything. They didn't ask us to remove the approval step on day one. If we give it full spend control before we've measured how it performs on their accounts, the first bad week will cost us the customer, and we won't have the data to show what went wrong. Let's launch with recommend-and-approve, log everything, and give it more control per account as it beats a baseline. That gets them the outcome they want, and it gives us the evidence to back up the autonomy."

If you can pull even rough numbers (the average monthly budget of your target customers, and how often your current tool's recommendations are wrong or get reversed), put them in the message. A numbers person will weigh those more than any argument about principle.
