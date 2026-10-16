You can make a lot of progress without a redesign. These are roughly in order of payoff for effort.

**1. Keep orientation while scrolling**
- Freeze the header row and the identifying columns (patient/sample, date). Without this, users lose track of which row and which test they're looking at.
- Keep the header visible during vertical scroll too.

**2. Let users choose which columns to see**
- Add a column picker, with show/hide and reorder.
- Save the choice per user.
- Ship **preset views** such as "CBC", "Metabolic panel", "Liver", and "Abnormal only". Most people only need 5–10 columns for a given task.

**3. Group columns**
- Add a second header row that groups by panel (Hematology, Chemistry, Lipids, ...).
- Make the groups collapsible. A collapsed group can show one summary cell, such as "2 abnormal".

**4. Make abnormal results easy to spot**
- Flag out-of-range values with more than color: an arrow or H/L marker, plus bold for critical values. Color alone fails for colorblind users and in print.
- Keep normal values visually quiet, since most cells are normal.
- Add a filter or toggle for "only rows with abnormal values" and "only columns with abnormal values".

**5. Tighten the cells**
- Put units and reference ranges in the column header or a tooltip, not in every cell.
- Right-align numbers, use consistent decimal places, and use a tabular-figure font.
- Set sensible column widths and use compact row density, with a density toggle.

**6. Add search, sort, and filter**
- Add a jump-to-column search ("type 'creat' to find Creatinine").
- Sort by any column, and filter on value ranges or flags.

**7. Add a detail view for trends**
- Clicking a cell or column header opens a side panel with that test's history, a sparkline, and the reference range. This is often what users are really trying to do when they scan across columns.

**8. Consider a transpose option**
- With 40 tests and few samples, a tests-as-rows layout with dates or samples as columns is often much easier to read. It's also how clinicians are used to seeing lab results. A "flip table" toggle is cheap and works well with frozen columns.

**9. Accessibility and performance**
- Support keyboard navigation and sticky headers that work with screen readers.
- If rows number in the hundreds or more, virtualize the table. Rendering 40 columns multiplies the cost.

**Where I'd start:** frozen headers and ID columns, column presets with a picker, and abnormal-value flagging with a filter. Those three address most "too much to look at" complaints.

Before building, ask a few users which 5–10 columns they use most and what task they're doing when they get frustrated. If it's mostly comparing one patient over time, the trend panel and transpose option matter more. If it's scanning many patients for problems, abnormal filtering matters more.

If you tell me the stack (React, a grid library like AG Grid or TanStack Table, etc.) or point me to the code, I can look at what's feasible and sketch the changes.
