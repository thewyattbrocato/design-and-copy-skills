The digits are probably proportional, so each one has a different width and the decimal points drift out of line. Add this to the total column:

```css
td.total { font-variant-numeric: tabular-nums; text-align: right; }
```

Right-alignment only lines up the decimals if every row has two decimals, so format each amount with two (`$98.00`, not `$98`).
