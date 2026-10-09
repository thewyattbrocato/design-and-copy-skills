I couldn't save the file because the Write tool is disabled in this session. Below is the full HTML. Save it as `pricing-table.html` and it will work as is.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pricing comparison</title>
<style>
  :root {
    --bg: #f6f7f9;
    --surface: #ffffff;
    --text: #1c2430;
    --muted: #5b6676;
    --border: #e3e7ed;
    --head-bg: #f0f3f7;
    --stripe: #fafbfc;
    --accent: #1f5fd1;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #12161c;
      --surface: #1a2029;
      --text: #e8ecf2;
      --muted: #9aa5b5;
      --border: #2b3441;
      --head-bg: #212935;
      --stripe: #1e252f;
      --accent: #7aa7ff;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 2rem 1rem;
    background: var(--bg);
    color: var(--text);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.5;
  }
  .wrap {
    max-width: 44rem;
    margin: 0 auto;
    overflow-x: auto;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-variant-numeric: tabular-nums;
  }
  caption {
    padding: 1.25rem 1.5rem 0.75rem;
    text-align: left;
    font-size: 1.25rem;
    font-weight: 650;
  }
  th, td {
    padding: 0.9rem 1.5rem;
    text-align: center;
    border-top: 1px solid var(--border);
  }
  thead th {
    background: var(--head-bg);
    font-size: 0.8rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--muted);
  }
  tbody th {
    text-align: left;
    font-weight: 500;
    color: var(--muted);
    white-space: nowrap;
  }
  tbody tr:nth-child(even) > * { background: var(--stripe); }
  tbody tr:hover > * { background: var(--head-bg); }
  tbody tr:last-child > * { border-top: 2px solid var(--border); }
  tbody tr:last-child th { color: var(--text); font-weight: 650; }
  tbody tr:last-child td {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--accent);
  }
  .sr-only {
    position: absolute;
    left: -9999px;
  }
  @media (max-width: 30rem) {
    th, td { padding: 0.75rem; }
    caption { padding: 1rem 0.75rem 0.5rem; }
  }
</style>
</head>
<body>
  <div class="wrap">
    <table>
      <caption>Pricing comparison</caption>
      <thead>
        <tr>
          <th scope="col"><span class="sr-only">Feature</span></th>
          <th scope="col">Basic</th>
          <th scope="col">Plus</th>
          <th scope="col">Max</th>
        </tr>
      </thead>
      <tbody>
        <tr><th scope="row">Storage</th><td>10 GB</td><td>100 GB</td><td>1 TB</td></tr>
        <tr><th scope="row">Users</th><td>1</td><td>5</td><td>Unlimited</td></tr>
        <tr><th scope="row">Support</th><td>Email</td><td>Email + chat</td><td>Phone</td></tr>
        <tr><th scope="row">Price per month</th><td>$4</td><td>$12</td><td>$39</td></tr>
      </tbody>
    </table>
  </div>
</body>
</html>
```

The data is exactly as you gave it. These are the readability changes:
- **Structure:** it uses a real table with a caption, column headers and row headers (`scope`). The empty corner cell has a visually hidden "Feature" label for screen readers.
- **Hierarchy:** column headers are small uppercase labels on a tinted background. Row labels are left-aligned in a muted color, and values are centered.
- **Price row:** it is separated by a heavier rule and shown larger, bold and in the accent color, so the price stands out.
- **Scanning:** rows have subtle zebra striping and a hover highlight, and numbers use tabular figures.
- **Layout:** cell padding is generous. The table scrolls horizontally on narrow screens, with tighter padding below 30rem.
- **Theme and assets:** it follows the system light or dark theme. It uses only system fonts and inline CSS, with no external assets.

I didn't add a "most popular" badge or any other content, since you asked not to change the data.
