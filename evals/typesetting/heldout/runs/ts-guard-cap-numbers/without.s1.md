The numbers are almost certainly left-aligned or in a proportional font, so the digits and decimal points don't line up.

Fix:
- Right-align the column (`text-align: right`).
- Use tabular digits (`font-variant-numeric: tabular-nums`).
- Always show two decimals.

If it's still off, check for stray whitespace or mixed formatting in the cells.
