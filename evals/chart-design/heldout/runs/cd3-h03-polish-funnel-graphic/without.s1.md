I haven't seen the image, so this works from your description. The trapezoids are the main problem, and I'd drop them for a bar funnel.

**Why it feels cluttered and the bottom is unreadable**
- Trapezoid width encodes the value, but the slanted sides blur it. Readers can't tell whether the value is the top edge, the bottom edge or the area.
- Paid subscription is 8.9% of downloads, so it gets a sliver. The label has to fit inside that sliver, and it can't.
- The gradient adds no information. Each trapezoid carries a stage name and a percentage in the same box, so they compete with the shape.

**What I'd change**
1. **Use horizontal bars on a shared left baseline.** Length is the easiest thing to compare. Keep the top-to-bottom funnel order. A small bar stays small, but it stays legible because its label isn't inside it.
2. **Put the stage names in a left column and the values in a right column.** Nothing sits inside a bar, so the bottom stage is as readable as the top one.
3. **Use one flat blue, with no gradient.** Order already carries the sequence. If you want emphasis, make only "Paid subscription" the darker blue, since that's the number investors care about.
4. **Give each row two numbers.** Show the count, then the percent of downloads. Put the step-to-step conversion in muted text between rows.
5. **Use one percentage definition and say so in a subtitle.** For example: "% of downloads. Arrows show conversion from the previous step."
6. **Remove everything else.** That means no borders, no shadows, no axis, no gridlines and no legend. A single series needs no legend, and the title names it.
7. **Add a takeaway headline** in place of "Funnel", such as "Only 1 in 11 downloads becomes a paid subscriber."

**Sketch**

```
Wavecrest conversion funnel
% of downloads · muted figures show conversion from the previous step

Downloaded          ████████████████████████████████████████  12,400  100%
                                         ↓ 63.7%
Created account    █████████████████████████▌                 7,900   64%
                                         ↓ 54.4%
Added first device  ██████████████▏                            4,300   35%
                                         ↓ 91.9%
Finished setup      █████████████                              3,950   32%
                                         ↓ 27.8%
Paid subscription   ███▌ (darker blue)                         1,100    9%
```

**Numbers behind it**

| Stage | Users | % of downloads | Conversion from previous step |
|---|---|---|---|
| Downloaded | 12,400 | 100% | n/a |
| Created account | 7,900 | 63.7% | 63.7% |
| Added first device | 4,300 | 34.7% | 54.4% |
| Finished setup | 3,950 | 31.9% | 91.9% |
| Paid subscription | 1,100 | 8.9% | 27.8% |

**What the cleaner version shows**
- Finished setup converts at 92% from adding a first device. Setup isn't a drop-off point.
- The weakest step is setup to paid at 27.8%. That's the biggest rate loss in the funnel (2,850 users).
- The largest absolute loss is download to account, at 4,500 users.

Rounding the percentages to whole numbers on the chart is fine for an investor update, as long as the table or notes carry one decimal.

If you want a rendered version, send me the data format you prefer (SVG, PNG or HTML) and your brand blue hex. I'll build it and check it for label collisions and contrast.
