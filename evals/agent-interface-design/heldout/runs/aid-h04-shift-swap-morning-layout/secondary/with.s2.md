**Assumption:** the GM is one person who sees all six locations. Each action is reversible until the shift starts (the undo window is a placeholder, [X hours]). Messages already read by staff can't be unsent, so the screen says that plainly.

## The screen, top to bottom

**1. Status bar (always visible, not scrollable)**
- "Salt Cellar · Shift cover · Tue 4 Nov"
- "Ran 02:00–05:40 · 9 actions · 2 need you"
- A green **Running** chip. If paused, a yellow **Paused since [time]** banner replaces it.
- Tap the chip: **Pause** / **Resume**. Pause is one tap from the top of the screen.
- Location filter chips: **All · Oak St · …** (tap to narrow every section below).

**2. Needs you (only shown when present; always expanded; sorted by shift start)**
One card per stuck item:
- Title: "No one has accepted Fri 6 pm Line Cook, Oak St"
- Detail: "Offered to 4 people, no reply. Shift starts in 31 h."
- Buttons: **Offer to more people** · **Assign myself** · **Leave open & tell staff**

Overtime variant:
- Title: "Cover found, but Dana would pass 40 h this week"
- Detail: "Priya accepted Sat lunch. Covering it puts Dana at 42 h."
- Buttons: **Approve overtime** · **Find someone else** · **Hold**

Tapping the card opens the full thread and the rota diff.

**3. Concerns (only when a trend is heading toward a limit)**
- Example: "Oak St has had 3 cover requests this week; 2 went unfilled. Keep watching?"
- Tap: detail view with the trend and what the agent is doing about it.
- Buttons: **Look closer** · **Dismiss for this week**

**4. Covered overnight (collapsed by default; one digest line)**
- Summary row: "7 covered · tap to review" (no total without items).
- Expanded list, doubtful items first:
  - "Sat 12 pm Front of House, Brighton: covered by Marco (accepted 23:14). Low confidence: Marco swapped twice this week."
  - Routine rows below: "Mon 5 pm Bar, Eastside: covered by Ana (accepted 22:02)."
- Each row is tappable and opens:
  - **Undo** (available until [X hours] or shift start, whichever is first)
  - **Not this one** (optional: just this shift, or this week)
  - **Always / never for this kind** (shows the resulting rule in plain words before saving)
- Batch button at top: **Undo all covered tonight**.

**5. Skipped and not acted on (collapsed; low-confidence first)**
- Example: "Wed 6 pm Host, Oak St: request received, no eligible cover, no action taken."
- Tap a row for the same **Not this one / Always or never** choices. This is where missed actions get noticed.

**6. Suggestions (rare; hidden when empty)**
- Shown only when the agent has a strong case, e.g. "Staff at Brighton accept Sunday cover 90% of the time; add Sunday to the opt-in list?" Tap **Accept** or **Not now**, with a per-kind **Turn off suggestions**.

**7. Footer**
- "Last check 05:40 · Next check 02:00 tomorrow" (proof the agent is alive when nothing happened).
- **Rules** (opens the standing instruction restated in plain words, with three example cases the agent would act on, and a **Change** button).
- **Staff opt-in list**.
- **Notifications**: separate off switches for problems, concerns, digest, suggestions, check-in. Each kind has a frequency setting.
- **Turn off agent** (no reason asked; the screen says what happens to open requests and past actions).

## Notification rules that shape the screen
- Only "Needs you" items push a notification in the morning. Everything else waits in the digest.
- The digest arrives at a time the GM picks.
- A total ceiling applies to pushes per day.

## Things to confirm before going live
- The undo window length and whether it's shorter than the shortest notice time.
- Whether staff offers go out automatically (current design: yes, within caps) or wait for GM approval for overtime cases (current design: yes, always).
