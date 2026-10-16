Proportional sans-serif fonts give each digit a different width: "1" is much narrower than "0" or "8". When the number changes, the span's total width changes, and anything after it moves.

Use tabular figures, where every digit has the same width:

```css
.attendee-count {
  font-variant-numeric: tabular-nums;
}
```

If it still shifts, set `display: inline-block` and a `min-width` in `ch` units wide enough for the largest count.
