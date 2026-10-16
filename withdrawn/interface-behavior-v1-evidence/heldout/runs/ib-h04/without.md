## Recommended design: checkbox column plus a contextual action bar

**The list**
- Each row has a checkbox in the leftmost column. The header has a select-all checkbox with three states: none, some (indeterminate) and all.
- Clicking anywhere on a row's blank space does not select it. Rows may open details on click, so selection stays an explicit act. Only the checkbox, or Space on a focused row, toggles it.
- Shift-click selects a range, which is useful for "everyone in the 9–11am block." Cmd/Ctrl-click isn't needed because checkboxes already allow multiple picks.
- At about 60 rows, the list is one scrolling page with no pagination. Select-all means all rows that match the current filters, and the bar says so: "Select all 14 shown."

**Where the actions go**
- When nothing is selected, the area above the table shows only the filters (vet, status).
- When at least one row is selected, an action bar replaces the filter row, or sits directly above the table and stays sticky while scrolling. It shows:
  - "5 selected" and a Clear link
  - **Send reminder**, **Check in**, **Reschedule** and **Cancel** as buttons with text labels
- The actions are in one place and not repeated on every row. That keeps the rows clean and makes it clear that the actions apply to the whole selection.
- Rows may still have a single-appointment shortcut, such as an overflow menu. Staff often act on just one appointment, and this avoids "tick box, then reach up to the bar."

**Selection and filters**
- Changing a filter does not silently keep hidden selections. The simplest rule is that a filter change clears any selected rows that are no longer visible, and the bar's count always matches what's on screen. Staff should never act on appointments they can't see.
- Status changes (e.g. after check-in) leave the rows selected unless they drop out of the filter. If they drop out, they're removed from the selection.

**Applying actions**
- Some actions don't fit every selected row, so the bar handles that explicitly:
  - **Check in** applies only to appointments that aren't already checked in or cancelled.
  - **Send reminder** skips appointments that were reminded recently or have no phone number.
  - The confirmation states the effect: "Send reminder to 5 owners (1 skipped: already checked in)."
- **Send reminder** and **Check in** are reversible or low-risk. They run after a single click and show a toast with Undo where possible. Reminder texts can't be unsent, so that one gets a brief confirm dialog listing the recipients and the message.
- **Cancel** is destructive and always opens a confirm dialog with the count and names. It may also offer an option to notify the owners.
- **Reschedule** opens a dialog with a date and time picker. For multiple appointments, it should either move them all by the same offset or step through them one at a time. I'd start with "pick a new date, keep each appointment's time, with an editable time per row," because bulk rescheduling to a single identical time usually collides with the vet's schedule. If it needs to be simpler, limit Reschedule to a single selection and disable it, with a tooltip, when several are selected.
- After any bulk action, the bar shows a result summary ("4 done, 1 failed: no phone number") with failures left selected so staff can fix and retry.

**Other details**
- Keyboard: Tab to checkboxes, Space toggles, Shift+arrows extends a range, and Esc clears the selection.
- Leave the action bar visible with disabled buttons and an explanation, not hidden, whenever an action can't apply to any selected row.

I'd start with this layout. The main thing to check with staff is how Reschedule should behave for multiple appointments.
