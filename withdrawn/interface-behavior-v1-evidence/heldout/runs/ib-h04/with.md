**Assumption:** Front-desk staff use a desktop or tablet with mouse or touch, all day, with a few dozen to a hundred appointments in view. They are past their first week. About 60 rows fit on one scrolling list, so there's no paging.

## Selecting

- **Every row has a visible checkbox in a left column.** Checkboxes say "many" and still work after scrolling. Clicking the row itself opens the appointment in a side panel and doesn't select it. This keeps "look at this one" apart from "act on several."
- **Shift-click extends a range. Ctrl/Cmd-click toggles single rows.** On a keyboard, Space toggles the focused row and Shift+arrows extends the selection. Checkboxes cover touch.
- **The header checkbox selects every row that matches the current filters.** It does not select hidden rows. Its label says so, for example "Select all 14 shown." With three states (none, some, all), it also works as a clear control.
- **A selected row differs by more than color.** It gets a checked box plus a tint or edge marker.
- **Changing a filter keeps the selection, but the bar counts hidden rows.** For example: "5 selected (2 hidden by filters)." It has a "Show/clear hidden" link. Silently acting on rows the person can't see is the one real danger here. If someone filters to Dr. Lee, selects three, then switches to Dr. Park, they should see what is still selected.
- **Esc clears the selection.**

## Where the actions go

- **A bar appears when at least one row is selected.** It sits pinned at the top of the list, above the column headers, and replaces the filter row's empty space instead of overlaying rows. Pinning keeps it visible while the list scrolls, and it doesn't cover the rows being worked on.
- **The bar shows the count, the four actions and a Clear control.** For example: "3 selected · Send reminder · Check in · Reschedule · Cancel · Clear". All four are visible labeled buttons. At this volume, nothing should hide in an overflow menu.
- **Row-level actions stay available too.** Each row has a visible "⋯" menu with the same four actions, so one-off work doesn't need a checkbox. These controls are visible and keyboard-focusable, never hover-only.
- **Actions that don't apply are disabled, with a reason on focus or hover.** "Check in" is disabled for cancelled appointments. When only some of the selected rows qualify, the button states the number it will act on ("Check in 2 of 3"), and the other rows are skipped and named afterward. The bar says exactly what will change.

## How each action behaves

| Action | Behavior | Why |
|---|---|---|
| **Check in** | Applies at once. A toast says "3 checked in" with **Undo**. Status badges update in place. | It's reversible and used constantly, so no confirmation. |
| **Send reminder** | Opens a small preview: message text, recipient count, owners with no phone number flagged. One **Send** button. Remember the last template. | A text to owners can't be recalled, so this gets the one specific confirmation. It names the recipients and doesn't just ask "Are you sure?" |
| **Cancel** | Applies at once and the rows move to Cancelled. The toast says "3 cancelled" with **Undo**. Notifying owners is a separate, unticked-by-default option, or a follow-up offer after the cancel. | The cancel is reversible. Anything sent to owners is not. |
| **Reschedule** | Opens a side panel. For several selected appointments, it asks for a shift (same time on another day, or move by N minutes) and shows each row's new slot with conflicts flagged. Nothing changes until **Apply**. | Rescheduling needs input per appointment and can collide with other bookings, so it can't be a one-click action. |

After any action:
- **The selection clears,** except when part of the batch failed. Then only the failed rows stay selected and an inline message says why.
- **The toast is announced to screen readers** through a polite live region. It stays long enough to read and has an Undo that works from the keyboard.

## Open points
- If bulk cancel should always notify owners, make that the default instead. I assumed not, since it's the outward-facing part.
- I assumed reminders go out by text only, with no per-owner opt-out. Confirm that, because opt-outs would add a skipped-recipients line to the preview.
