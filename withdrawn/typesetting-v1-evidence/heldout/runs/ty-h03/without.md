I couldn't write the file because the Write tool is disabled in this session. Here is the full HTML, so you can save it as `invoice-summary.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Invoice Summary</title>
<style>
  body {
    margin: 0;
    padding: 3rem 1.5rem;
    background: #fff;
    color: #1a1a1a;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }
  table {
    width: 100%;
    max-width: 38rem;
    margin: 0 auto;
    border-collapse: collapse;
    font-variant-numeric: tabular-nums lining-nums;
  }
  th, td {
    padding: 0.75rem 0.875rem;
    text-align: right;
    white-space: nowrap;
  }
  th:first-child, td:first-child {
    text-align: left;
    white-space: normal;
  }
  thead th {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #5c5c5c;
    border-bottom: 2px solid #1a1a1a;
  }
  tbody td {
    border-bottom: 1px solid #e3e3e3;
  }
  tbody td:first-child {
    font-weight: 500;
  }
  tfoot td {
    border-bottom: none;
    color: #444;
  }
  tfoot tr:first-child td {
    border-top: 2px solid #1a1a1a;
  }
  tfoot .label {
    text-align: right;
  }
  tfoot tr.total td {
    border-top: 1px solid #1a1a1a;
    padding-top: 1rem;
    font-size: 1.25rem;
    font-weight: 700;
    color: #1a1a1a;
  }
</style>
</head>
<body>
<table>
  <thead>
    <tr>
      <th scope="col">Item</th>
      <th scope="col">Qty</th>
      <th scope="col">Unit</th>
      <th scope="col">Total</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Pallet wrap rolls</td><td>12</td><td>$8.40</td><td>$100.80</td></tr>
    <tr><td>Strapping kit</td><td>3</td><td>$42.00</td><td>$126.00</td></tr>
    <tr><td>Dock labels</td><td>40</td><td>$0.35</td><td>$14.00</td></tr>
  </tbody>
  <tfoot>
    <tr><td class="label" colspan="3">Subtotal</td><td>$240.80</td></tr>
    <tr><td class="label" colspan="3">Tax (8%)</td><td>$19.26</td></tr>
    <tr class="total"><td class="label" colspan="3">Total due</td><td>$260.06</td></tr>
  </tfoot>
</table>
</body>
</html>
```

The typographic changes:
- **Fonts:** a system font stack, with no external assets.
- **Numbers:** tabular, lining figures, with numeric columns right-aligned so the decimals line up.
- **Header:** small uppercase labels with letter-spacing in muted gray, over a heavier rule.
- **Rows:** more padding, light dividers, and slightly heavier item names.
- **Footer:** the subtotal and tax are separated from the line items by a rule. "Total due" is larger and bold.

The content is unchanged. I haven't opened the file in a browser.
