Your numbers are probably left-aligned or in proportional figures, so the decimal points don't line up. Right-align the column and turn on tabular numerals:

```css
td.total { text-align: right; font-variant-numeric: tabular-nums; }
```

Keep two decimals on every value. The header should be right-aligned too.
