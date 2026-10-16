Your numbers are almost certainly left-aligned (or centered), so the digits don't line up by place value. Fix it by right-aligning the column, and use tabular (monospaced) digits so each digit has equal width.

In CSS:
```css
td.total { text-align: right; font-variant-numeric: tabular-nums; }
```
