# GM morning summary (phone, single scroll)

## 1. Header (fixed at top)
- **Salt Cellar · Tue 27 Oct**
- One sentence that states the night: **"11 swaps handled. 2 need you."** The "2 need you" is bold and colored. If nothing is stuck, it reads **"11 swaps handled. Nothing needs you."**
- Below that is a horizontally scrolling chip row: **All** (default), then the six locations. A location with stuck items shows a small count badge. Tapping a chip filters every section below. This is the only filter.

## 2. Needs you (shown first, only if there are stuck items)
Cards are sorted by how soon the shift starts, not by when the problem happened. A shift tonight outranks one next Thursday.

Each card has:
- **Top line:** location and urgency, e.g. "Harbor · tonight 5pm" (red if under 24h).
- **The shift:** "Dana K., server, Fri dinner" and "was asking to drop: sick".
- **The problem in plain words:**
  - *Nobody accepted:* "Asked 8 people, 5 no reply, 3 declined."
  - *Overtime:* "Only taker is Sam R., which puts Sam at 43h (3h over)."
- **Buttons on the card**, so the GM can resolve it without leaving the screen:
  - *Nobody accepted:* **Widen to other locations** (primary), **Call/Text [manager on shift]**.
  - *Overtime:* **Approve overtime** (primary), **Find someone else**.
- **Tapping the card body** opens the detail view (below).

After a button is tapped, the card collapses to a one-line confirmation ("Approved, Sam R. is on Fri dinner") with **Undo** for a few seconds. It then drops down into Handled.

## 3. Waiting on replies (only if any)
These are offers still out that haven't failed yet, so the GM knows what might become a problem. Each row is one line: "Harbor · Sat lunch · 4 asked · decides by 2pm". Tapping a row opens the detail view. There are no action buttons here, because the agent is still working on them.

## 4. Handled overnight (collapsed by default)
- A single row: **"Handled (11) ›"**. Tapping it expands the list.
- Expanded, the rows are grouped by location (or just the filtered one). Each row is one line: "Maria → Jo · Fri dinner, line · Harbor".
- Tapping a row opens the detail view.
- The list is collapsed because these are routine. The count is the reassurance and the detail is available if wanted.

## Detail view (pushed screen, back arrow top-left)
- Shift, who dropped it and why (their original message, quoted).
- **Timeline:** who the agent messaged, when, and each response. For handled swaps, it also shows what changed on the rota.
- **Hours impact** for the person covering (this week's total before and after).
- Actions at the bottom: **Message [person]**, **Open in rota**, and for handled swaps **Reverse this swap**.

## Edge cases
- **0 things overnight:** the header says "Quiet night. No swap requests." The rest of the screen is empty. No empty section headers.
- **15 things:** Needs you is never truncated. Handled stays collapsed, so the screen stays short regardless of volume.
- **Multiple stuck items at the same location:** they stay as separate cards. Don't group them, because each needs its own decision.

## Footer
A small link, **Agent settings** (opt-in pool, overtime threshold, how far ahead it will offer shifts). It's at the bottom because it's rarely used.

## Reasoning
The GM's first question is whether they need to do anything. So the count of stuck items goes in the header, and the stuck items come first with the action on the card. Routine swaps are one tap away for anyone who wants to audit them.
