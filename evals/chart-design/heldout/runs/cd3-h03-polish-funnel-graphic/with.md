I haven't seen the image, only your description, so these changes are based on that. My main recommendation is to turn the funnel into horizontal bars. A trapezoid funnel makes the reader judge area and slant, and its widths rarely match the numbers. The bars give each stage its own readable label. The last stage is 9% of the first, so it can't be tiny and unreadable.

**What I'd change**

1. **Use flat bars in stage order, not trapezoids.** Bar length is proportional to the count, starting at zero. Left-align them, which makes the lengths easier to compare than centered shapes.
2. **Move the labels outside the shapes.** Put the stage name on the left. Put the count and conversion to the right of each bar. Nothing sits inside a shape, so the small last bar stays readable.
3. **Show two percentages and label them.** Your current label is probably percent of the top stage. The step conversion (from the previous stage) is what shows where people drop off, so I'd show both: "63.7% of previous" and "% of downloads".
4. **Drop the blue gradient.** Use one flat color for all bars. Make the Paid subscription bar a darker or stronger blue, since it's the outcome investors care about.
5. **Add a headline that states the finding.** The data supports: "Only 28% of people who finish setup go on to pay."
6. **Add a quiet source line.** For example: "Wavecrest app, [period], as of [date], source: [source]." I left placeholders because you didn't give me those.

**The numbers**

| Stage | Count | % of downloads | Step conversion |
|---|---|---|---|
| Downloaded | 12,400 | 100% | n/a |
| Created account | 7,900 | 63.7% | 63.7% |
| Added first device | 4,300 | 34.7% | 54.4% |
| Finished setup | 3,950 | 31.9% | 91.9% |
| Paid subscription | 1,100 | 8.9% | 27.8% |

The two big drop-offs are account to first device (45.6% lost) and setup to paid (72.2% lost). Once people add a device, they almost always finish setup (92%). I'd put a small note on the chart at those two steps.

**Sketch**

```
Only 28% of people who finish setup go on to pay

Downloaded          ████████████████████████████████████████  12,400   100%
Created account     ██████████████████████████                 7,900   64%   (64% of prev.)
Added first device  ██████████████                             4,300   35%   (54% of prev.)
Finished setup      █████████████                              3,950   32%   (92% of prev.)
Paid subscription   ████                                       1,100    9%   (28% of prev.)

Wavecrest app, [period], as of [date], source: [source]
```

**If you want to keep the funnel shape**

You can keep it centered, but make these changes:
- Use plain rectangles, or trapezoids whose top width is the stage's own count, so the widths match the data.
- Put all the text outside the shapes.
- Use one flat color with the last stage highlighted.
- Add the step-conversion labels between stages.

It will look more like a funnel, but it will be harder to compare stages than with the bars.

If you send me the file or the underlying data, I can build the cleaned-up version as an SVG or PNG.
