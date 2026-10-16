I moved the repeated inline styles into the stylesheet and left the content and prices as they were. Here's the cleaned-up version:

```html
<table>
  <caption>Autumn wholesale prices, effective Oct 1. Prices per unit, excluding delivery.</caption>
  <thead>
    <tr>
      <th scope="col">Item</th>
      <th scope="col">Unit</th>
      <th scope="col" class="num">Price (USD)</th>
      <th scope="col" class="num">Min. order</th>
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

What changed:
- **Inline styles:** each cell's `style="..."` is now a single `.num` class, and left-alignment and the row-header weight are set once in the CSS. The rendering is identical.
- **Accessibility:** the `scope` attributes and the caption are unchanged.

Before you send it:
- **Effective date:** the caption says "effective Oct 1", but today is Oct 14. If these prices are current now, you may want to reword it, for example "effective Oct 1 through the autumn season", or update the date.
- **Email clients:** many, including Outlook and some webmail, strip or ignore `<style>` blocks. If this is going into the body of an email, tell me and I'll inline the styles again. If it's an attachment or a web page, this version is fine.
