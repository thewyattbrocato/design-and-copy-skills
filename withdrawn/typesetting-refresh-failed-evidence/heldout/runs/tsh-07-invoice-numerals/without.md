Neither one everywhere. Choose by what the numbers are doing.

- **Table (hours, rate, amount, total):** use tabular lining figures. Columns of numbers need equal-width digits so the decimal points line up and the amounts can be compared down the column. Old-style figures are a poor fit here. Their varying heights and widths make columns look ragged, and descending digits like 3, 4, 5, 7 and 9 bounce around in a column of money.
- **Dashboard sentences:** use proportional figures. Tabular digits in running text leave awkward gaps, for example around a "1". Old-style figures are fine here, because they blend into lowercase text. That gives your designer what they want where it helps.

So the dev is right about the table and the designer is right about the prose.

```css
/* Prose: friendly sentences */
.dashboard-summary {
  font-variant-numeric: oldstyle-nums proportional-nums;
}

/* Anywhere numbers are compared or summed */
.line-items td.num,
.line-items th.num,
.invoice-total {
  font-variant-numeric: lining-nums tabular-nums;
  text-align: right;
}

/* Optional: a utility class for any other aligned figures (e.g. invoice lists) */
.tnum { font-variant-numeric: lining-nums tabular-nums; }
```

Some practical notes:

1. **Check that your font has the features.** `font-variant-numeric` only works if the font ships `onum`, `pnum`, `tnum` and `lnum`. Many UI fonts lack old-style figures. Inter has them, but many web fonts don't. If yours doesn't, the browser silently ignores the request. Test it, and don't assume.
2. **Don't let it fall back to faux figures.** If you use a subsetted web font, make sure the subset keeps these OpenType features. Subsetting often strips them.
3. **Dashboard numbers that stand alone are a judgment call.** In "You earned $4,820.50 this month, up from $3,990.00 in February," old-style figures read nicely. If the dashboard also has big stat tiles or a column of figures, treat those like the table and use lining and tabular.
4. **Keep the format consistent.** Use the same currency formatting (`Intl.NumberFormat`) in both places, so only the figure style differs, not the content.

If the designer pushes back on the table, show them the same column both ways. The alignment difference is usually enough to settle it.
