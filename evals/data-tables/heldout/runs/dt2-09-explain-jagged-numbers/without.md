**What's going on:** Right-alignment only lines up the right edge of each string. The digits still don't line up, for two reasons:

1. **Proportional digits.** Trebuchet MS and Verdana use proportional figures by default, so a "1" is narrower than a "0" or "4". Equal-length numbers end up with different pixel widths.
2. **Differing decimal places.** Your values have 1, 0, 2, 3 and 1 decimals (`1,204.5`, `98`, `12,030.25`, `7.125`, `640.0`). Right-aligning puts the *units* at the edge, so the decimal points land in different columns. This matters more than the font. You can't compare magnitudes when the ones place isn't in the same spot.

**Fix:**

1. **Make the digits fixed-width** (CSS):

```css
td.numeric, th.numeric {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

   Verdana has tabular figures by default, so this may change little. Trebuchet MS's default digits are not reliably tabular, so `tabular-nums` helps there, but it only works if the font has the feature. Since your stack can fall back between fonts, the column's look could vary by machine. If it still looks off, set the column to a font with guaranteed tabular figures (e.g. `font-family: ui-monospace, "SF Mono", Consolas, monospace;`, or a font like Inter or Roboto, which support `tnum`).

2. **Use a consistent number of decimals** (the data formatting fix, which is the more important one). Format every value to the same precision, for example with `toLocaleString`:

```js
value.toLocaleString('en-US', {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2
})
```

   Result:

```
 1,204.50 km
    98.00 km
12,030.25 km
     7.13 km
   640.00 km
```

   Note that `7.125` rounds to `7.13`, so pick a precision that's acceptable for your data. If you need to keep 3 decimals, use 3 for the whole column.

With both changes the decimal points and every digit position line up vertically, so you can compare down the column. Also check that the unit "km" isn't making the alignment ragged. If it's in the cell text, it's fine as long as it's identical on every row. Moving it to the column header (`Distance (km)`) is cleaner, and then the cells hold only numbers.
