Your team is probably reacting to density. Almost every slide is 4 to 7 bullets, and several are dense with numbers. In a room of 40 people on a big screen, people can't read that and listen to you at the same time. The content is good, and most of the fix is cutting and re-titling.

**Assumptions:** you have about 12 to 15 minutes. You mainly want the product group to know where Harbor stands, so I picked one ask for the close. Correct me if either is wrong.

**Takeaway:** Harbor delivered more, and more predictably, in Q3. One incident taught us to load test before changing the queue.

## What I'd change

**Cut:**
- **Overview (slide 2).** Say the five topics out loud in your opening instead.
- **Thank You / Questions (slide 8).** End on your last content slide and leave it up during Q&A.

**Rewrite titles as claims.** "Velocity," "Quality" and "Q4 Plan" are labels. Someone reading only the titles should get the argument.

**Rebuilt deck (6 slides):**

| # | Title (claim) | What's on screen |
|---|---|---|
| 1 | Q3: Harbor delivered more, and more predictably | Two big numbers: average velocity **36.5 → 41.8** and commitment accuracy **71% → 84%**. Your name and the sprint range go on a small subtitle. |
| 2 | Velocity climbed to 52 points by Sprint 19 | A bar chart of the six sprints. Label Sprint 17 "holiday week, 2 out" directly on the bar. Carry-over (9 → 4) can go in one caption line. |
| 3 | We shipped seven features, mostly for dispatchers | Group them rather than list seven bullets: **Dispatcher workflow** (saved filters, assignment modal, bulk edit, dark mode), **Access and data** (subcontractor roles, 50k-row CSV) and **Platform** (notification rewrite). Screenshots work better than text here. |
| 4 | Fewer bugs escaped, and we fixed them faster | Two paired numbers: defects **31 → 17** and P2 fix time **6.2 → 3.5 days**. |
| 5 | The notification rewrite caused a 3-hour alert backlog | **3h 10m** and **1,140 delayed driver alerts**. Add one line for the cause (prefetch limit too low) and one for the fix (same-day fix, queue-depth alert added, load test before the next change). |
| 6 | Q4: finish permissions, close our test gaps, and decide on release cadence | Three short groups, plus the ask below. |

**Where the rest went:**
- **Slide 4 (quality), details:** dispatch-module coverage (58% → 71%) and the flaky-suite replacement go in the appendix or your spoken remarks.
- **Slide 4 (quality), CSV gap:** the missing CSV export check moves to slide 6 as "add CSV export test." That's where it's actionable.
- **Slide 3 (velocity), per-sprint numbers:** the chart replaces the six-number sentence.
- **Slide 7 (Q4 plan), items:**
  - Group the plan as **Finish** (permissions phase 2), **Protect** (tech debt, CSV test, queue load testing) and **Explore** (route-optimization spike, monthly cadence).
  - Put the senior hire in your spoken remarks, since the product group can't act on it.

**Order:** I kept the incident after quality and didn't push it to the end. It's tied to the notification rewrite on slide 3, so it's better to say it plainly than to have someone raise it in Q&A.

## Make Slide 6 carry an ask

A review with no ask is easy to forget. The only Q4 item that needs product's input is **investigating a monthly release cadence**. I'd end on the slide with something like "Product: tell us by [date] what a monthly cadence would break for you," with a named owner. I've left the date as a placeholder because I don't know it.

## For the big screen
- Keep body text at about 32 px or larger, with roughly 30 words per slide at most. If it doesn't fit, split or cut. Don't shrink it.
- Make the chart's bars and labels readable from the back row.
- Skip animation and speaker-note walls. If you want notes, use one line per slide with the number to say and the hand-off.

## Likely hard questions (keep a backup slide for each)
1. "Was the velocity gain real, or did points inflate?" Be ready with commitment accuracy and carry-over as evidence.
2. "How do we know the queue won't fail again?" Have the load-test plan and its timing.
3. "Why is there still no CSV export test, when we raised the row limit?" Have an owner and a sprint.

I can draft the exact wording for each slide, or write a 60-second opening that previews the three topics by voice.
