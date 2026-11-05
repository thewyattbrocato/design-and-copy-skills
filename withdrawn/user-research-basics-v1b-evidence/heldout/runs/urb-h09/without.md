# Lead with decisions, not a tour of the test

Product teams act when they see a clear ask, an owner, and a reason it matters. Don't walk through the screens in test order.

## Suggested structure (about 6 slides or sections)

**1. One-slide summary (the "if you read nothing else" slide)**
- Headline: "Seat selection is broken for both sighted and screen-reader users. Fix it before anything else."
- Three bullets: the top 3 issues, each with its ask.
- Method line: 5 participants, moderated, last week. Keep it small.

**2. Severity-ranked table**

| Priority | Issue | Evidence | Impact | Proposed action |
|---|---|---|---|---|
| **Critical** | Seat picker doesn't show availability | 4/5 confused, 2 bought the wrong deck | Wrong purchases mean refunds and support load | Redesign the availability states |
| **Critical** | Seat selection inaccessible to screen readers | 1/1 screen-reader user couldn't complete it | Total blocker, possible compliance risk | Accessibility fix, ideally alongside the redesign |
| **High** | Card entry error | 1/5 abandoned | Lost revenue, cause unknown | Engineering to check logs and reproduce |
| **Medium** | Terminal map link missed | 2/5, both first-time visitors | Hurts the audience that needs it most | Make the link more prominent |
| **Low** | Promo field unnoticed | 3/5 missed, 1 would have used one | Possible missed conversions | Decide whether to surface it (a business call) |
| **Minor** | Date picker, home screen colors | 1/5 self-corrected, 2/5 said "dull" | Little or none | Backlog |

**3. One slide per Critical/High issue**
Use the same format each time: what happened, a screenshot or 15-second clip, a participant quote, why it matters, the recommendation, and a suggested owner. Video of someone buying the wrong deck persuades far more than a statistic.

**4. What worked**
The confirmation page was 5/5. It's worth a short slide. It builds credibility and tells the team what not to touch.

**5. Next steps with owners and dates**
End with a list of who does what by when. Ask for those commitments in the room.

## Framing tips

- **Rank by severity, not frequency.** The payment error (1/5) and the screen-reader failure (1/1) outrank the 3/5 promo finding because they block the task or the sale. Say this explicitly, or people will read the small numbers as small problems.
- **Use counts ("4 of 5"), not percentages.** With n=5, percentages overstate precision. Add one line saying the test finds problems and doesn't measure how often they occur.
- **Separate observation from interpretation.** "Two bought the wrong deck" is a fact. "The color contrast is the cause" is a hypothesis, so label it as one.
- **Flag the unknowns.** For the payment error, say you don't yet know whether it's a bug or user error, and make finding out an action item.
- **Don't dilute the top message.** Put the minor items in an appendix or a single "backlog" row. Eight equal-weight findings make people act on none.
- **Note the participant mix.** Mentioning that both map-link misses were first-time visitors shows the finding is tied to a user segment.

If you'd like, I can draft the summary slide or the per-issue template in full.
