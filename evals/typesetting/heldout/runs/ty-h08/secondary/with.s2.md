**Why:** In most sans-serif fonts, digits are proportional, so "1" is narrower than "0" or "8." When the number changes, the span's width changes, and any centered or adjacent text moves.

**Fix:** Use tabular figures, where every digit has the same width:

```css
.attendee-counter {
  font-variant-numeric: tabular-nums;
}
```

If the font lacks `tnum`, add a `min-width` sized to the largest expected value, or use `display: inline-block` with a fixed width.
