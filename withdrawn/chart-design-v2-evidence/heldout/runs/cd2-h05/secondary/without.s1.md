Mostly no. The zero-baseline rule applies to bar charts, where bar length is the encoded value, so truncating the axis makes differences look bigger or smaller than they are. A line chart encodes value by position and slope, so a non-zero baseline is standard practice. Plenty of time-series charts (stock prices, temperature, sensor data) don't start at zero.

Your 20 to 26 range is reasonable for data between 21.4 and 24.9. It fits the data with a little margin, and the trend is readable.

A few things would make the chart clearer and address her concern:

- **Label the axis clearly** with units ("Water temperature (°C)") and keep the tick labels visible so no one has to guess the baseline.
- **Mention the range in the title or caption**, for example "Lake Verity, July daily water temperature (21.4–24.9 °C)."
- **Don't go much narrower.** A 20 to 25 axis would exaggerate the day-to-day swings, which is where the real misreading risk is.

If the audience is likely to read the chart as showing dramatic change, or if you want to convey that temperatures were stable, a wider axis like 0 to 30 would flatten the line. That's a legitimate choice, but it's a choice about the message, not a rule that the axis must start at zero. If you want to settle it with your coworker, you could show both versions and see which one matches the point you're making.
