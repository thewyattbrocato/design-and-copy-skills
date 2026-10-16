Your rows are right-aligned, but the digits in Gill Sans are proportional. A "1" is narrower than a "0", so the columns of digits don't stack, and the semibold weight makes the mismatch more visible. Fixing it doesn't mean changing the typeface.

**First try tabular figures:**

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums lining-nums;
}
```

Put it on the numeric cells only, so the rest of the table keeps its normal spacing. `lining-nums` also protects against old-style figures, which would make prices bounce vertically.

**Check that it worked.** `tabular-nums` only does something if the font has a `tnum` feature, and the stack may resolve to different fonts on different machines:
- **Gill Sans on macOS**: I don't believe the system version has `tnum`, so the property will do nothing there.
- **Gill Sans MT on Windows**: this is also not guaranteed to have it.
- **Calibri**: it has tabular figures, so it should work. It's also the font users on machines without Gill Sans will see.

If the prices still jump in Gill Sans, here are two fixes that keep the look:

1. **Use a web font with real `tnum` support.** Gill Sans-like humanist options include Lato, Source Sans 3 (both have `tnum`), or a licensed Gill Sans from Monotype (check that the web license includes OpenType features). Self-hosting one also makes the table look the same on every OS.
2. **Use a different font for digits only.** Define a `@font-face` with `unicode-range: U+0030-0039, U+0024, U+002C, U+002E` pointing at a tabular humanist face, and put it first in the `font-family` stack for the numeric cells. The text stays Gill Sans, and only the numerals, `$`, comma and period come from the other font.

If you tell me which OS and browser you're seeing this on, I can say which case applies. I can also look at the actual stylesheet and markup if you'd like me to apply the change.
