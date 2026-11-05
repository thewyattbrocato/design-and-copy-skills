**Do C and B together, with a cap on holds. Don't do A.**

**Why not A.** Cutting to 40 flags a day doesn't make the other 80 safer. Those invoices just get paid unreviewed. The clerks already skip them in practice, so A only makes that official. A flag is worth a clerk's three minutes whenever (probability of duplicate × invoice amount) is more than roughly $1.50 of clerk time. On a $2,000 invoice that's a probability of about 0.1%. Most of your 120 flags clear that bar, so the problem is limited review capacity, not too many flags.

**What to build**
1. **Rank by expected loss, not by probability alone.** Sort by P(duplicate) × invoice amount. A 30% chance on a $12,000 invoice should come before a 90% chance on a $40 one.
2. **Hold payment only on the top tier.** Choose the cutoff so holds stay well under the 40-a-day review capacity. A hold still needs a clerk to release it, so it uses the same capacity. Holds are only cheap when nearly all of them are real duplicates. A wrong hold costs a late payment, a possible lost early-pay discount, and an annoyed vendor.
3. **Flag the next tier, ranked,** so the clerks work from the top down until their time runs out.
4. **Handle the unreviewed tail deliberately.** Let low-value, low-probability flags pay, and add a weekly post-payment sweep or sample audit. That catches duplicates later, and the recovery cost is bounded by the small amounts involved.
5. **Calibrate first.** Backtest the agent's scores against past confirmed duplicates. Ranking and holding only work if "80%" really means about 80%.

Also check whether the capacity limit is firm. 120 flags × 3 minutes is about 6 clerk-hours a day. If catching duplicates is worth that, adding a few hours of help may be the cheapest fix.

**How to show it to the AP manager**

Don't show a raw threshold like "0.72". Show the tradeoff in units the manager cares about:
- **One main control** with a readout that updates as it moves: *"Holds: 12/day · Flagged for review: 28/day · Paid unreviewed: 80/day."* Mark the 40-a-day capacity line on it.
- **A curve of cumulative expected duplicate dollars against flags reviewed per day.** It shows where more review stops paying off, and what the unreviewed tail is expected to cost, for example *"Unreviewed tail: about $X/month at risk."*
- **Hold impact:** the number of invoices held, the dollar value held, and the average delay.
- **Health metrics by tier,** all tracked over time:
  - confirmed-duplicate rate
  - median seconds per flag
  - backlog
  - duplicates found after payment

  A median time per flag that drops toward zero is the sign of bulk clearing, and the manager should see it before it becomes a problem again.

Frame the setting as "how many invoices we hold or review per day, and how much exposure we accept on the rest." That is the decision the manager is making, so the setting should read that way.
