I can't see the image. Nothing came through in this conversation, so this is based on your description and numbers. If you attach it, I can check the specifics.

## What I'd change

1. **Replace the trapezoids with horizontal bars.** The bars are left-aligned and their lengths are proportional to the counts. Trapezoids make readers judge area and slanted edges, and they force the narrow stages to hold their own label. The bottom stage is unreadable because its label has to fit inside a shape that is 9% as wide as the top one. Bars fix that, and a bar at 9% of the track is still a clear, visible bar.
2. **Move all text out of the shapes.** The stage name goes on the left, in a fixed column. The count and percentage go to the right of each bar. Nothing needs to fit inside a shape, so nothing gets cramped.
3. **Drop the gradient.** Use one flat blue for all bars. A gradient implies a second variable, and the bar length already shows the drop. Put a 2px gap between rows. Keep the bars thin, with a 4px rounded right end.
4. **Cut each row to two numbers.** Show the count and the percentage of downloads. Right now the percentage label could mean either of two things, so say which one it is. I'd use "% of downloads" in the column header and keep it consistent.
5. **Show step-to-step conversion once, as muted text between rows.** The investor question is where people drop off, and this answers it directly. Keep it small and gray so it doesn't compete with the bars.
6. **Use one accent for the story.** Make the Paid subscription bar a darker blue, or the only saturated one. Everything else stays a mid-light blue. Text stays in dark gray, never blue.
7. **Remove the extras.** Cut borders, shadows, and the gridlines or axis. The labels carry the values, so the plot doesn't need an axis.

## The numbers

| Stage | Count | % of downloads | Step conversion |
|---|---|---|---|
| Downloaded | 12,400 | 100% | n/a |
| Created account | 7,900 | 63.7% | 63.7% |
| Added first device | 4,300 | 34.7% | 54.4% |
| Finished setup | 3,950 | 31.9% | 91.9% |
| Paid subscription | 1,100 | 8.9% | 27.8% |

The most useful point for investors is that setup is not the leak. Almost everyone who adds a device finishes setup (92%). The two big drops are account to first device (54%) and setup to paid (28%). Your current graphic hides that second drop in the tiny bottom shape.

## Sketch

```
Wavecrest conversion funnel                    % of downloads

Downloaded          ████████████████████████████████  12,400   100%
                                          ↓ 64%
Created account     ████████████████████              7,900    64%
                                          ↓ 54%
Added first device  ███████████                       4,300    35%
                                          ↓ 92%
Finished setup      ██████████                        3,950    32%
                                          ↓ 28%
Paid subscription   ███  (darker blue)                 1,100     9%
```

In the real version:
- The stage-name column is fixed-width and right-aligned, and the bars start at one shared left edge.
- The counts and percentages sit in two aligned columns at the right, so they scan like a table.
- The step-conversion arrows are small gray text, indented under the bars.
- The title says what the graphic shows, for example "Only 9% of downloads become paying subscribers", with the stage detail below it.

## If you want to keep the funnel silhouette

You could keep a centered, tapered look, but then:
- Make each shape's width proportional to its count, and don't use a fixed taper.
- Keep the labels outside.
- Use one flat color.

You'd still get the tiny bottom shape, so I'd go with the bars.

I can build this as an SVG or HTML file you can drop into the deck. If you tell me your slide background (light or dark) and any brand blue, I'll use those.
