## Selecting

- **Checkbox column on the far left.** Clicking the checkbox toggles selection. Clicking elsewhere on the row opens the appointment detail, so staff don't select by accident.
- **Header checkbox selects all rows currently shown.** It's tri-state (none, some, all). With vet and status filters applied, "all" means the filtered rows only. At about 60 rows everything fits on one page, so there's no "select all across pages" step.
- **Shift-click selects a range.** Staff can grab a block, such as all of Dr. Lee's 9–11am appointments, in two clicks. Space toggles the focused row for keyboard users.
- **Selection survives filter changes, but actions only apply to visible rows.** If staff select 5 rows and then switch the vet filter, the bar says "3 selected · 2 hidden by filters" with a "Clear hidden" link. Hidden rows never get acted on silently, which matters most for Cancel.
- **Selected rows get a clear highlight.** Selection must not depend on color alone, so the checkbox carries it too.

## Where the actions go

- **A bulk action bar appears when 1 or more rows are selected.** It sits directly above the table, between the filters and the rows, and stays sticky so it's still there while scrolling. With nothing selected it's hidden (or shows a quiet "Select appointments to act on them").
- **Bar contents, left to right:** "N selected", then **Send reminder**, **Check in**, **Reschedule**, a visual gap, **Cancel** (styled as destructive), and **Clear selection** on the far right.
- **Don't duplicate the actions in a per-row menu.** Keep the row-level path (detail view or a small "⋯") for single-appointment work. The bar is only for bulk.

## Handling mixed statuses

Not every action fits every row. A cancelled appointment can't be checked in, and a checked-in patient doesn't need a reminder.

- Each button shows how many selected rows it applies to, e.g. **Check in (4 of 5)**. A tooltip or the confirm step names the skipped ones and why ("1 already checked in").
- If it applies to none, the button is disabled with a reason.
- Staff never have to fix their selection before acting. The action just skips ineligible rows and says so.

## What happens when each action is clicked

- **Send reminder:** Opens a small dialog with the message preview, the recipient count, and any owners with no mobile number on file (those are skipped and listed). One "Send" button.
- **Check in:** Runs immediately with no dialog, because it's low-risk and high-frequency. A toast says "4 checked in · Undo". Rows update in place.
- **Reschedule:** This one doesn't bulk well, since each appointment needs a specific new time. Offer two modes in a dialog: *shift all by…* (e.g. +1 day, or +30 min when a vet is running late), or *step through one at a time*, a queue where staff pick a new slot for each and move to the next. Owners get notified as an optional checkbox.
- **Cancel:** Always confirms. The dialog lists the affected pet and owner names and has a "Notify owners" checkbox. The confirm button repeats the count ("Cancel 5 appointments"). It's the only action that requires a typed or deliberate confirm, and it's visually separated from the others to prevent mis-clicks.

## After the action

- A toast summarizes the result. Partial failures (e.g. 2 texts failed) stay visible as a persistent inline notice with a "Retry failed" button, and the failed rows remain selected.
- After a fully successful action, the selection clears. The exception is when staff are likely to chain actions (remind, then check in), so consider keeping it selected after Send reminder only.

## Summary

Checkbox column with range select, a sticky contextual action bar above the table, per-action eligibility counts instead of making staff clean up their selection, no confirmation for check-in, a preview for reminders, and a heavier confirmation for cancel.
