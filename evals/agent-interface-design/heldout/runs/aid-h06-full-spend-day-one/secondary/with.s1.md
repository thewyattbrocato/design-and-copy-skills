Your instinct is right, and you can make the case in his terms. "Handle everything" is a request for outcomes: the shop gets more customers for less money and doesn't have to babysit ads. Full spend control from day one is one way to deliver that, and it's the riskiest one. The numbers show why.

**1. The downside is asymmetric.** Small shops run thin budgets, so a bad day costs a large share of their monthly revenue. Say a shop spends $3,000/month on ads. One runaway bid setting, a bad audience, or broken conversion tracking that makes the model think a campaign is working could burn $1,000+ in a day. For a shop that nets maybe $10k/month, that's a 10% hit from one error, and the customer will blame the product, not the bug. The upside of the assistant being slightly better than the owner is a few percent. Small losses are tolerable, but a rare large loss can end the account.

**2. Churn is the real cost.** Each lost small-shop account is a recurring revenue stream plus a reference that either helps or hurts your sales. One incident that a customer finds out about after the fact will cost more in churn and refunds than the assistant saves in a quarter. Expected loss is probability times severity, and at small-shop scale, severity is high.

**3. You can't prove it works without a baseline.** A numbers person should object that day-one full control means no measurement. You won't know whether the assistant beat the shop's own manual performance, so you can't show ROI, and you can't tell if a bad week is noise or a bug. A staged rollout with a holdout group produces the evidence he'll want to see.

**4. Stated preferences are not revealed ones.** Interview answers say "do everything." Customers rarely mean "spend $5k without asking me." Test that directly. Your approval data will show what they actually accept.

**What to propose instead:** not "no autonomy," but autonomy that scales with evidence.

- **Hard guardrails from day one:** daily and per-campaign spend caps set by the owner, a maximum budget change per day (e.g., ±20%), auto-pause on anomalies (spend spike, conversion drop, tracking gap), and a one-click undo with a log.
- **Approval queue for big moves:** new campaigns, budget increases above a threshold, and new audiences need sign-off at first.
- **Graduation metrics:** each *class* of decision goes autonomous only after it clears a bar, such as:
  - Approval rate above ~90% for that class over several weeks (the owner keeps approving it, so stop asking).
  - Assistant CPA or ROAS beats a holdout or the shop's prior baseline.
  - Zero guardrail breaches, or breaches all caught and explained.

This gives him what he wants: autonomy is the end state, and it's gated by numbers he can read. The approval rate in particular tells you which decisions to automate, and it's a metric the CTO can track on a dashboard.

**Line you can use:** "Customers asked for it to handle everything. The question is what happens on the bad day, and a small shop might not survive that day. Let's ship full autonomy when the data shows it earns it, and make the path to that visible from day one."
