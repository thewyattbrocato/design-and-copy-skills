I changed very little, because the table already followed most of the good habits: a real caption, `th scope`, right-aligned numbers, and the currency stated once in the header. I made these changes:

- **Spacing:** I increased the row padding from 8px to 11px so the rows are easier to scan.
- **Min. order header:** It now reads "Min. order (units)". Before, "6" could have meant loaves, cases or dollars.
- **Caption:** I split it into a short title and a smaller note, so the title is the first thing people read.
- **Repeated styling:** I moved the inline alignment and tabular-figures styles into two classes, `num` and `item`. The table now looks the same but is much shorter.
- **Small screens:** I wrapped it in a horizontal scroll region, so a café owner reading on a phone won't get wrapped numbers.

```html
<div class="price-list" role="region" aria-labelledby="pl-cap" tabindex="0">
<table>
  <caption id="pl-cap">
    Autumn wholesale prices
    <small>Effective Oct 1. Prices per unit, excluding delivery.</small>
  </caption>
  <thead>
    <tr>
      <th scope="col" class="item">Item</th>
      <th scope="col" class="item">Unit</th>
      <th scope="col" class="num">Price (USD)</th>
      <th scope="col" class="num">Min. order (units)</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row" class="item">Sourdough loaf</th><td>800 g</td><td class="num">4.20</td><td class="num">6</td></tr>
    <tr><th scope="row" class="item">Seeded rye</th><td>700 g</td><td class="num">4.60</td><td class="num">6</td></tr>
    <tr><th scope="row" class="item">Cardamom bun</th><td>each</td><td class="num">1.35</td><td class="num">24</td></tr>
    <tr><th scope="row" class="item">Pear and almond tart</th><td>20 cm</td><td class="num">14.00</td><td class="num">2</td></tr>
    <tr><th scope="row" class="item">Pumpkin loaf</th><td>600 g</td><td class="num">6.75</td><td class="num">4</td></tr>
  </tbody>
</table>
</div>
<style>
.price-list{overflow-x:auto;max-width:100%}
.price-list table{border-collapse:collapse;font:15px/1.4 system-ui,sans-serif;white-space:nowrap}
.price-list caption{text-align:left;padding-bottom:10px;font-weight:600;font-size:17px}
.price-list caption small{display:block;font-weight:400;font-size:14px;color:#444}
.price-list th,.price-list td{padding:11px 20px 11px 0;border-bottom:1px solid #ddd;text-align:left}
.price-list thead th{border-bottom:2px solid #999}
.price-list tbody th{font-weight:400}
.price-list .num{text-align:right;font-variant-numeric:tabular-nums}
</style>
```

If you're pasting this into an email rather than putting it on a web page, many mail clients strip or ignore `<style>` blocks. In that case, tell me and I'll give you a version with the styles written inline.

I kept the item order as you had it. If you'd like it grouped, with breads together and then pastries, say so and I'll reorder it.
