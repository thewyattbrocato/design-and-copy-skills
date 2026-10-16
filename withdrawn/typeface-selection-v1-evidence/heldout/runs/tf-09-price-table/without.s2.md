Gill Sans uses proportional (variable-width) digits by default, so "$1,240" and "$119" don't have digits of equal width. Right-aligned columns then wobble from row to row. Calibri, your fallback, has the same issue. Gill Sans also uses old-style numerals in some versions, which adds to the jumpiness.

You can keep the typeface and turn on tabular figures for just those cells:

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: lining-nums tabular-nums;
}
```

Notes:

- **`tabular-nums`** gives every digit the same advance width, so the ones, tens and hundreds columns stack. This is the main fix.
- **`lining-nums`** forces full-height numerals instead of old-style ones, so the baseline looks even. Drop it if you like the old-style look.
- **Font support:** this only works if the font has a `tnum` feature. Gill Sans MT and Calibri do. Some versions of macOS's bundled Gill Sans don't. If you see no change on a Mac, that's likely the cause. You can check by opening the table in Safari and Chrome and comparing.
- **Fallback:** if a font lacks `tnum`, the usual option is to self-host a humanist sans that has it, such as Gill Sans Nova or Lato. Use it only for the numeric cells so the rest of the table keeps its look.
- **Commas and `$`:** the comma and dollar sign are narrow glyphs, and `$9` has no comma. With tabular figures, digits still line up from the right, since the table is right-aligned. The comma in "$1,240" just pushes the number left, which is expected.

If the "/ N seats" text is in the same cell, put the number in its own `td` or `span`. Otherwise the trailing word "seats" will break the right alignment of the digits.

If it's still jumpy after this, send me the rendered HTML for a row or two. Differing cell padding or `font-weight: 600` falling back to a synthetic bold could also be a factor.
