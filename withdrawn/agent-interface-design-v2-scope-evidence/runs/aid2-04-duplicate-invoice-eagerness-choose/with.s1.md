**Recommendation: B as the base, with a narrow version of C on top. Don't do A.**

**Why**

- **A is the worst option.** It makes the same cut as B, but by a blunt threshold. The 80 flags it drops are never seen, and some are real duplicates. Raising the threshold also ignores invoice size, even though that is what a miss costs.
- **B is better than A at the same workload.** Clerks read the 40 flags most worth reading instead of a random 40 of 120. Rank by expected loss (likelihood of duplicate × invoice amount), not likelihood alone. A 60%-likely duplicate on a $9,000 invoice should outrank a 90%-likely one on $40.
- **B alone leaves a gap.** The agent still flags 80 a day that nobody reads, and those get paid by default. You'd then be relying on clerks to notice the worst flags, which is the habit that already broke.
- **C fixes that gap, but only for the top tier.** Paying is the step you can't easily undo, while a hold can be released. So hold automatically when the agent is very confident and the amount is large. Keep the hold tier small and capped. A wrong hold costs a late payment and a vendor call, which is more than three minutes. Set the cutoff by testing, not by guessing.
- **Break-even:** a flag is worth a clerk's time when likelihood × amount is above roughly the cost of three minutes of review. That is a dollar-weighted rule, so small invoices can pass unflagged while large ones get flagged at lower likelihoods.

**Queue rules**

- Sort by expected loss, with ties broken by payment due date.
- Anything that reaches its due date unreviewed should surface at the top the day before. It should not silently pay.
- Clerks get "not a duplicate, this time" and "never flag this vendor/pattern," and the second shows the rule it creates.

**What the AP manager sees**

Show the setting as an outcome, not a sensitivity slider.

1. **One-line statement of the rule.** For example: "Invoices most likely to be duplicates, weighted by amount, are held automatically (up to N a day and $X total). The next 40 a day go to the review queue, best first. The rest pay normally."
2. **Three counts with dollar totals:** held, queued for review, and paid without review. Show the dollar value of the third group, since that is the exposure. Back-test this on your last few weeks of invoices and label it as a replay. Don't show accuracy figures you haven't measured.
3. **Edge cases around each cutoff.** Show a few invoices just above and just below it, so the manager sees what changes if they move the line.
4. **Caps on the hold tier.** A maximum number held per day and a maximum dollar value held. State them on the same screen as the setting.
5. **A status view with:**
   - queue size against the 40-a-day capacity
   - oldest unreviewed flag
   - held count and value
   - the nearest due date among unreviewed items
   - a pause control one step away
6. **A warning before the queue overflows.** Alert when the queue is trending past what two clerks can clear before due dates, and say what the agent is doing about it. Don't wait until flags are already going unread.
7. **Skipped and rejected list.** Show the invoices the agent passed with the closest-to-flagged first. Misses are invisible otherwise.
8. **Rubber-stamping signal.** If clerks are clearing flags in bulk, show that as a concern notice. It means the queue is too noisy, and the fix is to adjust the ranking or the cutoff.

**Rollout:** run the hold tier in dry-run first, listing what it would have held for a couple of weeks, before it touches payments.
