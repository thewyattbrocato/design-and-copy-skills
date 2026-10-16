## Layout for Monday

**Slide 1: The headline and the ask (30 seconds)**
- One sentence: "5 people tried to buy a ticket. The seat picker is where it broke: 4 of 5 couldn't tell which seats were available, and 2 bought the wrong deck."
- Below it, list the 2–3 decisions you need from the room (see "Decisions to ask for" below). Putting the ask on slide 1 gets people reading for what to do.

**Slide 2: One-table summary, ranked by severity, then by how central the task is**

| # | Task | Hit | What happened | Severity |
|---|---|---|---|---|
| 1 | Seat selection | 4 of 5 | Couldn't tell which seats were available; 2 bought the wrong deck | Blocks, and caused a wrong purchase |
| 2 | Seat selection (screen reader) | 1 of 1 screen reader user | Couldn't complete seat selection at all | Blocks |
| 3 | Payment | 1 of 5 | Error on card entry; abandoned the task | Blocks (single source, so a lead) |
| 4 | Promo code | 3 of 5 | Didn't notice the field; 1 of them said they'd have used a code | Slows or costs value |
| 5 | Terminal map link | 2 of 5 | Missed it; both were first-time visitors to the port | Slows |
| 6 | Date picker | 1 of 5 | Chose the wrong month, noticed, fixed it | Annoys |

Row 2 is the same task as row 1, so show them together on the next slide. Keep them as separate rows here so the accessibility failure doesn't get lost inside a usability finding.

**Slide 3: Seat picker deep dive (this is the one to spend time on)**
- Show a screenshot or short clip of a participant mid-task. A video clip persuades more than a stat.
- State the two failures side by side: sighted users couldn't read availability, and the screen reader user couldn't finish.
- Say what the cost was: 2 of 5 ended up with the wrong deck, so this is a wrong purchase, not just friction.

**Slide 4: Payment and promo code (one slide, two items)**
- Payment is 1 of 5, so say plainly that it's a lead. Because it ends in abandonment on the revenue step, ask for a check of error logs for card entry before debating it.
- Promo: 3 of 5 missed the field, and only 1 of those 3 said they'd have used a code. Present this as "not noticed", not "wanted".

**Slide 5: Smaller items**
- Terminal map: 2 of 5 missed it, both first-time visitors. That is a pattern worth watching, because first-timers are the ones who need it.
- Date picker: 1 of 5, self-corrected. Log it and move on.

**Slide 6: What worked**
- Confirmation page: 5 of 5 found their ticket without trouble. Say it out loud. It shows the test wasn't only bad news, and it tells the team to leave that page alone.

**Slide 7: What we're not treating as a finding**
- Home screen colors: 2 of 5 called them "a bit dull." That's a preference, not a task failure. Mention it in one line and park it.

**Slide 8: Decisions to ask for, and what's still unknown**
Ask for an owner and a date on each:
1. Seat picker availability: who owns a redesign and when it gets retested with new people.
2. Screen reader path for seat selection: an owner, and whether it ships in the same fix as #1.
3. Payment error: someone to pull logs this week to see whether it's more than 1 in 5.

Unknowns: how often the payment error happens in production, whether promo visibility affects redemption, and whether the map miss is specific to first-timers beyond these 2 people.

**Presentation rules that help people act**
- Report counts as "4 of 5", never percentages. With 5 people, a percentage overstates certainty.
- Say once, up front, that this was 5 people, not a measurement of how often things happen. It's a good way to find problems but not a way to size them.
- Keep fixes out of the findings slides. Put proposed solutions on the decisions slide or leave them for the working session. Otherwise the room argues about solutions instead of agreeing on the problem.
- Cut the order if you're short on time: slides 1, 2, 3, 8.

Two notes:
- I assumed the screen reader participant is one of the 5. If they're a sixth person, change the counts to match.
- You'll need to bring the clip or screenshots from your session recordings. I can't produce those.
