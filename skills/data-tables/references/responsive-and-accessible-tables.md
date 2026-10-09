# Responsive and accessible tables

Load this for narrow screens, table markup, captions, scroll regions and sort announcements.

## Choosing a narrow-screen strategy

Decide by what the reader does with the table, not by habit.

| Task | Strategy | Why |
| --- | --- | --- |
| Compare values across many columns (specs, prices, schedules) | Horizontal scroll with a frozen first column | Keeps the comparison and the row identity |
| Look up one record, with several columns that rarely matter | Priority columns; the rest in an expandable row or a detail view | Keeps the table scannable |
| Three or four fields per row, read one row at a time (an order list) | Stacked label and value list | Reads like a card; no horizontal movement |
| More than about 5 columns of numbers to compare | Do not stack; scroll or reduce columns | Stacking destroys comparison |

Never solve a narrow screen by shrinking text or letting numbers wrap.

## Horizontal scroll that works

```html
<div class="table-scroll" role="region" aria-labelledby="orders-cap" tabindex="0">
  <table>
    <caption id="orders-cap">Open orders</caption>
    ...
  </table>
</div>
```

```css
.table-scroll { overflow-x: auto; }
.table-scroll th:first-child, .table-scroll td:first-child {
  position: sticky; left: 0; background: var(--surface);
}
```

- Name the scroll region and make it keyboard focusable, so keyboard users can scroll it.
- Give a visible cue that more content exists: a clipped column peeking in, or an edge shadow.
- Freeze the identifying column. Give the sticky cells an opaque background and a subtle right edge.
- Keep minimum column widths so numbers stay on one line.

## Priority columns

Mark each column as essential, helpful or optional. Keep the essential ones in every view, show the helpful ones from a middle width, and move optional ones into a "more" row, a details panel, or a column chooser. Hiding with `display: none` removes data from assistive technology too, so make sure the same facts remain reachable.

## Stacked rows without false semantics

When a table becomes label and value pairs, the markup should match what the eye sees:

- Real option: keep the `<table>` and restyle it (`display: block` on cells with a `data-label` pseudo-element). Be aware that changing `display` on table elements can strip table roles in some browsers; restore them with explicit roles, or test with a screen reader.
- Safer option: render a separate stacked structure (a list of items, each a description list) at the narrow width and keep the real table at wide widths, showing one and hiding the other.
- Whichever you choose, every stacked value must still show its label, and the order must match the table.

## Table markup

```html
<table>
  <caption>Quarterly revenue, USD thousands</caption>
  <thead>
    <tr><th scope="col">Region</th><th scope="col" class="num">Q1</th><th scope="col" class="num">Q2</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">North</th><td class="num">1,240</td><td class="num">1,310</td></tr>
  </tbody>
  <tfoot>
    <tr><th scope="row">Total</th><td class="num">3,100</td><td class="num">3,260</td></tr>
  </tfoot>
</table>
```

- Use `<table>`, `<thead>`, `<tbody>`, `<th>` and `<td>`. Divs with grid styling announce nothing.
- Add `scope="col"` to column headers and `scope="row"` to the cell that names the row.
- A `<caption>` names the table and can hold a one-sentence summary or the unit; it can be visually quiet but should not be hidden.
- A table with two header levels needs `headers`/`id` pairs or nested `colgroup`/`scope="colgroup"`; keep complexity as low as you can.
- Do not use tables for layout, and do not use `role="grid"` unless cells really have arrow-key navigation and editing.
- Use `font-variant-numeric` and classes for numeric cells; the markup does not need to change.

## Sort controls

```html
<th scope="col" aria-sort="ascending">
  <button type="button">Due date <span aria-hidden="true">▲</span></button>
</th>
```

- Put a `<button>` inside the header cell; do not attach the click handler to the cell.
- Set `aria-sort="ascending" | "descending"` on the sorted header only; leave it off the others (use "none" sparingly).
- Show the direction with an icon and keep a text equivalent in the control's name or a live region ("Sorted by due date, ascending").
- Make the first click's result predictable: ascending for text, descending for dates and amounts where the biggest or newest is wanted first, and say which.
- Sorting must be stable, and a secondary sort (usually the identifying column) keeps equal values in a steady order.

## Color, contrast and focus

- Text in cells, headers and stripes meets the current accessibility contrast guidance (about 4.5 to 1 for normal text).
- Status needs a word or shape in addition to color.
- Focus outlines must be visible on buttons, links, checkboxes and sticky header controls, and must not be hidden under the sticky header when scrolled into view (`scroll-margin-top`).
