---
name: data-tables
description: Use when you build, style or review a table of data in a page, app, document or report - an invoice list, an order or admin table, a comparison of products, a financial statement - covering column order, alignment, number formats, units, missing values, headers and sorting, row separation, density, narrow screens, table markup, and empty or loading states. Not for charts, whole dashboards, page grids, short lists that are not tabular, or editing behavior inside spreadsheet engines.
---

# Data tables

A table is for looking things up and comparing across rows and columns. Make the numbers line up, keep the furniture light, say what each value means, and make the table work on small screens and with assistive technology.

## When to use

- Building or restyling any table: invoices, orders, comparisons, reports, admin lists, financial statements.
- Reviewing table CSS or markup for alignment, number formatting, borders, density or semantics.
- Deciding whether content should be a table at all, or how a wide table should behave on a phone.
- Designing sorting, selection, row actions and the empty, loading and error states of a table.

## When not to use

- Choosing a chart or styling one: use chart-design if installed. If a few values are better read as a shape, say so and switch.
- Arranging tables together with charts and summary figures on a dashboard: multi-chart dashboard layout, outside this skill. This skill covers the table inside it.
- Page grids and columns of layout: use layout-structure if installed.
- General figure styles in running text: use typesetting if installed. This skill applies them inside table cells.
- Inline validation of editable cells: use form-design if installed.
- Interactive widget behavior (menus, dialogs, full keyboard models for data grids): detailed component accessibility work, outside this skill.
- Content that is a short list, a set of steps, or a few label and value pairs (a profile, a settings summary). Do not turn it into a table.
- When a neighbor skill named above is not installed, use ordinary judgment for that part.

An explicit instruction, an existing design system or a platform convention beats every default below. If the user wants gridlines, zebra stripes or centered headers, do it and apply the rest around it. For a one-line fix, use only the check that matters.

## Procedure

Work through these in order and skip what the task does not touch.

1. Confirm that a table is the right form.
2. Order the columns by the reader's task.
3. Align each column by its data type.
4. Format numbers, dates, units and negatives for the decision.
5. Mark missing values.
6. Separate rows with as little furniture as possible.
7. Set density, widths and wrapping.
8. Write headers, and show the sort state.
9. Show status and emphasis in words first.
10. Choose a narrow-screen strategy by task.
11. Use real table markup.
12. Design the empty, loading, error and action states.

## Judgment calls

**Table or not.** Default to a table when people compare across rows and columns or look up exact values. Use cards or a list when each item is read alone, has mixed fields, or carries long text. Use a chart when the point is a trend or a shape rather than exact values. Change when the user asks for a table: build it, and choose the columns so it stays tabular.

**Column order.** Default to the identifying column first, then the values people compare most, grouped by relationship, with the action or status column last. Drop internal ids and fields nobody reads. Change when a convention exists, such as a date column first in a log or a ledger.

**Alignment.** Default to text and dates flush left, numbers right-aligned, or lined up on the decimal point if the count of decimals varies, and each header aligned like its data. Short fixed-width codes and icons can be centered. Never center numbers. Change when a column holds mixed text and numbers: treat it as text. See [references/alignment-and-numbers.md](references/alignment-and-numbers.md).

**Figure style.** Default to tabular lining figures in every numeric column (`font-variant-numeric: tabular-nums`) so digits stack by place value. Change when the face has no tabular figures: set the column in a face that does, rather than leaving it ragged.

**Precision.** Default to the fewest digits that still support the decision, the same in every row of a column. Add thousands separators. Use compact forms (1.2M) only when scanning for magnitude matters more than exact values. Change when the table is a ledger or an invoice that must reconcile: keep the full cents.

**Units and currency.** Default to putting the unit or currency once, in the column header, and leaving cells bare. On a mixed-currency column, keep the code in each cell. In a financial table with a single currency, the first row and the totals can carry the symbol. Change when units differ by row: put them in the cell and align on the number.

**Negatives.** Default to a real minus sign (U+2212) or a leading hyphen, never color alone. Use parentheses when the domain does, such as accounting statements. Keep the convention the same across the table.

**Missing values.** Default to an em dash, or "n/a" for not applicable, with a short note in the caption or footer when the meaning is not obvious. Never leave a cell blank, and never write 0 unless the value is zero. Change when the table has a few possible reasons for a gap: use distinct marks and explain them.

**Row separation.** Default to generous row padding plus a light hairline under each row (or no rules, with space alone). Use a slightly heavier rule under the header and above totals. Pick one device per table. Alternating shading is fine for wide tables where the eye must follow a row across many columns. Change to full gridlines when cells are edited individually, as in a spreadsheet grid, or when the user asks. Add vertical rules only where columns sit dangerously close.

**Density.** Default to rows about 40 to 48px tall for general use and 32 to 36px for expert tools that show many rows, with cell text at 14px or larger (13px at the lowest, and only in compact tables). Change when the table is very large and the reader scans, not reads: tighten the rows, not the text size. Give touch targets inside rows about 44px.

**Wrapping and truncation.** Default to letting one designated text column wrap, and keeping numbers, dates and codes on one line. Truncate only non-critical text, and make the full value available through a title, a tooltip that works on focus, or an expand control. Change when one outlier row would stretch a column for everyone: cap the width and wrap or truncate that column.

**Headers.** Default to short sentence-case labels that name the field and carry the unit. Make headers stay visible when a long table scrolls. Avoid rotated headers; shorten them or let them wrap. Group related columns under a spanning header only when three or more share it.

**Sorting.** Default to sorting only the columns people would actually sort by, with a button inside the header cell. Show the current direction on the active column only, and give the control a name that says the result of activating it. Mark the sorted header with `aria-sort`. Change when the table is short: skip sorting.

**Status and emphasis.** Default to a text label with a small shape or icon, with color as a third cue. Make the weight carry totals, and use one quiet mark for outliers or the best value, labeled when its meaning is not obvious. Do not color every positive number green. Inline bars suit a column where relative magnitude matters; keep the number visible beside the bar.

**Narrow screens.** Default to the strategy that fits the task: a scroll region with a frozen first column and a visible cue for comparison tables; priority columns, with the rest in an expandable row or a details view, for lookup tables; a stacked label and value list for a few fields per row. Never shrink a table until numbers wrap. See [references/responsive-and-accessible-tables.md](references/responsive-and-accessible-tables.md).

**Markup.** Default to a real `<table>` with `<caption>`, `<thead>`, `<th scope>` for column and row headers, and numeric cells marked for styling. Do not use grid widget roles unless the table is a genuinely interactive spreadsheet with cell-level keyboard navigation. A stacked mobile layout should keep the semantics that match what the eye sees.

**Actions and selection.** Default to keeping row actions visible, or revealed on both hover and keyboard focus, in one consistent column or an overflow menu. Show a count with bulk selection. Keep the selection state when the data refreshes. See [references/table-states-and-actions.md](references/table-states-and-actions.md).

**States.** Default to designing four: empty (no data yet, with the next step), no results (a filter removed everything, with a way to clear it), loading (placeholder rows with the real header), and error (what failed, how to retry, existing data kept if any). Say which state the numbers are in when data is partial or stale.

See [references/structure-and-separation.md](references/structure-and-separation.md) for headers, totals, grouped rows, widths and the rule hierarchy.

## Common failures

- Numbers centered or left-aligned in proportional figures → right or decimal alignment with tabular figures.
- A border on every cell, plus stripes, plus a hover shadow → one device, usually hairlines or space.
- "$" or "kg" repeated in every cell → unit once in the header.
- 1234567.891 → 1,234,567.89 or 1.23M, the same in the whole column.
- Blank cells for unknown values, or 0 for unknown → a dash with a stated meaning.
- Green, amber and red dots with no words → a text label plus color.
- Row actions that only appear on hover → visible, or revealed on focus too.
- A wide table squeezed on a phone so numbers wrap → scroll region, priority columns, or stacked rows.
- A table made of divs, with sort arrows on every column → a real table, with a sort state on the active column.
- Rotated header text → shorter header, or wrapped lines.
- Tiny text with oversized padding on every row → 14px or larger text, tighter padding if density is the goal.
- A profile page or a three-step list built as a table → a list or a definition list.
- Removing the grid from an editable spreadsheet-style grid → keep cell borders where cells are edited.
- A written answer that runs past a length limit the user gave → keep to it; cut material before the limit.

## Quick checks

- Is a table the right form for this content?
- Are numbers right-aligned, in tabular figures, with the same decimals in each column?
- Do units and currency appear once, in the header, and negatives show by sign or parentheses?
- Is every missing value a dash or "n/a" rather than a blank or a false zero?
- Is there one row-separation device, with a heavier rule only under the header and above totals?
- Is cell text 14px or larger, and do numbers stay on one line?
- Does a long table keep its header visible, and does the active column show its sort state?
- Is status written as a word, not color alone, and are row actions reachable by keyboard?
- On a 360px wide screen, can the reader still compare or look up values?
- Does the markup use `table`, `caption` and `th scope`, and are the empty, no-results, loading and error states designed?

## References

- [references/alignment-and-numbers.md](references/alignment-and-numbers.md): load whenever a table has numbers, dates, currency, percentages, negatives or missing values.
- [references/structure-and-separation.md](references/structure-and-separation.md): load when styling the table: header design, rules versus shading, density, totals, grouped rows, widths, wrapping.
- [references/responsive-and-accessible-tables.md](references/responsive-and-accessible-tables.md): load for narrow screens, markup, captions, scrollable regions and sort announcements.
- [references/table-states-and-actions.md](references/table-states-and-actions.md): load for interactive tables: sorting, filtering, selection, row actions, paging, and empty, loading and error states.
