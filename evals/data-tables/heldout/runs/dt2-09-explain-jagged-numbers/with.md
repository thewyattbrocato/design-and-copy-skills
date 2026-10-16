The values have different numbers of decimals, and each cell also ends in a unit. Right-alignment lines up the right edge of the text, not the decimal point. Here the right edge is " km", so the digits fall at different places:

```
 1,204.5 km
 98 km
 12,030.25 km
 7.125 km
 640.0 km
```

Two secondary problems can add to the jaggedness:
- **Proportional digits:** if a font draws "1" narrower than "0", digits stop stacking by place value, even with equal decimals. Trebuchet MS and Verdana are usually fine, but I haven't checked how your browser renders them.
- **Mixed precision:** the digits after the point don't line up unless every row has the same number of them.

**Fix**

1. Use the same number of decimals in every row of the column.
2. Move the unit into the header, so the cells hold only numbers.
3. Turn on tabular figures.

```html
<th scope="col" class="num">Distance (km)</th>
...
<td class="num">1,204.50</td>
<td class="num">98.00</td>
<td class="num">12,030.25</td>
<td class="num">7.13</td>
<td class="num">640.00</td>
```

```css
.num {
  text-align: right;               /* header and cells */
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
```

Choose the decimal count by what the reader needs to decide. Two decimals suits most report tables, but it rounds 7.125 to 7.13. If that third digit matters, use three decimals for the whole column. If it doesn't, one or zero decimals gives a cleaner column. Do the rounding in the formatting step, for example `toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})`. The underlying data stays as it is.

If the digits still don't stack after this, the font is the cause. Browsers ignore `tabular-nums` when the font has no such feature. Set just the numeric columns in a font that has it, such as `font-family: system-ui, "Segoe UI", Verdana, sans-serif`, or use a monospaced fallback.

I haven't seen your actual markup, so check the result in your browser. If you share the table's HTML and CSS, I can make the changes directly.
