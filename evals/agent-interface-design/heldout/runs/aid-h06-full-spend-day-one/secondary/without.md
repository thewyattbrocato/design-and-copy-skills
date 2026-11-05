Don't argue that autonomy is wrong. Argue that full spend control on day one is a risk the numbers don't support yet. Customers asked for less work, and they didn't ask to hand over their card without limits. Here's how I'd make that case to a numbers person.

**1. The losses are asymmetric, and small shops feel them most.** Suppose the agent is right 90% of the time. The 10% of bad decisions (a bid runaway, broken conversion tracking, a budget pushed into a dead campaign, a learning-phase reset) can cost a small shop its whole monthly budget in a day. Their cash buffer is small, so one bad week can end the relationship even if the average month looks great. Expected value looks fine, but ruin probability is what matters for a $3k/month advertiser.

**2. Trust is the retention metric, and it breaks fast.** Ask him what a single $2,000 overspend does to churn for a customer paying you a few hundred a month. One blowout costs far more than the spend it wasted. Autonomy the customer hasn't yet seen working is a liability, not a feature.

**3. You don't have the data to justify full autonomy yet.** You don't know your recommendation acceptance rate, your override rate, or how often a proposed change would have hurt. Shipping full control means betting on numbers you haven't measured. Put it in his language: "We're buying the right to be autonomous with evidence, not assuming it."

**4. Propose a staged rollout with graduation criteria.**
- **Shadow mode:** the agent logs what it would have done, and you compare it to what the human did.
- **Approve-to-act:** the agent proposes, and the customer approves with one click.
- **Bounded autonomy:** the agent acts inside caps the customer sets, such as a daily spend ceiling, a per-campaign cap, a maximum percentage change per day, and an anomaly pause.
- **Full autonomy:** a customer graduates when their approval rate and outcome metrics clear a threshold you agree on in advance.

This is an experiment with a control and a success criterion, which is how a numbers person likes to see product decisions made.

**5. Reframe "what they asked for."** Interviews capture what people want to be true, not how they'd act after a bad day. "Handle everything" means "stop making me do this," and bounded autonomy with hard caps delivers that. Full control with no caps delivers the outcome they fear most.

**A line you could use:** "We're not saying the agent shouldn't have control. We're saying no customer should give it control of money before we can show it's right, and the first customer it hurts is the one we lose. Let's ship with hard caps by default, measure acceptance and outcomes for 60 days, and widen autonomy per customer as the data supports it."

Before the meeting, pull whatever pilot or shadow-mode data you have. Even a rough acceptance rate or a count of "would have been a bad change" cases will carry more weight than any argument.
