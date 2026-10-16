Proportional sans-serif fonts give digits different widths; "1" is narrower than "0". When the count changes, the span's width changes and the text beside it moves. Fix it with tabular figures:

```css
.attendee-count {
  font-variant-numeric: tabular-nums;
}
```

If the font lacks tabular figures, set a fixed width, such as `min-width: 6ch; display: inline-block; text-align: right;`.
