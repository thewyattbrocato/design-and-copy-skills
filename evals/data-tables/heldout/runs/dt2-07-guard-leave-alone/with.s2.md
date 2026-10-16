I made only light changes, because the table was already in good shape. Your alignment, tabular figures, units in the header, `<caption>` and `<th scope>` markup were all right.

**What I changed**
- **Min. order header:** it's now "Min. order (units)", so the number has a unit like the price column does.
- **Row spacing:** padding goes up from 8px to 11px, so the rows are about 43px tall and easier to scan.
- **Hairlines:** the rule under the last row is removed, and the header rule now has a little space below it.
- **Phones:** the table sits in a horizontally scrolling wrapper, so numbers never wrap on a narrow screen.
- **Styles:** the repeated inline styles are now CSS classes, which makes the file shorter and easier to edit.

```html
<div class="wrap" role="region" aria-label="Autumn wholesale prices" tabindex="0">
<table class="prices">
  <caption>Autumn wholesale prices, effective Oct 1. Prices per unit, excluding delivery.</caption>
  <thead>
    <tr><th scope="col">Item</th><th scope="col">Unit</th><th scope="col" class="num">Price (USD)</th><th scope="col" class="num">Min. order (units)</th></tr>
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
.wrap{overflow-x:auto}
.prices{border-collapse:collapse;font:15px/1.4 system-ui,sans-serif;font-variant-numeric:tabular-nums}
.prices caption{text-align:left;padding-bottom:10px;color:#444}
.prices th,.prices td{padding:11px 20px 11px 0;border-bottom:1px solid #ddd;text-align:left;white-space:nowrap}
.prices thead th{border-bottom:2px solid #999}
.prices tbody th{font-weight:400}
.prices .num{text-align:right}
.prices tbody tr:last-child th,.prices tbody tr:last-child td{border-bottom:0}
</style>
```

**Before you send it:** most email clients strip `<style>` blocks. If you're pasting this into an email rather than attaching it or hosting it as a page, say so and I'll turn the classes back into inline styles.

**Things to check**
- **Unit column:** "each" for the bun is correct next to "800 g". If any prices are actually per case or per dozen, that needs to be stated.
- **Prices:** I didn't change any figures or the item order.
