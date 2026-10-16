I don't see an image attached, so I'm working from your description and the numbers. The fixes below follow from those, but if something in the file doesn't match, tell me.

## What I'd change

**1. Replace the trapezoids with horizontal bars.**
- This is the fix for the unreadable bottom stage. A funnel shape has to shrink to match the data, and your last stage is only 8.9% of the first, so its label has no room.
- Bars start at a shared left edge and their lengths are directly comparable. Trapezoid widths and slopes are hard to judge, and the slanted sides imply a smooth flow between stages that the data doesn't have.

**2. Move the labels outside the marks.**
- Put the stage name on the left, in a column.
- Put the count at the end of each bar.
- Nothing is written inside a shape, so the small bar can't clip its text.

**3. Show one percentage per stage and make it the conversion from the previous stage.**
- Put it in the gap between rows, for example "↓ 64%".
- Investors usually want to know where people drop off, and this shows it directly.
- Keep the percent-of-downloads figure only for the final stage, as a single callout: "8.9% of downloads pay."

**4. Drop the gradient.**
- Use one flat blue, since the stage order is already shown by position.
- Make the "Paid subscription" bar the full-strength blue and the other four a lighter tint of the same hue. That makes the endpoint the focus.
- Leave out gridlines, borders and axis lines. Leave a small gap between rows.

**5. Add a headline that states the takeaway.**
- The numbers show where the funnel leaks. 92% of people who start setup finish it, but only 28% of those who finish pay.
- Suggested title: **"Setup isn't the problem: 72% of users who finish setup don't subscribe."**

## The numbers

| Stage | Users | From previous stage | Of downloads |
|---|---|---|---|
| Downloaded | 12,400 | n/a | 100% |
| Created account | 7,900 | 64% | 64% |
| Added first device | 4,300 | 54% | 35% |
| Finished setup | 3,950 | 92% | 32% |
| Paid subscription | 1,100 | 28% | 8.9% |

## Sketch

```
Wavecrest: setup isn't the problem, 72% of users who finish it don't subscribe

Downloaded            ██████████████████████████████████████  12,400
                                   ↓ 64%
Created account      ████████████████████████                 7,900
                                   ↓ 54%
Added first device   █████████████                            4,300
                                   ↓ 92%
Finished setup       ████████████                             3,950
                                   ↓ 28%
Paid subscription    ███▌                                     1,100   ← 8.9% of downloads
                     (darkest blue; the rest are a lighter tint)
```

## Notes
- If you want to keep the funnel look, a centered version with a straight-sided, uniform-height bar for each stage would also work. Labels would still go outside the bars. I think the left-aligned bars read better, though.
- Text stays in dark gray, not blue. Use a ≥12pt font for the percentages so they're readable on a slide.
- I haven't rendered or color-checked anything. If you send the file or tell me the format (slide, SVG, or HTML), I can build it and check the contrast.
