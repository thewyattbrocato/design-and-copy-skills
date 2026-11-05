**Do C, built on B's ranking. Don't do A.**

**Why not A.** Missing a duplicate costs the full invoice amount and weeks of chasing. A false flag costs about three minutes. With that gap, you should accept many false flags before accepting a missed duplicate. Cutting to 40 flags a day does fix the queue, but it does so by discarding the tail of the ranking. Some of those discarded invoices will be large and fairly likely duplicates. A flat threshold also treats a $60 invoice and a $60,000 invoice the same, which makes no sense when the loss is the invoice amount.

**Why not B alone.** Sorting only helps if clerks work from the top and stop. Today they clear in bulk, so the tail is rubber-stamped, and B does nothing to stop the highest-risk invoices from being paid if someone clears them carelessly. Also, 120 flags against a capacity of 40 means about 80 a day go unreviewed, so the backlog grows.

**What I'd build:**
1. **Rank by expected loss, not probability.** Use P(duplicate) × invoice amount, compared with the roughly $2–3 cost of a clerk's three minutes. A 5% chance on a $20,000 invoice outranks a 60% chance on a $40 one.
2. **Hold payment on the top slice, sized to clerk capacity (about 40 a day).** Holding is reversible and costs only a short payment delay. Paying a duplicate costs weeks of chasing. The hold count must not exceed what the clerks can actually review. Otherwise held invoices sit and vendors get paid late.
3. **Handle the other ~80 differently from the held ones.** Don't put them in the same queue. Keep them in a visible, lower-priority list that clerks work only if they have time. Auto-release the ones whose expected loss is below review cost. Audit a small random sample of the released ones each week so you can measure what you're missing.
4. **Check the cutoff against history.** Backtest on past invoices with known outcomes before going live. I don't have your data, so the 40-a-day split and the catch rate are estimates until you do.

**How to show the setting to the AP manager.** Don't show a raw "threshold = 0.7" slider. Show the tradeoff it produces:

- **One control:** "Hold invoices with expected loss above $X". Set the default so held invoices per day equals clerk capacity.
- **A live preview next to it**, from the backtest:
  - Held per day, against the 40-a-day capacity line (highlight it if it's exceeded).
  - Estimated duplicates caught and missed per week, and the dollars at risk in the missed ones.
  - Clerk hours per day.
  - Average payment delay on held invoices.
- **The two costs as editable inputs:** minutes per review and clerk hourly cost. Duplicate cost is the invoice amount. The manager can then see why the cutoff sits where it does.
- **Health metrics on the same screen:**
  - Share of flags cleared in under N seconds. This is your bulk-clearing signal.
  - Confirmed-duplicate rate in the held set.
  - Age of the oldest unreviewed item.
  - Findings from the weekly sample audit.

The bulk-clearing rate is the one to watch. If it climbs, the cutoff is too loose or the queue is too long, and the manager should see that before a duplicate payment shows it.
