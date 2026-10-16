The likely cause is proportional figures. Gill Sans, like many humanist sans faces, uses digits of different widths by default (a "1" is narrower than a "0"), so right-aligned numbers don't stack cleanly. The fix is tabular figures, which give every digit the same width and keep the typeface unchanged:

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums;
  text-align: right;
}
```

Add it to both the price and seats cells. The `font-variant-numeric` property is the standard way to request tabular figures. Also check that `font-weight: 600` on prices renders as you expect. Gill Sans often has only regular and bold, so 600 may snap to bold.

If the numbers still don't line up, the installed Gill Sans may lack the `tnum` feature. Two options:

- **Fixed-width digit cells:** set a minimum width in `ch` units, which is based on the width of "0", and keep right alignment:
  ```css
  .plan-table td.price,
  .plan-table td.seats {
    min-width: 6ch;
    text-align: right;
  }
  ```
- **Fallback font for numerals only:** use a tabular-figure face such as Calibri (which has tabular lining figures by default) for the numeric cells, while keeping Gill Sans for the rest of the table.

Commas in "$1,240" and "1,000" will still sit at different positions, which is normal. The digits themselves should now stack in the same columns.
