The jumpiness comes from **proportional figures**. Gill Sans digits are not all the same width, so "1" is narrower than "0" or "9". Right-aligning keeps the right edges flush, but the digits inside each column shift as the numbers change. Tabular figures give every digit the same width, so the columns line up without changing the typeface.

Add this to your CSS:

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums;
}
```

Or apply it to the whole table if you have no other numeric columns:

```css
.plan-table { font-variant-numeric: tabular-nums; }
```

Two things to check:

- **Does your Gill Sans have a tabular-figure feature?** Not every version includes `tnum`. If the digits still wobble after the change, the font doesn't support it. I can't check the installed font from here. You can check in Font Book or a design app by looking for "Tabular" or "tnum" in the OpenType features. If it's missing, you could load a small numerals-only font for these cells with `@font-face` and a `unicode-range` covering `0-9`, `$`, and `,`, which keeps the look of the rest of the table.
- **Your fallback stack may explain why it only looks wrong sometimes.** Calibri has tabular lining digits by default, so on a machine without Gill Sans the table may already line up. If you see the problem on Macs but not Windows, that's the likely cause.

The `font-weight: 600` on prices may also be a factor. Gill Sans MT often has no semibold, so the browser synthesizes or substitutes a weight, and that can change digit widths. If the tabular fix doesn't fully settle it, try `font-weight: 700` or `normal` on the price cells to compare.
