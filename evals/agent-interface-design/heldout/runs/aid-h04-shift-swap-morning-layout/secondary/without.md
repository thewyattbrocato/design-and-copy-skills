# Morning summary screen (phone, single scrolling view)

The screen is ordered by what needs a decision, then what the agent already finished. Nothing requires scrolling to find a stuck item.

## 1. Header (fixed at top)
- **Date and time of last run**, e.g. "Tue 27 Oct · updated 6:02am"
- **Location filter**: a horizontal chip row, *All · Harbor St · …* (six chips). Tapping a chip filters every section below. Default is All.
- **One-line headline**, e.g. "12 swaps handled · 2 need you." If nothing needs them: "12 swaps handled. Nothing needs you."

## 2. Needs you (always first, hidden if empty)
One card per stuck swap, sorted by shift start time, soonest first, because the earliest deadline is the most urgent. Each card shows:
- **Shift**: role, location, date, start–end time (e.g. "Line cook · Harbor St · Fri 27 · 5–11pm")
- **Why it's stuck** in one sentence, one of two types:
  - *No taker:* "Offered to 9 opted-in staff, no acceptances. Last offer sent 11:48pm."
  - *Overtime:* "Covering puts Dev at 43.5 hrs this week. Overtime cost ≈ $68."
- **Action buttons**, specific to the stuck type:
  - *No taker:* **Widen search** (adds other locations or cross-trained staff, shown as a count before sending), **Call list** (opens the contact list with tap-to-call and tap-to-text per person), **Cancel shift** (confirm dialog required).
  - *Overtime:* **Approve OT** (confirm dialog shows the hours and cost), **Pick another** (opens a ranked list of alternates, each with their weekly hours), **Cancel shift**.
- **Tap the card body** to expand: the candidate list the agent tried, with each person's response (declined, no reply, not available) and a link to the rota.

The agent never approves overtime or cancels a shift on its own. Those are always taps by the GM.

## 3. In progress (hidden if empty)
Swaps the agent is still working on, usually ones waiting on a reply or a cutoff. Each row shows the shift, the status ("Waiting on 3 replies, cutoff 10am"), and a **Take over** button that moves it into Needs you early. These rows are not tappable into the chat log.

## 4. Done overnight (collapsed by default)
- **Header row**: "9 covered, rota updated" with a chevron to expand.
- **Expanded**: one row per completed swap, newest first. Each row reads "Maria → Dev · Fri 5pm line cook · Harbor St," with a small tick for a confirmed rota update.
- **Tap a row** to open a detail sheet with the message thread summary, the rota before/after, and an **Undo** button (confirm dialog, then the agent reverses the rota change and notifies both staff).

Sub-group by location only if the chip filter isn't enough; I'd start without it.

## 5. Footer
- **Notifications off/on** toggle for the morning digest? Probably not needed here, so I'd skip it.
- **Ask the agent** text field for questions like "why did Sam's swap fail?" This is optional for v1.

## Interaction rules
- **Every row and card is tappable**; no tap leads to a dead end.
- **Destructive or cost-bearing actions** (Approve OT, Cancel shift, Undo) always show a confirm dialog with the consequence written out.
- **Counts before lists**: the headline and section headers carry the numbers, so the 0–15 range never makes the screen long on a quiet night.
- **Empty states**: zero swaps shows "Quiet night. No swap requests." and hides the empty sections.

## Assumptions to confirm
- Overtime is a per-person weekly threshold you can configure. If the rule is per-location or per-pay-period, the card text changes but the layout doesn't.
- Staff reply via the agent's messaging channel, so "Call list" is a fallback rather than the main path.
- The GM is the only person who sees this screen. If shift managers also need it, they'd need the same screen filtered to their location.
