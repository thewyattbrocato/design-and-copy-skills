I kept the content and order the same. The table was already in good shape, with a real caption, `th scope`, right-aligned numbers and tabular figures. I only tightened the spacing, moved the repeated inline styles into the stylesheet, and made it hold up on a phone.

```html
<div class="table-wrap" role="region" aria-labelledby="price-caption" tabindex="0">
  <table>
    <caption id="price-caption">Autumn wholesale prices, effective Oct 1. Prices per unit, excluding delivery.</caption>
    <thead>
      <tr>
        <th scope="col">Item</th>
        <th scope="col">Unit</th>
        <th scope="col" class="num">Price (USD)</th>
        <th scope="col" class="num">Min. order (units)</th>
      </tr>
    </thead>
    <tbody>
      <tr><th scope="row">Sourdough loaf</th><td>800 g</td><td class="num">4.20</td><td class="num">6</td></tr>
      <tr><th scope="row">Seeded rye</th><td>700 g</td><td class="num">4.60</td><td class="num">6</td></tr>
      <tr><th scope="row">Cardamom bun</th><td>each</td><td class="num">1.35</td><td class="num">24</td></tr>
      <tr><th scope="row">Pear and almond tart</th><td>20 cm</td><td class="num">14.00</td><td class="num">2</td></tr>
      <tr><th scope="row">Pumpkin loaf</th><td>600 g</td><td class="num">6.75</td><td class="num">4</td></tr>
    </tbody>
  </table>
</div>
<style>
.table-wrap{overflow-x:auto;max-width:100%}
table{border-collapse:collapse;font:15px/1.4 system-ui,sans-serif;min-width:480px}
caption{text-align:left;padding-bottom:12px;color:#444}
th,td{padding:12px 20px 12px 0;border-bottom:1px solid #ddd;text-align:left}
thead th{border-bottom:2px solid #999;font-weight:600;vertical-align:bottom}
tbody th{font-weight:400}
.num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
th.num,td.num:last-child{padding-right:0}
</style>
```

- **Spacing:** Rows are taller (12px padding instead of 8px), so they're easier to scan. The hairlines, the heavier rule under the header, and the right-aligned numbers stay as they were.
- **Styles:** The inline styles are now `.num` and `tbody th` rules, which makes later edits easier.
- **Phones:** The table scrolls sideways inside its wrapper instead of squashing the numbers. The wrapper is keyboard-focusable and labelled by the caption.
- **Header:** "Min. order" is now "Min. order (units)". That makes it clear the 24 for buns means 24 buns and the 2 for tarts means 2 tarts.

**Check before sending:** the caption says "effective Oct 1", but today is Oct 15, so that date has already passed. If the prices have been live since then, you may want to say so. Adding the year, such as "Oct 1, 2026", would also stop it being misread next autumn. I left the wording alone since I don't know which you mean.
