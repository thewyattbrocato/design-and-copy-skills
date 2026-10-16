Here is what I'd do, roughly in order of payoff. None of it needs a redesign.

**1. Cut the columns people see by default**
- Add a column chooser and ship sensible defaults. Show about 8–12 columns, such as the panels or tests clinicians check most often.
- Let users save column sets as named views, for example "Metabolic panel" or "CBC". A preset per panel often fixes the problem on its own.
- Drop internal ids and fields nobody reads.

**2. Order and group the columns**
- Put the identifying columns first (patient or sample, collection date). Then group related analytes together, with the status or action column last.
- Add a spanning header over groups of three or more related columns, such as "Liver panel". It lets people find a section without reading 40 headers.

**3. Keep context while scrolling**
- Freeze the header row and the first identifying column. This matters most for a wide table.
- Add a visible cue (a shadow or fade) that more columns sit off-screen.

**4. Make abnormal results stand out**
- Flag out-of-range values with a word or symbol (H, L, "critical") and use color only as a third cue. Don't rely on color alone, and don't color every normal value.
- Keep reference ranges and units out of the cells. Put the unit once in the header and the range in a tooltip or an expandable row.
- Consider a "show abnormal only" filter. For 40 columns it is probably the single most useful one.

**5. Format the numbers consistently**
- Right-align numeric columns and use tabular figures (`font-variant-numeric: tabular-nums`).
- Use the same decimal places within each column, matched to the assay's precision.
- Use a dash for "not tested" and "n/a" for not applicable. Never leave a cell blank or show 0 for a missing result.

**6. Add sorting and filtering where they help**
- Sort only the columns people actually sort by, and show the direction on the active column.
- Add a filter by date range, panel, or abnormal status. Show a clear "no results" state with a way to reset the filter.

**7. Reduce the scanning effort**
- Use one light row-separation device (hairlines or zebra striping, not both). Zebra striping is fine on a wide table because it helps the eye follow a row.
- Use rows of 32–40px for an expert tool, with text at 14px or larger. Tighten the padding rather than shrinking the text.
- Add a row-hover or focus highlight.

**8. Consider flipping the axes**
Lab results are often easier to read with tests as rows and dates as columns, which is the usual trend view. If users compare one patient over time, offer that as a toggle. This is the biggest change here, and it may not fit your data model.

**9. Handle small screens**
Don't squeeze 40 columns onto a phone. Use priority columns with the rest in an expandable row, or a scroll region with a frozen first column.

**10. Keep the markup accessible**
Use a real `<table>` with `<caption>`, `<th scope>`, and `aria-sort` on the sorted header. Row actions should be reachable by keyboard.

**Where I'd start**
Items 1, 3 and 4 (column chooser with saved views, frozen header and first column, abnormal flags with an abnormal-only filter) are usually the biggest wins for the least work.

If you share the table's code or a screenshot, I can turn this into specific changes.
