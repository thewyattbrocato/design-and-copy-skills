**Use a line chart, and it's fine for the y axis not to start at zero.**

**Why a line chart**
- Your question is whether the numbers are growing, which is a trend over time. A line shows direction and slope, and the eye follows it easily from week to week.
- Bars are better for comparing separate categories or showing totals. With 12 sequential points, 12 bars add visual weight without adding information.
- An area chart is a line with a filled region. The fill suggests cumulative volume, and it adds nothing here unless you're stacking segments, such as new vs. returning users.

**Y axis**
- The zero-baseline rule is strict for bar charts, because bar length encodes value. Truncating a bar axis exaggerates differences.
- For a line chart, position and slope carry the message, so a non-zero baseline is acceptable. Your data runs from 41 to 75, and a zero baseline would compress the movement into the top part of the plot.
- Starting at zero would still be honest, and the growth is large enough (about 83%) to read clearly either way. If the audience is non-technical, or the chart might be read as "how big is this," zero is the safer choice. If you want to show the week-to-week shape, use something like 30–80.
- If you truncate the axis, label the ticks clearly and don't make the scale so tight that small dips like weeks 3 and 7 look dramatic.

**Making the growth claim clearer**
- Label the first and last points directly (41K → 75K) instead of relying on gridlines.
- Add a subtitle with the takeaway, such as "Weekly active users up 83% in 12 weeks."
- Consider a light trend line, since the series is slightly noisy (small dips in weeks 3, 6, and 9).

I can build the chart if you tell me the format you want (matplotlib, HTML, etc.).
