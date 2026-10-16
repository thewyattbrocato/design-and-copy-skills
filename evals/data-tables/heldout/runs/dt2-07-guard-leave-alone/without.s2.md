Your table was already in good shape, so I made only a few small changes:

- **Inline styles:** Many email clients strip or ignore `<style>` blocks, so the formatting is now on the elements themselves.
- **Unit column:** It's now left-aligned, like the Item column. Before, it fell back to the default alignment.
- **Header:** "Min. order" is now "Min. order (units)", so it's clear that 6 means six loaves and not six dollars.
- **Rows:** I added light zebra-free spacing, with a slightly larger bottom border so the rows scan more easily.

```html
<table style="border-collapse:collapse;font:15px/1.4 system-ui,-apple-system,Arial,sans-serif;color:#222">
  <caption style="text-align:left;padding-bottom:8px;color:#444">
    Autumn wholesale prices, effective Oct 1. Prices per unit, excluding delivery.
  </caption>
  <thead>
    <tr>
      <th scope="col" style="text-align:left;padding:8px 16px 8px 0;border-bottom:2px solid #999">Item</th>
      <th scope="col" style="text-align:left;padding:8px 16px 8px 0;border-bottom:2px solid #999">Unit</th>
      <th scope="col" style="text-align:right;padding:8px 16px 8px 0;border-bottom:2px solid #999">Price (USD)</th>
      <th scope="col" style="text-align:right;padding:8px 0;border-bottom:2px solid #999">Min. order (units)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" style="text-align:left;font-weight:400;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">Sourdough loaf</th>
      <td style="text-align:left;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">800 g</td>
      <td style="text-align:right;padding:8px 16px 8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">4.20</td>
      <td style="text-align:right;padding:8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">6</td>
    </tr>
    <tr>
      <th scope="row" style="text-align:left;font-weight:400;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">Seeded rye</th>
      <td style="text-align:left;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">700 g</td>
      <td style="text-align:right;padding:8px 16px 8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">4.60</td>
      <td style="text-align:right;padding:8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">6</td>
    </tr>
    <tr>
      <th scope="row" style="text-align:left;font-weight:400;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">Cardamom bun</th>
      <td style="text-align:left;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">each</td>
      <td style="text-align:right;padding:8px 16px 8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">1.35</td>
      <td style="text-align:right;padding:8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">24</td>
    </tr>
    <tr>
      <th scope="row" style="text-align:left;font-weight:400;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">Pear and almond tart</th>
      <td style="text-align:left;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">20 cm</td>
      <td style="text-align:right;padding:8px 16px 8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">14.00</td>
      <td style="text-align:right;padding:8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">2</td>
    </tr>
    <tr>
      <th scope="row" style="text-align:left;font-weight:400;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">Pumpkin loaf</th>
      <td style="text-align:left;padding:8px 16px 8px 0;border-bottom:1px solid #ddd">600 g</td>
      <td style="text-align:right;padding:8px 16px 8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">6.75</td>
      <td style="text-align:right;padding:8px 0;border-bottom:1px solid #ddd;font-variant-numeric:tabular-nums">4</td>
    </tr>
  </tbody>
</table>
```

Two things to check before you send it:

1. **Effective date:** The caption says "effective Oct 1", but today is Oct 14. You may want to say "effective Oct 1, 2026" or give the date the prices are valid from or until.
2. **Tart size:** "20 cm" in the Unit column is a size, not a unit. "each (20 cm)" would match the other rows better. I left the wording alone since it's your content.

I haven't changed any prices or quantities.
