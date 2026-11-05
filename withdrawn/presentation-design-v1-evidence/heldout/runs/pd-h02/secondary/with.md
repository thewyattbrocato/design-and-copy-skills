**Assumed slot: about 10 minutes, so 4 content slides plus the title.** You didn't give a time, so if you have 15 minutes, keep the same four slides and talk longer on the incident. The takeaway: *Q3 delivery got faster and more predictable, and the Aug 29 incident and the CSV export gap are what Q4 addresses.*

Your deck is not too long in slide count. It's too long in words per slide and in the number of facts per slide. Six content slides plus a closing slide is about 20 facts for a room that will remember three.

## Proposed structure

1. **Title.** Keep as is. Add a one-line subtitle with the takeaway if you want one.
2. **"Velocity rose to 41.8 points a sprint, and we now land 84% of commitments."**
   - One chart: the six sprint values, with Q2 average as a reference line. Sprint 17 gets a label: "two engineers out, holiday week."
   - Say the Q2 comparison (36.5 → 41.8; accuracy 71% → 84%) aloud, not on screen.
   - Carry-over (9 → 4) moves to the appendix or to speech.
3. **"Seven features shipped, led by the driver-assignment modal."**
   - Group into three short lines: *Dispatcher tools* (driver-assignment modal, bulk edit, saved filters), *Platform* (CSV export to 50k rows, notification service rewrite), *Access* (subcontractor accounts).
   - Dark mode can go to the appendix. It's real work but the room will not remember it.
4. **"Escaped defects nearly halved, and P2 bugs now close in half the time."**
   - Two numbers: 31 → 17 and 6.2 → 3.5 days.
   - Keep the last bullet: "No automated check on the CSV export path yet." It's the honest gap, and it sets up the Q4 plan. Put it on the slide, not in the appendix.
   - Coverage (58% → 71%) and the flaky-suite swap move to the appendix.
5. **"A 3-hour notification backup delayed 1,140 driver alerts; we now load-test queue changes first."**
   - Four lines max: what happened, the cause in one sentence (prefetch limit too low in the rewrite's consumer config), what changed (fixed same day, depth alert added), and the follow-up (load test before any queue change).
   - This is your strongest slide. Say the impact plainly and own the miss in one spoken sentence.
6. **"Q4: finish subcontractor permissions, close the CSV test gap, and start route optimization."**
   - Three items. Put "pay down dispatch tech debt" under the CSV item as a group.
   - Hiring a senior engineer and investigating monthly releases are decisions for the room, not status items. Either name an owner and a date for each, or move them to the appendix. "Investigate" items on a product-group slide invite questions you may not be ready for.
   - Close here. End with the ask if you have one; otherwise say "Questions" on this slide.

**Cut:** the Overview slide (replace with one spoken sentence: "Six sprints, what shipped, how quality moved, one incident, what's next") and the "Thank You / Questions" slide. Both add a slide with no content.

## Moves to the appendix

- Sprint-by-sprint point table
- Carry-over numbers
- Dark mode and the full feature list
- Test coverage and the flaky-suite change
- Incident detail: alert threshold timing and the exact queue metrics

## Before Monday

- **Prepare backup slides for the two likely hard questions:** "Was the velocity jump real or just easier sprints?" (sprint 17 context, carry-over trend) and "Why do we still have no CSV export test?" (the cause and the Q4 date). Put them after the appendix divider.
- **Check the word count on each slide.** After the cuts, each content slide should be under about 30 words. If one is over 50, it still has too much.
- **Confirm the body text size.** A 40-person room with a big screen needs the body text at least as large as your title's minimum; if a line wraps to two lines at that size, shorten it rather than shrinking it.

If you tell me the exact slot length and whether there's a decision you want from the room, I can tighten the titles and the closing ask.
