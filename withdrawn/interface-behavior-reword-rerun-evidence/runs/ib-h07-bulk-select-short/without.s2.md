Use checkbox selection with explicit scope levels:

- Row checkboxes, plus a header checkbox that selects the current page.
- After selecting a page, show a banner: "50 selected. **Select all 4,000 matching invoices**."
- "Select all" should store the filter criteria, not 4,000 IDs, so it stays correct across pages. Allow deselecting exceptions.
- Keep a sticky action bar showing the count.
- Confirm bulk actions with a summary (count and total amount), process them asynchronously, and report per-invoice failures.
- Encourage filtering first, for example "overdue".
