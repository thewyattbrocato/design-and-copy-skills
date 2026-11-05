I made only a few changes, because your table already follows most good practice. It has right-aligned tabular figures, the currency once in the header, a caption, and `th scope`.

- **Row height:** I raised the row padding from 8px to 12px, so rows are about 46px tall and easier to scan.
- **"Unit" is now "Size":** the column holds weights, diameters and "each", so "Size" says what it is.
- **"Min. order" is now "Min. order (units)":** the minimum is 24 for buns but 2 for tarts, so the header now says it counts items.
- **Scroll wrapper:** I wrapped the table in a horizontally scrolling container so the numbers don't wrap on a phone.
- **No-wrap on numbers:** I added `white-space:nowrap` to the numeric cells for the same reason.

```html
<div style="overflow-x:auto">
<table>
  <caption>Autumn wholesale prices, effective Oct 1. Prices per unit, excluding delivery.</caption>
  <thead>
    <tr><th scope="col" style="text-align:left">Item</th><th scope="col" style="text-align:left">Size</th><th scope="col" style="text-align:right">Price (USD)</th><th scope="col" style="text-align:right">Min. order (units)</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row" style="text-align:left;font-weight:400">Sourdough loaf</th><td>800 g</td><td class="n">4.20</td><td class="n">6</td></tr>
    <tr><th scope="row" style="text-align:left;font-weight:400">Seeded rye</th><td>700 g</td><td class="n">4.60</td><td class="n">6</td></tr>
    <tr><th scope="row" style="text-align:left;font-weight:400">Cardamom bun</th><td>each</td><td class="n">1.35</td><td class="n">24</td></tr>
    <tr><th scope="row" style="text-align:left;font-weight:400">Pear and almond tart</th><td>20 cm</td><td class="n">14.00</td><td class="n">2</td></tr>
    <tr><th scope="row" style="text-align:left;font-weight:400">Pumpkin loaf</th><td>600 g</td><td class="n">6.75</td><td class="n">4</td></tr>
  </tbody>
</table>
</div>
<style>
table{border-collapse:collapse;font:15px/1.4 system-ui,sans-serif}
caption{text-align:left;padding-bottom:8px;color:#444}
th,td{padding:12px 16px 12px 0;border-bottom:1px solid #ddd}
thead th{border-bottom:2px solid #999;vertical-align:bottom}
.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
</style>
```

If you paste this into an email body instead of attaching it as a page, many email clients strip `<style>` blocks. In that case, move the CSS inline on each cell. I can do that conversion if you'd like.
