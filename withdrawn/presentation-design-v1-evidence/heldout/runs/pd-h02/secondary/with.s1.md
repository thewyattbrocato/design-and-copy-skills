**Assumed: about 15-20 minutes. Five content slides plus title and a backup appendix. Takeaway: velocity is back up and escaped defects are down, and the Aug 29 incident is the reason the queue has its new safeguards.**

The problem is density, not slide count. Six content slides is fine for this slot. The current slides are reports: each one lists every fact, and slide 2 and slide 8 are the agenda and "Thank you" slides. Here's the rebuild.

**1. Title** (keep)
Q3 Sprint Review / Team Harbor, Sprints 14-19 / Imani Okafor

**2. "Velocity is back to 52 points, and commitments land more often"**
- Visual: bar chart of the six sprints, with sprint 17 labeled "two engineers out, holiday week."
- Two callouts: **41.8** avg points (Q2: 36.5), **84%** commitment accuracy (Q2: 71%).
- Carry-over (9 to 4) moves to the appendix or gets said aloud.
- About 20 words.

**3. "Seven features shipped, led by dispatcher tools"**
- Three groups, short labels only:
  - Dispatcher console: driver-assignment modal, bulk edit for delivery windows, dark mode
  - Shipments: saved filters, CSV export up to 50,000 rows
  - Access and platform: subcontractor roles, notification service rewrite
- Speaker says one line on the rewrite and points to slide 5.
- About 25 words.

**4. "Escaped defects nearly halved; P2 fixes now take 3.5 days, not 6.2"**
- Visual: two big-number tiles, 31 to 17 and 6.2 to 3.5 days.
- Bottom line: "Still missing: automated check for the CSV export path." Being upfront about this builds trust.
- Coverage (58% to 71%) and the removed flaky suites go to the appendix.
- About 25 words.

**5. "A too-low prefetch limit delayed 1,140 driver alerts for three hours"**
- Visual: three-row strip, one line each:
  - What happened: queue backed up 3h 10m
  - Why: consumer config shipped with the rewrite had the prefetch limit set too low
  - What changed: fixed same day, queue-depth alert added the next week, load test before future queue changes
- About 40 words. Trim further if it runs long on screen.

**6. "Q4: three commitments, and one thing we need from you"**
- Visual: three items: finish subcontractor permissions (phase 2), start the route-optimization spike, add the missing CSV export test.
- Smaller line: "Also planned: dispatch tech debt, hire one senior engineer, evaluate monthly releases."
- The ask: `[ask, owner, date — not in the source material]`. Fill this in before Monday. Leaving it blank would mean the deck ends with no request.
- This slide stays up during questions.

**Appendix (backup, not presented):** full six-sprint table, carry-over numbers, coverage, flaky-suite detail, the complete seven-feature list.

**Cut to fit, in this order:** the secondary Q4 line, then the velocity callouts, then the incident's "what changed" row.

**Changes from your current deck:** drop the Overview slide (say the agenda aloud in one sentence) and the "Thank you / Questions" slide (the last content slide carries the ask).

Two things to check before Monday:
- **Hiring on a product-group slide.** Confirm you're cleared to share the senior hire outside the team. If not, move it to speaker notes.
- **Naming the config on screen.** The incident slide says the prefetch limit was too low. Confirm the team is comfortable with that wording, since the room includes people outside engineering.
