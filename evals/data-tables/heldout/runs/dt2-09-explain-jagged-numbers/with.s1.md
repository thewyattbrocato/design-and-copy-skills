The jaggedness comes from the data, not the alignment. Right-alignment lines up the *end* of each string, but the values have different numbers of decimals (0, 1, 2 and 3) and each one is followed by " km". The decimal points land in a different place on every row, and so do the digits of the same place value. For example, the 4 in 1,204.5 doesn't sit above anything meaningful in the next row.

**The fix has three parts:**

1. **Use the same number of decimals in every row.** Pick the fewest digits that support the comparison. For distances, 1 or 2 is probably plenty:

   ```
    1,204.50
       98.00
   12,030.25
        7.13
      640.00
   ```
   Use 3 decimals only if 7.125 has to stay exact. Format with something like `toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})` so the formatter, not the data, controls the digits.

2. **Move the unit into the header and drop it from the cells.** Use "Distance (km)" as the header. A repeated "km" adds a trailing suffix that has to line up too. It's also the clutter that makes the column hard to scan.

3. **Turn on tabular figures** so every digit has the same width and digits stack by place value:

   ```css
   td.num, th.num {
     text-align: right;
     font-variant-numeric: tabular-nums;
   }
   ```
   Put the `num` class on the header cell as well, so the header's alignment matches its data. Verdana and Trebuchet MS both generally have fixed-width digits, so this is mostly a safeguard. If the digits still look uneven in your rendering, set that column in a face with real tabular figures.

If the units really do differ by row (some km, some m), keep the unit in the cell. In that case, align on the number, for example with the unit in a separate narrow column or a fixed-width span.

I haven't seen your markup, so I haven't checked whether another style, such as `text-align: center` on a wrapper or `white-space` rules, is overriding the right-alignment. If it's still jagged after these changes, send me the table's HTML and CSS.
