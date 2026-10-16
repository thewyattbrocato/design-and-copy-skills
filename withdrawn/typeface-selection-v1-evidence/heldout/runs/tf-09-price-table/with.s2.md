The likely cause is proportional figures. Humanist sans fonts like Gill Sans usually draw digits at different widths, so a `1` is narrower than a `4`. Right-aligned prices then have digits that don't line up column by column, and the `$`, comma and digits drift between rows.

Add tabular figures to the numeric cells:

```css
.plan-table td.price,
.plan-table td.seats {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

This keeps the typeface and makes every digit the same width, so columns stack cleanly. You can also put it on `.plan-table` itself if you want it everywhere.

**Check that it worked.** `tabular-nums` only works if the font has a `tnum` feature, and I can't tell from here whether yours does:
- **Calibri** (your fallback) has tabular figures, and they're its default.
- **Gill Sans** on macOS and **Gill Sans MT** on Windows may not have `tnum`. If the property has no visible effect, that's why.

**If Gill Sans has no `tnum`**, here are two options:
1. Use a different font for the numbers only. Pick a humanist face with tabular figures, such as Source Sans 3, Fira Sans or Lato. Put it on `td.price` and `td.seats` and leave the rest of the table in Gill Sans. At 18px the difference in digit shapes is small.
2. Switch the whole table to one of those fonts. This is more consistent but changes the look you like.

Two smaller things to check:
- **Weight:** `font-weight: 600` can fall back to synthetic bold if the font has no semibold. That also changes digit widths, so `700` or a real semibold face is safer.
- **Alignment:** `$9` and `$1,240` right-align on the last digit, which is correct. Once the digits are tabular, the thousands comma will still push the `$` out further on larger prices. That's normal and reads fine.

If you tell me which font actually renders in your browser, I can say whether option 1 is needed.
