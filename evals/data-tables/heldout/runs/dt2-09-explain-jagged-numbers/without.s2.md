Right-alignment lines up the right edge of each cell, which here is the "km". It doesn't line up the decimal points. The rows have 0, 1, 2 and 3 decimal places, so the same digit position sits in a different column on each row:

```
 1,204.5 km      decimal point at 4 chars from the unit
    98 km        no decimal point
12,030.25 km     decimal point at 5 chars from the unit
     7.125 km    decimal point at 6 chars from the unit
   640.0 km      decimal point at 4 chars from the unit
```

The font stack isn't the cause. Verdana's digits are already fixed-width, and Trebuchet's mostly are. It's worth adding a safeguard for that, though.

**Fix**

1. **Format every value with the same number of decimals.** Use 3, the most any row has, so nothing gets rounded:
   ```
    1,204.500 km
       98.000 km
   12,030.250 km
        7.125 km
      640.000 km
   ```
   In JS, `n.toLocaleString('en-US', { minimumFractionDigits: 3, maximumFractionDigits: 3 })`. Server-side, use the equivalent fixed-precision formatter. If 3 decimals is more precision than readers need, round to 1 or 2, but do it consistently.

2. **Force tabular digits in the cell CSS** so the digit widths are guaranteed equal, even if the font falls back to something else:
   ```css
   td.numeric {
     text-align: right;
     font-variant-numeric: tabular-nums;
   }
   ```

3. **Optional: move "km" into the column header**, as in "Distance (km)". The unit then stops being the right edge, and the numbers end flush with each other.

After step 1, the decimal points line up in a straight vertical line. Step 2 keeps the digits and commas from drifting if the font changes.
