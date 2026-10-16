Digits in most sans-serif fonts have different widths (a "1" is narrower than a "0"), so the span's width changes with each value and pushes neighboring text around.

Fix with tabular figures:

```css
.counter { font-variant-numeric: tabular-nums; }
```

If the font lacks them, give the span a fixed `min-width` (e.g. `5ch`) with `display: inline-block`.
