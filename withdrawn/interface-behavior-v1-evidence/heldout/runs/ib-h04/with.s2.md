**Assumption:** Front-desk staff use a desktop or laptop with a mouse and keyboard. They work in this view all day, so they're past the first week. About 60 rows fit on one scrolling page, so there's no paging.

## Layout

- **Filters** (vet, status) sit above the table as controls with removable chips and a result count, such as "Dr. Lee · Not checked in · 14 appointments". They're remembered for the session.
- **The table** has a checkbox in every row, plus a "select all" checkbox in the header. Each row shows time, patient and owner, vet, reason and status.
- **The action bar** appears when at least one row is selected. It sits in a sticky strip pinned to the top of the table, so it stays visible while scrolling. It's not at the bottom of the page, because 60 rows scroll away from it.
- **A detail panel** can open beside the list when a row is clicked. It holds the single-appointment view, so the table never navigates away.

## Selecting

- **Checkboxes** add and remove rows. Shift-click on a checkbox selects a range, which is the fast way to take "everything from 9:00 to 11:00."
- **Clicking a row** opens its detail panel and doesn't select it. This keeps "look at this one" and "act on several" as separate gestures, so no gesture means two things.
- **Selected rows** get a tint and a checked box, so color isn't the only cue.
- **Header checkbox** selects all rows matching the current filters, not all 60. The bar says so: "14 selected (all matching filters)".
- **Changing a filter** keeps the selection, but rows that are now hidden are dropped, and the count always matches what's visible. Staff never act on rows they can't see.
- **Keyboard:** arrows move focus between rows, Space toggles the checkbox, Shift+Space or Shift+arrows extend the range, and Esc clears the selection.

## The action bar

When rows are selected, the bar shows the count on the left ("5 selected"), then the actions, then a "Clear" control. The actions are:

- **Send reminder**
- **Check in**
- **Reschedule**
- **Cancel appointment**

Each action is a labeled button that always names its target, and none are hidden in a "More" menu. Actions that don't apply to some of the selected rows are handled in the open, not by silently skipping those rows. If you select 5 rows and 2 are already checked in, "Check in" changes to "Check in 3" and a short note says "2 already checked in." If an action applies to none of the rows, its button is disabled and says why on focus or hover.

## What each action does

Texts to owners can't be recalled, and cancelling and rescheduling affect other people. Those get different treatment from check-in, which is easily undone.

| Action | Behavior | Recovery |
|---|---|---|
| **Check in** | Applies immediately. Status badges update in the rows. | Toast: "5 checked in · Undo". |
| **Send reminder** | Opens a small preview: the message text, the number of owners, and a list of any owners with no phone number, who are skipped. One **Send 5 texts** button. | Texts can't be unsent. This one confirmation is justified, and it names the recipients. Rows get a "reminded" mark afterward. |
| **Reschedule** | Opens a panel, since each appointment needs a new time. It can offer "move all by X" or pick a new slot per row. It applies only after the staff member confirms the new times. | Toast with Undo that restores the old times. Owners are notified only if the staff member chose that in the panel. |
| **Cancel** | One specific confirmation: "Cancel 3 appointments for Dr. Lee? Owners will not be notified unless you tick this." Confirm button reads "Cancel 3 appointments". | Toast with Undo that restores the slots, as long as nothing else has taken them. If it can't restore a slot, the toast says which one. |

Cancel gets no one-key shortcut and is styled as the danger action. It sits last in the bar, away from Check in, so a mis-click is less likely.

## After an action

- The rows update in place, and the selection **clears** for Check in and Cancel because those rows are done. After Send reminder, the selection stays so the staff member can follow up with Check in.
- Success never opens a dialog. The only feedback is the updated status badges and a polite live-region announcement for screen readers.
- **Partial failure** is reported in place: "4 of 5 texts sent. 1 failed: Rosie (Hart)". The failed row stays selected and gets a Retry.

## Edge cases

- Filtering to a status, such as "Not checked in", then "select all" then "Send reminder" is the main flow. It should take two clicks plus one Send.
- On a touch screen, the same checkboxes work, and the bar becomes a bottom-anchored strip.
- If another staff member changes a selected appointment while it's selected, its row shows a "changed" marker. The action then skips it and says so.

## Open question

Do owners get notified automatically on Cancel and Reschedule? I assumed it's a choice made at the time. If the clinic has a standard policy, that choice should become a remembered default shown next to the checkbox.
