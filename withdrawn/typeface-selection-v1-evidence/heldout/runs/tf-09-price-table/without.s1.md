The cause is almost certainly that Gill Sans uses proportional digits by default, so each numeral has a different width. A `1` is narrower than a `0` or `4`. Right-aligned prices then end at the same edge, but the digits inside them don't stack in columns. Totals like `$119` and `$1,240` look ragged against each other, and so do `3` and `1,000` in the seats column.

You can fix this without changing the typeface by turning on tabular figures:

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums;
}
```

This makes every digit the same width, so the ones, tens and hundreds places line up from row to row. You can put it on `.plan-table` instead if you want it on every number in the table.

**Caveats**

- **Font support:** `tabular-nums` only works if the font has a `tnum` feature. Gill Sans MT on Mac and Windows generally does. Calibri, your fallback, does too, and its default digits are already tabular. Gill Sans on macOS is older and may not have it, so check how it renders on a Mac. If the digits don't change, that font simply lacks the feature, and your options are to switch the numerals to a similar font or accept the difference.
- **Fallback differences:** the table can render in different fonts on different machines, and some fallbacks are proportional. If that matters, load a webfont with tabular figures and use it for the numbers only.
- **Commas and `$`:** the comma in `$1,240` is narrow, so the digits in `1,240` won't line up with those in `119` even with tabular figures. Digits only line up by place value if every row has the same separators. If you want the thousands digit to align perfectly, you could right-align and accept that, or use `font-feature-settings: "tnum"` plus consistent formatting. Right alignment with tabular digits is usually enough to look steady.
- **Weight:** the `font-weight: 600` on prices can fall back to a synthesized bold if the font has no semibold. Tabular numbers still work, but the glyph widths can change slightly from the regular weight. Check that the browser isn't faux-bolding.

If the numbers still look jumpy after this, tell me what you see. Paste a screenshot or the rendered font name from DevTools (Computed → Rendered Fonts) and I can narrow it down.
