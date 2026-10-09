I couldn't save the file because the Write tool is disabled in this session, so the full HTML is below. Save it as `income_statement.html`.

The figures tie out: each quarter's lines add up to its totals, and the four quarters add up to FY 2026. Negative values are the returns line and a Q2 gain in restructuring. The YoY column compares FY 2026 with FY 2025. I haven't opened it in a browser, so the 1280x800 fit is untested.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1280">
<title>Quarterly Income Statement — FY2026</title>
<style>
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    width: 1280px;
    min-height: 800px;
    background: #f4f5f7;
    color: #1d2330;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 13px;
    padding: 28px 56px 20px;
  }
  header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px; }
  h1 { font-size: 22px; font-weight: 650; margin: 0; letter-spacing: -0.01em; }
  .sub { color: #5d6678; font-size: 13px; }
  .card { background: #fff; border: 1px solid #dde1e8; border-radius: 8px; overflow: hidden; }
  table { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }
  th, td { padding: 0 16px; height: 27px; text-align: right; white-space: nowrap; }
  th:first-child, td:first-child { text-align: left; width: 300px; }
  thead th {
    height: 38px; background: #1f2a44; color: #fff; font-weight: 600;
    font-size: 12px; letter-spacing: 0.04em; text-transform: uppercase;
  }
  thead th.fy { background: #2b3a5e; }
  th.yoy, td.yoy { border-left: 1px solid #dde1e8; width: 110px; }
  thead th.yoy { border-left: 1px solid #3b4b72; }
  td.fy { background: #fafbfc; font-weight: 600; }
  tbody tr { border-bottom: 1px solid #eef0f4; }
  tr.section td {
    height: 26px; background: #eaedf3; color: #3a4560; font-weight: 700;
    font-size: 11.5px; letter-spacing: 0.06em; text-transform: uppercase;
    border-bottom: 1px solid #dde1e8;
  }
  tr.item td:first-child { padding-left: 32px; }
  tr.total td { font-weight: 650; border-top: 1px solid #b9c0cf; }
  tr.total td:first-child { padding-left: 16px; }
  tr.key td {
    height: 31px; font-weight: 700; font-size: 14px; background: #e6efff;
    border-top: 1.5px solid #1f2a44; border-bottom: 0;
  }
  tr.key td.fy { background: #dce8fd; }
  tr.margin td { height: 22px; color: #5d6678; font-style: italic; font-size: 12px; }
  tr.margin td:first-child { padding-left: 32px; }
  .neg { color: #b42318; }
  .nil { color: #9aa2b2; }
  footer { margin-top: 10px; color: #5d6678; font-size: 11.5px; line-height: 1.5; }
</style>
</head>
<body>

<header>
  <h1>Meridian Works, Inc. — Quarterly Income Statement</h1>
  <div class="sub">Fiscal year 2026 &nbsp;·&nbsp; USD in thousands</div>
</header>

<div class="card">
<table>
  <thead>
    <tr>
      <th>Line item</th>
      <th>Q1 2026</th>
      <th>Q2 2026</th>
      <th>Q3 2026</th>
      <th>Q4 2026</th>
      <th class="fy">FY 2026</th>
      <th class="fy">FY 2025</th>
      <th class="yoy">YoY change</th>
    </tr>
  </thead>
  <tbody>
    <tr class="section"><td colspan="8">Revenue</td></tr>
    <tr class="item"><td>Product sales</td><td>12,480</td><td>13,120</td><td>14,060</td><td>16,250</td><td class="fy">55,910</td><td>51,400</td><td class="yoy">+8.8%</td></tr>
    <tr class="item"><td>Subscription revenue</td><td>6,340</td><td>6,880</td><td>7,410</td><td>7,920</td><td class="fy">28,550</td><td>22,900</td><td class="yoy">+24.7%</td></tr>
    <tr class="item"><td>Professional services</td><td>2,150</td><td>2,310</td><td>2,090</td><td>2,480</td><td class="fy">9,030</td><td>9,480</td><td class="yoy neg">(4.7%)</td></tr>
    <tr class="item"><td>Less: returns &amp; allowances</td><td class="neg">(420)</td><td class="neg">(465)</td><td class="neg">(510)</td><td class="neg">(610)</td><td class="fy neg">(2,005)</td><td class="neg">(1,720)</td><td class="yoy neg">(16.6%)</td></tr>
    <tr class="total"><td>Total revenue</td><td>20,550</td><td>21,845</td><td>23,050</td><td>26,040</td><td class="fy">91,485</td><td>82,060</td><td class="yoy">+11.5%</td></tr>

    <tr class="section"><td colspan="8">Cost of sales</td></tr>
    <tr class="item"><td>Product costs</td><td>6,870</td><td>7,150</td><td>7,590</td><td>8,640</td><td class="fy">30,250</td><td>28,100</td><td class="yoy">+7.7%</td></tr>
    <tr class="item"><td>Hosting &amp; delivery</td><td>1,980</td><td>2,060</td><td>2,190</td><td>2,310</td><td class="fy">8,540</td><td>7,350</td><td class="yoy">+16.2%</td></tr>
    <tr class="item"><td>Service delivery labor</td><td>1,520</td><td>1,610</td><td>1,580</td><td>1,740</td><td class="fy">6,450</td><td>6,280</td><td class="yoy">+2.7%</td></tr>
    <tr class="total"><td>Total cost of sales</td><td>10,370</td><td>10,820</td><td>11,360</td><td>12,690</td><td class="fy">45,240</td><td>41,730</td><td class="yoy">+8.4%</td></tr>

    <tr class="key"><td>Gross profit</td><td>10,180</td><td>11,025</td><td>11,690</td><td>13,350</td><td class="fy">46,245</td><td>40,330</td><td class="yoy">+14.7%</td></tr>
    <tr class="margin"><td>Gross margin</td><td>49.5%</td><td>50.5%</td><td>50.7%</td><td>51.3%</td><td class="fy">50.5%</td><td>49.1%</td><td class="yoy">+1.4 pts</td></tr>

    <tr class="section"><td colspan="8">Operating expenses</td></tr>
    <tr class="item"><td>Sales &amp; marketing</td><td>3,620</td><td>3,810</td><td>4,150</td><td>5,020</td><td class="fy">16,600</td><td>15,200</td><td class="yoy">+9.2%</td></tr>
    <tr class="item"><td>Research &amp; development</td><td>3,240</td><td>3,310</td><td>3,480</td><td>3,560</td><td class="fy">13,590</td><td>12,400</td><td class="yoy">+9.6%</td></tr>
    <tr class="item"><td>General &amp; administrative</td><td>1,860</td><td>1,910</td><td>1,980</td><td>2,040</td><td class="fy">7,790</td><td>7,350</td><td class="yoy">+6.0%</td></tr>
    <tr class="item"><td>Restructuring &amp; other, net</td><td class="nil">—</td><td class="neg">(350)</td><td>920</td><td class="nil">—</td><td class="fy">570</td><td>1,100</td><td class="yoy neg">(48.2%)</td></tr>
    <tr class="total"><td>Total operating expenses</td><td>8,720</td><td>8,680</td><td>10,530</td><td>10,620</td><td class="fy">38,550</td><td>36,050</td><td class="yoy">+6.9%</td></tr>

    <tr class="key"><td>Operating income</td><td>1,460</td><td>2,345</td><td>1,160</td><td>2,730</td><td class="fy">7,695</td><td>4,280</td><td class="yoy">+79.8%</td></tr>
    <tr class="margin"><td>Operating margin</td><td>7.1%</td><td>10.7%</td><td>5.0%</td><td>10.5%</td><td class="fy">8.4%</td><td>5.2%</td><td class="yoy">+3.2 pts</td></tr>
  </tbody>
</table>
</div>

<footer>
  Figures are illustrative. Parentheses and red denote negative values or unfavorable changes. Q2 restructuring &amp; other includes a $350K gain on sale of equipment.
  YoY change compares FY 2026 with FY 2025 as (FY26 − FY25) ÷ |FY25|; margin rows show the change in percentage points.
</footer>

</body>
</html>
```

- **Layout:** The page is 1280px wide with system fonts and inline CSS only. The 20-row table should fit in 800px of height without scrolling.
- **Columns:** I added FY 2026 and FY 2025 columns next to the four quarters, so the YoY change has a visible basis. The YoY column is full-year versus full-year, not quarter versus the same quarter last year.
- **Margin rows:** Gross margin and operating margin appear as italic rows under their profit lines. Their YoY change is in percentage points.
