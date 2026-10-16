Assumed: desktop, daily use by accounting staff.

- **Checkboxes:** Show a visible checkbox on every row. Shift-click selects a range, and Space toggles the focused row.
- **Select all:** The header checkbox selects the current page. A banner then offers "Select all 4,000 matching," which is scoped to the active filters.
- **Persistence:** Selection survives paging, sorting and filtering. An action bar shows the count, "Mark paid" and "Send reminders," plus Clear.
- **Ineligible rows:** Skip invoices that are already paid, and say how many were skipped.
- **Mark paid:** Run it immediately and show a toast with Undo, because it's reversible.
- **Reminders:** Reminders can't be unsent. Confirm once, naming the count and recipients, or add a short send delay with a cancel option.
- **Large batches:** Run them in the background with progress, and report any failures per invoice.
