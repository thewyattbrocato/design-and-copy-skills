Assumption: desktop, bookkeeping staff using this daily.

- **Checkboxes:** Show a visible checkbox on every row. Shift-click selects a range, and the keyboard works too (Space toggles a row).
- **Header checkbox:** It selects the current page. Then show a bar: "50 selected. Select all 4,000 matching this filter." Selection is tied to the filter, not the page, so people can narrow to "overdue" first and select everything in it.
- **Persistence:** Selection survives paging, sorting and back-navigation. The action bar always shows the count and a "Clear" button.
- **Actions:** Show the exact count on each button ("Mark 212 paid"). Run the action in the background with progress, and list any failures afterward.
- **Undo:** "Mark paid" gets an Undo toast. "Send reminders" can't be recalled, so it gets one confirmation that names the count and recipients, plus a short send delay.
