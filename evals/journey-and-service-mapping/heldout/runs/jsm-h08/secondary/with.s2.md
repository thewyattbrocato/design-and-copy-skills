**Frame**
- **Person:** a dog owner on the monthly subscription, whose dog has to eat the food.
- **Slice:** from sign-up on the intro offer to the cancel-or-stay choice around month 4. Starts before the first box, ends when they cancel or pass month 4.
- **Decision:** which of the three marked moments to fix first to reduce churn at months 2 to 4.

**Status:** built from 31 cancellation survey answers and support tickets (ticket count `[to collect]`). Survey answers have no timing, so placing each reason in a phase is an assumption. Feelings are not measured.

| # | Phase (when) | Doing | Asking | Feeling | Touchpoint | What goes wrong | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | Sign up on intro offer (before box 1) | Pick plan, pay intro price | "What do I pay after the intro?" | Hopeful | Sign-up page | Post-intro price unclear `[to check]` | none |
| 2 | Try the first boxes (month 1) | Serve new recipe | "Will the dog eat it?" | Hopeful, then doubtful `[not measured]` | First box, welcome email | Dog refuses the recipe | **11 of 31** |
| 3 | Intro price ends (month 2, assumed) | Notice higher charge | "Why did it go up?" | Surprised `[not measured]` | Renewal charge | Price jump, no notice `[suspected]` | **9 of 31** |
| 4 | Food piles up (months 2 to 3) | Count bags in cupboard | "Why do I have so much?" | Annoyed `[not measured]` | Scheduled box arrives | Arrives faster than eaten | **6 of 31** |
| 5 | Try to skip a delivery (months 2 to 4) | Search account for skip | "Where is skip?" | Stuck | Account page | Skip hard to find, no status | Tickets `[to collect]` |
| 6 | Box comes on a day nobody is home (months 2 to 4) | Find box, or miss it | "Can I change the day?" | Frustrated | Delivery date, carrier | Day not visible or changeable `[to check]` | Tickets `[to collect]` |
| 7 | Keep or cancel (months 3 to 4) | Look for cancel or pause; answer survey | "Is it still worth it?" | Done with it | Cancel flow, exit survey | Pause not offered `[to check]` | 31 surveys; 5 "other" unplaced |

**Marked moments**
- **A. Phase 2, dog refuses the recipe.** Largest reason (11 of 31) and the earliest failure in the window.
- **B. Phase 3, intro price ends.** 9 of 31 cite price. Suspected cause: no notice before the charge changes. Check the renewal email.
- **C. Phase 5, skip search.** Tickets say people can't find skip, and there is no status while they look. Suspected link: a failed skip leads to stacked food (phase 4) and then cancellation (phase 7). Check: of people who cancelled, how many contacted support about skipping first?

**Next step: hypotheses**
1. For a dog owner at moment A, offering a recipe swap or smaller trial size should reduce recipe-cited cancellations. Measure: recipe-cited cancels per month, baseline `[to measure]`. Owner `[owner]`, by `[date]`.
2. For a dog owner at moment B, a notice before the price rises should reduce price-cited cancels and month-3 churn. Measure: price-cited cancels, baseline `[to measure]`. Owner `[owner]`, by `[date]`.
3. For a dog owner at moment C, putting skip on the account home and in each box email should reduce skip tickets and food-piling cancels. Measure: skip tickets and overstock-cited cancels, baseline `[to measure]`. Owner `[owner]`, by `[date]`.

Shelved: the wrong-day fix, until the ticket count is in. "Personalize the experience" is not tied to a moment, so it is out.

**Notes**
- Add "which month did you cancel?" to the exit survey so the phase placement can be checked.
- The survey and tickets don't show who skipped and stayed. Pull the skip-tickets count by subscriber status to see whether skipping helps retention or not.
