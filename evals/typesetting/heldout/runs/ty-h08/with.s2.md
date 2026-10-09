Sans-serif digits are usually proportional, so a "1" is narrower than an "8". When the count changes, the span's width changes, and the neighbouring text moves with it.

Fix it with tabular figures:

```css
.attendee-count {
  font-variant-numeric: tabular-nums;
  display: inline-block;
  min-width: 4ch; /* room for the longest count */
}
```

`tabular-nums` makes every digit the same width. The `min-width` stops the text shifting when the count gains a digit. If your font has no tabular figures, switch to one that does.
