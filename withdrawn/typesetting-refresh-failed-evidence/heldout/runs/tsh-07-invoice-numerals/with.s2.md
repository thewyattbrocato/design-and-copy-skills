**Go with neither "everywhere". Use tabular lining figures wherever numbers sit in columns or get compared. Use proportional lining figures in the dashboard sentences.** The dev is right about the billing table. The designer's old-style figures don't fit either place in a money app.

**Why not old-style figures for this app**
- Old-style figures suit long editorial prose with lowercase text. They don't suit money. In "$4,820.50", the 4, 6, 7, 9 drop below the baseline and 3, 5 rise unevenly. That makes amounts harder to scan and compare.
- Old-style figures are usually proportional, so digits won't line up in a column. Hours, rate and amount, plus the total, need to stack on the decimal.
- If the font's default figures are already old-style (some serifs do this), you have to turn them off explicitly.

**Why not tabular everywhere**
- Tabular figures give every digit the same width. In running prose that leaves gaps around the 1 and uneven rhythm. "$3,990.00 in February" reads better with proportional lining figures.

**CSS**

```css
/* Prose, including the dashboard sentences: proportional lining */
body {
  font-variant-numeric: lining-nums proportional-nums;
  font-synthesis: none;
}

/* Anything in a column, or that changes live: tabular lining */
.invoice-table td.num,
.invoice-table th.num,
.invoice-total,
.stat-value {
  font-variant-numeric: lining-nums tabular-nums;
  text-align: right;
}
```

For the table, also do the following:
- Show the same number of decimals on every row. Use two for money, and pick one format for hours (e.g. `12.50`).
- Right-align the hours, rate and amount columns, and their headers.
- Make the total one step stronger than the rows, by weight or a slightly larger size. Don't change several properties at once. Keep it right-aligned in the same amount column so it lands under the decimals.
- Put a non-breaking space between a number and its unit, e.g. `12.5&nbsp;hrs`. Never truncate an amount.

**For the dashboard sentence**
- Leave the figures proportional inside the sentence.
- If a big stat tile repeats the amount on its own (a KPI card, for example), use tabular figures there, since it may update or sit next to other numbers.

**What to tell the designer:** they still have a place for typographic care. Give them the font choice, the weight and size of the total, and the spacing around the table. Old-style figures only make sense if the app later gets long-form editorial copy, such as a blog or a help article.

**Check your font first.** Not every font has `tnum`, `lnum` and `pnum`. Confirm that yours does, because if it doesn't, the CSS silently does nothing. If it has no tabular figures, pick a different face for the table numbers, or use a numeric-friendly fallback for those cells.
