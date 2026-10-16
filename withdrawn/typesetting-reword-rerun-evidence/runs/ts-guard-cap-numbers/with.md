Your numbers are probably proportional-width and left-aligned, so the digits and decimal points don't line up. Right-align the total column and use tabular figures:

```css
td.total { text-align: right; font-variant-numeric: tabular-nums; }
```

Keep two decimals on every row, so $98.00 stays $98.00.
