The numbers are probably left-aligned (the default) and set in a proportional font, so the digits and decimal points don't line up.

Fix it with:
- Right-align the column: `text-align: right`.
- Use tabular digits: `font-variant-numeric: tabular-nums`.
- Always show two decimal places.

If you share the table's code, I can make the change.
