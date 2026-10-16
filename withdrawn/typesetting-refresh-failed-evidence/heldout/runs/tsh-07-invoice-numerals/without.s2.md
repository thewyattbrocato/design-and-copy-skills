Use both, by context. Neither "everywhere" is right.

**Tables and totals: tabular lining numbers.** In the line-items table, digits in a column have to line up so the decimals align and the eye can scan down and compare or add. That needs tabular (fixed-width) figures. It should also be lining (cap-height) figures. Old-style figures have 3, 4, 5, 7 and 9 dropping below the baseline and 6 and 8 rising. In a column of money that makes the numbers look jagged and harder to read, and it can make a total look wrong at a glance.

**Running prose: proportional old-style figures are fine.** In a sentence like "You earned $4,820.50 this month, up from $3,990.00 in February," nothing needs to align. Old-style figures blend into lowercase text and don't shout, so the designer is right here. Proportional spacing also avoids awkward gaps around the 1s.

So the dev wins on the billing table and the designer wins on the dashboard sentences. Often the designer's preference is mostly about the dashboard, and the dev's concern is mostly about the table, so this settles the dispute without a loser.

**Caveats**

- This only works if your font has these features. Many UI fonts (Inter, Roboto, SF) have tabular figures. Fewer have old-style figures. Check the font's feature list (e.g. on Wakamai Fondue) before promising the designer anything. If the font lacks `onum`, the declaration does nothing and you get lining figures silently.
- Some fonts default to old-style figures. In that case you need to set `lnum` explicitly in the table, not just `tnum`.
- Don't mix styles inside one number. The currency amounts in the dashboard sentence should all use the same style.
- If the dashboard also has big KPI tiles or any numbers that change live, use tabular lining there too, since they're data rather than prose.

**CSS**

```css
/* Default: prose gets old-style, proportional figures */
body {
  font-variant-numeric: oldstyle-nums proportional-nums;
}

/* Anything tabular or data-like: lining, fixed-width */
.line-items,
.line-items td,
.invoice-total,
.kpi {
  font-variant-numeric: lining-nums tabular-nums;
}

/* Right-align numeric columns so the decimals line up */
.line-items td.num,
.line-items th.num {
  text-align: right;
}
```

If you'd rather not set old-style on the whole body, scope it to the dashboard summary instead:

```css
.dashboard-summary {
  font-variant-numeric: oldstyle-nums proportional-nums;
}
```

`font-variant-numeric` is well supported and is preferable to writing `font-feature-settings: "onum", "pnum"` by hand. The low-level property overrides other font-feature settings and can clobber ligatures and other features.

**Recommendation:** make tabular lining the default for the app, since most of a billing product is data. Then opt in to old-style only on the dashboard prose sentences. That's the safer default because a missing opt-in looks fine, while a missing opt-out in a table looks broken.
