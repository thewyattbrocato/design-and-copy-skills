Your numbers are in proportional figures, where each digit has a different width, and they probably aren't right-aligned. Fix both on the total column:

```css
.total {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

Every row also needs the same number of decimals, so $98.00 and not $98.
