Sans-serif fonts use proportional digits by default, so "1" is narrower than "8". When the number changes, the span's width changes and neighbouring text reflows.

Fix it with tabular (fixed-width) digits:

```css
.counter {
  font-variant-numeric: tabular-nums;
}
```

If the digit count changes (99 → 100), also give the span a `min-width` in `ch` units, e.g. `min-width: 4ch`.
