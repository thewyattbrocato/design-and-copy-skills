Your numbers are almost certainly right-aligned incorrectly or using proportional digits. Fix:

```css
td.total {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

Right-align lines up the decimal points (always two decimals), and `tabular-nums` makes every digit the same width. Also check the header is right-aligned too.
