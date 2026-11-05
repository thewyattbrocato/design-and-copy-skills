I'd replace the trapezoids with horizontal bars. I'm swapping the form rather than polishing it because the tiny bottom stage comes from the shape itself. A funnel's width and area stand in for the count, and 1,100 against 12,400 is always going to be a sliver. A label can't fit inside a sliver. The shape also hides the number an investor cares about most, which is how many people drop out between stages.

## What I'd change

1. **Use horizontal bars in stage order.** Bars start at zero, share one scale and are left-aligned, so lengths compare directly. Keep the top-to-bottom order so it still reads as a funnel.
2. **Move the labels outside the bars.** The stage name goes at the left and the count at the bar tip. Nothing has to fit inside a shape, so the last stage is as legible as the first.
3. **Add a step-conversion column on the right.** This replaces the percentage you had inside each shape. Each figure is the share that made it from the previous stage, which shows where people leak out.
4. **Drop the gradient.** Use one flat color for the bars and a stronger accent on "Paid subscription", since that's the stage investors will look at. A gradient implies a second quantity that isn't in the data.
5. **Remove the decoration.** No frame, gridlines, shadows or axis. The printed values make an axis redundant.
6. **Write the title as the finding.** For example: *"9% of downloads become paying subscribers. The steepest drop is between finished setup and paying."*
7. **Add a provenance line.** Put the unit, period, as-of date and source under the chart. You haven't given me those, so I'd leave `[period]`, `[as of date]` and `[source]` as visible placeholders for you to fill in.

## Sketch

```
9% of downloads become paying subscribers.
The steepest drop is between finished setup and paying.

                                            Count    Step conversion
Downloaded          ████████████████████████████████████████  12,400
Created account     █████████████████████████                  7,900    64% of previous
Added first device  ██████████████                             4,300    54%
Finished setup      █████████████                              3,950    92%
Paid subscription   ████  (accent color)                       1,100    28%

Users, [period], as of [date]. Source: [source].
```

Bar lengths are drawn to scale. The values behind the right-hand columns:

| Stage | Count | Of previous stage | Of downloads |
|---|---|---|---|
| Downloaded | 12,400 | n/a | 100% |
| Created account | 7,900 | 64% | 64% |
| Added first device | 4,300 | 54% | 35% |
| Finished setup | 3,950 | 92% | 32% |
| Paid subscription | 1,100 | 28% | 9% |

## What the chart shows

- **Biggest relative drop:** 72% of people who finish setup never pay. That's why I'd put the accent on the last bar and use it in the title.
- **Biggest drop before setup:** 46% of new accounts never add a device.
- **Healthy step:** 92% of people who add a device finish setup, so the setup flow itself isn't losing people.

If you'd like a "Of downloads" column as well, it fits next to the step conversion. I'd keep only one of the two in the main view, because showing both gets cluttered again. I'd keep the step conversion, since it points to where the problem is.

I can also write this as an SVG or HTML file if you want something to drop into the update.
