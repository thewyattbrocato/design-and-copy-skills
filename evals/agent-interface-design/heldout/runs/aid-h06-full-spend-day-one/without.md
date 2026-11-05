**Reframe it. You're not arguing against what customers asked for. You're arguing about how to deliver it.**

**1. Interviews measure what people say, not what they'll tolerate.**
"Handle everything" is cheap to say. It costs nothing in an interview, and it describes the outcome they want (no work, good results). It doesn't say they'd accept an unbounded, unreviewable bill. Ask any of them, "If it spent $800 in a day on the wrong campaign, would you still want that?" and you'll likely hear a different answer. Your CTO should treat the interview as a stated preference that needs validating, not as a spec.

**2. The payoff is asymmetric, and the numbers favor a cap.**
Run it as expected value:
- **Upside of full control on day one over a capped version:** a modest bump in convenience and maybe somewhat better optimization.
- **Downside of one bad incident:** for a shop spending $1–3k a month, one runaway day can wipe out a meaningful share of their budget. That means a churned customer, a refund or credit, a support burden, and a bad review or word-of-mouth hit. In a small-shop market, referrals are likely a major acquisition channel.

Your system doesn't have to fail often for this to matter. If a 1–2% incident rate costs you each affected customer plus their referrals, that can outweigh the convenience gain across the whole base. Plug in your real numbers (average spend, expected incident rate, CAC, LTV) and I expect the cap wins. If it doesn't, you've learned that too.

**3. Day one is when you know the least.**
You have no production data on how often the assistant makes bad spend decisions. Full autonomy means you find out at customers' expense. Guardrails turn unknown failures into bounded, observable ones.

**4. You can still ship "handles everything" as the product.**
Propose an autonomy ladder:
- Default: the assistant runs everything within a daily and monthly cap the customer sets. Alerts fire on anomalies.
- Big changes, like raising budgets or launching new channels, need one-tap approval.
- Customers who get a clean track record, or who opt in, get the cap raised or removed.

To the customer this still feels like "it just handles it." You also get data on approval rates, override rates, and cap hits. That data is the evidence for loosening the limits later.

**5. If he wants to test it, make it an experiment.**
Split new customers into capped and uncapped arms. Track 30/60/90-day retention, complaint and refund rates, spend variance versus budget, and NPS. Set a pre-agreed rule, such as "if uncapped doesn't beat capped on retention by X without raising incidents above Y, we ship capped." That gives a numbers person a decision rule instead of an opinion fight.

**One-line version for the meeting:** "Customers told us the outcome they want. Caps are how we deliver it without betting their money on a system with no track record. We can widen the caps as the data earns it."

Before the meeting, pull your actual spend distribution and any internal error rates from testing. Even rough numbers will carry more weight than the argument above.
