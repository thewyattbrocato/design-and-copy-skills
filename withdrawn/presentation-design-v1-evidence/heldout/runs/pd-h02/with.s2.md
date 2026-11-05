Your team is right: the deck follows the order the work happened, and it reads like a document. I'm assuming a 15-minute slot, which supports about 6 content slides. Your deck has 8 slides with 30+ bullets.

## Main changes

1. **Cut slide 2 (Overview) and slide 8 (Thank You).** In a room of 40, a purpose-and-agenda slide costs you attention for nothing. Preview the structure out loud in one sentence. End on your Q4 slide and leave it up during questions.
2. **Open with the takeaway.** For example: *"Q3 was our strongest quarter: we shipped more, with fewer bugs. One incident showed us what to fix."* Then the slides prove it.
3. **Make titles claims, not labels.** "Velocity", "Quality" and "Q4 Plan" tell the room nothing. If someone reads only your titles, they should get the whole story.
4. **Cap each slide at about 30 words, with one visual.** Keep body text at 32 px or larger for a big screen. Spoken details like "holiday week" or "two flaky suites replaced with contract tests" belong in your mouth, not on the slide.
5. **Move tables and secondary stats to the appendix.** Sprint-by-sprint numbers, test coverage and the flaky-suite swap go there.

## Proposed deck

| # | Title (claim) | What's on it |
|---|---|---|
| 1 | Q3 was our strongest quarter, with one incident to learn from | Three big numbers: 41.8 avg points (was 36.5), escaped defects 17 (was 31), 84% commitment accuracy (was 71%) |
| 2 | Velocity climbed from 41 to 52 points a sprint | One bar chart of sprints 14–19. Label the sprint 17 dip "2 out, holiday". Nothing else |
| 3 | We shipped seven features, mostly for dispatchers | Group them in three lines: *Dispatcher tools* (saved filters, bulk edit, assignment modal, dark mode), *Partners* (subcontractor access, 50k-row CSV export), *Platform* (new notification queue) |
| 4 | Escaped defects nearly halved, and P2 fixes take half the time | 31→17 and 6.2→3.5 days, as two big before/after pairs |
| 5 | The notification rewrite caused a 3-hour alert backlog on Aug 29 | 1,140 delayed driver alerts. Cause: queue prefetch limit set too low. Fixed same day, with a queue-depth alert added |
| 6 | In Q4 we protect what we shipped, then move forward | Three items: load-test the queue before changes, add the missing CSV export test, finish subcontractor permissions phase 2. Then your ask (see below) |

Appendix: the full velocity table, test coverage (58%→71%), the carry-over drop (9→4), the flaky-suite replacement, and the lower-priority Q4 items (route-optimization spike, dispatch tech debt).

## Things to decide

- **What do you want from this group?** Right now the deck only informs. The Q4 items the product group can weigh in on are the hire and the monthly release cadence. Pick one, put it on the last slide with an owner and date, and make that your call to action. I'd lead with the cadence question, since it affects them directly.
- **Tie the incident to the quality story.** The notification rewrite is both a shipped feature and the cause of your worst day. Say that directly. It builds trust, and it explains why the load-test follow-up comes first in Q4.
- **Connect the CSV gap to the plan.** Your quality slide admits there's no CSV export check, and the Q4 slide fixes it. Say that in one breath rather than listing it twice.
- **Prepare for two likely questions.** They'll probably ask whether the velocity gain is real or just point inflation, and whether another incident like Aug 29 could happen. Your commitment accuracy and carry-over numbers answer the first. The load-test and alerting follow-ups answer the second. Park them as backup slides after the end.

I can draft the exact wording for each slide, or an opening paragraph for you to say out loud, if you'd like.
