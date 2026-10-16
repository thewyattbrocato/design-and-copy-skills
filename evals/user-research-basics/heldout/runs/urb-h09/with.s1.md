# Layout for Monday

**Lead with the decisions you need, not the list of findings.** Eight items at equal weight will get a nod and no action. Use this order:

1. **Slide 1: the headline and the ask (30 seconds).** For example: "5 people tried to buy a ticket. The seat picker is the main problem: 4 of 5 couldn't tell which seats were available, and 2 bought the wrong deck. We need a decision on that today." Name the 2–3 things you want owners for.
2. **Slide 2: what worked.** The confirmation page had 5 of 5 finding their ticket without trouble. It's short and it builds credibility, so the team doesn't hear "everything is broken."
3. **Slides 3–5: one slide per top issue.** Use the same structure each time:
   - Task
   - How many of 5 hit it
   - What happened
   - Severity
   - A 20–30 second clip or a verbatim quote
   - The decision needed, with a suggested owner
4. **Slide 6: a single ranked table of everything else.**
5. **Last slide: what we don't know yet and the cheapest next check.**

## Ranked table

Severity: **Blocks** means the person couldn't finish or made a wrong purchase. **Slows** means they hesitated or missed something. **Annoys** means minor friction.

| # | Issue | Hit | Severity | Note |
|---|---|---|---|---|
| 1 | Seat picker: can't tell which seats are available | 4 of 5 | Blocks | 2 bought the wrong deck. This is the core task and it cost people money. |
| 2 | Seat selection with a screen reader | 1 of 1 screen-reader user | Blocks | Couldn't complete at all. One person, but a total block. Likely related to #1, so check whether one fix covers both. |
| 3 | Card entry error | 1 of 5 | Blocks | Abandoned the task. This is a lead until you check payment error logs for the same failure. |
| 4 | Terminal map link missed | 2 of 5 | Slows | Both were first-time visitors to the port, which is probably the group that needs it most. |
| 5 | Promo code field not noticed | 3 of 5 | Slows | 1 of those 3 said they'd have used one. That's a statement about intent, not behavior, so treat it as weak. |
| 6 | Date picker: wrong month | 1 of 5 | Annoys | They noticed and fixed it themselves. |
| 7 | Home screen colors "a bit dull" | 2 of 5 | n/a | This is a preference, not a usability problem. Put it in the appendix. |

## Tips for getting action

- **Say "4 of 5", never "80%".** Percentages from five people invite pushback and overstate certainty. Be upfront that this is a small qualitative test that finds problems. It doesn't measure how common they are.
- **Keep findings separate from fixes.** Show what happened first, then put suggested directions in a "decision needed" line. Otherwise the meeting turns into a design debate about your solution.
- **Show, don't summarize, for #1.** A clip of someone confidently picking the wrong deck persuades faster than any slide.
- **Treat the screen-reader result as its own item, not a footnote.** It's one person, so flag it as a single source. But a blocked core task is a severity argument, not a frequency one. If there's an accessibility commitment or legal exposure, say so here.
- **Give each top item an owner and a next step.** For example, "Seat picker: design to propose options by [date]." Ask for these in the room rather than after.
- **Cross-check the leads with data you already have.** Payment error logs and map-link click rates would turn #3 and #4 from anecdotes into evidence.
- **Don't rank colors alongside usability.** Two "a bit dull" comments is taste, so don't let it take airtime from #1.

## Caveats to state on the last slide

- Five people won't show how often these issues occur. They show that the problems exist and what they look like.
- I don't know how the five were recruited. If they weren't representative (for example, mostly regular riders), say who the sample leaves out.
- After fixing #1 and #2, retest with new people, including more than one screen-reader user.

Your notes didn't include participant details, quotes, or clip timestamps. Pull those from your recordings for the top three issues, and I haven't invented any. If you share your session notes, I can draft the actual slide text.
