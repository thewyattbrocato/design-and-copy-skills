## Lay it out as a ranked list of decisions

Product teams act when each item has a severity, a count, an owner and a decision. They don't act on a list of observations. Here's a structure for Monday.

### Slide 1: The headline (one sentence plus the ask)
> "In 5 sessions, the seat picker failed 4 people, cost 2 of them the wrong deck, and blocked the one screen reader user completely. We need a decision on it today. Everything else is smaller."

Open with this. If the meeting is cut short, the seat picker is the part that has to land.

### Slide 2: One-page summary table
Sort by severity, then by how central the task is to buying a ticket. Give counts as n of 5, not percentages.

| # | Area | Hit | What happened | Severity |
|---|------|-----|---------------|----------|
| 1 | Seat picker | 4 of 5 | Couldn't tell which seats were available. 2 bought the wrong deck. | **Blocks** (wrong purchase) |
| 2 | Seat picker, screen reader | 1 of 1 | Couldn't complete seat selection at all. | **Blocks** |
| 3 | Card entry | 1 of 5 | Hit an error and abandoned the task. | **Blocks** (single source, so a lead) |
| 4 | Promo code field | 3 of 5 | Didn't notice it. 1 said they'd have used one. | Slows / missed value |
| 5 | Terminal map link | 2 of 5 | Missed it. Both were first-time visitors to the port. | Slows (specific group) |
| 6 | Date picker | 1 of 5 | Chose the wrong month, noticed and fixed it. | Annoys |

### Slides 3–5: One slide per top finding
Use the same template each time:
- **Task**, e.g. "Choose a seat on a deck."
- **What happened**: counts plus a 20–30 second clip or a quote. Clips persuade far better than bullets.
- **Why it matters**: 2 of 5 bought the wrong deck. Spell out the cost, such as refunds, support contacts or lost trust.
- **Decision needed**: a named owner and a date.

Keep the finding itself free of solutions. Put options in a separate "decision" line so the team debates the problem first. Treat the screen reader result as part of the seat picker, not a footnote. It's one person, but a total failure on the core task.

### Slide 6: What worked
The confirmation page was found without trouble by 5 of 5. Saying so builds credibility, and it shows the team what not to touch.

### Slide 7: Parked items
- **Home screen colors** (2 of 5 said "a bit dull"): this is a preference, not a usability problem. No one failed a task because of it. List it as an observation and don't ask for action.
- **Date picker**: the person caught and fixed the error, so keep it on the watch list.

### Slide 8: What we don't know yet, and the next check
- **Payment error**: 1 person is a lead, not a pattern. The cheapest check is to look at card-entry error rates and logs for that step. That will tell you whether it's a real defect or a one-off.
- **Promo code**: the evidence on value is thin (1 person). Check how often codes are redeemed.
- **Map link**: 2 of 2 first-timers missed it, but you tested few first-time visitors. Note how many of the 5 were first-timers.
- **Retest**: after the seat picker changes, run 3–5 new people, including a screen reader user.

### Caveats to state on one line
With 5 people, these are problems observed, not rates. Don't quote "80% failed" (4 of 5). Say "4 of 5". Also say who the 5 were, and note that only one screen reader user took part.

### Things only you can do
- Pick the 2–3 clips for the top findings, and get participant consent if the recordings will be shown.
- Assign an owner to each decision before the meeting, so the room isn't assigning them live.

I assumed the team wants a decision-oriented readout rather than a full research report. If you tell me the meeting length, I can cut this to a 3-slide version.
