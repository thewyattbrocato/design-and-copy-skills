I couldn't save this as a file because the Write tool is disabled in this session, so the full HTML is below. Save it as `income-statement.html` and open it in a 1280×800 window. I haven't opened it in a browser, but I checked the arithmetic: every subtotal, total and year-over-year percentage reconciles.

The table has the four quarters, FY2026 and FY2025 totals, and a year-over-year change column. The negatives are the returns and allowances row, shown in parentheses. The Q2 restructuring charge is the only value in that row, so the other quarters show a dash.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quarterly income statement, FY2026</title>
<style>
  :root {
    --ink: #1d232b;
    --muted: #5d6673;
    --hair: #e3e6ea;
    --rule: #1d232b;
    --band: #f4f6f8;
    --bg: #ffffff;
    --pos: #1b6b3a;
    --neg: #a3261f;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; background: var(--bg); color: var(--ink); }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 14px;
    line-height: 1.3;
    padding: 20px 40px 16px;
    max-width: 1280px;
    margin: 0 auto;
  }
  h1 { font-size: 20px; margin: 0 0 2px; font-weight: 650; letter-spacing: -0.01em; }
  .sub { margin: 0 0 12px; color: var(--muted); }
  .scroll { overflow-x: auto; }

  table {
    width: 100%;
    min-width: 900px;
    border-collapse: collapse;
    font-variant-numeric: tabular-nums lining-nums;
  }
  caption {
    caption-side: bottom;
    text-align: left;
    color: var(--muted);
    font-size: 13px;
    padding-top: 10px;
  }
  th, td { padding: 0 12px; height: 28px; white-space: nowrap; }
  td { border-bottom: 1px solid var(--hair); }

  thead th {
    font-weight: 600;
    font-size: 13px;
    color: var(--muted);
    height: 36px;
    vertical-align: bottom;
    padding-bottom: 6px;
    border-bottom: 2px solid var(--rule);
  }
  thead th.num { text-align: right; }
  thead th.total-col, td.total-col { background: var(--band); }
  thead th.yoy, td.yoy { border-left: 1px solid var(--hair); }

  th[scope="row"] { text-align: left; font-weight: 400; border-bottom: 1px solid var(--hair); }
  tbody th[scope="row"].indent { padding-left: 28px; }
  td.num { text-align: right; padding-right: calc(12px + 0.6ch); }
  td.num.neg { padding-right: 12px; }

  tr.section th {
    height: 30px;
    padding-top: 6px;
    text-align: left;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--muted);
    border-bottom: 1px solid var(--hair);
  }

  tr.subtotal th, tr.subtotal td { font-weight: 650; border-top: 1px solid var(--rule); }
  tr.key th, tr.key td {
    font-weight: 700;
    background: var(--band);
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
  }
  tr.key td.total-col { background: #e9edf1; }

  .up { color: var(--pos); }
  .down { color: var(--neg); }
  .na { color: var(--muted); }
</style>
</head>
<body>
  <h1>Income statement by quarter, FY2026</h1>
  <p class="sub">Amounts in US dollars, thousands. Fiscal year ended December 31, 2026.</p>

  <div class="scroll">
  <table>
    <caption>
      Parentheses show negative amounts. A dash (—) means none recorded. Year-over-year change is (FY2026 − FY2025) ÷ |FY2025|, so a larger deduction such as returns shows as a negative change.
    </caption>
    <thead>
      <tr>
        <th scope="col" style="text-align:left">US$ thousands</th>
        <th scope="col" class="num">Q1</th>
        <th scope="col" class="num">Q2</th>
        <th scope="col" class="num">Q3</th>
        <th scope="col" class="num">Q4</th>
        <th scope="col" class="num total-col">FY2026</th>
        <th scope="col" class="num total-col">FY2025</th>
        <th scope="col" class="num yoy">YoY change</th>
      </tr>
    </thead>
    <tbody>
      <tr class="section"><th scope="rowgroup" colspan="8">Revenue</th></tr>
      <tr>
        <th scope="row" class="indent">Product sales</th>
        <td class="num">8,420</td><td class="num">9,110</td><td class="num">9,870</td><td class="num">11,640</td>
        <td class="num total-col">39,040</td><td class="num total-col">35,200</td>
        <td class="num yoy up">+10.9%</td>
      </tr>
      <tr>
        <th scope="row" class="indent">Subscriptions</th>
        <td class="num">3,150</td><td class="num">3,420</td><td class="num">3,780</td><td class="num">4,050</td>
        <td class="num total-col">14,400</td><td class="num total-col">11,900</td>
        <td class="num yoy up">+21.0%</td>
      </tr>
      <tr>
        <th scope="row" class="indent">Professional services</th>
        <td class="num">1,280</td><td class="num">1,190</td><td class="num">1,410</td><td class="num">1,560</td>
        <td class="num total-col">5,440</td><td class="num total-col">5,300</td>
        <td class="num yoy up">+2.6%</td>
      </tr>
      <tr>
        <th scope="row" class="indent">Returns and allowances</th>
        <td class="num neg">(310)</td><td class="num neg">(285)</td><td class="num neg">(340)</td><td class="num neg">(462)</td>
        <td class="num neg total-col">(1,397)</td><td class="num neg total-col">(1,240)</td>
        <td class="num yoy down">−12.7%</td>
      </tr>
      <tr class="subtotal">
        <th scope="row">Net revenue</th>
        <td class="num">12,540</td><td class="num">13,435</td><td class="num">14,720</td><td class="num">16,788</td>
        <td class="num total-col">57,483</td><td class="num total-col">51,160</td>
        <td class="num yoy up">+12.4%</td>
      </tr>

      <tr class="section"><th scope="rowgroup" colspan="8">Cost of sales</th></tr>
      <tr>
        <th scope="row" class="indent">Product costs</th>
        <td class="num">4,630</td><td class="num">4,980</td><td class="num">5,320</td><td class="num">6,150</td>
        <td class="num total-col">21,080</td><td class="num total-col">19,300</td>
        <td class="num yoy">+9.2%</td>
      </tr>
      <tr>
        <th scope="row" class="indent">Subscription hosting</th>
        <td class="num">780</td><td class="num">810</td><td class="num">850</td><td class="num">905</td>
        <td class="num total-col">3,345</td><td class="num total-col">2,800</td>
        <td class="num yoy">+19.5%</td>
      </tr>
      <tr>
        <th scope="row" class="indent">Services delivery</th>
        <td class="num">940</td><td class="num">905</td><td class="num">1,010</td><td class="num">1,085</td>
        <td class="num total-col">3,940</td><td class="num total-col">3,900</td>
        <td class="num yoy">+1.0%</td>
      </tr>
      <tr class="subtotal">
        <th scope="row">Total cost of sales</th>
        <td class="num">6,350</td><td class="num">6,695</td><td class="num">7,180</td><td class="num">8,140</td>
        <td class="num total-col">28,365</td><td class="num total-col">26,000</td>
        <td class="num yoy">+9.1%</td>
      </tr>

      <tr class="key">
        <th scope="row">Gross profit</th>
        <td class="num">6,190</td><td class="num">6,740</td><td class="num">7,540</td><td class="num">8,648</td>
        <td class="num total-col">29,118</td><td class="num total-col">25,160</td>
        <td class="num yoy up">+15.7%</td>
      </tr>

      <tr class="section"><th scope="rowgroup" colspan="8">Operating expenses</th></tr>
      <tr>
        <th scope="row" class="indent">Sales and marketing</th>
        <td class="num">2,310</td><td class="num">2,380</td><td class="num">2,520</td><td class="num">2,940</td>
        <td class="num total-col">10,150</td><td class="num total-col">9,100</td>
        <td class="num yoy">+11.5%</td>
      </tr>
      <tr>
        <th scope="row" class="indent">Research and development</th>
        <td class="num">2,050</td><td class="num">2,120</td><td class="num">2,200</td><td class="num">2,260</td>
        <td class="num total-col">8,630</td><td class="num total-col">7,900</td>
        <td class="num yoy">+9.2%</td>
      </tr>
      <tr>
        <th scope="row" class="indent">General and administrative</th>
        <td class="num">1,180</td><td class="num">1,210</td><td class="num">1,240</td><td class="num">1,290</td>
        <td class="num total-col">4,920</td><td class="num total-col">4,700</td>
        <td class="num yoy">+4.7%</td>
      </tr>
      <tr>
        <th scope="row" class="indent">Restructuring</th>
        <td class="num na">—</td><td class="num">640</td><td class="num na">—</td><td class="num na">—</td>
        <td class="num total-col">640</td><td class="num total-col na">—</td>
        <td class="num yoy na">n/a</td>
      </tr>
      <tr class="subtotal">
        <th scope="row">Total operating expenses</th>
        <td class="num">5,540</td><td class="num">6,350</td><td class="num">5,960</td><td class="num">6,490</td>
        <td class="num total-col">24,340</td><td class="num total-col">21,700</td>
        <td class="num yoy">+12.2%</td>
      </tr>

      <tr class="key">
        <th scope="row">Operating income</th>
        <td class="num">650</td><td class="num">390</td><td class="num">1,580</td><td class="num">2,158</td>
        <td class="num total-col">4,778</td><td class="num total-col">3,460</td>
        <td class="num yoy up">+38.1%</td>
      </tr>
    </tbody>
  </table>
  </div>
</body>
</html>
```

- **Layout:** Rows are 28px with 14px text, so the whole statement fits in 1280×800 without scrolling. Below 900px wide the table scrolls horizontally instead of squeezing the numbers.
- **Alignment:** Numbers are right-aligned in tabular figures. Positive values get a small right pad so they line up with the closing parenthesis of the negatives.
- **Totals:** Subtotals have a heavier rule above them. Gross profit and operating income sit on shaded bands.
- **Colour:** Green and red appear only on the year-over-year change for revenue lines, gross profit and operating income, and the sign is always shown too. Cost lines stay neutral, because a cost going up isn't good news.
