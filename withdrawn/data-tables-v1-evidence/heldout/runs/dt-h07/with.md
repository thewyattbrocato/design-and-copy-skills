I couldn't save the file: the Write tool is disabled in this session, and I have no other way to write files. Nothing has been created on disk and I haven't opened the page in a browser. Below is the full file. Save it as `food-bank-inventory.html` and open it in a browser.

I read "25 rows, show 8 rows realistically" as 25 items in total, with the table area sized to show about 8 rows at once. The header stays fixed while the rest scrolls. If you meant only 8 rows of data in total, delete the extra rows from the `DATA` array and remove `max-height` from `.scroll`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Food bank inventory</title>
<style>
  :root {
    --ink: #1f2a24;
    --muted: #5a6760;
    --line: #e1e6e2;
    --line-strong: #b9c3bc;
    --bg: #f6f7f4;
    --panel: #ffffff;
    --accent: #1f6b45;
    --accent-soft: #e3f0e8;
    --warn: #8a4b00;
    --bad: #a12626;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font: 15px/1.4 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  main { max-width: 1040px; margin: 0 auto; padding: 28px 24px 40px; }
  h1 { font-size: 22px; margin: 0 0 4px; }
  .sub { margin: 0 0 20px; color: var(--muted); }

  .filters { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 12px; }
  .filters button {
    font: inherit; color: var(--ink); background: var(--panel);
    border: 1px solid var(--line-strong); border-radius: 999px;
    padding: 5px 14px; cursor: pointer;
  }
  .filters button:hover { background: var(--accent-soft); }
  .filters button[aria-pressed="true"] {
    background: var(--accent); border-color: var(--accent); color: #fff;
  }
  .filters .n { font-variant-numeric: tabular-nums; opacity: .75; margin-left: 4px; }
  button:focus-visible, .scroll:focus-visible { outline: 3px solid #1a5fd0; outline-offset: 2px; }

  .scroll {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 8px;
    max-height: 408px;           /* header + 8 rows */
    overflow: auto;
  }
  table { width: 100%; border-collapse: collapse; }
  caption { display: none; }
  th, td { padding: 0 16px; height: 44px; text-align: left; white-space: nowrap; }
  thead th {
    position: sticky; top: 0; z-index: 1;
    background: var(--panel);
    border-bottom: 2px solid var(--line-strong);
    font-size: 14px; font-weight: 600;
  }
  tbody th { font-weight: 600; }
  tbody tr + tr > * { border-top: 1px solid var(--line); }
  .num { text-align: right; font-variant-numeric: tabular-nums; }
  td.unit { padding-left: 8px; color: var(--muted); }
  th.unit-h { padding-left: 8px; }
  td.date { font-variant-numeric: tabular-nums; }
  .code { font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; font-size: 14px; }
  .none { color: var(--muted); }
  .flag { margin-left: 8px; font-size: 13px; font-weight: 600; }
  .flag.soon { color: var(--warn); }
  .flag.expired { color: var(--bad); }

  th button {
    font: inherit; font-weight: 600; color: inherit; background: none; border: 0;
    padding: 0; cursor: pointer; display: inline-flex; gap: 6px; align-items: center;
  }
  th.num button { flex-direction: row-reverse; }
  th button .arrow { width: 1em; color: var(--accent); }

  .foot { margin: 10px 2px 0; color: var(--muted); font-size: 14px; }
  .foot span + span { margin-left: 16px; }
</style>
</head>
<body>
<main>
  <h1>Food bank inventory</h1>
  <p class="sub">Stock on hand by shelf. Check the expiry column when planning this week's packing.</p>

  <div class="filters" id="filters" role="group" aria-label="Filter by category"></div>

  <div class="scroll" tabindex="0" role="region" aria-label="Inventory table, scrollable">
    <table>
      <caption>Food bank inventory</caption>
      <thead>
        <tr>
          <th scope="col" aria-sort="none"><button type="button" data-key="item">Item <span class="arrow" aria-hidden="true"></span></button></th>
          <th scope="col">Category</th>
          <th scope="col" class="num" aria-sort="none"><button type="button" data-key="qty">Quantity on hand <span class="arrow" aria-hidden="true"></span></button></th>
          <th scope="col" class="unit-h">Unit</th>
          <th scope="col" aria-sort="none"><button type="button" data-key="exp">Expiry date <span class="arrow" aria-hidden="true"></span></button></th>
          <th scope="col">Location</th>
        </tr>
      </thead>
      <tbody id="rows"></tbody>
    </table>
  </div>

  <p class="foot" id="foot"></p>
</main>

<script>
  const DATA = [
    ["Black beans", "Canned goods", 96, "cans", "2028-01-22", "A-02"],
    ["Chicken noodle soup", "Canned goods", 40, "cans", "2026-10-21", "A-04"],
    ["Chickpeas", "Canned goods", 148, "cans", "2028-03-14", "A-02"],
    ["Diced tomatoes", "Canned goods", 212, "cans", "2027-11-30", "A-01"],
    ["Sweetcorn", "Canned goods", 33, "cans", "2027-05-17", "A-01"],
    ["Tuna in water", "Canned goods", 64, "cans", "2027-08-09", "A-03"],
    ["Cornflakes", "Dry goods", 72, "boxes", "2027-01-15", "B-04"],
    ["Green lentils", "Dry goods", 41, "kg", "2028-05-05", "B-03"],
    ["Long grain rice", "Dry goods", 120, "kg", "2027-09-01", "B-01"],
    ["Rolled oats", "Dry goods", 54, "kg", "2027-06-30", "B-03"],
    ["Spaghetti", "Dry goods", 38, "boxes", "2028-02-10", "B-02"],
    ["Apples", "Fresh produce", 70, "kg", "2026-10-19", "C-03"],
    ["Bananas", "Fresh produce", 18, "kg", "2026-10-07", "C-04"],
    ["Carrots", "Fresh produce", 45, "kg", "2026-10-14", "C-02"],
    ["Onions", "Fresh produce", 52, "kg", "2026-11-20", "C-01"],
    ["Potatoes", "Fresh produce", 160, "kg", "2026-10-28", "C-01"],
    ["Cheddar cheese", "Dairy & eggs", 12, "kg", "2026-10-30", "D-03"],
    ["Eggs (tray of 30)", "Dairy & eggs", 30, "boxes", "2026-10-16", "D-02"],
    ["Long-life milk (1 L)", "Dairy & eggs", 90, "boxes", "2027-02-03", "D-01"],
    ["Baby cereal", "Baby", 18, "boxes", "2027-03-01", "E-02"],
    ["Infant formula", "Baby", 26, "cans", "2027-04-12", "E-01"],
    ["Nappies, size 4", "Baby", 14, "boxes", null, "E-03"],
    ["Bar soap", "Hygiene", 22, "boxes", null, "F-01"],
    ["Shampoo", "Hygiene", 17, "boxes", "2028-09-01", "F-02"],
    ["Toothpaste", "Hygiene", 31, "boxes", "2028-04-18", "F-02"]
  ];

  const CATS = [...new Set(DATA.map(r => r[1]))];
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const fmtDate = new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "short", year: "numeric" });
  const fmtNum = new Intl.NumberFormat("en-GB");

  let cat = "All";
  let sort = { key: "item", dir: 1 };
  const idx = { item: 0, qty: 2, exp: 4 };

  const rowsEl = document.getElementById("rows");
  const filtersEl = document.getElementById("filters");
  const footEl = document.getElementById("foot");

  function el(tag, props = {}, ...kids) {
    const e = Object.assign(document.createElement(tag), props);
    e.append(...kids);
    return e;
  }

  function buildFilters() {
    filtersEl.replaceChildren(...["All", ...CATS].map(c => {
      const n = c === "All" ? DATA.length : DATA.filter(r => r[1] === c).length;
      const b = el("button", { type: "button" }, c, el("span", { className: "n", textContent: n }));
      b.setAttribute("aria-pressed", String(c === cat));
      b.addEventListener("click", () => { cat = c; render(); });
      return b;
    }));
  }

  function expiryCell(iso) {
    const td = el("td", { className: "date" });
    if (!iso) {
      td.append(el("span", { className: "none", textContent: "—", title: "No expiry date" }));
      return td;
    }
    const d = new Date(iso + "T00:00:00");
    td.append(fmtDate.format(d));
    const days = Math.round((d - today) / 864e5);
    if (days < 0) td.append(el("span", { className: "flag expired", textContent: "Expired" }));
    else if (days <= 14) td.append(el("span", { className: "flag soon", textContent: "Expires soon" }));
    return td;
  }

  function render() {
    buildFilters();
    const k = idx[sort.key];
    const rows = DATA.filter(r => cat === "All" || r[1] === cat).sort((a, b) => {
      const x = a[k], y = b[k];
      if (x === y) return 0;
      if (x === null) return 1;            // missing dates always last
      if (y === null) return -1;
      return (x < y ? -1 : 1) * sort.dir;
    });

    rowsEl.replaceChildren(...rows.map(r => el("tr", {},
      el("th", { scope: "row", textContent: r[0] }),
      el("td", { textContent: r[1] }),
      el("td", { className: "num", textContent: fmtNum.format(r[2]) }),
      el("td", { className: "unit", textContent: r[3] }),
      expiryCell(r[4]),
      el("td", { className: "code", textContent: r[5] })
    )));

    document.querySelectorAll("th[aria-sort]").forEach(th => {
      const key = th.querySelector("button").dataset.key;
      const active = key === sort.key;
      th.setAttribute("aria-sort", active ? (sort.dir === 1 ? "ascending" : "descending") : "none");
      th.querySelector(".arrow").textContent = active ? (sort.dir === 1 ? "↑" : "↓") : "";
    });

    const soon = rows.filter(r => r[4] && (new Date(r[4] + "T00:00:00") - today) / 864e5 <= 14).length;
    footEl.replaceChildren(
      el("span", { textContent: `Showing ${rows.length} of ${DATA.length} items` + (cat === "All" ? "" : ` in ${cat}`) }),
      el("span", { textContent: `${soon} expired or expiring within 14 days` }),
      el("span", { textContent: "— means no expiry date" })
    );
  }

  document.querySelectorAll("th button").forEach(b => b.addEventListener("click", () => {
    const key = b.dataset.key;
    sort = { key, dir: sort.key === key ? -sort.dir : 1 };
    render();
  }));

  render();
</script>
</body>
</html>
```

**What it does**
- **Table:** There are 25 items across six categories: canned goods, dry goods, fresh produce, dairy and eggs, baby, and hygiene. Units are cans, kg and boxes.
- **Category filter:** A row of buttons sits above the table, each showing its item count. The footer updates to say "Showing N of 25".
- **Sorting:** Item, Quantity on hand and Expiry date can be sorted. The active column shows an arrow, and the header carries `aria-sort`.
- **Expiry flags:** Dates within 14 days, or already past, get a written "Expires soon" or "Expired" label next to them. The flags are computed from the date you open the page, so the sample dates will drift toward "Expired" over time.
- **Missing dates:** Items with no expiry, such as nappies and soap, show "—". The footer explains the dash.
- **Layout:** Quantities are right-aligned in tabular figures, with the unit in its own column beside them. Rows are 44px high, with a hairline between rows and a heavier line under the header. The file uses system fonts only and no external assets.
