Most of this stylesheet is already well set, so I changed one line.

```css
body { font: 1.0625rem/1.55 system-ui, sans-serif; color: #22262b; max-width: 38rem; margin: 0 auto; padding: 1.5rem; }
```

The body size was `17px`, which ignores a visitor's browser text-size setting. `1.0625rem` renders identically by default and scales for people who've enlarged their text. That matters for a dental practice's audience.

I left everything else alone:
- **Measure:** `38rem` gives roughly 65 characters per line.
- **Headings:** the `h1` and `h2` leading, the `h1` tracking and the `h2` spacing (4:1 above to below) are all fine.
- **Labels and figures:** the `.label` caps are tracked and at the 12px minimum. The `.time` figures are tabular, so appointment times will line up.
- **Contrast:** the `#5a6470` gray on white passes contrast.

Optional, and not applied: add `h1, h2 { text-wrap: balance; }` and `p { text-wrap: pretty; }` to avoid orphaned last words.

If the `.fineprint` at 13px carries anything people need to act on, such as cancellation terms, move it up to body size.
