Neither one everywhere. Use tabular lining figures in the table, the total, and anywhere numbers line up. Use proportional lining figures in the dashboard sentences. Old-style figures aren't the right choice for either screen.

**Why the split works**
- **Table and total:** Columns of hours, rate and amount only line up if every digit is the same width. Proportional digits make the decimals drift, and freelancers will be scanning and adding these up. The dev is right here.
- **Dashboard sentences:** These are prose, so tabular digits add gaps (a "1" gets as much room as an "8"). Use proportional figures there.
- **Old-style figures:** They are meant for lowercase-heavy editorial text. In a money app, descending 3s, 4s, 5s, 7s and 9s make amounts look uneven and harder to check, and `$4,820.50` is a number people act on. The designer's taste is better served by good proportional lining figures in the prose. If they insist, old-style is only defensible in the dashboard sentences, and only if the font's old-style set is good. Keep it out of anything tabular.

**CSS**

```css
/* Prose, including the dashboard sentences: proportional lining */
body {
  font-variant-numeric: lining-nums proportional-nums;
}

/* Table, totals, anything that stacks */
.line-items td,
.line-items th,
.invoice-total,
.amount {
  font-variant-numeric: lining-nums tabular-nums;
}

/* Numeric columns: right-aligned, same decimals on every row */
.line-items .num {
  text-align: right;
}

/* Total: one step up from the rows, same figures */
.invoice-total {
  font-weight: 600;
  font-size: 1.125rem;
}
```

**Practical notes**
- Always show two decimals on every money value (`$120.00`, not `$120`), and format with `Intl.NumberFormat` so locale separators are right.
- Hours should use a consistent decimal count too (`7.50`, `12.00`).
- Put the figure style on the cells or columns, not just on the table. Row-level overrides are easy to miss.
- Check that your font has real `tnum` and `lnum` features. Inter, IBM Plex Sans, Source Sans and system-ui on Apple platforms do. If a font lacks them, the browser fakes nothing and the property is silently ignored. Test by rendering a column of `1111.11` over `8888.88` and checking the widths match.
- If the dashboard uses a big stat tile (like a month's earnings) that sits next to other tiles, that one can use tabular figures. The sentence around it stays proportional.
