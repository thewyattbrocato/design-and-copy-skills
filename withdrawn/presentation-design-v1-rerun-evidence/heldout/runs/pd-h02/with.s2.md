Your team is right. The content is solid, but the deck reads like a document: a label title on every slide, a lot of bullets, and the same weight on everything. I'd cut it from 8 slides to 5 content slides.

I assumed about 15 minutes, a live room, and that the goal is for the product group to leave trusting Harbor's numbers and knowing what's next. You didn't say what you want from them. If you want something, such as input on the monthly release cadence, make that the closing ask.

**Takeaway:** Harbor shipped faster and with fewer defects in Q3. One rewrite caused an outage, and Q4 closes the gaps that exposed.

**What to change**
1. **Delete the Overview and Thank You slides.** Say the takeaway out loud in your first 30 seconds, then go straight to the numbers. End on the Q4 slide and leave it up during questions.
2. **Rewrite the titles as claims.** If someone reads only the titles, they should get the argument.
3. **Keep about 30 words per slide, with one visual.** The people at the back of the room need big text, so use 32 px or larger. Anything you'll just say out loud goes in the appendix.
4. **Group the lists.** Seven features, six sprints and six Q4 items are too many to read at once.

**Proposed deck**

| # | Title (the claim) | On screen |
|---|---|---|
| 1 | Harbor delivered more, and more reliably, in Q3 | Two big numbers: **41.8** points per sprint (was 36.5) and **84%** commitment accuracy (was 71%). Optionally a small bar chart of the six sprints with Sprint 17 labeled "2 engineers out, holiday". Say the carry-over drop (9 to 4) out loud. |
| 2 | We shipped seven features, mostly for dispatchers | Four groups: **Dispatcher workflow** (driver-assignment modal, bulk edit, saved filters, dark mode), **Data** (CSV export to 50k rows), **Access** (subcontractor roles), **Platform** (notification rewrite) |
| 3 | Fewer bugs escaped, and fixes got 44% faster | **31 → 17** escaped defects. **6.2 → 3.5 days** median P2 fix. Coverage and the flaky-suite swap go in the appendix. |
| 4 | The notification rewrite caused a 3-hour outage on Aug 29 | **3 h 10 min**, **1,140** delayed driver alerts. One line on the cause (prefetch limit set too low). One line on the fix (same day, plus a queue-depth alert). |
| 5 | Q4: close the gaps, then build on them | Three groups: **Harden** (CSV export test, queue load test), **Build** (subcontractor permissions phase 2, route-optimization spike), **Grow** (hire a senior engineer, tech debt). Add your ask here if you have one. |

Two things come out of this:
- **Slide 4 is a gap in your plan.** The incident slide promises to load test the queue before any future change, but the Q4 plan never mentions it. Someone in the room will notice, so put it on slide 5.
- **Slide 3 loses the line "We still have no automated check for the CSV export path."** It shows up on slide 5 as the CSV export test, which is a better place for it. Slide 2 mentions the 50k-row export, so say out loud that it's the one untested path. That connects the two.

**Moves and cuts**
- **Appendix:** the full sprint-by-sprint numbers, the coverage figure (58% → 71%), the flaky-suite replacement, and the full feature list.
- **Cut first if you run short:** slide 2. Fold the monthly-cadence idea into Q&A unless you want feedback on it.
- **Questions to prepare for, with backup slides after the end:** "Why was Sprint 17 so low, and is 52 sustainable?" and "How do we know the queue won't fail again before the load test exists?"

I haven't added any numbers. The 44% and 14.5% figures come from your own data (6.2 → 3.5 days, and 36.5 → 41.8 points).
