# Morning summary: GM screen layout

The screen answers one question first: does anything need me? Stuck items sit at the top, routine work is collapsed below, and each section has a clear tap target.

**1. Header (fixed, not scrolling)**
- Date and a one-line status: "Tue 27 Oct · 14 handled · **2 need you**"
- If nothing is stuck: "15 handled · nothing needs you." The screen is then just the header and the collapsed list.
- Location filter, tappable: **All locations ▾**, with a dropdown for the six sites. Stuck items are counted per location in the dropdown, so a GM can see which site has the problem.

**2. Needs you (expanded, always first, only shown if non-empty)**
Sorted by shift start time, soonest first. Each card is one stuck item.

*Card type A: Unfilled shift*
- Title: "Unfilled · Line cook · Hollis St · Wed 4pm–close"
- Status line: "Offered to 9 opted-in staff, 0 accepted. Last offer 5:40am."
- Buttons, in this order:
  - **Offer to wider pool**: the agent extends the search to other opted-in staff, including other locations if the group allows it.
  - **Assign…**: opens a picker of eligible staff, each showing their hours this week, so the GM can pick by hand.
  - **Call list** : opens the people who were contacted and didn't accept, with tap-to-call numbers.
  - **Mark handled** : for when the GM has fixed it outside the app.

*Card type B: Overtime conflict*
- Title: "Overtime · Sat dinner cover · Ash Ln"
- Status line: "Covering puts Jamie R. at 41.5 hrs (OT starts at 40)."
- Buttons:
  - **Approve overtime** : opens a confirm sheet ("Jamie R. +1.5 OT hrs, est. $X") and needs a second tap, because it costs money.
  - **Choose someone else** : same picker as above, with OT-free staff first.
  - **Leave unfilled** : the shift stays open and moves to card type A.
- The agent never approves overtime on its own.

**3. Still searching (shown if non-empty, below Needs you)**
- Shifts where offers are out and the agent is still waiting. Each row: shift name, "3 of 9 replied," and the time of the next automatic step.
- Tap a row to open the thread. No action buttons, so the GM isn't tempted to step in early.

**4. Handled overnight (collapsed by default)**
- Header: "Handled · 14 ▸" (tap to expand).
- Grouped by type inside: **Covered** (n), **Swapped** (n), **Rota updated** (n).
- One line per item: "11:02pm · Maria K. → Sat lunch, Ash Ln · covered by Devon T."
- Tap a row: a detail sheet shows who asked, who covered, the rota before and after, and the message thread.
- Inside the detail sheet, **Undo** appears only before the shift starts and reverts the rota only. It does not message staff, so the sheet should say so: "Staff already notified. Undo changes the rota only."

**5. Footer (fixed, small)**
- **Agent log**: full timeline, for when the GM wants to check the agent's work.
- **Opt-in pool**: count of opted-in staff per location, tappable to edit.

**Ordering rules, in short**
- Stuck items above everything else, soonest shift first.
- Overtime and unfilled cards are separate, because they need different decisions.
- Routine items are counted, not listed, until the GM asks.
- Every card's buttons are actions the agent can carry out. A status line never implies a button that isn't there.

**Assumptions I made:** the GM has rota-edit rights for all six sites, the group allows cross-location cover, and OT is measured weekly at 40 hours. If any of these differ, the "Offer to wider pool" button and the OT card change most.
