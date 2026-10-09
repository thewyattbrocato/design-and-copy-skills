```html
<table class="grid">
  <caption>Customer accounts</caption>
  <thead>
    <tr class="row head">
      <th class="cell" scope="col"><button type="button" onclick="sortBy('name')">Name</button></th>
      <th class="cell" scope="col"><button type="button" onclick="sortBy('seats')">Seats</button></th>
      <th class="cell" scope="col"><button type="button" onclick="sortBy('mrr')">Monthly revenue</button></th>
    </tr>
  </thead>
  <tbody>
    <tr class="row">
      <th class="cell" scope="row">Harbor Dental</th>
      <td class="cell">12</td>
      <td class="cell">$1,140.00</td>
    </tr>
    <tr class="row">
      <th class="cell" scope="row">Northwind Bakery</th>
      <td class="cell">4</td>
      <td class="cell">$360.00</td>
    </tr>
  </tbody>
</table>
```

You'll probably need this small reset so the buttons and `th` cells look like the old divs:

```css
.grid caption { /* visually hidden if you don't want it shown */ }
.cell { font-weight: inherit; text-align: inherit; }
.cell button { font: inherit; color: inherit; background: none; border: 0; padding: 0; cursor: pointer; text-align: inherit; }
```

**What changed and why**
- **Real table elements.** `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>` and `<td>` replace the divs. Screen readers can now announce "row 2, column 3, Monthly revenue", and users can move between cells. A div grid gives them none of that.
- **Header cells.** They are now `<th scope="col">`, and the first cell in each body row is `<th scope="row">`. Each value is announced with its column and its row name, for example "Harbor Dental".
- **Sorting.** The `onclick` on a div could only be used with a mouse. Each sort trigger is now a `<button>` inside its `th`, so it works with Tab, Enter and Space and is announced as a button. The `onclick` handlers are unchanged.
- **Caption.** I added a `<caption>` so the table has a name. "Customer accounts" is a placeholder, so use whatever fits.
- **Classes.** All the original classes are kept.

**Things to check**
- **Sort state.** `sortBy` should set `aria-sort="ascending"` or `"descending"` on the active `th` and remove it from the others. Without that, screen reader users can't tell which column is sorted.
- **Display rules.** If your CSS sets `display: flex` or `grid` on `.row`, some browsers and screen readers drop the table semantics. If you see that, either switch those rules to table display values or add explicit `role="row"`, `role="columnheader"` and similar attributes. I can't see the CSS, so I haven't changed anything for this.
- **Alignment.** I kept the cells as they were to preserve the look. Right-aligning the Seats and Revenue columns with `font-variant-numeric: tabular-nums` would make the numbers easier to compare, if you want to change that.
