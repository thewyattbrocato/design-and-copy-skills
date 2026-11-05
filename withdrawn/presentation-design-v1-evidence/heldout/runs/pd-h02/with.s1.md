Your team is right: the deck is organized by topic, not by what you want the room to take away. I've assumed a 15-minute slot, which gives about 6 content slides. Tell me if the slot is different.

**Takeaway to build around:** *Q3 was our most predictable quarter yet, but one untested change caused the Aug 29 incident, so Q4 starts with making the queue safe.*

## What I'd change

**Cut**
- **Slide 2 (Overview).** Say it out loud in 20 seconds. A preview slide costs you a minute with 40 people watching.
- **Slide 8 (Thank You / Questions).** Leave the Q4 slide up during questions.
- **Slide 1 as a title card.** Make it the takeaway slide and put "Team Harbor, sprints 14–19" in small type.

**Retitle every slide as a claim.** Right now the titles are labels ("Velocity", "Quality"). The titles alone should tell the story.

**Cap each slide at about 30 words.** Anything you won't say aloud goes to the appendix.

## Rebuilt deck

| # | Title (the claim) | On screen |
|---|---|---|
| 1 | Q3 was our most predictable quarter, and one untested change hurt us | Takeaway only. Small: Team Harbor · Sprints 14–19 · Imani Okafor |
| 2 | We hit 84% of commitments, up from 71% | Bar chart of sprints 14–19 with sprint 17 annotated "2 out, holiday week". Two big numbers: **41.8 avg pts (Q2: 36.5)** and **84% (Q2: 71%)** |
| 3 | Seven features shipped; these three matter most to dispatchers | Saved filters, driver-assignment modal, subcontractor roles. Other four go to the appendix. Swap in whichever three actually matter most. |
| 4 | Escaped defects nearly halved, and P2 fixes take half the time | **31 → 17** and **6.2 → 3.5 days**. Nothing else. |
| 5 | Our notification rewrite delayed 1,140 driver alerts for over 3 hours | One line of cause (prefetch limit set too low), one line of fix (same-day patch, queue-depth alert added). Own it plainly. |
| 6 | Q4: make the queue safe, close the test gap, then build | Three items: load-test the queue before changes, add the CSV export test, finish subcontractor permissions phase 2. Then the ask (below). |

**Appendix:**
- Full shipped list
- Coverage 58% → 71%
- Flaky suites replaced by contract tests
- Carry-over 9 → 4
- Per-sprint velocity numbers
- Remaining Q4 items

## Specific fixes
- **Slide 3 (Velocity).** Six sprint numbers in a bullet list can't be read from the back of a room. A chart shows the Sprint 17 dip and the late climb instantly, and you can explain the dip in one sentence.
- **Slide 5 (Quality).** The CSV-export gap is currently buried as the last bullet. Move it to Q4, where it becomes an action. It also links to the incident story: you ship untested paths, and they bite.
- **Slide 6 (Incident).** Put the incident before Q4 so the Q4 priorities read as a consequence of it. Your follow-up ("load test before future changes") becomes the lead item on the Q4 slide.
- **Slide 7 (Q4).** You list six items with equal weight. Pick three for the screen. The route-optimization spike, tech debt and hiring can go to the appendix or be said aloud.

## The ask
Your Q4 slide has no ask. The monthly release cadence affects the whole product group, so that's probably where you want their input. A closing line like *"Cadence: product group feedback to me by [date]"* gives the room something to do. I've left the date and owner as placeholders. Decide whether you want input on cadence, support on the hire, or neither.

## Two checks
- I called defects "nearly halved" (31 → 17 is a 45% drop) and P2 fixes "half the time" (6.2 → 3.5 days is 44% faster). Say "nearly" if someone challenges you.
- Expect questions on the incident and on why Sprint 19 (52 points) is so far above the others. Keep one backup slide on each after the appendix divider.

I can draft the speaker outline for each slide, or write out the opening 30 seconds, if you'd like.
