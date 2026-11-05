Assumption: one general manager reads this for all six locations, covers the previous night, and has about 30 seconds on their phone. Names and counts below are placeholders.

## Screen: "Shift swaps, overnight"

**1. Header (fixed, compact)**
- Title, date, and a status line: "Running · last action 11:42 pm · next check 6:00 am". If it's paused, this becomes a full-width amber bar: "Paused since Tue 4 pm. 2 requests came in and weren't handled. [Resume]".
- A pause button sits at the top right, one tap from here. Settings and "talk to a person" are in the overflow menu.
- The one-line summary under it is a sentence, not a stat tile: "9 handled, 2 need you." On a quiet night it reads "Nothing came in overnight. Agent is running." On a night with 0 stuck items it reads "9 handled, nothing needs you."

**2. "Needs you" (always first, only shown if non-empty)**
Each stuck item is a card. The cards are sorted by how soon the shift starts, soonest first, so a tonight-shift problem sits above a Saturday one.

Each card has:
- **A headline:** location, shift, and the problem. For example, "Harbor St · Fri dinner line cook · nobody accepted".
- **What happened, in one or two lines:** "Sam asked off Tue 9:10 pm. Offered to 6 opted-in cooks. 0 accepted. Offer expires Thu noon."
- **What the agent already did, and what it will do next:** "Re-offered to the 2 cooks at nearby locations this morning. Will tell you by Thu 9 am if still open."
- **Buttons, specific to the problem type:**
  - *Nobody accepted:* [Offer to more people], [Call someone yourself] (opens the shortlist with phone numbers), [Leave it open].
  - *Overtime:* The card says "Priya would reach 44 hrs this week if she covers. Held, not offered." Buttons: [Approve overtime], [Try someone else], [Cancel the swap].
- **Tap the card body** to open the full thread: the request, every person offered, their replies and timestamps.

Resolving a card moves it out of this section, so the section works as a to-do list.

**3. "Handled" (collapsed by default)**
- One row: "9 handled across 5 locations ▸". Tap to expand.
- Expanded, the rows are grouped by location. Each row reads "Fri lunch server: Maya → Jon, rota updated 8:14 pm".
- Any row the agent was less sure about sorts to the top of its group with a small "check" tag. Examples: cover accepted after a long gap, or a swap across locations.
- Tap a row to open the detail: the request, who was offered, who accepted, and what changed on the rota. That screen has [Undo this swap] and a "not this time / never for this kind" choice. Undo says plainly that the staff have already been messaged.

**4. "Watch" (only if something is drifting)**
This is for trends, not tonight's problems. For example: "Harbor St has had 3 unfilled swaps this month, and only 4 staff there have opted in." It names the limit or pattern, what the agent is doing about it, and a single action such as [Message the team to opt in].

**5. "Skipped" (collapsed, at the bottom)**
This lists requests the agent did not act on, with the reason: "Not opted in," "Outside the notice window," "Unclear message." Each has [Handle it now]. This list is how you'd find a miss, since nothing else shows one.

**6. Footer**
- "Last 7 days" link, which opens a plain list of past summaries.
- "What the agent is allowed to do": a link to its standing rules in plain words, covering who it may offer shifts to, the overtime limit, and the notice window.

## Why it's ordered this way
- Stuck items come first because they're the only things that need a decision. On a good night the screen is the header plus a single collapsed row.
- Routine work is collapsed but not hidden. The GM can verify it, and each swap has its own undo.
- Skipped requests get a home because a wrong action shows up in the list, but a missed one doesn't.

## Notifications (outside this screen)
- A stuck item whose shift starts within a few hours sends a push, because waiting for the morning summary would be too late. The threshold is a setting.
- Everything else waits for the morning summary. This screen is the daily digest, and the delivery time is adjustable.
