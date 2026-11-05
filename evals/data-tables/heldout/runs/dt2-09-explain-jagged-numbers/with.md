**Cause:** right alignment lines up the right edge of each string. Your values have 0, 1, 2 and 3 decimals, so the decimal points land in different places. `98 km` has no decimal at all, and the trailing ` km` shifts things further. The column ends up looking jagged even though every row is right-aligned.

**Fix:**

1. **Use the same number of decimals in every row.** Pick the fewest digits that support the comparison. For example, 1 decimal gives `1,204.5`, `98.0`, `12,030.3`, `7.1`, `640.0`. If the exact values matter, use 3 decimals instead: `98.000`, `7.125`, `12,030.250`. Either way the decimal points stack.
2. **Move the unit to the header,** `Distance (km)`, and leave the cells as bare numbers.
3. **Turn on tabular figures,** so each digit takes the same width and place values stack:

```css
td.num, th.num {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

Apply `class="num"` to both the header and the cells so the header aligns with its data.

With 1 decimal, the column becomes:

```
Distance (km)
    1,204.5
       98.0
   12,030.3
        7.1
      640.0
```

Verdana's digits are already fixed-width, so the decimal count is almost certainly the main problem. I'm less sure about Trebuchet MS. `tabular-nums` does nothing if the font has no tabular figures. If the digits still don't stack, set that column in a face that has them, such as `font-family: Verdana, sans-serif` or a system UI font.

If you need to keep each row's own precision, you can align on the decimal point instead. Split the number into integer and fraction spans, or pad the missing decimals. Fixed decimals is simpler and reads better.
