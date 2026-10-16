The table was already in good shape, with a caption, real header cells, right-aligned numbers and tabular figures. I made small changes:

- **Cleaner markup:** the repeated inline styles are now two classes, so the table is easier to edit next season.
- **Roomier rows:** padding goes up a little, which puts rows at about 42px and makes them easier to scan.
- **Clearer last column:** the header now reads "Min. order (units)", so it's obvious that 24 means 24 buns and 2 means 2 tarts.
- **Phone-friendly:** the table sits in a scrollable wrapper, so it won't squash if an owner opens it on a phone.
- **Unchanged:** the items, prices, order quantities and wording of the caption.

```html
<div class="price-list" role="region" aria-labelledby="price-caption" tabindex="0">
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
.price-list{overflow-x:auto}
.price-list table{border-collapse:collapse;font:15px/1.4 system-ui,sans-serif}
.price-list caption{text-align:left;padding-bottom:8px;color:#444}
.price-list th,.price-list td{padding:10px 16px 10px 0;border-bottom:1px solid #ddd;text-align:left}
.price-list thead th{border-bottom:2px solid #999}
.price-list tbody th{font-weight:400}
.price-list .num{text-align:right;font-variant-numeric:tabular-nums}
</style>
```

If any of the café owners get this as an email, check that it renders properly first. Many email clients drop `<style>` blocks. If so, I can switch it back to inline styles.
