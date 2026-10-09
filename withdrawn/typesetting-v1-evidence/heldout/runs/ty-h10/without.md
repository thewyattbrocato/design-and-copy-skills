**No, don't use monospace for the whole board. Use a proportional sans-serif with tabular numerals, and make the codes visually distinct.**

**Why not all monospace**
- Only a few columns benefit from alignment: times, gates and flight numbers. Destination cities and status text ("Delayed", "Now Boarding") are words, and monospace makes them wider and slower to scan.
- Wider text means fewer characters per row. Long city names like "Ho Chi Minh City" or "Frankfurt am Main" then truncate or force a smaller size, which hurts legibility from a distance.
- Monospace letterforms have uneven spacing (a narrow "i" gets the same width as an "m"). That is worse for reading words at a glance.

**What to do instead**
1. **Main typeface:** a highly legible proportional sans-serif built for signage or UI. Good options are Inter, Frutiger, Helvetica Neue, Roboto or Atkinson Hyperlegible. Use it for cities and status text.
2. **Numbers:** turn on tabular lining figures, so every digit has the same width and times and gates stack cleanly. In CSS that is `font-variant-numeric: tabular-nums lining-nums;`. Check that your chosen font supports it, since most good UI fonts do.
3. **Flight numbers and gates:** keep these in the same family but with tabular figures and slightly wider letter-spacing. This avoids confusing `0/O`, `1/I/l` and `5/S`. If the font has a slashed or dotted zero, use it. Only if you can't get that in the main font should you use a monospace face for just these two columns.
4. **Columns:** give each column a fixed width and align it deliberately. Times and gates go right-aligned or centered, and text goes left-aligned. This does more for alignment than a font choice does.
5. **Status:** don't rely on font changes to signal status. Use color plus a weight change or icon, so it still works for colorblind users and in glare.

This gives you the number alignment the proposal is after, and the text stays fast to read.
