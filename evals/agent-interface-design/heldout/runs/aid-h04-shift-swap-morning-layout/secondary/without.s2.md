# GM morning summary: layout

The screen is ordered by what needs the GM's decision, not by chronology. Routine results are shown as a count, so the GM only reads detail for exceptions.

```
┌──────────────────────────────────┐
│ Salt Cellar · Tue 27 Oct    [All ▾]│  ① Header
│ 9 covered · 2 need you           │
├──────────────────────────────────┤
│ NEEDS YOU (2)                    │  ② Exceptions
│ ┌──────────────────────────────┐ │
│ │ ⚠ UNFILLED · Fri 19:00 line  │ │
│ │ Salt Cellar Riverside         │ │
│ │ Asked 14 · 0 accepted         │ │
│ │ Agent resumes at 14:00        │ │
│ │ [Post to all]  [Call list]    │ │
│ │ [Cancel shift]                │ │
│ └──────────────────────────────┘ │
│ ┌──────────────────────────────┐ │
│ │ ⚠ OVERTIME · Wed 16:00 close │ │
│ │ Jordan R. → 41.5h → 46h      │ │
│ │ [Approve OT]  [Next candidate]│ │
│ └──────────────────────────────┘ │
├──────────────────────────────────┤
│ HANDLED OVERNIGHT (9)  ▸         │  ③ Routine
│ 7 swaps covered · 2 rota edits   │
├──────────────────────────────────┤
│ THIS WEEK AT RISK (1)  ▸         │  ④ Look-ahead
├──────────────────────────────────┤
│ [Open rota]        [Messages]    │  ⑤ Footer
└──────────────────────────────────┘
```

## ① Header (not tappable, except the location filter)
- Venue name, date, and a one-line summary: "9 covered · 2 need you."
- A location filter at top right, defaulting to All. It opens a list of the six sites.
- If nothing needs attention, the summary reads "Quiet night. Nothing needs you." and the screen ends after the footer.

## ② Needs you (always first, expanded)
Sorted by shift start time, soonest first. Each card is one stuck item.

**Unfilled card**
- Shift, role, and site, with a red "UNFILLED" tag.
- Who was asked and how many accepted, e.g. "Asked 14 · 0 accepted."
- Deadline line: the time the agent will act next if nothing changes, e.g. "Agent resumes at 14:00." This tells the GM whether they have to act now or can wait.
- Buttons:
  - **Post to all**: opens everyone opted in, including people who previously declined.
  - **Call list**: opens a list of phone numbers with the reason each person didn't take it.
  - **Cancel shift**: requires a confirm step.

**Overtime card**
- Person, current hours, and projected hours, e.g. "Jordan R. 41.5h → 46h."
- Buttons:
  - **Approve OT**: keeps the swap as proposed.
  - **Next candidate**: swaps in the next opted-in person who stays under the threshold.
- The card can be dismissed with a swipe, but only after one of the buttons has been used.

Tapping anywhere else on a card opens the full thread: staff messages, the agent's reasoning, and the rota before and after.

## ③ Handled overnight (collapsed by default)
- Header shows the count and a short breakdown, e.g. "7 swaps covered · 2 rota edits."
- Tapping the header expands a list, one row per action: "Sam covered Thu lunch for Priya, rota updated."
- Each row is tappable for detail, with an **Undo** button for the first 24 hours.
- Routine items never show buttons on the summary itself.

## ④ This week at risk (collapsed, optional)
- Upcoming shifts that are short-staffed or near overtime, based on the rota as it stands. This is a preview, not a stuck item.
- Each row opens that shift in the rota.

## ⑤ Footer (tappable)
- **Open rota**: the full schedule for the selected site.
- **Messages**: the staff inbox, so the GM can reply to anyone the agent escalated to.

## Design choices to review
- **Stuck items before routine ones.** The GM's time is scarce, and the routine results are only worth checking when something goes wrong.
- **Deadlines on every stuck card.** Without them the GM can't tell whether to act now or later.
- **Undo only for routine actions.** Stuck items need a decision, not a reversal.
- **Location filter in the header.** Six sites on one list would make the screen too long to scan.
