Most sans-serif fonts use proportional digits, so "1" is narrower than "8", and the span's width changes with each number. Surrounding inline text then reflows.

Fix it with tabular (fixed-width) digits:

```css
.counter {
  font-variant-numeric: tabular-nums;
}
```

If the font lacks tabular figures, give the span a `min-width` in `ch` units, with `display: inline-block` and `text-align: right`. You can also switch to a monospace font.
