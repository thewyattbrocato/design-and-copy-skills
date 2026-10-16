Your table was already in good shape: it has a proper caption, header scopes, right-aligned numbers and tabular figures. I only made small changes.

- **Styling:** I moved the repeated inline styles into classes, so the markup is shorter.
- **Headers:** "Unit" is now "Size / unit", since the tart is sold by diameter. "Min. order" is now "Min. order (qty)", so it's clear the number is a quantity.
- **Caption:** I added the year and split it into two short sentences.

```html
<table>
  <caption>Autumn wholesale prices, effective 1 Oct 2026. Prices are per unit, excluding delivery.</caption>
  <thead>
    <tr>
      <th scope="col">Item</th>
      <th scope="col">Size / unit</th>
      <th scope="col" class="num">Price (USD)</th>
      <th scope="col" class="num">Min. order (qty)</th>
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
<style>
table{border-collapse:collapse;font:15px/1.4 system-ui,sans-serif}
caption{text-align:left;padding-bottom:8px;color:#444}
th,td{padding:8px 16px 8px 0;border-bottom:1px solid #ddd;text-align:left}
thead th{border-bottom:2px solid #999}
tbody th{font-weight:400}
.num{text-align:right;font-variant-numeric:tabular-nums}
</style>
```

Two things to check before you send it:

1. **Effective date:** Today is 14 Oct, so "effective Oct 1" is already in the past. I wrote "1 Oct 2026" on the assumption that's right. If the prices start later, change the date.
2. **Email:** Many email clients, Gmail especially, strip or ignore `<style>` blocks. If you're pasting this into an email body, your original inline styles are safer, so use those instead of the classes. If you're attaching it as an HTML file or a PDF, this version is fine. I can produce an inline-styled version if you want one.
