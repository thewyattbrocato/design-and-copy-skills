Use per-row checkboxes plus a header checkbox that selects the current page. Once the page is selected, show a banner: "25 selected. Select all 4,000 matching invoices?" Selection should track the filter or query, not just row IDs, so "select all" works across pages.

Keep selection when paging. Show a sticky action bar with a count and the actions "Mark paid" and "Send reminders".

Before a bulk action runs, confirm it with the count and a summary. Run it as a background job and report any failures. Mark-paid should be undoable.
