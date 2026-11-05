# Morning shift-swap summary (phone)

The screen answers two questions in order: **do I need to do anything?** and **is anything about to go wrong today?** The routine items come after that and are collapsed.

## 1. Header (fixed, small)
- "Shift swaps, Tue 27 Oct" with the overnight window (e.g. "6pm to 7am").
- A one-line verdict in plain words, which is the only thing some mornings will need:
  - **"2 need you. 9 handled."**
  - Or, on a quiet night, **"All 6 handled. Nothing needs you."**
- Tapping the date opens a picker for earlier days.

## 2. Needs you (top, visually distinct, only shown if non-empty)
One card per stuck item, sorted by **how soon the shift starts**, so tonight's shift comes before Saturday's. Each card shows:
- The location and shift, e.g. "Harbour St · Line cook · tonight 5pm". Put "tonight" or "in 6 hrs" in a badge, since urgency is the sort key.
- Who asked to swap, and the reason it's stuck, in one line:
  - "Asked 11 people over 9 hrs. No one accepted."
  - Or "Dana could cover, but it puts her at 46 hrs (limit 40)."
- **Primary button:** the most likely action for that stuck type.
  - For no takers: **"Widen the ask"** (include other locations or non-opted-in staff, if you allow that).
  - For overtime: **"Approve overtime"**.
- **Secondary buttons:** "Offer to someone else…" (opens a list of candidates with their hours this week) and "Call [requester]" (a phone link).
- Tapping the card body opens the detail view (section 5).

Buttons that act on the rota show a confirm step with the cost or consequence ("Dana to 46 hrs, +6 hrs OT").

## 3. Coming up (conditional, only if relevant)
Anything handled but fragile, such as a swap that was accepted but not yet confirmed by the covering person, or a cover who is on a close-then-open turnaround. This section is short, at most 2 or 3 lines. If nothing applies, drop it.

## 4. Handled overnight (collapsed by default)
- A single row: **"9 swaps handled ›"**.
- Tapping it expands a compact list grouped by location. Each line reads "Sam → Priya · Fri dinner · Harbour St".
- Each line is tappable to open the detail view. Nothing in this list needs action.
- A small filter chip row at the top of the expanded list ("All locations / Harbour St / …") helps with six sites. Don't show it until the list is expanded.

## 5. Detail view (pushed screen from any item)
- A timeline of what the agent did: who it messaged, when, and who replied or didn't.
- The rota change, before and after.
- For stuck items, the action buttons from section 2 appear again here.
- A "Message staff member" link.
- A "Undo this swap" link on handled items, with a confirm step.

## 6. Footer (quiet)
- "Agent settings ›": the overtime threshold, who it may ask, and how long it waits before it escalates.
- "Report a wrong swap": a lightweight way to flag a mistake so you can trust the agent over time.

## Design notes
- **Zero-state matters most.** Most mornings will be 0 to 2 stuck items, so the "all clear" state should feel complete, not empty.
- **Don't count routine items as alerts.** No red badges on them, and no push notification for handled swaps.
- **Push only for urgent stuck items overnight,** for example a shift starting within a few hours with no cover. Everything else waits for the morning screen.
- **Keep the numbers honest.** If the agent sent a message that no one has read yet, show that as "No reply yet", not "declined".

If you tell me how the GM currently handles stuck swaps (phone calls, a group chat, the rota app), I can adjust which button is primary on each card.
