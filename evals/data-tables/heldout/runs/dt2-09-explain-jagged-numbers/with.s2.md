Right-alignment lines up the right edge of each string. Your values have 0, 1, 2 and 3 decimals, and the unit is attached, so the decimal points land in different places:

```
   1,204.5 km
      98 km
12,030.25 km
    7.125 km
   640.0 km
```

You can't compare magnitudes by place value when the ones digit sits in a different position on every row. Your font stack isn't the cause. Trebuchet MS and Verdana already use equal-width digits. The generic `sans-serif` fallback might not, so add `tabular-nums` as a safeguard.

**The fix has three parts:**

1. **Use the same number of decimals in every row.** Pick the precision the reader needs. One decimal is probably enough for km, and you can use two if the data needs it. If you must show every digit you have, pad to three decimals. Format the numbers rather than relying on CSS.
2. **Put the unit in the header** ("Distance (km)") and leave it out of the cells. A trailing " km" on some rows and not on others breaks the alignment too.
3. **Right-align the column and its header, with tabular figures.**

```css
th.num, td.num {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

```html
<th scope="col" class="num">Distance (km)</th>
...
<td class="num">1,204.5</td>
```

With one decimal, the column becomes:

```
 1,204.5
    98.0
12,030.3
     7.1
   640.0
```

The decimal points and place values now stack, so you can scan the column. This rounds 12,030.25 and 7.125. If the table has to reconcile to the exact figures, use three decimals (`1,204.500`, `98.000`, …) instead. That's wider, but nothing is lost.

If the decimals come from the raw data, format them in code with `toLocaleString('en-US', {minimumFractionDigits: 1, maximumFractionDigits: 1})`. Don't do the rounding in CSS.

I can apply this to your table if you point me to the file.
