**Assumption:** Desktop, finance staff using this regularly.

- **Checkboxes:** Show a visible checkbox on every row, with shift-click for ranges and keyboard support. Add a header checkbox that selects the current page.
- **Select all:** When the header box is ticked, show "20 selected. Select all 4,000 matching this filter." Selection follows the active filter, not the whole table. This avoids paging through 200 pages.
- **Persistence:** Selection survives paging, sorting and scrolling. A sticky bar shows the count, the actions (Mark paid, Send reminder) and Clear.
- **Mark paid:** Do it immediately and show a toast with Undo, because it's reversible. Announce the toast to screen readers.
- **Send reminder:** Ask for one specific confirmation, such as "Email 38 customers?", because a sent email can't be undone. Skip invoices where the action doesn't apply, and say so ("5 already paid, skipped").
- **Long runs:** Process large batches in the background with progress, and list any failures afterward.
