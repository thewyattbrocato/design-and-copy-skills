Your finding is that Dunmore climbed while the other five stayed flat. The chart should make that one thing obvious.

**1. Make Dunmore the only colored line.**
- Draw the other five in the same light gray, thin and unlabeled by color.
- Draw Dunmore in one strong accent color, thicker than the rest.
- The default six-hue palette gives every clinic equal weight, so the eye has nothing to land on. Gray context plus one accent fixes that.

**2. Label lines directly and delete the legend.**
- Put "Dunmore" in the accent color at the end of its line.
- Label the gray lines at their right ends in gray text, or with one note like "Other 5 clinics". Names are optional if nobody needs to pick out a specific clinic.
- Removing the legend also gives the plot the full width, and nobody has to match colors across the page.

**3. Mark the two numbers that matter.**
- Put "42" at Q1 2023 and "71 min" at Q4 2025 on Dunmore's line.
- If you can, shade or mark the 35–50 band the others stay within. That makes the gap visible, and it's the comparison your point depends on.

**4. Change the title to the finding.**
- Replace "Wait Time by Clinic" with something like "Dunmore ER waits rose from 42 to 71 minutes while five other clinics held at 35–50".
- Add a subtitle with the unit: "Average ER wait, minutes, Q1 2023 – Q4 2025".

**5. Quiet the structure.**
- Remove most gridlines. Keep a few faint horizontal ones, or none if the end values are labeled.
- Drop the plot frame.
- Label the y-axis in minutes.
- Lines can use a non-zero baseline, but if you zoom, say so on the axis. A 0–80 axis is safe here and still shows the rise clearly.
- Make the chart wider than tall, so the climb reads as a slope and not a cliff.

**6. Accessibility.**
- Don't rely on color alone. Dunmore's thicker line, its label and its end values already carry the point.
- Put the takeaway in the surrounding text or alt text, and keep the data available as a table.

**If viewers need to read the other clinics individually,** use small multiples instead. That means six small panels with a shared y-axis, with Dunmore highlighted in its panel. If they don't, one chart with gray context is cleaner.

I can write the code if you tell me what you're using (matplotlib, Excel, Plotly, etc.) or paste the data.
