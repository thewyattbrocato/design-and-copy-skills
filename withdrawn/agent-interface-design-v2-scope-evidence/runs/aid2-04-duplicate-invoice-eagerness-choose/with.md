**Recommendation: do B and C together, and rank by expected dollars at risk, not by likelihood alone. Don't do A as described.**

**Why not A.** A flat cutoff to 40 flags a day throws away 80 flags, and some of those are real duplicates, including large ones. The clerks are already doing this informally, except they pick the 80 at random through bulk-clearing. That is the worst version, because nobody knows which duplicates got through.

**Why capacity is the real constraint.** A review costs about 3 minutes, roughly $2–3 of clerk time. Almost any flag with a plausible chance of being a duplicate on a normal-sized invoice is worth reviewing. For example, a 2% chance on a $500 invoice is $10 of expected loss. So the problem isn't that there are too many low-value flags. There are 40 review slots and 120 candidates, and the slots need to go to the right ones.

**What to build**
1. **Score each flag by P(duplicate) × invoice amount.** A 30% chance on a $20,000 invoice should outrank a 90% chance on a $40 invoice.
2. **Auto-hold only the top tier**, where the probability is very high. A hold costs a late payment and a vendor call, and someone still has to release it. So holds count against the 40-a-day budget. Set the hold cutoff using past data: take several months of flagged invoices with known outcomes and check how often each score band was really a duplicate. Don't pick the cutoff by feel.
3. **Fill the rest of the 40 slots with the highest-ranked remaining flags**, sorted top to bottom.
4. **Don't leave the below-the-line flags unread and unlabeled.**
   - Let low-dollar ones pay and recover later through a periodic duplicate sweep of paid invoices.
   - Send a small random sample to the clerks. The sample's duplicate rate tells you what the cutoff is costing you.
5. **Consider adding capacity.** If the sample shows meaningful leakage, a third clerk for a few hours a day may pay for itself. The data will tell you.

**How to show it to the AP manager.** Don't show a raw threshold or score cutoff, because it means nothing to them. Show the setting as a trade-off they can read:

- **The control:** "Daily review capacity: 40" and "Auto-hold above: X% likelihood." Next to the hold control, show what it did yesterday: "7 held, $84k on hold."
- **A live preview of any change:** "At 60/day you'd review 20 more flags, about 1 hour of clerk time, and catch an estimated $X more in duplicates." "Raising the hold cutoff would release 3 invoices, $Y."
- **The below-the-line exposure:** "Not reviewed today: 80 flags, $Z total, estimated duplicate leakage $W (from sampling)." This is the number that justifies the setting, and it keeps the cost of the cutoff visible.
- **Outcome tracking, weekly:** duplicates caught, false holds, average hold-to-release time, and dollars recovered after payment.
- **A health check on the clerks:** the share of flags cleared in under N seconds, or cleared in batches. If bulk-clearing comes back, the setting is too high for the staff, and the dashboard should show that instead of hiding it.

I'd start with the historical backtest, since it sets both the hold cutoff and the below-the-line estimate. If you can share a sample of past flags with outcomes and amounts, I can help work out the bands.
