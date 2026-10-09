I couldn't save the file: the Write tool is disabled in this session, and I have no other way to create files. The full HTML is below, so you can save it as `invoice-summary.html`, or re-enable Write and I'll create it.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Invoice summary</title>
<style>
  body {
    margin: 0;
    padding: 2rem 1rem;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
    font-size: 1rem;
    line-height: 1.5;
    color: #1d1d1f;
    background: #fff;
  }
  table {
    width: 100%;
    max-width: 40rem;
    margin: 0 auto;
    border-collapse: collapse;
    font-variant-numeric: tabular-nums lining-nums;
  }
  th, td {
    padding: 0.625rem 0.75rem;
    text-align: right;
    vertical-align: baseline;
  }
  th:first-child, td:first-child { text-align: left; }
  thead th {
    font-size: 0.875rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #555;
    border-bottom: 2px solid #1d1d1f;
  }
  tbody td { border-bottom: 1px solid #ddd; }
  tbody tr:last-child td { border-bottom: 0; }
  tfoot th {
    font-weight: 400;
    letter-spacing: normal;
    text-transform: none;
  }
  tfoot tr:first-child th,
  tfoot tr:first-child td { border-top: 1px solid #1d1d1f; }
  tfoot tr.total th,
  tfoot tr.total td {
    font-size: 1.25rem;
    font-weight: 700;
    border-top: 2px solid #1d1d1f;
  }
</style>
</head>
<body>
<table>
  <thead>
    <tr><th scope="col">Item</th><th scope="col">Qty</th><th scope="col">Unit</th><th scope="col">Total</th></tr>
  </thead>
  <tbody>
    <tr><td>Pallet wrap rolls</td><td>12</td><td>$8.40</td><td>$100.80</td></tr>
    <tr><td>Strapping kit</td><td>3</td><td>$42.00</td><td>$126.00</td></tr>
    <tr><td>Dock labels</td><td>40</td><td>$0.35</td><td>$14.00</td></tr>
  </tbody>
  <tfoot>
    <tr><th scope="row" colspan="3">Subtotal</th><td>$240.80</td></tr>
    <tr><th scope="row" colspan="3">Tax (8%)</th><td>$19.26</td></tr>
    <tr class="total"><th scope="row" colspan="3">Total due</th><td>$260.06</td></tr>
  </tfoot>
</table>
</body>
</html>
```

I haven't opened it in a browser, so the rendering is untested. The content is unchanged.

- **Numbers:** Figures are tabular and right-aligned, with two decimals on every row, so the columns line up.
- **Sizes:** The body text is 1rem with a line height of 1.5. The header row is 0.875rem, and the total row is 1.25rem.
- **Headers:** The column headers are short uppercase labels with 0.06em tracking.
- **Total due:** It stands out through one step up in size and bold weight, plus a heavier rule above it.
- **Rules:** Thin rules separate the line items. The footer labels (Subtotal, Tax, Total due) are in sentence case and left-aligned.
- **Fonts:** The font stack is system fonts only, and there are no external assets.
