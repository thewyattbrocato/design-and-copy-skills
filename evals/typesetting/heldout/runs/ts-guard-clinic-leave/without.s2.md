The stylesheet is already in good shape, so I'd make only one change.

```css
body { font: 1.0625rem/1.55 system-ui, sans-serif; color: #22262b; max-width: 38rem; margin: 0 auto; padding: 1.5rem; }
```

**What changed:** the body size went from `17px` to `1.0625rem`, which renders the same at default settings. With `px`, the base size ignores a visitor's browser font-size preference. Everything else is already in `rem` or `em`, so this was the one place that wouldn't scale. That matters on a dental office page, where many visitors are older.

**What I left alone:**
- **Headings:** the `h1` `clamp()` scales well, and the tight line-height and slight negative tracking suit display sizes. The `h2` spacing gives a clear hierarchy.
- **Body text:** the 1.55 line-height and the roughly 38rem measure (about 65 characters per line) are comfortable to read.
- **Muted text:** `#5a6470` on white has a contrast ratio of about 6:1, which passes WCAG AA for both `.label` and `.fineprint`, even at their small sizes.
- **Times:** `tabular-nums` on `.time` is the right choice, because appointment times will line up in columns.

If you want to go further, `.label` at 12px is the smallest text on the page. It passes on contrast, and the uppercase tracking helps, but you could raise it to `0.8125rem` if it looks cramped on mobile. I didn't change it because it isn't broken.

You pasted the CSS rather than pointing me to a file, so I haven't edited anything on disk.
