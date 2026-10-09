Gill Sans uses proportional (variable-width) digits by default, so "1" is narrower than "0" or "4". In a right-aligned column, numbers with the same digit count end up with different widths, so the decimal edges and thousands separators don't line up from row to row. Calibri (your fallback) does the same by default. The bold weight on prices makes it worse.

You can keep the font and turn on tabular figures with one property:

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums;
}
```

Or apply it to the whole table:

```css
.plan-table {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, sans-serif;
  font-size: 18px;
  font-variant-numeric: tabular-nums;
}
```

This makes every digit the same width, so `$9`, `$49`, `$119` and `$1,240` right-align cleanly, and so do the seat counts. The typeface and its look stay the same.

Caveats:

- **Font support:** `tabular-nums` only works if the font ships a tabular-figures (`tnum`) feature. Calibri does. Gill Sans MT and Apple's Gill Sans have it in recent versions, but older copies may not. If you see no change on some machines, that font lacks the feature.
- **Fallback:** If a visitor's fallback font doesn't support it, the digits stay proportional. For a guaranteed result, you could load a webfont that has `tnum`, or use the lower-level `font-feature-settings: "tnum";`.
- **Optional polish:** Gill Sans may default to oldstyle figures in some versions. If digits sit at uneven heights, add `lining-nums` too: `font-variant-numeric: lining-nums tabular-nums;`.

I haven't seen your rendered page, so if the rows still look jumpy after this, check for inconsistent cell padding or a currency symbol sitting outside the right-aligned cell.
