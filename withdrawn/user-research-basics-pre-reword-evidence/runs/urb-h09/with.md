# Layout for Monday

**Assumption:** this was a moderated task test of the booking flow with 5 participants, one of whom uses a screen reader.

## 1. Open with the decision you need (slide 1)
Put the ask first, before any detail:

> "Seat selection is the one place the flow broke for most people, and it cost two participants the wrong ticket. We need an owner and a fix before the next release."

Add a one-line sample note: "5 participants, one task flow. Counts are people, not percentages."

## 2. Ranked findings table (slide 2)
Rank by severity (blocks, slows, annoys), then by how central the task is. Use the same columns for every row: **Task | n of 5 | What happened | Severity | Proposed owner**.

| # | Task | n of 5 | What happened | Severity |
|---|---|---|---|---|
| 1 | Seat picker | 4 | Couldn't tell which seats were available; 2 bought the wrong deck | Blocks (wrong purchase) |
| 2 | Seat picker, screen reader | 1 of 1 screen reader user | Couldn't complete seat selection | Blocks |
| 3 | Payment | 1 | Error on card entry; abandoned the task | Blocks (lead, see below) |
| 4 | Promo code field | 3 | Didn't notice it; 1 of those said they'd have used one | Slows |
| 5 | Terminal map link | 2 | Missed it; both were first-time visitors to the port | Slows |
| 6 | Date picker | 1 | Chose the wrong month, noticed, fixed it | Annoys |
| 7 | Home screen colors | 2 | Called them "a bit dull" | Preference, not a finding |

Rows 1 and 2 are the same screen, so give them one slide each in the detail section. Row 2 needs its own slide because the accessibility failure is easy to lose inside the "4 of 5" story.

## 3. One detail slide per top item (slides 3–5)
For each, use the same structure:
- **Task and count:** "Seat picker: 4 of 5."
- **What happened:** a screenshot or 20-second clip, plus a short verbatim quote if you have one in your notes.
- **Why it matters:** two of five bought the wrong deck. That is a real purchase error, not just friction.
- **Decision for the room:** who owns it and when they'll come back with options.

Keep proposed solutions on a separate "options" line. Findings state what happened. Fixes are the team's call.

## 4. Say what's solid and what's a lead
- **Solid:** seat picker. It's a majority of participants, with real consequences.
- **Lead:** payment. It's 1 of 5, but it blocks a purchase. Don't call it a pattern. Ask engineering to check card-entry error logs, which is cheaper than another test.
- **Lead:** the map link. It's 2 of 5, but both were first-time visitors, so it may matter mostly for new customers. Say so, and note that the sample is too small to tell.
- **Sample limit:** one screen reader user shows the failure exists, not how common it is.

## 5. Include what worked (one slide)
The confirmation page had 5 of 5 finding their ticket without trouble. Say "leave it alone." It stops the team from reworking something that works, and it makes the rest of the report more credible.

## 6. Close with asks and next steps
A short table: **Item | Owner | Next step | Date**. The date and owner cells are for you to fill in with the team. Then finish with what's still unknown and the cheapest check:
- Payment error cause: check logs.
- Seat picker fix: retest with 3–5 new people, including at least one screen reader user.

## Tips for the room
- Don't use percentages. "4 of 5" is honest, and "80%" invites someone to ask about significance.
- Cut or park the color comment. It's a preference from 2 people and will pull discussion away from the seat picker.
- Put the accessibility failure on its own slide, not in a footnote.

You'll need to supply the screenshots or clips, any verbatim quotes, and the owners. I haven't invented any of those.
