The likely cause is proportional figures. In most fonts, including Gill Sans, digits have different widths: a `1` is much narrower than a `0`. Right-aligning doesn't fix that, because the digits still shift as the number changes. Tabular figures give every digit the same width, so the columns line up.

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums;
}
```

This keeps Gill Sans, so the look you like doesn't change. Add it to the existing rules, or put it on the `.plan-table` selector so every number in the table gets it.

Some caveats:

- **Check that the font has a tabular feature.** Gill Sans MT on Windows and some other builds may not include tabular digits. If the numbers still wobble after the change, the font is the limit, not the CSS. In that case, wrap each number in a fixed-width inline-block span, such as `.num { display: inline-block; min-width: 4ch; text-align: right; }`. `ch` is the width of a `0`, so it works regardless of the font's figure set.
- **Confirm the font is actually loading.** Gill Sans is a system font on macOS but not on most Linux and Android systems. Where it's missing, the browser falls back to Calibri, then `sans-serif`, and those have different digit widths. Check in DevTools (Computed tab, look at the rendered font). If the table looks different across machines, a web font with a fixed weight set will make it consistent.
- **The 600 weight.** Gill Sans MT has only Regular and Bold, so `font-weight: 600` will snap to Bold or get synthesized. That's not what causes the jumpiness, but if the bold looks heavier than you intended, use `700` to make the mapping explicit.

I haven't seen the rendered table, so I can't confirm which of these applies. If the numbers still don't align after adding `tabular-nums`, send me a screenshot or the computed font-family and I'll narrow it down.
