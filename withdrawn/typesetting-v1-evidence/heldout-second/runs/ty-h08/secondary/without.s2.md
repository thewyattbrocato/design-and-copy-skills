Most sans-serif fonts use proportional digits, so a "1" is narrower than an "8." When the count changes, the span's width changes, and any text beside it moves.

Use tabular figures so every digit has the same width:

```css
.attendee-count {
  font-variant-numeric: tabular-nums;
  display: inline-block;
  min-width: 4ch;
}
```

The `min-width` stops the span from resizing as the count grows.
