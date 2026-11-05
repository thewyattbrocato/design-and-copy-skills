**Assumed: a 10-minute slot, so five content slides plus the title. Takeaway: Q3 delivery got faster and more predictable, quality improved, and the one serious incident is fixed and guarded.** If you have 15 minutes, keep the same five and add time to the talk, not slides.

The deck is "a lot" because it's a status document in slide form: an agenda, a closing that just says "Questions," and 20-plus facts that all want equal attention. Cut it to this:

| # | Claim title (on screen) | On-screen content | Move to appendix |
|---|---|---|---|
| 1 | Q3 Sprint Review: Team Harbor, sprints 14–19 | Title and presenter only | Nothing |
| 2 | Sprint commitments got reliable: 84% hit, up from 71% | Two big numbers: 41.8 avg points (Q2: 36.5), 84% accuracy (Q2: 71%). Carry-over 9 → 4 per sprint as a third line | The six per-sprint point values, with sprint 17's explanation spoken, not printed |
| 3 | Seven features shipped; three change your day | Saved filters, CSV export to 50,000 rows, driver-assignment conflict warnings. Remaining four in a small footer line | Full list, bulk edit, dark mode, subcontractor RBAC, notification rewrite |
| 4 | Escaped defects almost halved, and P2 bugs get fixed twice as fast | 31 → 17 defects; P2 median fix 6.2 → 3.5 days | Dispatch coverage 58 → 71%, flaky-suite swap |
| 5 | A 3-hour queue backup on Aug 29 delayed 1,140 driver alerts. It's fixed, and queue changes now get load-tested | Two numbers, one-line cause ("a config setting shipped with the notification rewrite"), one-line fix and guardrail | Prefetch-limit detail, the alert-threshold timeline |
| 6 | Q4: finish subcontractor permissions, start route optimization, hire a senior engineer | Three items. Monthly-release investigation and tech debt as a footer line | Full six-item list, the missing CSV export test (it's a real gap; say it aloud once) |

Changes that matter most:

- **Cut the overview slide.** Replace it with one spoken sentence: "Three parts: how we delivered, what we shipped, what went wrong, and what's next."
- **Cut the thank-you slide.** Slide 6 stays up during questions, so the ask is still visible when Q&A starts.
- **Use claim titles.** Each title states the point. Labels like "Velocity" or "Quality" waste the one line people read first.
- **Keep the incident, but own it plainly.** Put it right before the plan, not buried in quality. The product group felt those alerts, so say what it cost them in drivers' terms and don't soften it.
- **Put a full appendix behind it.** Sprint-by-sprint points, all seven features, all quality metrics, and the root-cause detail go there. Say "details in the appendix" once, at the end.

Two things would sharpen this further: how many minutes you actually have, and whether you want anything from the room (a decision, a volunteer, feedback on the Q4 plan). If you want a decision, the last slide needs that ask with an owner and date.
