The jumpiness is most likely from **proportional figures**. Gill Sans's default digits are not all the same width (a "1" is narrower than a "0"), so the right-aligned numbers don't line up digit by digit. `text-align: right` only aligns the right edge of each cell, not the digits inside it.

The fix is to turn on tabular figures, which give every digit the same advance width and keep the typeface unchanged:

```css
.plan-table {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, sans-serif;
  font-size: 18px;
  font-variant-numeric: tabular-nums;
}
```

`font-variant-numeric` is inherited, so setting it on the table covers the price and seat cells. You could also set it only on `td.price` and `td.seats`.

Two things to check:

- **Whether your Gill Sans has tabular figures.** Gill Sans MT and some macOS versions include them, but I can't confirm that for your exact build from here. If the digits still don't line up, the font probably lacks the `tnum` feature and the browser is ignoring the property. You can check in Font Book (macOS) or with `fonttools` by looking for `tnum` in the GSUB table.
- **Platform differences.** macOS uses "Gill Sans" and Windows uses "Gill Sans MT", which have different metrics. If the table looks right on one platform and not the other, that's the cause.

If your build has no `tnum` feature, the fallback is to wrap only the numerals in a span with a font that has tabular figures, such as Calibri (its default figures are tabular). That keeps the humanist sans for the labels. Tell me if you want that version.
