The table was already in good shape: real markup, right-aligned numbers, tabular figures, one hairline per row, and the unit in the header. I made a few small changes and left the data alone.

```html
<div class="wrap" role="region" aria-labelledby="cap" tabindex="0">
<table>
  <caption id="cap">Autumn wholesale prices, effective Oct 1. Price is per item as sized in the Unit column, excluding delivery.</caption>
  <thead>
    <tr>
      <th scope="col" class="t">Item</th>
      <th scope="col" class="t">Unit</th>
      <th scope="col" class="n">Price (USD)</th>
      <th scope="col" class="n">Min. order (items)</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row" class="t">Sourdough loaf</th><td>800 g</td><td class="n">4.20</td><td class="n">6</td></tr>
    <tr><th scope="row" class="t">Seeded rye</th><td>700 g</td><td class="n">4.60</td><td class="n">6</td></tr>
    <tr><th scope="row" class="t">Pumpkin loaf</th><td>600 g</td><td class="n">6.75</td><td class="n">4</td></tr>
    <tr><th scope="row" class="t">Cardamom bun</th><td>each</td><td class="n">1.35</td><td class="n">24</td></tr>
    <tr><th scope="row" class="t">Pear and almond tart</th><td>20 cm</td><td class="n">14.00</td><td class="n">2</td></tr>
  </tbody>
</table>
</div>
<style>
.wrap{overflow-x:auto;max-width:100%}
table{border-collapse:collapse;font:15px/1.4 system-ui,sans-serif}
caption{text-align:left;padding-bottom:8px;color:#444}
th,td{padding:12px 20px 12px 0;border-bottom:1px solid #ddd;white-space:nowrap}
thead th{border-bottom:2px solid #999}
tbody th{font-weight:400}
.t{text-align:left}
.n{text-align:right;font-variant-numeric:tabular-nums}
td.n:last-child,th.n:last-child{padding-right:0}
caption{white-space:normal}
</style>
```

- **Row order:** I moved the pumpkin loaf up so the loaves sit together, followed by the bun and the tart. If you'd rather keep your original order, move that row back.
- **Header and caption wording:** "Min. order" is now "Min. order (items)". The caption now says price is per item as sized in the Unit column, which fixes the clash between "per unit" and the Unit column.
- **Row height:** Rows are a little taller (12px padding), so they're easier to scan. Prices and minimums still stay on one line.
- **Phones:** The table sits in a scrollable, keyboard-focusable wrapper, so it won't squash on a narrow screen.
- **Styles:** I moved the repeated inline styles into `.t` and `.n` classes. It looks the same, but it's easier to edit.

If this goes out as an email, many mail clients drop `<style>` blocks and classes. Tell me if that's the plan, and I'll give you an inline-styled version.
