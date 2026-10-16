Neither "everywhere" is right. Use each where it fits: **tabular lining figures in the table and totals, proportional old-style figures in the dashboard sentences** (if the typeface supports them and the designer still likes them there).

**Why**

- **Table/totals:** Digits in a column need to be the same width so decimals and place values line up vertically. Hours, rate, amount and the total are things people scan and compare down a column. Old-style figures also have varying heights and descenders (3, 4, 5, 7, 9 drop below the baseline). That makes a column of amounts look ragged and makes money harder to read quickly. Use lining and tabular here.
- **Dashboard sentences:** These are inline prose, read once and not compared. Old-style proportional figures blend into running text, so the designer is right. "$4,820.50" in lining caps in the middle of a sentence looks like it's shouting. Tabular spacing in prose also adds odd gaps around the 1s.

So the dev is right about the table and the designer is right about the sentences. The combination is the standard answer.

**CSS**

```css
/* Default: prose / dashboard sentences */
body {
  font-variant-numeric: oldstyle-nums proportional-nums;
}

/* Table, totals, anything aligned or compared */
.invoice-table td,
.invoice-table th,
.invoice-total,
.num {
  font-variant-numeric: lining-nums tabular-nums;
  text-align: right; /* numeric columns right-aligned */
}
```

Notes:

- Apply the sentence style to the dashboard container rather than `body` if you'd rather not make old-style figures the global default. That would also affect things like dates, IDs and form fields. A utility class (`.num`) for the tabular case, used on any number that sits in a column, is easiest to maintain.
- **Check the font first.** `font-variant-numeric` only works if the font has those OpenType features (`onum`, `lnum`, `tnum`, `pnum`). Many fonts don't. Inter, for example, has tabular and lining but its old-style support is limited. If the font lacks old-style, the designer's request can't be met in CSS. If you use Google Fonts or another subsetting service, confirm the feature tables survive the subset.
- **Fallback for features:** if you need to force it, `font-feature-settings: "onum" 1, "pnum" 1;` and `"lnum" 1, "tnum" 1;` do the same thing, but prefer `font-variant-numeric` because it's higher level and doesn't clobber other feature settings.
- **Mixed-in numbers in prose:** if you want the amounts in sentences to stay old-style but the surrounding dashboard has a stat tile (big "$4,820.50" on its own), treat the tile as a "display" number and probably use lining, since it's not running text. It's a judgment call for the designer.
- Right-align numeric columns, and keep a consistent number of decimals (always 2 for currency) so tabular figures actually line up.

If the two still disagree, show the table with each style side by side. The ragged old-style column usually settles it.
