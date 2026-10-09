**No, don't set the whole board in monospace. Use one proportional sans-serif with tabular lining figures, and put each field in its own fixed column.**

**Why not all monospace**
- Only the numeric fields need to align: flight number, gate and departure time. Cities and status text ("Delayed", "Now boarding") are words, and monospace spaces them unevenly. That slows scanning, and it makes the board look like a terminal.
- Monospace letters are all the same width, so "il" is as wide as "mw". Long city names such as "Ho Chi Minh City" take up more room, which forces smaller type or truncation. On a board that people read from a distance, you want the largest legible size.
- Monospace isn't what makes numbers line up. Column structure does that, and tabular figures handle the digits.

**The approach**
1. Pick a legible proportional sans with tabular lining figures, such as Inter, IBM Plex Sans, Roboto or Source Sans. Turn them on with `font-variant-numeric: tabular-nums lining-nums;`.
2. Give each field its own column, with left-aligned text columns and fixed column widths. Cities and status text align flush-left. Departure time uses tabular figures and always has a fixed format (`09:05`, not `9:05`). Gate and flight number use tabular figures and a consistent format (e.g. `B12`, `UA 0457`, with zero-padding if that's your convention).
3. Don't truncate cities or status text. If a column is too narrow for the longest value, give the column more width instead.
4. Use all caps only for short column headers (DEST, FLIGHT, GATE, STATUS, TIME), with about 0.08em tracking, at a legible size.
5. Use weight, not a different typeface, to separate fields. A bolder weight for the time and a regular weight for the rest works well.

**One exception:** if your brand typeface has no tabular figures, set only the flight number, gate and time in a monospace or system face that does, and leave the rest in the brand face. Don't change the whole board to fix the digits.

If you share the current CSS or mockup, I can check the column widths and figure settings.
