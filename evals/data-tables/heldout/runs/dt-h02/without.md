Here's what I'd change, roughly in order of impact.

**1. Reorder the columns**
Put the identifying and decision-relevant fields first: **Name, Employee ID, Department, Hire date, Salary, Phone, Notes**. Managers scan by person and department, and Phone and Notes are lookup fields that belong at the end. Freeze the Name column so it stays visible if the table scrolls horizontally.

**2. Align cells by data type, not center**
Centering everything makes columns ragged and hard to compare.
- Name, Department, Notes, Phone: left-aligned.
- Salary: right-aligned, so digits line up.
- Hire date and Employee ID: left-aligned. Use a monospace or tabular-nums font for the ID.
- Headers use the same alignment as their column.

**3. Format salary consistently**
`85000`, `102500.5` and `67k` can't be compared or sorted. Fix it at the data layer first, by storing a number and rejecting or normalizing `67k` to 67000. Then display it uniformly, e.g. `$85,000`, `$102,501` or `$102,500.50`. Pick one precision, use thousands separators, include the currency, and right-align with `font-variant-numeric: tabular-nums`.

**4. Add sorting, then filtering and search**
Sorting is probably the main complaint.
- Click-to-sort headers with an arrow indicator and `aria-sort`.
- Default sort by Name.
- Sort dates and salaries by their real values, not as strings.
- A search box for name or ID, and a department filter dropdown.
- Optionally, a sticky header and pagination or virtual scrolling for long rosters.

**5. Fix the header styling**
Dark gray on black has very poor contrast, probably under 3:1, and it fails WCAG. 11px bold uppercase makes it worse.
- Use a light background (or white text on dark) with at least 4.5:1 contrast.
- Go up to 12–13px, in sentence case or lightly tracked caps. Keep the weight at semibold.
- Make the header visually distinct from the body with a subtle background and a bottom border.

**6. Lighten the borders**
A 1px black border on every cell is heavy and noisy. Use horizontal row dividers only, in a light gray such as `#e5e7eb`. Add zebra striping or a row hover highlight, and enough padding (about 8–12px vertically) to make rows scannable.

**7. Handle Notes and Phone**
- Notes can be long, so truncate with an ellipsis, a fixed max width and a tooltip or expandable row, so one note doesn't stretch the row height.
- Normalize phone numbers to one format, e.g. `(555) 123-4567`, and make them `tel:` links.

**8. Standardize hire dates**
Use a single unambiguous format such as `2021-03-15` or `Mar 15, 2021`. Avoid `03/04/21`, which is ambiguous between US and other conventions. Store the value as an ISO date.

**9. Accessibility and semantics**
Use a real `<table>` with `<thead>`, `<th scope="col">` and a caption. Make the sort controls buttons that work from the keyboard, with visible focus states.

**If you can only do three things:** add sorting and search, fix the header contrast, and normalize the salary format. Those address usability, readability and data quality directly.

If you share the code or the framework (plain HTML, React, a grid library), I can make these changes directly.
