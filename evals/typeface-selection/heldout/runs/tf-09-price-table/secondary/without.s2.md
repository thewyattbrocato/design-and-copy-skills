The cause is almost certainly **proportional figures**. Most humanist sans fonts, Gill Sans included, default to digits of different widths: a `1` is narrower than a `0`. Right-aligning numbers that use proportional digits makes the digits drift, so `$119` and `$49` don't line up column by column.

The fix is to ask the font for **tabular figures**, where every digit has the same advance width. Keep the font and add this to the table:

```css
.plan-table { font-family: 'Gill Sans', 'Gill Sans MT', Calibri, sans-serif; font-size: 18px; }
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums lining-nums;
  text-align: right;
}
.plan-table td.price { font-weight: 600; }
```

`lining-nums` keeps the digits at cap height. Some humanist fonts default to old-style figures, which bounce above and below the baseline and would look jumpy even with tabular widths.

Two things to check:

- **Whether your Gill Sans build has the `tnum` feature.** Gill Sans MT from Office generally does, but I can't confirm that for your exact file. You can check in DevTools: select a price cell, open the Computed panel, and look for `font-variant-numeric`. If the digits still don't align after the change, the installed font likely lacks tabular figures. In that case, either load a webfont version that includes them, or use a humanist sans with tabular figures as the price-column font. The browser can't fake tabular figures, so there's no CSS-only fallback that keeps Gill Sans.
- **The `font-weight: 600` on prices.** If the font only ships regular and bold, 600 renders as bold. That's fine, but make sure the tabular setting still applies to the bold face, which it should.
