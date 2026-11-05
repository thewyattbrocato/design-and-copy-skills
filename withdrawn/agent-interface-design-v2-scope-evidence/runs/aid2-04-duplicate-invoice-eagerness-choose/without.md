**Recommendation: do C, with B's ranking inside it.** Rank by expected loss (duplicate probability × invoice amount), not probability alone. Don't do A.

**Why not A.** A threshold set by clerk capacity ignores your costs. A missed duplicate costs the full invoice amount, and a false flag costs about 3 minutes of clerk time. At those prices, an invoice is worth flagging whenever the duplicate probability is above roughly (clerk cost ÷ invoice amount). For a $2,000 invoice that's a fraction of a percent. Cutting from 120 to 40 flags throws away flags that are worth far more than they cost. It also doesn't fix the real problem. The clerks have run out of time, and the cure isn't to flag less.

**Why not B alone.** Ranking helps the clerks spend their 40 reviews on the best candidates. But the other 80 flags still go unread, and if a flag doesn't stop payment, those invoices get paid anyway. B improves the order of review but doesn't change what happens to the unreviewed flags.

**Why C.** Holding payment is cheap compared with paying a duplicate. A short delay costs you vendor friction and the occasional missed early-pay discount, and a paid duplicate costs weeks of chasing. So the agent should act on its own for the clearest cases instead of relying on a human who has no time.

**How to set it up**
- **Hold tier.** Hold invoices at the top of the expected-loss ranking, and size the tier to fit the clerks. Held invoices must be reviewed to be released, so a hold tier of about 20–25 a day leaves room for the rest.
- **Flag tier.** Everything else goes into a queue sorted by expected loss. Clerks work from the top, and the low-dollar, low-probability tail can stay unreviewed on purpose.
- **Tail check.** Have the clerks spot-check a small random sample of the tail each week. That tells you whether the ranking is working and whether duplicates are slipping through.
- **Bulk-clear rate.** Track it as a health metric. If clerks are clearing items in bulk, the queue is too big.

**How to show the setting to the AP manager.** Don't show a raw score threshold, because it means nothing to them. Show the tradeoff in their own terms:

1. **One control:** "Hold the top N invoices per day." N is the single setting, with a marker for clerk capacity.
2. **For each value of N, a small table or curve showing:**
   - invoices held per day and flagged per day
   - clerk hours needed against the hours available (40 reviews ≈ 2 hours)
   - estimated duplicate dollars paid unreviewed per week
   - estimated dollars delayed on legitimate invoices per week
3. **The default,** set where the review workload just fits the clerks, with the cost of moving up or down in plain dollars. For example: "Raising N by 10 adds 30 clerk-minutes a day and cuts expected unreviewed duplicate exposure by about $X a week."
4. **Live health numbers:** the share of held items that turned out to be real duplicates, the same figure for the flagged band, and the bulk-clear rate.

All the dollar estimates need calibrating against your history of confirmed duplicates and clerk outcomes. I haven't seen those numbers, so treat the 20–25 hold figure as a starting point. Replay the last few months of invoices to pick N before you go live.
