**Assumption:** Front-desk staff use a desktop or laptop with a mouse and keyboard, all day, every day. The list is about 60 rows, so it fits on one page with light scrolling.

## Selecting

- **Every row has a visible checkbox in a left column.** Use checkboxes because the list scrolls and the staff are picking several rows. A header checkbox selects all rows currently shown. Clicking anywhere else on a row opens its detail panel and does not select it. This stops accidental selections and keeps "look" separate from "act".
- **Shift-click extends a range.** Space toggles the focused row, and Shift+arrows extend the selection. Cmd/Ctrl+A selects all visible rows.
- **Selection applies to what's visible.** The header checkbox selects only the rows that pass the current vet and status filters. If a filter change hides selected rows, they stay selected, and the bar says so: "5 selected (2 hidden by filters)". The bar offers "Show" for those rows and "Deselect hidden". Hidden selections are the main way to act on the wrong appointments, so they must be visible.
- **Selected rows differ by more than color.** The checkbox is checked and the row has a tint. Both cues are announced to screen readers.
- **Selection survives status changes.** Checking in three appointments shouldn't clear the selection, because the next action is often on the same group (for example, check in, then text). The clear control and Esc empty it.

## Where the actions go

- **A bar appears above the table when one or more rows are selected.** It replaces or overlays the filter row, so it stays in view where the staff are already looking. It doesn't float at the bottom of the screen or sit in a side menu.
- **The bar shows the count and clear control on the left, then four visible, labeled buttons:** Send reminder, Check in, Reschedule, Cancel. Each label names what will change, and the count appears in the button or beside it ("Check in 3"). Cancel sits apart from the other three and has no one-key shortcut.
- **Row-level actions also exist.** Each row has a visible "⋯" menu with the same four actions, for the common single-appointment case. They are visible and keyboard-focusable, not hover-only.
- **Actions that don't apply are disabled with a reason, or skipped and counted.** Examples: checking in an already checked-in or cancelled appointment, or sending a reminder to a cancelled one. Prefer skipping and reporting: "Checked in 3. Skipped 1 (already checked in)." Disabling the whole button because one row doesn't qualify blocks the staff for no good reason.

## How each action behaves

- **Check in:** it happens immediately, and the status chips update in place. A toast says "3 checked in" with Undo, which lasts several seconds and is announced politely to screen readers. No confirmation, because it's reversible.
- **Send reminder:** this one reaches owners, and it can't be taken back once sent. So it opens one specific confirmation. The confirmation names the number of owners and shows the message text, and the primary button reads "Send 4 texts". The confirmation also notes any appointments skipped, for example for missing phone numbers or a reminder already sent today. The message template is remembered, and editing it is a link in the confirmation, not a separate step. If you build a short send delay with Undo, it can replace the dialog.
- **Reschedule:** this needs a decision, so it opens a panel. The panel offers a date and time, or "move all by N minutes/days", with the vet kept by default. It shows the new times before applying, and conflicts are flagged in place. Rescheduling several appointments to one exact slot rarely makes sense, so the multi-select version should be a shift ("later by…") or one-at-a-time stepping. Applying it gives a toast with Undo. Whether to also text the owners is a checkbox in the panel, and it remembers the last choice.
- **Cancel:** this is destructive to the schedule and may notify owners. Use one confirmation that names the count and the pets or owners ("Cancel 3 appointments: Biscuit, Mochi, Pepper?"), with a "notify owners" checkbox. Once confirmed, the appointments are marked cancelled rather than removed, and a toast with Undo follows, so they can be restored. If an owner was already texted, the message says so, since that part can't be undone.

## Keeping it fast

- Cmd/Ctrl+Enter confirms the open dialog. Esc closes dialogs, and if none is open, clears the selection.
- Filters (vet, status) show as removable chips with a result count. They're remembered between sessions.
- Zero results names the filters that caused it and offers one click to relax them.

## Why this shape

The staff pick a group, then do one of four things. A bar tied to the selection keeps the actions where the eyes are and says exactly what will change. Reversible actions run and offer Undo. Only the actions that notify other people, sending a text or cancelling, get a specific confirmation, so those dialogs stay rare and people still read them.
