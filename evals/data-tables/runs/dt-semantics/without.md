```html
<table class="grid">
  <thead>
    <tr class="row head">
      <th class="cell" scope="col" aria-sort="none">
        <button type="button" onclick="sortBy('name')">Name</button>
      </th>
      <th class="cell" scope="col" aria-sort="none">
        <button type="button" onclick="sortBy('seats')">Seats</button>
      </th>
      <th class="cell" scope="col" aria-sort="none">
        <button type="button" onclick="sortBy('mrr')">Monthly revenue</button>
      </th>
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

**What changed and why**

- **Real table elements.** `table`, `thead`, `tbody`, `tr`, `th` and `td` replace the divs. Screen readers can then announce the table, its row and column counts, and each cell's headers. The original classes are kept on each element.
- **Header cells are `th scope="col"`.** This ties each data cell to its column header. The first cell in each body row is a `th scope="row"`, so the business name identifies the row. If you'd rather not have it as a header, make it a plain `td`.
- **Buttons inside the headers.** An `onclick` on a div can't be reached by keyboard and isn't announced as interactive. A `<button>` is focusable, activates with Enter and Space, and is announced as a button. The `onclick` handlers are unchanged.
- **`aria-sort="none"`.** This is the starting state. Have `sortBy` set it to `ascending` or `descending` on the active column's `th`, and reset the others to `none`. That way the sort state is announced, not only shown.

**Caveats on "looks the same"**

- Browsers give `table`, `th` and `button` their own default styles: `th` is bold and centered, buttons get a border, background and their own font, and tables use `display: table`. If your `.grid`, `.row` and `.cell` rules use flex or grid, they should still apply, but the table's internal layout may shift a little. I can't see the CSS, so check it in a browser.
- If anything looks off, the usual fix is a small reset such as `.cell button { all: unset; cursor: pointer; }`, plus `text-align: inherit` and `font-weight` on `th.cell`. Keep a visible `:focus-visible` outline on the buttons so keyboard users can see where they are.
