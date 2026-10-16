I'd swap the trapezoids for left-aligned horizontal bars. I couldn't see your graphic, so this is based on your description and numbers.

**Why it's cluttered and the bottom stage is unreadable**
- Trapezoid width is the only thing carrying the value, so the 1,100 stage ends up about 9% as wide as the top. The name and percentage have to fit inside that sliver.
- The sloped sides make it hard to compare widths. A trapezoid that narrows toward its bottom edge doesn't show whether the width means its top edge, its bottom edge or its average.
- The gradient adds no information, and every shape holds two labels.

**What I'd change**
1. **Use bars on a shared zero baseline, one row per stage in funnel order.** Length is easy to compare, and the 1,100 bar stays visible (about 9% of the top bar).
2. **Put stage names outside the bars, in a column on the left.** Then the bar length doesn't limit the label length.
3. **Put the count and % of downloads at the end of each bar.** Use "7,900 · 64%", so one label does the work of two.
4. **Show step conversion between rows in small gray text** (for example "↓ 64% continue"). This answers "where do we lose people?", which a percent-of-top label can't.
5. **Use flat, solid fills with no gradient.** Make the first four bars a muted blue and the last bar (Paid subscription) the strong accent blue, because that's the number investors care about.
6. **Make the title state the finding,** and add a one-line source note.

**Sketch**

```
Only 9% of downloads become paid; most of the loss after setup is at the paywall

Downloaded           ████████████████████████████████████████  12,400 · 100%
                       ↓ 64% continue
Created account      ██████████████████████████  7,900 · 64%
                       ↓ 54%
Added first device   ██████████████  4,300 · 35%
                       ↓ 92%
Finished setup       █████████████  3,950 · 32%
                       ↓ 28%
Paid subscription    ████  1,100 · 9%      ← accent color

Wavecrest app users by stage · [period] · as of [date] · source: [source]
```

**What the numbers say**
- The step into **Added first device** loses about 46% of account creators (7,900 to 4,300).
- **Added first device → Finished setup** is healthy at 92%.
- **Finished setup → Paid** converts only 28%, the weakest step. About 2,850 people who finished setup didn't pay.
- Overall, 8.9% of downloads become paying subscribers.

Be careful with the title wording. I'd call the setup-to-paid step the weakest conversion, but I wouldn't say why people don't pay, because the data doesn't show that.

**Keeping the funnel shape:** if you want it for the investor deck's look, keep the centered shape but make widths strictly proportional to the counts. Put all text outside, in a column to the left and right of the shapes. Even then, the last stage will be a thin sliver, so I'd still recommend the bars.

**Placeholders:** I left the period, as-of date and source in brackets because you didn't give them. If you send those, or the file itself, I can build the final version in SVG.
