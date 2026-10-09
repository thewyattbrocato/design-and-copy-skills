Digits in most sans-serif fonts have different widths (proportional figures; "1" is narrower than "0"), so the span's width changes as the number changes, nudging neighbors.

Fix it with tabular figures:

```css
.counter { font-variant-numeric: tabular-nums; }
```

If the digit count changes (99→100), also give it a `min-width` (e.g. `min-width: 4ch; display: inline-block;`).
