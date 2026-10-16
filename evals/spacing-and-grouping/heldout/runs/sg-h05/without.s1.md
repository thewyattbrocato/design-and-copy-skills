**Recommendation: a 1px divider line between rows**, in a low-contrast neutral color.

**Why it fits this case**
- **Scanning across columns:** Each row has date, merchant and amount. Users compare amounts and dates down the list and then trace back across to the merchant. A hairline gives the eye a clear horizontal track without adding visual noise.
- **Density:** With 30 rows, a line costs about 1px per row. Extra spacing would make the list noticeably longer and add scrolling.
- **Low clutter:** Financial UIs benefit from calm, quiet surfaces. A subtle line is the lightest separator that still groups each row clearly.

**Why not the others**
- **Alternating backgrounds (zebra stripes):** These work in wide, many-column tables where the eye has to travel far. A 3-field mobile row is short, so stripes add contrast noise. They also complicate selected, pressed and pending states, and they behave badly in dark mode and with accessibility settings such as high contrast.
- **Extra space only:** Whitespace alone is a weak grouping cue when the rows are uniform. Dates and amounts on adjacent rows can blur together, and it lengthens the list.

**Implementation tips**
- Use a divider color with roughly 10–15% contrast against the background. It should be visible but not dominant.
- Inset the line to align with the text start, not the screen edge. This is the iOS convention, and it looks cleaner.
- Keep row height at 56–64px with consistent vertical padding. That gives enough breathing room that the line is the only separator you need.
- Right-align amounts and use tabular (monospaced) numerals so digits line up.
- If the list is grouped by day, use a date header and skip repeating the date on each row. That reduces the need for separators even more.

If you ever need to test it, run a quick A/B on how fast users find a specific transaction. I'd expect the 1px line to win or tie.
