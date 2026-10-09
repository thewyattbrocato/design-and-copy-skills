No, don't narrow the grid. The 60–75 character guideline applies to **prose**: paragraphs of running text, where long lines make it hard for the eye to find the next line. A 14-column inventory grid is tabular data, and people use it differently. They scan across a row and compare values down a column.

Capping the grid at 70 characters would hurt usability:
- It would force horizontal scrolling or truncated columns.
- It would push key fields (quantity, reorder point, supplier) out of view.
- It would make cross-column comparison harder.

What to do instead:
- Let the grid use the full width.
- Pin the SKU/name columns so they stay visible when scrolling.
- Set sensible column widths, and use row banding or hover highlighting to help the eye track across a row.
- Apply the 70-character cap only to prose, such as help text, descriptions, notes, and empty-state messages.
