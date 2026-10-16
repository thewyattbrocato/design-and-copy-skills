Right-aligning lines up the right edge of each string, which is the "km". The decimal points sit in different places because the values have different numbers of decimal places (0, 1, 2 and 3). The digits then sit at different offsets from the right, so the place values don't stack.

There are two fixes, and you'll probably want both.

**1. Use the same number of decimals in every row.**

```js
const fmt = new Intl.NumberFormat("en-US", {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});
fmt.format(7.125); // "7.13"
```

Pick the precision deliberately. Your data goes to 3 decimals (7.125), so 2 would round it. If that matters, use 3 for every row.

**2. Force tabular (fixed-width) digits.**

```css
td.distance {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

Many fonts use proportional digits, where "1" is narrower than "0". Even with matching decimals, the columns then drift slightly. `tabular-nums` makes every digit the same width. It only works if the font has tabular figures. Verdana's digits are already fixed-width, but I'm not certain about Trebuchet MS. Since the stack can fall through to `sans-serif`, which could be any system font, keep the property so the result doesn't depend on which font loads.

**Optional: move the unit into the header.** Put "Distance (km)" in the header and drop " km" from each cell. If you want to keep the unit in the cell, give it its own fixed-width span so it can't shift the numbers:

```html
<td class="distance">1,204.50<span class="unit">km</span></td>
```
```css
.unit { display: inline-block; width: 2.5em; text-align: left; margin-left: .25em; }
```

After the changes, the column would look like this:

```
 1,204.500
    98.000
12,030.250
     7.125
   640.000
```

Every decimal point and every place value now lines up.
