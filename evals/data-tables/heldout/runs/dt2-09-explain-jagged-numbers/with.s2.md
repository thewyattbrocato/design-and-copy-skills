Right-aligning only lines up the right edge of each cell. Two things are still breaking the column.

1. **The decimal places vary.** The rows have 1, 0, 2, 3 and 1 decimal places. With right alignment the decimal point lands in a different spot on each row, so `98 km` and `7.125 km` don't line up by place value.
2. **The unit is inside every cell.** The right edge is now the `km` suffix, not the digits. `98 km` and `640.0 km` also have different suffix offsets relative to their numbers.

Digit widths can matter too. If the font draws `1` narrower than `0`, digits won't stack even when the decimals match.

## Fix

1. **Use one precision for the whole column.** `7.125` is your most precise value. If you must keep every value exactly as is, pad to 3 decimals. If 1 or 2 decimals is enough for the decision, round to that instead, but that changes some displayed values (`7.125` becomes `7.13`).
2. **Move the unit to the header** (`Distance (km)`) and leave the cells as bare numbers.
3. **Turn on tabular figures** so every digit has the same width.

```css
th.num,
td.num {
  text-align: right;
  font-variant-numeric: tabular-nums lining-nums;
}
```

```html
<th scope="col" class="num">Distance (km)</th>
...
<td class="num">1,204.500</td>
<td class="num">98.000</td>
<td class="num">12,030.250</td>
<td class="num">7.125</td>
<td class="num">640.000</td>
```

Verdana has tabular digits by default. I'm not sure Trebuchet MS does, and `tabular-nums` only takes effect if the font supports it. If the digits still look uneven after the change, set just this column in Verdana. You can also use a system face with tabular figures, such as `ui-monospace` or `system-ui`.

Format the numbers with the same call in every row (for example `toLocaleString('en-US', {minimumFractionDigits: 3, maximumFractionDigits: 3})`). That way no row gets a different number of decimals.
