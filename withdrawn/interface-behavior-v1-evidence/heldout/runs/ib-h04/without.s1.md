**Recommendation: checkbox column plus a contextual action bar that appears when something is selected.**

**Selecting**
- Each row has a checkbox in a left-hand column. Clicking anywhere else on the row still opens that appointment's detail, so the checkbox is the only thing that selects. That keeps accidental bulk actions unlikely.
- The header checkbox selects all *currently visible* rows, meaning rows that pass the vet and status filters. It shows an indeterminate state when only some are selected. With about 60 rows, everything is on one page, so there's no "select across pages" problem.
- Shift-click selects a range, which is useful for "everyone from 9:00 to 11:00."
- Selection survives changing a filter, but the action bar always shows the true count, e.g. "5 selected (2 hidden by filters)", with a "Clear" link. Hidden selections are the main way people end up texting or cancelling the wrong people. The simpler alternative is to clear the selection whenever filters change. I'd pick that one if staff rarely build a selection across filters, because it's easier to trust.

**Where the actions go**
- When 0 rows are selected, the table looks normal, with no action buttons.
- When 1 or more rows are selected, a bar appears pinned just above the table. It stays visible while scrolling. It shows the count and the four actions: **Send reminder**, **Check in**, **Reschedule**, **Cancel**. Cancel is visually separated from the others and styled as destructive.
- Row-level actions (a "⋯" menu) are unnecessary. A single appointment is just a selection of one, so staff learn one pattern.

**Handling rows an action doesn't apply to**
Statuses will often be mixed, such as already checked in, already cancelled, or completed.
- Keep all four actions visible. Don't hide them.
- On click, the confirmation states exactly what will happen: "Send reminder to 4 owners. 1 skipped (already checked in)." Skipped rows are listed.
- If an action applies to none of the selection, disable it and give the reason on hover.

**How each action behaves**
- **Check in:** applies immediately, with no confirmation. It's low-risk and frequent. Show a toast with **Undo**, and clear the selection.
- **Send reminder:** opens a small confirmation with the recipient count, a preview of the message text, and a Send button. Texts can't be recalled. Flag appointments whose owner has no phone number or has opted out, and skip them.
- **Cancel:** opens a confirmation listing the appointments (time, pet, owner) with an optional "notify owners" checkbox. The button label repeats the count: "Cancel 3 appointments."
- **Reschedule:** this is the odd one out, because several appointments can't sensibly share one new time. Two options:
  - Choose a new date and vet for the group. Then step through the appointments one by one to pick each time slot.
  - Or limit bulk reschedule to a shift of the whole group, such as "move all +1 day" or "same times, different vet."
  
  I'd start with the step-through flow, since it covers the real cases, such as a vet who's out sick.

**After an action**
Rows update in place, and the selection clears, except after a partial failure. Then the failed rows stay selected and the bar says "3 of 4 sent. 1 failed, retry?"

**Keyboard**
Space toggles the focused row's checkbox, and Esc clears the selection.
