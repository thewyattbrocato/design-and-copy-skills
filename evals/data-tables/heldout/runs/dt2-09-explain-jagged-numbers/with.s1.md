**Cause:** right-alignment only lines up the right edge of each string. Your rows have 1, 0, 2, 3 and 1 decimal places, and the " km" is attached to each one. So the decimal points land in different places and the digits don't stack by place value. The values are correct, but the eye can't compare them.

**Fix:** three changes.

1. **Use the same number of decimals in every row of the column.** This is the main fix. Once every value has the same decimals, right-aligning also aligns the decimal points.
2. **Move the unit into the header**, "Distance (km)", and leave the cells as bare numbers. Otherwise " km" sits after the number and is part of what you're trying to align.
3. **Turn on tabular figures** so every digit has the same width:

```css
td.num, th.num {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

Put the `num` class on the header cell too, so the header lines up with its data.

Don't blame the font stack. Trebuchet MS and Verdana normally have fixed-width digits already. The `tabular-nums` rule is cheap insurance, and it guarantees the behavior if the stack falls through to `sans-serif`.

**Choosing the decimals:**

| Option | When to use | Result |
|---|---|---|
| 1 decimal | Distance only needs to be comparable. | 1,204.5 / 98.0 / 12,030.3 / 7.1 / 640.0 |
| 3 decimals | You must keep every value exact. | 1,204.500 / 98.000 / 12,030.250 / 7.125 / 640.000 |

The 1-decimal option rounds 12,030.25 and 7.125, so it changes what's displayed. If anyone needs to reconcile these against source data, use 3 decimals. Format with `toFixed(n)`, or with `Intl.NumberFormat` and `minimumFractionDigits` set equal to `maximumFractionDigits`. That keeps the thousands separators and forces the same decimals in every row.
