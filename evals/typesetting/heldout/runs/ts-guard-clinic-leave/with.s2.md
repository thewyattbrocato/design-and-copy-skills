This stylesheet is mostly sound, so I changed one line.

```css
body { font: 1.0625rem/1.55 system-ui, sans-serif; color: #22262b; max-width: 38rem; margin: 0 auto; padding: 1.5rem; }
```

I changed `17px` to `1.0625rem`. It renders the same at default settings, but a fixed px size ignores a visitor's browser font-size preference, which matters for a dental office's patients.

These already work, so I left them alone:
- **Body:** 17px is a comfortable size, and the 1.55 line height suits it. The 38rem column gives about 65 characters per line.
- **Headings:** the h1 has tighter leading and slight negative tracking, and it scales with `clamp()`. The h2 has about four times as much space above as below.
- **Labels and small print:** the caps label is 12px with 0.08em tracking. The grey `#5a6470` has enough contrast on white. The 13px fine print is fine as long as it's secondary information.
- **Times:** `tabular-nums` on `.time` keeps the appointment slots aligned.

If you want one optional tweak, add `h1, h2 { text-wrap: balance; }` and `p { text-wrap: pretty; }` to avoid orphaned last words. The page doesn't need it.
