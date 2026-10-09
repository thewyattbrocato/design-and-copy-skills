The designer is right, assuming "different font setting" means tabular figures. That's `font-variant-numeric: tabular-nums`, not a different typeface. It's one line of CSS, so it isn't overkill.

**Why it matters for your data:**
- **Prices, ETAs and counts** are all numbers people compare down a column. With proportional figures, a "1" is narrower than an "8", so digits drift out of line and the column looks ragged. Tabular figures give every digit the same width, so the ones, tens and decimals line up.
- **Live-updating values** such as ETAs that tick down or counts that refresh also benefit. Proportional digits make the cell's width, and any neighboring text, jitter on every update.
- **Headings** are prose-like text where proportional figures look better. So the split the designer wants is correct: tabular in data cells, proportional elsewhere.

**What to apply:**
```css
td.num, .metric {
  font-variant-numeric: tabular-nums;
  text-align: right;
}
```
- Right-align numeric columns, and put the header over them with the same alignment.
- Use the same number of decimals on every row. For prices that's `$4.50`, not `$4.5`.
- Put a non-breaking space between a number and its unit (`12 min`) so they don't wrap apart.

**Caveat:** some typefaces have no tabular figures, and the CSS then does nothing. Check by rendering a column of `1111` over `8888`. If the widths differ, use a system or monospace face for the number cells instead of forcing it.

You're right that it shouldn't become a heavy design-system exercise. Don't add a separate font family, size or weight for numbers. The tabular-nums rule on numeric cells covers it.
