Almost all of it is fine, so I changed one line.

```css
body { font: 1.0625rem/1.55 system-ui, sans-serif; color: #22262b; max-width: 38rem; margin: 0 auto; padding: 1.5rem; }
```

**What changed:** `17px` is now `1.0625rem`. It renders the same at default settings. But a pixel size on `body` ignores a user's browser font-size preference, and that matters for a dental practice's patients, who may skew older. Everything else in the sheet already uses `rem`, so this makes `body` consistent with the rest.

**What I left alone, and why:**
- **`h1`:** The `clamp()` range, tight line-height and slight negative tracking suit a large heading.
- **`h2` and `p`:** The sizes and margins give a clear vertical rhythm.
- **`.label`:** 12px uppercase is small, but the `0.08em` tracking is the right fix for that. `#5a6470` on white is about 5.9:1, which passes AA.
- **`.fineprint`:** 13px with `#5a6470` also passes AA. The tighter 1.45 line-height is fine for short legal text.
- **`.time`:** `tabular-nums` is the right choice for appointment times that line up in a list.
- **`max-width: 38rem`:** That's about 65 characters per line, a good measure for reading.

The other rules are unchanged from what you pasted.
