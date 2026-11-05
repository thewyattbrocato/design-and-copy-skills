**25 minutes: 9 content slides in about 20 minutes of talk, plus 5 for questions.**
**Takeaway:** One unchecked config change took checkout down for 2h40m. It can happen again today, and two engineers for one quarter close that gap.
**Action:** The execs approve the staffing. The engineers adopt the new change controls.

Execs get the verdict and the ask in the first two minutes. The engineers get the detail in the middle, and the ask returns at the end. Bracketed items are placeholders for your real data. I haven't invented any numbers.

| # | Slide title (the claim) | On screen | Time |
|---|---|---|---|
| 1 | **A single config change took checkout down for 2h 40m. Two engineers for a quarter stops it recurring.** | Big "2h 40m", the Saturday's date, and the ask in one line | 2 min |
| 2 | **The outage cost us [N orders / $X revenue / N customers affected]** | One or two numbers, large | 1 min |
| 3 | **[Your claim from the data, e.g. "Most of the 160 minutes went on finding the cause, not fixing it"]** | A horizontal timeline bar split into detect, diagnose, fix and recover, with 4–5 labelled moments | 3 min |
| 4 | **A connection-pool change in the payment service [exhausted connections under Saturday load]** | Simple diagram: the old value against the new value, and what failed downstream. Fill in the real mechanism. | 3 min |
| 5 | **Nothing between the change and production could have caught it** | Four checkpoints (review, staging, canary, alerting), with the ones that failed or were missing crossed out. Confirm which applies. | 2 min |
| 6 | **As things stand, it will happen again: [N] other services have the same exposure** | One number, plus a short list of the riskiest services. If you can't count them, say "we don't know yet" and make that the finding. | 2 min |
| 7 | **Three controls make a bad config change unable to take down checkout** | Three short labels, e.g. validate before deploy, roll out in stages, roll back automatically. Swap in your real proposal. | 3 min |
| 8 | **Two engineers for one quarter costs less than [one more outage]** | Cost of the project next to the cost per hour of downtime × 2h 40m. Add your own estimate of how likely a repeat is. | 2 min |
| 9 | **Decision needed: approve 2 engineers for Q[_], owner [name], by [date]** | Ask, owner, date, and the first milestone. This slide stays up during questions. | 2 min |

**Recap:** Slides 3–5 are "what happened, how, why it got through". Slides 6–8 are "will it recur, what fixes it, what it costs". Say those labels out loud in the opening and again before slide 9.

**Backup slides, parked after slide 9:**
- Why not just fix this one value? (Slide 6 is the answer.)
- Why two engineers and why a quarter? (Scope and milestones.)
- Whose fault was it? (Blameless framing: the process allowed it.)
- What did we change right away, and what's still open?

**Appendix:**
- The detailed minute-by-minute timeline
- The config diff
- The alert and log excerpts

Engineers who want more can get it there, and none of it goes on the live slides.

**If you lose time, cut in this order:** fold slide 2 into slide 1, turn slide 5 into one spoken sentence, then compress slide 3 to three moments.

**Assumptions to check:**
- I assumed the fix is controls on config changes in general, not only on the pool setting. If it's narrower, slides 6 and 7 change.
- I assumed slide 5's gaps (review, staging, canary, alerting) are real. Correct them from your postmortem.
