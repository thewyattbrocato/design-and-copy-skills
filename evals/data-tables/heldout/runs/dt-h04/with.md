I couldn't save the file because the Write tool is disabled in this session. The full HTML is below, so you can save it as `pricing.html` yourself.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Plan comparison</title>
<style>
  body {
    margin: 0;
    padding: 2rem 1rem;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1b1f24;
    background: #fff;
  }
  .scroll { max-width: 44rem; margin: 0 auto; overflow-x: auto; }
  table {
    width: 100%;
    min-width: 30rem;
    border-collapse: collapse;
    font-size: 1rem;
    font-variant-numeric: tabular-nums lining-nums;
    text-align: left;
  }
  caption { padding-bottom: 0.75rem; text-align: left; font-size: 1.25rem; font-weight: 600; }
  th, td { padding: 0.8rem 1rem; vertical-align: middle; white-space: nowrap; }
  thead th { font-weight: 600; border-bottom: 2px solid #1b1f24; }
  tbody th { font-weight: 500; color: #4a5260; }
  tbody tr { border-bottom: 1px solid #dfe3e8; }
  tbody tr:last-child { border-bottom: 0; }
  tbody tr:last-child th,
  tbody tr:last-child td { font-weight: 700; color: #1b1f24; border-top: 2px solid #1b1f24; }
  tbody tr:last-child td { font-size: 1.125rem; }
  th[scope="row"], thead th:first-child { position: sticky; left: 0; background: #fff; }
  tbody tr:hover th, tbody tr:hover td { background: #f6f8fa; }
</style>
</head>
<body>
<div class="scroll" role="region" aria-labelledby="cap" tabindex="0">
  <table>
    <caption id="cap">Plan comparison</caption>
    <thead>
      <tr>
        <th scope="col"><span style="position:absolute;left:-9999px">Feature</span></th>
        <th scope="col">Basic</th>
        <th scope="col">Plus</th>
        <th scope="col">Max</th>
      </tr>
    </thead>
    <tbody>
      <tr><th scope="row">Storage</th><td>10 GB</td><td>100 GB</td><td>1 TB</td></tr>
      <tr><th scope="row">Users</th><td>1</td><td>5</td><td>unlimited</td></tr>
      <tr><th scope="row">Support</th><td>Email</td><td>Email + chat</td><td>Phone</td></tr>
      <tr><th scope="row">Price per month</th><td>$4</td><td>$12</td><td>$39</td></tr>
    </tbody>
  </table>
</div>
</body>
</html>
```

What I changed, with every value left exactly as you gave it:
- **Markup:** it's a real `<table>` with a caption, `<th scope="col">` plan headers and `<th scope="row">` row labels. The empty top-left header cell has a visually hidden "Feature" label for screen readers.
- **Separation:** each row has a light hairline under it, and the header has a heavier rule. The price row has a heavier rule above it and bolder, slightly larger text, so the figure readers compare last stands out.
- **Alignment:** all cells are left-aligned, because each row mixes text and numbers. Tabular figures keep the digits lined up.
- **Spacing:** rows have generous padding and 16px text. Cells don't wrap.
- **Narrow screens:** the table scrolls sideways, and the row-label column stays pinned so you can still tell which row you're reading.
- **Fonts and assets:** it uses system fonts only, with no external assets.
