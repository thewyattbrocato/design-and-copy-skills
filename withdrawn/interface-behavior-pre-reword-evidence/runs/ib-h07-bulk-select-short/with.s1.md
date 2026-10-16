Assumed: desktop, finance staff, daily use.

- **Checkboxes:** Show them on every row. Shift-click selects a range, and the header checkbox selects the current page.
- **Selection bar:** Once a row is selected, show a bar with the count and the actions "Mark paid" and "Send reminder".
- **Select all:** After a page-select, offer "Select all 4,000 matching filter". Selection should follow the filter, not the page, and it should survive paging.
- **Mark paid:** Run it immediately and show an Undo toast. Money records aren't moved, so undo is enough.
- **Send reminder:** Emails can't be unsent. Confirm once, naming the count and the recipients.
- **Mixed selections:** Skip invoices that are already paid, and say how many were skipped.
- **Keyboard and screen readers:** Every selection route works from the keyboard, and the count is announced.
