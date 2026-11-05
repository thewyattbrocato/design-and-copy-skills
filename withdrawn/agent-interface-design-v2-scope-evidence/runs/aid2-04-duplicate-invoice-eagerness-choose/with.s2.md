**Do B and C together, ranked by expected dollars rather than likelihood alone. Don't do A.**

**Why not A.** Raising the threshold throws away flags before anyone has checked whether they were duplicates. A flag costs about three minutes and a missed duplicate costs the whole invoice, so the agent should flag far more liberally than 40 a day. Your clerk capacity is the limit, not the right threshold. A also hides the problem: you'd never see the real duplicates that fell below the line.

**Why not B alone.** Sorting helps, but 120 flags against 40 reviews still leaves 80 unread, and those 80 are the ones that get cleared in bulk. That's fine only if the bottom of the list is nearly all false. You can't tell until you test it.

**Why C for the top tier.** A hold is reversible. If the top few flags a day are very likely duplicates, a clerk releasing a wrong hold costs a short payment delay. Paying a duplicate costs weeks of chasing. Hold only where the agent is very confident, and keep that tier small. Watch the cost of delay: early-pay discounts, vendors who escalate, and critical suppliers. Consider letting a hold expire into the review queue after a set time.

**Ranking.** Sort the queue by probability × invoice amount. A 60% match on a $14,000 invoice should come before a 90% match on $40.

**Before you commit, replay the last 60 to 90 days of invoices.** Check what share of true duplicates fall in the top 10, 40 and 120 flags a day by that ranking. If the top 40 holds nearly all the duplicates, then B plus a small C is clearly right. If duplicates are spread through the lower 80, you need more clerk time or cheaper checks, such as a one-click "same PO and amount" confirm. A bigger threshold won't fix that.

**How to show the setting to the AP manager.** Don't show a raw threshold or score cutoff. Show it as a budget with the consequences next to it.

1. **One control:** "Review capacity: 40 flags/day". Beside it, show what that setting buys, based on the replay: for example, "catches an estimated X% of duplicates by count and Y% by dollars. Unreviewed flags carry about $Z of exposure per week." Let the manager compare 20, 40, 80 and 120 on that same line.
2. **A separate control for auto-hold:** "Hold payment when confidence is at least N%". Show the expected holds per day, the share expected to be real duplicates, and the invoice dollars held at any time.
3. **A daily one-line status:** flagged, held, reviewed, cleared, left unread, and how many were cleared in under about 20 seconds each. That last number shows bulk-clearing as it happens.
4. **A feedback measure:** duplicates found after payment, by whether the agent had flagged them. If the agent flagged them and they were cleared, that points to review behavior. If it never flagged them, that points to the model.
5. **Show changes before they apply:** "Raising auto-hold from 95% to 85% would have held 9 more invoices last month, 6 of them real duplicates, and delayed $48K of payments."

Start conservatively with a small hold tier, review the numbers weekly for the first month, and let the manager widen it as the measured hold accuracy earns it.
