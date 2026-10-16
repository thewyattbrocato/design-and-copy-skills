This stylesheet is sound, so I changed nothing.

- **Measure:** `38rem` at 17px is about 60–65 characters per line, which is right for reading.
- **Leading:** body at 1.55, `h2` at 1.25 and `h1` at 1.1 all fit their sizes, and the `h1` is tightened slightly.
- **Scale:** the sizes are `h1` (fluid), 1.35rem, 17px body, 13px fineprint and 12px label. Each has its own job.
- **Spacing:** `h2` has 2rem above and 0.5rem below, so it clearly belongs to the text under it. Paragraphs are separated by a gap only.
- **Labels and figures:** the caps label is 12px with 0.08em tracking. `.time` uses `tabular-nums`, so appointment times will line up.
- **Contrast:** `#5a6470` on a light ground is readable at the small sizes.

One optional tweak, only if your headings wrap to a lonely last word on phones:

```css
h1, h2 { text-wrap: balance; }
```

I left `font: 17px` on `body` alone. Switching it to `1.0625rem` would let it follow the browser's text-size setting, but it would also be a unit swap you didn't ask for.
