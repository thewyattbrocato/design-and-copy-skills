The tiny bottom stage isn't a styling flaw. Paid subscription is 1,100 of 12,400, or 8.9%, so a shape scaled honestly to the data will be small. Fix the layout so a small stage can still be read, and don't enlarge the shape to fit the text.

**What I'd change**

1. **Use flat bars instead of trapezoids.** Each sloped edge implies a smooth taper between stages that the data doesn't have. Make each stage a rectangle, centered, with width proportional to its count. Downloaded is 100%. Created account is 64%, Added first device 35%, Finished setup 32%, and Paid subscription 9% of that width.
2. **Move all text outside the shapes.** Stage names go in a left column, right-aligned. Counts and conversion go in a right column. The 9% bar can then be thin and still fully readable.
3. **Show one percentage per row.** It should be the step conversion, meaning the share of the previous stage that moved on. Don't also print percent-of-downloads on every row, which is probably the clutter you're seeing. Give the overall figure once, in the subtitle.
4. **Use one flat blue.** Drop the gradient, since it adds shading that carries no data. Use mid-blue for stages 1–4 and a darker or more saturated blue for Paid subscription, because that's the number investors care about.
5. **Add a headline that states the finding.** The data supports this: **"Only 28% of users who finish setup go on to pay."** Setup itself is healthy at 92%, so the problem is the step to payment.
6. **Add a source line.** Use something like "Wavecrest app, [period], as of [date], source: [source]". I don't have your period, date or source, so I left them as placeholders.

**Step conversions (recomputed from your counts)**

| Stage | Count | Step conversion |
|---|---|---|
| Downloaded | 12,400 | n/a |
| Created account | 7,900 | 64% |
| Added first device | 4,300 | 54% |
| Finished setup | 3,950 | 92% |
| Paid subscription | 1,100 | 28% |

Overall, 8.9% of downloads became paid.

**Sketch**

```
Download to paid: 8.9% overall
Only 28% of users who finish setup go on to pay

                 ┌────────────────────────────────┐
 Downloaded      │████████████████████████████████│  12,400
                 └────────────────────────────────┘
                    ┌────────────────────────┐
 Created account    │████████████████████████│        7,900   64%
                    └────────────────────────┘
                         ┌──────────────┐
 Added first device      │██████████████│              4,300   54%
                         └──────────────┘
                          ┌─────────────┐
 Finished setup           │█████████████│              3,950   92%
                          └─────────────┘
                              ┌────┐
 Paid subscription            │████│ (darker blue)    1,100   28%
                              └────┘

 % = share of the previous stage.
 Wavecrest app, [period], as of [date], source: [source]
```

Bars should have a small, even gap between them, with no connecting slopes.

**Alternative:** If you're open to dropping the funnel silhouette, left-aligned horizontal bars would be easier to read. A shared left edge lets people compare lengths directly, and the 9% bar sits next to the 100% bar at the same baseline. The content would be identical. The centered version above keeps the funnel look you wanted, so I'd go with that unless you want the more precise one.

If you share the file or the colors you used, I can give exact hex values and spacing.
