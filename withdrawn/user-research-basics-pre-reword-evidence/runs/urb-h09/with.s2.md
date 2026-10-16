## Suggested layout (about 6 slides)

**1. The headline, in one sentence.** For example: "People can't tell which seats are open, and that led to wrong-deck purchases. A screen reader user couldn't finish seat selection at all. Everything after seat selection mostly worked."

**2. What we did.** Say "5 participants, task-based sessions, last week." Add who they were, including that some were first-time port visitors. I don't have those details, so fill them in. Report counts as "4 of 5", not percentages. With 5 people, percentages will make the product team over-trust the numbers.

**3. Priority table.** This is the slide people will act on. Order it by severity and by how central the task is, not by how many people mentioned it.

| # | Issue | Task | Hit | What happened | Severity |
|---|---|---|---|---|---|
| 1 | Seat availability unclear | Choose seat | 4 of 5 | Couldn't tell which seats were available; 2 bought the wrong deck | Blocks (money and trust) |
| 2 | Screen reader can't complete seat selection | Choose seat | 1 of 1 screen reader user | Could not complete the task | Blocks |
| 3 | Card entry error | Pay | 1 of 5 | Hit an error and abandoned | Blocks (lead, single source) |
| 4 | Terminal map link missed | Find terminal info | 2 of 5, both first-time visitors | Didn't see the link | Slows |
| 5 | Promo field not noticed | Pay | 3 of 5 | Didn't notice it; 1 said they'd have used a code | Slows (lead) |
| 6 | Wrong month in date picker | Pick date | 1 of 5 | Noticed and fixed it | Annoys |

Add a final column, "Decision needed / owner", so each row ends with a named person or team. That column is what gets things acted on. Put proposed fixes there, labeled as proposals, and keep them out of the findings themselves.

**4. Deep dive on #1 and #2.** Together they are the story, so give them their own slide. Use a screenshot or short clip of someone misreading the seat map. A 20-second clip of a person buying the wrong deck persuades more than any table. Show the screen reader failure on the same slide, since it's the same screen. Accessibility often gets treated as a footnote, so state clearly that this participant could not complete a core task.

**5. What worked.** Say that 5 of 5 found their ticket on the confirmation page. It tells the team what not to touch, and it makes the rest of the report read as balanced.

**6. Open questions and next steps.**
- **Payment error:** you have one observation. Before Monday, check payment logs or error tracking to see whether it's a known issue. That could turn a lead into a confirmed bug.
- **Promo field:** 1 person said they'd have used a code, which is a weak signal. Check how often codes are redeemed to see if this matters.
- **Retest:** after the seat picker changes, retest with new participants, including at least one screen reader user.

## What to leave out or demote
- **"Colors felt a bit dull" (2 of 5).** That's a preference, not a usability problem. Nobody failed a task because of it. Put it in an appendix or "other observations" line, not the main table.
- **The date picker.** It's one person who self-corrected, so keep it at the bottom as low severity.

## Tips for Monday
- Send the priority table as a pre-read, and spend the meeting on slide 4 and on assigning owners.
- Ask for a decision on each of the top three rows before the meeting ends.
- If someone asks "is 4 of 5 significant?", say this was a small qualitative test. It shows where problems exist and why, not how often they occur across all users.

A human needs to confirm the participant details and pull the payment logs. I haven't seen either.
