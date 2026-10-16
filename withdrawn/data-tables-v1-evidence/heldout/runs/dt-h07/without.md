I couldn't save the file because the Write tool is disabled in this session. The full file is below, so you can save it as `food-bank-inventory.html` and open it in a browser. I haven't opened it in a browser, so the layout is untested.

I read "show 8 rows realistically" as: all 25 rows are in the table, and the scroll area shows 8 rows plus a small peek of the ninth, with a sticky header. That fits a laptop screen. If you meant only 8 rows of data in total, trim the `data` array.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Food Bank Inventory</title>
<style>
  :root {
    --bg: #f6f5f1;
    --surface: #ffffff;
    --ink: #1f2a24;
    --muted: #5d6b63;
    --line: #e2e0d8;
    --head: #eeece4;
    --accent: #1f6b4a;
    --accent-ink: #ffffff;
    --warn-bg: #fff1d6;
    --warn-ink: #7a4a00;
    --bad-bg: #fde3e0;
    --bad-ink: #8f1d12;
    --row-h: 46px;
    --head-h: 44px;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #151a17;
      --surface: #1d2420;
      --ink: #e9eee9;
      --muted: #a2b0a7;
      --line: #313b35;
      --head: #26302a;
      --accent: #6fcf9f;
      --accent-ink: #0f1f17;
      --warn-bg: #4a3910;
      --warn-ink: #ffd88a;
      --bad-bg: #521f1a;
      --bad-ink: #ffb4aa;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 28px 32px;
    background: var(--bg);
    color: var(--ink);
    font: 15px/1.4 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  main { max-width: 1200px; margin: 0 auto; }
  header { display: flex; justify-content: space-between; align-items: end; gap: 24px; flex-wrap: wrap; }
  h1 { margin: 0 0 4px; font-size: 24px; letter-spacing: -0.01em; }
  .sub { margin: 0; color: var(--muted); }
  .alerts { display: flex; gap: 8px; }

  .badge {
    display: inline-block;
    padding: 2px 9px;
    border-radius: 999px;
    font-size: 12.5px;
    font-weight: 600;
    white-space: nowrap;
  }
  .badge.soon { background: var(--warn-bg); color: var(--warn-ink); }
  .badge.expired { background: var(--bad-bg); color: var(--bad-ink); }

  .filters { margin: 22px 0 14px; display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
  .filters .label { color: var(--muted); font-weight: 600; margin-right: 4px; }
  .chip {
    font: inherit;
    color: var(--ink);
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 999px;
    padding: 6px 14px;
    cursor: pointer;
  }
  .chip:hover { border-color: var(--accent); }
  .chip .n { color: var(--muted); margin-left: 4px; font-variant-numeric: tabular-nums; }
  .chip[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }
  .chip[aria-pressed="true"] .n { color: inherit; opacity: .8; }
  .chip:focus-visible, th button:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }

  .count { margin: 0 0 8px; color: var(--muted); }

  /* Scroll area sized to show 8 rows plus a peek of the next one */
  .table-wrap {
    max-height: calc(var(--head-h) + var(--row-h) * 8.4);
    overflow-y: auto;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 10px;
  }
  table { width: 100%; border-collapse: separate; border-spacing: 0; }
  th, td { padding: 0 16px; height: var(--row-h); text-align: left; border-bottom: 1px solid var(--line); white-space: nowrap; }
  tbody tr:last-child td { border-bottom: 0; }
  thead th {
    position: sticky; top: 0; z-index: 1;
    height: var(--head-h);
    background: var(--head);
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: .04em;
    color: var(--muted);
  }
  th button {
    all: unset;
    cursor: pointer;
    display: inline-flex; gap: 6px; align-items: center;
    text-transform: inherit; letter-spacing: inherit; font-weight: 700;
  }
  th button::after { content: "↕"; opacity: .4; }
  th[aria-sort="ascending"] button::after { content: "↑"; opacity: 1; }
  th[aria-sort="descending"] button::after { content: "↓"; opacity: 1; }
  th.num, td.num { text-align: right; font-variant-numeric: tabular-nums; }
  th.num button { flex-direction: row-reverse; }
  td.item { font-weight: 600; }
  td.loc { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
  td.exp .badge { margin-left: 8px; }
  tbody tr:hover td { background: color-mix(in srgb, var(--accent) 7%, transparent); }
  .empty { padding: 32px; text-align: center; color: var(--muted); }
</style>
</head>
<body>
<main>
  <header>
    <div>
      <h1>Food bank inventory</h1>
      <p class="sub">Stock on hand as of <span id="asof"></span></p>
    </div>
    <div class="alerts" id="alerts"></div>
  </header>

  <div class="filters" id="filters" role="group" aria-label="Filter by category">
    <span class="label">Category</span>
  </div>

  <p class="count" id="count" aria-live="polite"></p>

  <div class="table-wrap" tabindex="0" role="region" aria-label="Inventory table">
    <table>
      <thead>
        <tr>
          <th data-key="item"><button type="button">Item</button></th>
          <th data-key="category"><button type="button">Category</button></th>
          <th data-key="qty" class="num"><button type="button">Quantity on hand</button></th>
          <th data-key="unit">Unit</th>
          <th data-key="expiry"><button type="button">Expiry date</button></th>
          <th data-key="loc">Location</th>
        </tr>
      </thead>
      <tbody id="rows"></tbody>
    </table>
    <div class="empty" id="empty" hidden>No items in this category.</div>
  </div>
</main>

<script>
  // Reference date for expiry flags. Swap for `new Date()` when using live data.
  const TODAY = new Date("2026-10-05T00:00:00");
  const SOON_DAYS = 14;

  const data = [
    ["Black beans",           "Canned Goods",      240, "cans",  "2028-03-14", "A-02"],
    ["Diced tomatoes",        "Canned Goods",      186, "cans",  "2027-11-30", "A-03"],
    ["Chickpeas",             "Canned Goods",       74, "cans",  "2027-08-19", "A-02"],
    ["Chicken noodle soup",   "Canned Goods",       58, "cans",  "2026-10-18", "A-04"],
    ["Sweet corn",            "Canned Goods",       15, "cans",  "2026-09-28", "A-04"],
    ["Canned tuna",           "Protein",           132, "cans",  "2027-05-22", "B-01"],
    ["Peanut butter",         "Protein",            30, "kg",    "2027-02-14", "B-02"],
    ["Dried lentils",         "Protein",            48, "kg",    "2028-02-20", "B-04"],
    ["Frozen chicken thighs", "Protein",            90, "kg",    "2027-01-12", "Z-01"],
    ["Long-grain rice",       "Grains & Pasta",     85, "kg",    "2027-12-01", "C-01"],
    ["Spaghetti",             "Grains & Pasta",     42, "kg",    "2028-01-15", "C-02"],
    ["Macaroni",              "Grains & Pasta",     28, "boxes", "2027-09-10", "C-02"],
    ["Rolled oats",           "Grains & Pasta",     36, "kg",    "2027-06-30", "C-03"],
    ["Plain flour",           "Grains & Pasta",     60, "kg",    "2027-04-17", "C-04"],
    ["Potatoes",              "Produce",           120, "kg",    "2026-10-26", "P-01"],
    ["Onions",                "Produce",            55, "kg",    "2026-11-12", "P-01"],
    ["Carrots",               "Produce",            64, "kg",    "2026-10-19", "P-02"],
    ["Apples",                "Produce",            48, "kg",    "2026-10-14", "P-03"],
    ["Bananas",               "Produce",            22, "kg",    "2026-10-07", "P-03"],
    ["UHT milk (1 L)",        "Dairy & Eggs",       36, "boxes", "2027-02-08", "B-03"],
    ["Eggs (30 count)",       "Dairy & Eggs",       18, "boxes", "2026-10-21", "F-01"],
    ["Cheddar cheese",        "Dairy & Eggs",       12, "kg",    "2026-11-04", "F-02"],
    ["Corn flakes",           "Breakfast & Snacks", 40, "boxes", "2027-03-03", "D-01"],
    ["Granola bars",          "Breakfast & Snacks", 55, "boxes", "2027-01-25", "D-03"],
    ["Crackers",              "Breakfast & Snacks", 31, "boxes", "2026-12-09", "D-02"]
  ].map(([item, category, qty, unit, expiry, loc]) => ({ item, category, qty, unit, expiry, loc }));

  const fmtDate = iso => new Date(iso + "T00:00:00").toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });
  const daysLeft = iso => Math.round((new Date(iso + "T00:00:00") - TODAY) / 86400000);
  const status = iso => { const d = daysLeft(iso); return d < 0 ? "expired" : d <= SOON_DAYS ? "soon" : ""; };

  const state = { category: "All", sortKey: null, dir: 1 };
  const categories = ["All", ...[...new Set(data.map(r => r.category))].sort()];

  const $ = id => document.getElementById(id);
  $("asof").textContent = fmtDate("2026-10-05");

  const nExpired = data.filter(r => status(r.expiry) === "expired").length;
  const nSoon = data.filter(r => status(r.expiry) === "soon").length;
  $("alerts").innerHTML =
    `<span class="badge expired">${nExpired} expired</span><span class="badge soon">${nSoon} expiring within ${SOON_DAYS} days</span>`;

  function renderFilters() {
    const box = $("filters");
    box.querySelectorAll(".chip").forEach(c => c.remove());
    for (const cat of categories) {
      const n = cat === "All" ? data.length : data.filter(r => r.category === cat).length;
      const b = document.createElement("button");
      b.type = "button";
      b.className = "chip";
      b.setAttribute("aria-pressed", String(cat === state.category));
      b.innerHTML = `${cat}<span class="n">${n}</span>`;
      b.onclick = () => { state.category = cat; renderFilters(); renderRows(); };
      box.appendChild(b);
    }
  }

  function renderRows() {
    let rows = data.filter(r => state.category === "All" || r.category === state.category);
    if (state.sortKey) {
      const k = state.sortKey;
      rows = [...rows].sort((a, b) =>
        (typeof a[k] === "number" ? a[k] - b[k] : String(a[k]).localeCompare(String(b[k]))) * state.dir);
    }
    $("rows").innerHTML = rows.map(r => {
      const s = status(r.expiry);
      const tag = s ? `<span class="badge ${s}">${s === "expired" ? "Expired" : daysLeft(r.expiry) + " days left"}</span>` : "";
      return `<tr>
        <td class="item">${r.item}</td>
        <td>${r.category}</td>
        <td class="num">${r.qty.toLocaleString("en-GB")}</td>
        <td>${r.unit}</td>
        <td class="exp">${fmtDate(r.expiry)}${tag}</td>
        <td class="loc">${r.loc}</td>
      </tr>`;
    }).join("");
    $("empty").hidden = rows.length > 0;
    $("count").textContent = `Showing ${rows.length} of ${data.length} items` +
      (state.category === "All" ? "" : ` in ${state.category}`) + (rows.length > 8 ? " — scroll for more" : "");
  }

  document.querySelectorAll("th[data-key] button").forEach(btn => {
    const th = btn.parentElement;
    btn.onclick = () => {
      const k = th.dataset.key;
      state.dir = state.sortKey === k ? -state.dir : 1;
      state.sortKey = k;
      document.querySelectorAll("th[data-key]").forEach(t => t.removeAttribute("aria-sort"));
      th.setAttribute("aria-sort", state.dir === 1 ? "ascending" : "descending");
      renderRows();
    };
  });

  renderFilters();
  renderRows();
</script>
</body>
</html>
```

**What it does**
- **Table:** 25 realistic items with the six columns you asked for. Units are only cans, kg and boxes. Shelf codes follow a pattern: A–D are dry shelving, P is produce, F is fridge and Z is freezer.
- **Category filter:** a row of buttons above the table, one per category plus "All". Each button shows an item count, and a line under them reads "Showing 8 of 25 items".
- **Expiry flags:** the page treats 5 Oct 2026 as today. Items already past date get a red "Expired" badge. Items expiring within 14 days get an amber "N days left" badge. The badges are text as well as color. The page header counts both.
- **Sorting:** you can sort by Item, Category, Quantity and Expiry date by clicking the column headers.
- **Self-contained:** inline CSS and JavaScript, system fonts only, no external assets. It has a dark mode that follows the system setting.

The `TODAY` constant near the top of the script is fixed so the demo data stays meaningful. Change it to `new Date()` if you plug in live data.
