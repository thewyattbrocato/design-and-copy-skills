The digits are proportional, so each one has a different width, and the decimal points don't line up. Fix it in the CSS for the total column:

```css
td.total {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

Also keep two decimals on every row, so `$98.00` stays as is.
