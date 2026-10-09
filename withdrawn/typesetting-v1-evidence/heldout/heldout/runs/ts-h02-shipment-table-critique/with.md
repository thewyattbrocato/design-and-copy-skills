Two things cause both symptoms: Georgia's figures, and the way the numeric columns are aligned.

**What's wrong**

1. **Georgia uses old-style figures.** Digits like 3, 4, 5, 7 and 9 drop below the baseline, and every digit has a different width. Georgia has no tabular-figure option, so `font-variant-numeric` can't fix this. That's why the numbers seem to wander.
2. **The numeric columns are left-aligned.** Digits only stack by place value when the columns are right-aligned. Left-aligned, `98.10` and `14,650.00` start at the same edge, so their decimal points land in different places.
3. **Decimals are uneven.** Weight shows `4,120.5`, `9,876.0` and `611.25`, so the decimal points don't line up even when right-aligned. This is a data-formatting problem, not a CSS one.
4. **The header row doesn't read as a header.** `font-weight: 400` makes it identical to the data. Its labels are also left-aligned over what should be right-aligned numbers.

**Changes**

```css
table { width: 100%; border-collapse: collapse; font-family: Georgia, serif; font-size: 15px; }
th, td { padding: 8px 12px; text-align: left; border-bottom: 1px solid #ddd; }
th { font-weight: 600; }

th.num, td.num { text-align: right; }
td.num {
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-variant-numeric: tabular-nums lining-nums;
}
```

Add `class="num"` to the Pallets, Weight and Cost `th` and `td` cells. Keep Georgia for the text columns.

**Format the data to a fixed number of decimals.** Format weight with 2 decimals (`4,120.50`, `9,876.00`, `611.25`, `15,004.80`), keep cost at 2, and show pallets as integers. Do this in whatever generates the rows, for example `toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})`.

I left the 15px size and the padding alone. They're fine for a dense table.
