**Use neither one everywhere.** Use tabular lining figures in the table and total, and proportional lining figures (the default) in the dashboard sentences. Old-style figures don't belong in either place.

- **Table and total:** Columns of hours, rates and amounts only line up if every digit has the same width. That makes the dev right for this part. Right-align the columns and show two decimals on every row.
- **Dashboard sentences:** Tabular figures add odd gaps in running text, such as around the "1" in "$4,820.50", so proportional is better here. The dev's "everywhere" doesn't hold.
- **Old-style figures:** They suit long editorial prose full of lowercase letters. These are short sentences with dollar amounts that the user compares ($4,820.50 against $3,990.00), and descending and ascending digits make that harder. The designer's preference for how they look gives way to legibility on a billing screen. If the brand wants some personality, put it in the typeface or weight, not the digit style.

```css
/* Money and quantities in columns: aligned, lining */
.invoice-table td,
.invoice-table th,
.invoice-total {
  font-variant-numeric: lining-nums tabular-nums;
}

.invoice-table td.num,
.invoice-table th.num,
.invoice-total {
  text-align: right;
}

/* Dashboard sentences: proportional, lining */
.dashboard-summary {
  font-variant-numeric: lining-nums proportional-nums;
}
```

- **Fixed decimals:** Format every amount with two decimals, for example `Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' })`. A column with mixed decimals won't align, even with tabular figures.
- **Total:** Make it one step stronger than the rows, using weight or a slightly larger size, not both. Keep it tabular and on the same baseline as its label.
- **Font support:** Check that your typeface has the `tnum`, `lnum` and `pnum` features. Inter, for example, does. If it doesn't, the CSS silently does nothing, and you'll need a different face for the table.
- **Default numerals:** If the face defaults to old-style figures, the `lining-nums` declarations above already override that.
