Digits in most sans-serif fonts have different widths (proportional figures; "1" is narrower than "0"), so the span's width changes with each value and neighbouring text reflows.

Fix it with tabular figures:

```css
.counter { font-variant-numeric: tabular-nums; }
```

If the font lacks them, give the span a fixed `min-width` (e.g. `6ch`) or use a monospace font for the number.
