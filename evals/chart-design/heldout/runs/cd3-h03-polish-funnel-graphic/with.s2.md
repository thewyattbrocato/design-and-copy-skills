Here's what I'd change. The short version is to drop the trapezoids and use plain horizontal bars.

## Why it looks cluttered and the bottom stage is unreadable

- **The shape carries the number.** Each trapezoid's width is the value, so Paid subscription (1,100) is about 9% as wide as Downloaded. The label has to fit inside that sliver.
- **Trapezoid slopes mislead.** The edges taper toward the next stage, so the eye reads area and slope, not width. Finished setup (3,950) looks almost the same as Added first device (4,300), but the connecting slopes make the step look bigger or smaller than it is.
- **The gradient adds ink without data.** Every label also sits on a changing background.

## What I'd change

1. **Use horizontal bars in stage order, left-aligned on a common zero.** Length on a shared baseline is the easiest thing to compare. The 1,100 bar is short but still visible, and its label doesn't depend on the bar's size.
2. **Put the text outside the bars.** Stage names go on the left. The count goes at the end of each bar, with the step conversion beside it. Nothing is squeezed inside a shape.
3. **Show two percentages and label them differently.**
   - Step conversion is the share who made it from the previous stage. It's the useful number because it shows where people drop off.
   - Share of downloads is a quiet secondary number. It's only needed for the headline, so I'd show it just on the last row.
4. **Use one flat blue.** Drop the gradient. Use a mid-blue for stages 1–4 and a darker or more saturated blue for the last bar, since that's the one investors care about.
5. **Title with the finding.** Something like "9% of Wavecrest downloads become paying subscribers". The title does the emphasis, so the chart needs no extra callouts.
6. **Add one quiet source line.** I don't have the period, as-of date or source, so I've left them as placeholders for you to fill in.

## Numbers

| Stage | Count | Step conversion | % of downloads |
|---|---|---|---|
| Downloaded | 12,400 | n/a | 100% |
| Created account | 7,900 | 64% | 64% |
| Added first device | 4,300 | 54% | 35% |
| Finished setup | 3,950 | 92% | 32% |
| Paid subscription | 1,100 | 28% | 9% |

## Sketch

```
9% of Wavecrest downloads become paying subscribers

Downloaded          ████████████████████████████████████████  12,400
Created account     █████████████████████████▌                 7,900   64% of previous
Added first device  █████████████▉                             4,300   54%
Finished setup      ████████████▊                              3,950   92%
Paid subscription   ███▌  (darker blue)                        1,100   28%   = 9% of downloads

Bars start at zero and share one scale.
[Period] · [as of date] · Source: [source]
```

## What the chart shows

- Setup is not the problem. 92% of people who add a device finish setup.
- The biggest relative drop is the last step. Only 28% of people who finish setup subscribe.
- The biggest drop in headcount is the first step, with 4,500 people lost between download and account creation.

If investors will ask "where do we lose people?", I'd add a small "−4,500 / −3,600 / −350 / −2,850" note between the bars. I left it out because it adds clutter. Say so if you want it.

## If you want to keep the funnel look

Keep the funnel only if the narrowing shape is part of your deck's style. If so, make these changes:

- Use rectangles centered on a vertical axis, not trapezoids.
- Put every label outside the shape.
- Set a minimum height for the bottom stage.

The bottom stage would still be tiny, though, and the bar version reads better.

If you share the file or the SVG source, I can make these edits directly.
