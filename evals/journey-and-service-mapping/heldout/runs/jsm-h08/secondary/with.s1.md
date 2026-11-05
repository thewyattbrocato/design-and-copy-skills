**Frame**
- **Person:** a dog owner on the monthly plan, signed up for the intro discount.
- **Slice:** starts at sign-up, ends at cancellation. Covers months 0 to 4, where churn clusters.
- **Decision:** which of the three problems to fix first, and where the next sprint goes.

**Status:** Built from 31 cancellation survey answers and the two support-ticket themes. Ticket counts are not known (`[to measure]`). Feelings are inferred from survey wording, not measured. Nothing here is backstage, so internal causes are unmapped.

**The map**

| | 1. Sign up on intro offer | 2. Try the first boxes | 3. Full price starts | 4. Food piles up, box lands wrong | 5. Look for a skip or pause | 6. Cancel |
|---|---|---|---|---|---|---|
| **Doing** | Picks plan at intro price | Serves new recipe, watches dog | Sees first full-price charge | Stacks boxes; box arrives when no one is home | Searches account for skip | Submits cancellation |
| **Asking** | "Is this worth trying?" | "Will the dog eat it?" | "Is this still worth the money?" | "Can I pause these?" | "How do I skip a delivery?" | "Why am I leaving?" |
| **Feels** (inferred) | hopeful | uncertain | doubtful | annoyed | frustrated | decided |
| **Touchpoint** | Sign-up page, intro offer | First box, recipe | First full-price charge | Delivery schedule, carrier drop-off | Account page | Cancel flow with reason |
| **Goes wrong** | Full price not shown (`[to check]`) | Dog refuses recipe: **11 of 31** reasons | Price step-up: **9 of 31** reasons | Too much food: **6 of 31**; wrong-day drops (ticket theme) | Skip hard to find (ticket theme) | Cancel offers no pause (`[to check]`) |

**Marked moments**
- **Phase 2, recipe refusal.** The largest cancel reason, and no known path (swap, smaller pack, skip) at the moment the dog refuses food.
- **Phase 3, first full-price charge.** Second-largest reason, arriving right when the customer has no warning. This is the most likely point of month-2 loss.

Phases 4 and 5 are ticket-sized friction, not moments. They are fixed with small changes, not a redesign.

**Opportunities, each on a moment**
- Phase 2: offer a recipe swap or a half-size trial at the first refusal signal.
- Phase 3: show the full price at sign-up and send notice before the first full charge.
- Phase 4: add an "I'm away" hold and let customers pick delivery day.
- Phase 5: move skip and pause onto the delivery screen, not under settings.

**Hypotheses for the next conversation** (owners and dates to be set)
1. For a dog owner at recipe refusal (phase 2), a swap offer should cut recipe-reason cancels. Measure: share of cancels citing the recipe. Baseline: 11 of 31. Owner: `[owner]`. Date: `[date]`.
2. For a subscriber at the first full charge (phase 3), showing the full price at sign-up should cut price-reason cancels. Measure: share citing price. Baseline: 9 of 31. Owner: `[owner]`. Date: `[date]`.
3. For a subscriber looking for skip (phase 5), moving skip to the delivery screen should cut "how do I skip" tickets. Baseline: `[to measure]`. Owner: `[owner]`. Date: `[date]`.

**Notes**
- Shelved: "personalize the experience". It attaches to no moment.
- To collect before trusting the map: cancel month for each survey answer, ticket counts per theme, and conversion at each phase boundary. Those will show whether phase 3 really is where month-2 loss happens.
