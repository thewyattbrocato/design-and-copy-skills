Don't argue that customers are wrong. Argue that "handle everything" describes the outcome they want, and spend authority is a separate decision. Interviews tell you what they want. They don't tell you what happens when the assistant spends $400 they didn't expect.

**The case in numbers-person terms**

1. **The payoff is lopsided.** Full control from day one gains you some extra efficiency per customer. The downside is money spent that can't be recalled, and for a small shop ad budget is often real cash, not a rounding error. A customer with a bad surprise churns and tells other shop owners. Even if bad events are rare, a bounded gain against an unbounded, irreversible loss is a bad bet.

2. **Losses are correlated.** A bug, a bad model update, or an ad-platform API change hits every customer at once. You wouldn't see independent small failures. You'd see one big simultaneous one.

3. **You have no measured error rate yet.** Setting autonomy on day one means picking a number with zero data behind it. Shipping with limits is how you get the data. Track how often customers approve the assistant's proposed changes unchanged. That approval rate is the evidence for removing the gate.

4. **The two mistakes cost different amounts.** If you start constrained and it turns out to be unnecessary, you lose a little convenience, and you can widen the limits later with one release. If you start unconstrained and it turns out to be wrong, you lose trust, and that's slow and expensive to rebuild.

**What to propose instead**

This keeps his promise of "it handles everything" and adds a ceiling:

- **Day one:** The assistant acts on its own inside a spend cap the customer sets (daily and monthly). Anything above the cap, or any large change to what it's spending on, becomes a draft they approve. Both thresholds are starting values to tune.
- **Visibility:** One status view shows what it's doing, what it spent, and what's coming up. Pause is one tap away. Changes can be reversed where the ad platform allows it.
- **Widening:** After a stretch of clean results the customer can see, the assistant offers to raise its own limits, and the customer accepts or declines. It never widens silently.
- **Pitch to customers:** "It handles everything, and you set the most it can spend."

**Concede one point to him.** If approvals are frequent and annoying, the product stops feeling like it handles everything. So the design goal is to make approvals rare by choosing a sensible cap. It is not to remove the cap. If the approval-rate data later shows customers approve nearly everything, he'll have his evidence and you can lift the gate.

**The question to put to him:** "What's our plan if it overspends for one customer in week one, and what does that cost us compared with the convenience we'd gain by skipping the cap?" If he has no number for that, the cap is the cheaper way to find out.
