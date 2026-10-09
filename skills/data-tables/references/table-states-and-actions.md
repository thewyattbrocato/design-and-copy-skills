# Table states and actions

Load this for interactive tables: filtering, selection, row actions, paging and the non-default states.

## Filtering and search

- Put filters above the table, with the active ones shown as removable chips and a "Clear all".
- Show the result count ("23 of 180 orders") and keep it readable by screen readers.
- Keep the header and sort state when filters change.
- A filter that returns nothing needs a "no results" state, not an empty body.

## Selection

- A checkbox column at the far left, with a header checkbox for "select all on this page".
- State the scope of "all": this page only, or every match? Offer "Select all 180" only when it is real, and say so.
- Show a count and the bulk actions in a bar that appears on selection ("3 selected: Archive, Export").
- Selected rows get a clear tint beyond the hover color. Keep the selection when the data refreshes or the sort changes.
- Make checkbox hit areas large enough to tap (about 44px), even if the box is small.

## Row actions

- Keep actions in one place, usually the last column, right-aligned.
- With one or two common actions, show them as labeled buttons or icon buttons with names. With more, put them in an overflow menu button with an accessible name ("Actions for invoice 1042").
- Do not reveal actions only on hover. Show them on hover and on keyboard focus within the row, and keep them visible on touch screens.
- Destructive actions ask for confirmation or offer undo, and are never the first item in a menu.
- If the whole row is clickable, give the main cell a real link, so keyboard and screen reader users get a target; avoid nested interactive elements inside a fully clickable row.

## Paging, scrolling and loading more

| Choice | Good when |
| --- | --- |
| Pagination | The reader needs to find their place, link to a page, or reach the footer |
| Load more | Records are browsed, with no need for position |
| Virtual scrolling | Thousands of rows and the user scans or searches |

Show the range and total ("21 to 40 of 180"). Keep the header visible. Preserve scroll position and focus when returning from a detail view.

## The four non-default states

**Empty (no data yet).** Say what the table will hold and give the next step: "No invoices yet. Create your first invoice." Keep the header row so the table still reads as a table, or replace it with a single block, but not both.

**No results.** Say that filters removed everything and offer a way out: "No orders match these filters. Clear filters." Keep the filter controls in place.

**Loading.** Show the real header and placeholder rows with the right number of columns, so the layout does not jump. Do not show a bare spinner when you know the shape. For refreshing existing data, keep the old rows and show a quiet progress indicator.

**Error.** Say what failed in plain words and how to try again: "We could not load orders. Check your connection and retry." Keep any rows already loaded. Keep error text in a live region so assistive technology announces it.

**Partial or stale data.** Say it where the numbers are: "Showing data to 6 March; later rows are still syncing." A silently incomplete total is worse than an empty cell.

## Editing in cells

Inline editing is a form problem: use form-design for validation and messages. For the table, keep the active cell visibly outlined, keep the row's identifying value in view, and restore the display style when the edit ends. When a table is meant to be edited like a spreadsheet, visible cell borders are appropriate, because every cell is a separate target.
