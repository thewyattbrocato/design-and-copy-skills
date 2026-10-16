Sans-serif fonts usually use **proportional digits**, so each digit has a different width ("1" is narrower than "8"). When the count changes, the span's width changes, and any text beside it or centred around it shifts.

Fix it with **tabular digits**, which give every digit the same width:

```css
.attendee-count {
  font-variant-numeric: tabular-nums;
  display: inline-block;
  min-width: 6ch; /* optional: stops the span resizing as the count grows */
}
```
