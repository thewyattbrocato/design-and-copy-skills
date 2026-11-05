**Framing**
- **Person:** a new subscriber whose dog eats the box, months 1 to 4.
- **Slice:** from the first box arriving to the cancel click. Starts at signup, ends at cancel or the month-4 renewal.
- **Decision:** which of the three churn causes to fix first, and where in the journey.
- **Status:** assumption draft built from 31 cancellation survey answers and support-ticket themes. Ticket counts were not provided, so ticket-based cells are unquantified. Feelings are inferred, not measured.

**Churn reasons (from the 31 survey answers)**

| Reason | Count | Share |
|---|---|---|
| Dog wouldn't eat new recipe | 11 | 35% |
| Price after intro discount ended | 9 | 29% |
| Too much food piling up | 6 | 19% |
| Other | 5 | 16% |

These are single-count answers. I'm assuming one reason per respondent, which needs confirming.

**Journey map**

| | 1. Sign up, get first box | 2. Switch dog to new recipe | 3. Food builds up, box lands on wrong day | 4. Look for how to skip | 5. Full price hits | 6. Cancel |
|---|---|---|---|---|---|---|
| **Does** | Picks plan and delivery day, starts intro discount | Mixes new food into old, watches dog eat | Stores extra bags, misses delivery | Searches account for "skip" | Sees first full-price charge | Finds cancel, leaves survey |
| **Asks / thinks** | "Will my dog like this?" | "Is it supposed to be this hard?" | "Why do I have so much food?" | "How do I skip without cancelling?" | "Is this worth it now?" | "I'll just stop." |
| **Feels** (inferred) | Hopeful | Uncertain | Overwhelmed | Frustrated | Surprised | Resigned |
| **Touches org** | Signup, delivery-day picker | First box, any feeding guide | Delivery email, carrier drop-off | Account page (skip not findable) | Renewal charge, notice email | Cancel flow, survey |
| **Goes wrong** | Delivery day set without a way to see or change it later | Dog refuses; no transition path seen | Quantity exceeds need; box lands when no one is home | Skip is hard to find, so people give up | Price change not expected | Exit happens here, but the cause started earlier |
| **Survey / ticket link** | Ticket: "box came on a day I'm not home" | Survey: recipe refusal, 11 | Survey: oversupply, 6; ticket: wrong-day delivery | Ticket: "how do I skip?" | Survey: price, 9 | Survey: other, 5 |

**Marked moments** (suspected, to be confirmed)
1. **Phase 2, switching the dog to the new recipe.** This is the largest cause (11 of 31), and the refusal happens in months 1 to 2 while the cancel lands in months 2 to 4. The failure starts early and shows late. Check: days from first box to first refusal versus cancel date.
2. **Phase 4, first skip attempt.** This is where "too much food" turns into a cancel, because the only visible option is cancelling. Check: skip-ticket volume by cohort month.
3. **Phase 5, intro discount ends.** Nine people left at the price change. Check: whether a notice went out before the first full charge and how many cancels follow within 7 days of it.

**Backstage gap (ticket themes only)**
Delivery day is set at signup, and changes to it appear to go through the same hidden path as skips. Oversupply and wrong-day delivery both trace back to that. Confirm how delivery scheduling works before changing anything.

**Next step: three hypotheses**
1. For subscribers making a first skip attempt (months 2 to 3), a visible "skip next box" action in the account and the delivery email should cut skip-related tickets and cancels. Measure: skip tickets and cancel rate for the cohort. Baseline: [to measure]. Owner: [owner]. Date: [date].
2. For subscribers 14 days before the intro discount ends, a notice with the full price and a skip/pause option should reduce price-driven cancels. Measure: cancel rate in the 7 days after first full charge. Baseline: [to measure]. Owner: [owner]. Date: [date].
3. For dogs refusing the new recipe in the first two boxes, a gradual transition plan or a swap to the old recipe should reduce taste-driven cancels. Measure: taste-reason cancels for the cohort. Baseline: [to measure]. Owner: [owner]. Date: [date].

Shelved for now: a general "improve onboarding" effort, since it has no marked moment behind it.

**Before building the map further**
Pull three dates per cancelled customer (first box, first skip attempt, cancel), plus the ticket count by theme. That would turn the suspected moments into measured drop-off points.
