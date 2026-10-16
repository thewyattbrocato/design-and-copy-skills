Your numbers are probably left-aligned or in a proportional-width font. Fix both:

```css
td.total {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

Right-alignment lines up the decimal points, because every value has two decimals. Tabular figures give every digit the same width, so the columns stay straight.
