Here's what I'd change. I haven't seen the file, so I'm working from your description.

**Changes**

1. **Make width mean the count.** Each stage becomes a flat rectangle, and its width is proportional to its count on one shared scale (12,400 = full width). Sloping trapezoids make the reader guess whether the slope or the width carries the number. Rectangles remove that guess. If your current widths aren't proportional, fix that first, because it's the most important change.
2. **Move all text outside the shapes.** Stage names go on the left, aligned. The count and the step conversion go on the right. Nothing sits inside a shape, so the 1,100 stage no longer has a label problem.
3. **Don't pad the bottom stage.** Paid is 8.9% of downloads, so it really is narrow. Inflating it would misstate the drop. With its label outside it's readable, and the narrowness is the story.
4. **Drop the gradient.** Use one flat blue for every stage. Use a darker shade, or an accent color, only on the Paid stage, since that's the one you want people to look at.
5. **Show two percentages, not one.** Each row gets its step conversion ("64% of previous"). The cumulative share of downloads appears only on the last row (8.9%). A single unlabeled percentage per stage is probably part of the clutter now.
6. **Use a title that states the finding.** Add a thin gap between stages and a quiet source line. I've left bracketed placeholders because you didn't give me a period, date, or source.

**Result**

```
Of 12,400 downloads, 1,100 (9%) become paying subscribers.
The steepest step is setup → paid: 72% of finished setups don't convert.

                 ████████████████████████████████████████   12,400
Downloaded

                    █████████████████████████████████         7,900   64% of previous
Created account

                         ████████████████████████              4,300   54%
Added first device

                          ███████████████████████              3,950   92%
Finished setup

                                  ██████                       1,100   28%   (8.9% of downloads)
Paid subscription

Wavecrest app, [period], as of [date], source: [source]
```

In the real graphic the stage names sit in a left column, the bars are centered on one axis, and the numbers sit in a right column. Every stage is the same flat blue except Paid, which is the darker accent.

**What the numbers show**
- The step conversions are 64%, 54%, 92% and 28%.
- Device → setup is nearly lossless, so setup isn't a problem.
- The worst rate is setup → paid. The largest absolute loss is download → account (4,500 people).
- Decide which of those two you want the headline to be. I used the rate because it's the sharper drop.

**An alternative.** Shape and width are a weak way to compare five values. Left-aligned horizontal bars with the same labels would be easier to read, especially the 3,950 vs 4,300 pair, which look almost the same in a centered funnel. I kept your centered look because you asked for a cleanup of the funnel. I can draw the left-aligned version if you want it.
