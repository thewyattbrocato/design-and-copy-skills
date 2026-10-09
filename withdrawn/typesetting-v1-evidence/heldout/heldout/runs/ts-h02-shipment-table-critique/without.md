Two things are making the numbers wander. Both come from the numeric columns being treated like text.

**1. Numeric columns are left-aligned.**
With `text-align: left`, the decimal points land wherever the string length puts them. `4,120.5` and `611.25` start at the same edge but their digits don't stack. Numbers need to be right-aligned so the ones, tens and hundreds columns line up.

**2. Georgia has old-style figures.**
Georgia's digits are text figures: `3`, `4`, `5`, `7` and `9` drop below the baseline, `1` looks like a small-cap I, and widths vary by digit. That's why the numbers bounce up and down and look uneven. Georgia has no lining or tabular figure alternates, so `font-variant-numeric: tabular-nums` won't fix it. You need a different font for those cells.

**Smaller issues**
- **Inconsistent decimals.** Weight mixes `4,120.5`, `9,876.0` and `611.25`. Even with right alignment, the decimal points won't line up. Format every value in a column to the same number of decimals (weight to 1 or 2, cost to 2).
- **Headers look like data.** `font-weight: 400` makes them blend into the rows. Numeric headers also need to be right-aligned to sit over their data.
- **Pallets** are integers, so right alignment is enough.

**What I'd change**

```css
table {
  width: 100%;
  border-collapse: collapse;
  font-family: Georgia, serif;   /* fine for text columns */
  font-size: 15px;
}
th, td { padding: 8px 12px; text-align: left; border-bottom: 1px solid #ddd; }

th {
  font-weight: 600;
  font-size: 13px;
  color: #444;
  border-bottom: 2px solid #999;
}

/* Numeric columns: add class="num" to the th and td */
.num {
  text-align: right;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-variant-numeric: tabular-nums lining-nums;
}
```

For the shipment IDs (`NB-20418`), you could also give that column the `.num` font treatment, so the digits stack when people scan down the IDs.

In the data, format each column to fixed decimals before rendering. In JS, `toLocaleString('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 1 })` does this for weight, and the same with `2` does it for cost. The rows would then read `4,120.5 / 9,876.0 / 611.3 / 15,004.8`. Use 2 decimals for weight if you need to keep `611.25`.

If you'd rather not add a class to every cell, `td:nth-child(n+3), th:nth-child(n+3) { … }` covers columns 3–5, but it breaks if the column order changes.
