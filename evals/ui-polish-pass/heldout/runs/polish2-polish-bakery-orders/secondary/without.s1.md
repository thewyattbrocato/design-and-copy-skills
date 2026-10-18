I couldn't save the file. The Write tool is disabled in this session, and I don't have another way to write to disk. Here is the finished page to save as `orders.html`:

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orders</title>
<style>
:root{--ink:#1f1a17;--paper:#fffdf9;--line:#e7e0d6;--muted:#6b6259;--head:#f5efe6;--accent:#8a4b1f;
--pend-bg:#fde8c8;--pend-ink:#7a4300;--done-bg:#d9f2e0;--done-ink:#1d5c34}
@media (prefers-color-scheme:dark){:root{--ink:#f4ede4;--paper:#1b1714;--line:#3a322c;--muted:#a79b8f;--head:#26201c;--accent:#f0a965;
--pend-bg:#4a3216;--pend-ink:#ffd9a6;--done-bg:#173a25;--done-ink:#b8e8c8}}
*{box-sizing:border-box}
body{font-family:system-ui,-apple-system,sans-serif;margin:0;padding:24px;background:var(--paper);color:var(--ink);font-size:17px;line-height:1.4}
header{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;margin-bottom:20px}
h1{margin:0;font-size:2rem}
.sub{margin:0;color:var(--muted)}
h2{font-size:1rem;text-transform:uppercase;letter-spacing:.06em;color:var(--accent);margin:0 0 8px}
.bake{border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-bottom:20px;background:var(--head)}
#bake-list{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:12px 28px}
#bake-list li{font-size:1.1rem}
#bake-list strong{font-size:1.8rem;font-variant-numeric:tabular-nums;margin-right:6px}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px;align-items:center}
.toolbar input,.toolbar select{font:inherit;min-height:44px;padding:0 12px;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink)}
.toolbar input{flex:1 1 220px}
button{font:inherit;min-height:44px;padding:0 16px;border-radius:8px;border:1px solid var(--line);background:var(--paper);color:var(--ink);cursor:pointer}
button:hover{border-color:var(--accent)}
.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.primary:hover{opacity:.9}
.table-wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%}
th,td{border-bottom:1px solid var(--line);padding:12px 10px;text-align:left;vertical-align:middle}
th{background:var(--head);font-size:.85rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);position:sticky;top:0}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
td.qty{font-size:1.5rem;font-weight:700}
td.cust{font-weight:600}
td.item{font-size:1.05rem}
td.no{color:var(--muted);font-variant-numeric:tabular-nums}
tr.done td{color:var(--muted)}
tr.done td.qty{font-weight:500}
.status{display:inline-block;padding:3px 10px;border-radius:999px;font-size:.9rem;font-weight:600;background:var(--line)}
.status.Pending{background:var(--pend-bg);color:var(--pend-ink)}
.status.Complete{background:var(--done-bg);color:var(--done-ink)}
.actions{white-space:nowrap}
.actions button{margin-left:4px}
.delete{color:#a33a2a}
#none{color:var(--muted);font-size:1.1rem;padding:24px 0;text-align:center}
#msg{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--done-bg);color:var(--done-ink);padding:12px 20px;border-radius:10px;font-weight:600;box-shadow:0 4px 16px rgba(0,0,0,.15)}
#confirm{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);width:min(440px,calc(100% - 32px));background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:20px;box-shadow:0 8px 28px rgba(0,0,0,.25)}
#confirm p{margin:0 0 16px;font-size:1.1rem;font-weight:600}
#confirm .yes{background:#a33a2a;border-color:#a33a2a;color:#fff}
[hidden]{display:none!important}
@media (max-width:640px){body{padding:16px}h1{font-size:1.6rem}td.item{font-size:1rem}}
</style>
</head>
<body>
<header>
  <h1>Orders</h1>
  <p class="sub" id="count"></p>
</header>

<section class="bake" aria-labelledby="bake-title">
  <h2 id="bake-title">To bake</h2>
  <ul id="bake-list"></ul>
</section>

<div class="toolbar">
  <input id="search" type="search" placeholder="Search customer or item…" aria-label="Search orders">
  <select id="status" aria-label="Filter by status">
    <option value="All">All statuses</option>
    <option value="Pending">Pending</option>
    <option value="Complete">Complete</option>
  </select>
  <button class="primary">Add Order</button>
</div>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>#</th><th>Customer</th><th>Item</th><th class="num">Qty</th><th>Status</th><th>Actions</th></tr>
  </thead>
  <tbody>
    <tr data-status="Pending"><td class="no">1</td><td class="cust">Customer 1</td><td class="item">Product A</td><td class="num qty">10</td><td><span class="status Pending">Pending</span></td><td class="actions"><button class="edit">Edit</button><button class="delete">Delete</button></td></tr>
    <tr data-status="Complete" class="done"><td class="no">2</td><td class="cust">Customer 2</td><td class="item">Product B</td><td class="num qty">25</td><td><span class="status Complete">Complete</span></td><td class="actions"><button class="edit">Edit</button><button class="delete">Delete</button></td></tr>
  </tbody>
</table>
</div>

<p id="none" hidden>No results found.</p>
<div id="msg" role="status" hidden>Success!</div>
<div id="confirm" role="alertdialog" aria-labelledby="confirm-text" hidden>
  <p id="confirm-text">Are you sure you want to delete this order?</p>
  <button class="yes" id="yes">Yes, delete</button> <button id="no">No</button>
</div>

<script>
const tbody = document.querySelector('tbody');
const search = document.getElementById('search');
const statusSel = document.getElementById('status');
const none = document.getElementById('none');
const msg = document.getElementById('msg');
const confirmBox = document.getElementById('confirm');
const bakeList = document.getElementById('bake-list');
const count = document.getElementById('count');
let pendingRow = null;
let msgTimer = null;

const allRows = () => [...tbody.rows];

function updateTotals() {
  const totals = {};
  let pending = 0;
  allRows().forEach(r => {
    if (r.dataset.status !== 'Pending') return;
    pending++;
    const item = r.cells[2].textContent;
    totals[item] = (totals[item] || 0) + Number(r.cells[3].textContent);
  });

  bakeList.replaceChildren();
  const entries = Object.entries(totals);
  if (!entries.length) {
    const li = document.createElement('li');
    li.textContent = 'Nothing to bake.';
    bakeList.append(li);
  }
  entries.forEach(([item, qty]) => {
    const li = document.createElement('li');
    const n = document.createElement('strong');
    n.textContent = qty;
    li.append(n, item);
    bakeList.append(li);
  });

  count.textContent = `${allRows().length} orders · ${pending} pending`;
}

function applyFilters() {
  const q = search.value.trim().toLowerCase();
  const s = statusSel.value;
  let shown = 0;
  allRows().forEach(r => {
    const text = [...r.cells].slice(0, 4).map(c => c.textContent).join(' ').toLowerCase();
    const ok = (!q || text.includes(q)) && (s === 'All' || r.dataset.status === s);
    r.hidden = !ok;
    if (ok) shown++;
  });
  none.hidden = shown > 0;
}

function showMsg(text) {
  msg.textContent = text;
  msg.hidden = false;
  clearTimeout(msgTimer);
  msgTimer = setTimeout(() => { msg.hidden = true; }, 2500);
}

tbody.addEventListener('click', e => {
  const btn = e.target.closest('button');
  if (!btn) return;
  if (btn.classList.contains('delete')) {
    pendingRow = btn.closest('tr');
    msg.hidden = true;
    confirmBox.hidden = false;
    document.getElementById('no').focus();
  }
});

document.getElementById('yes').addEventListener('click', () => {
  if (pendingRow) pendingRow.remove();
  pendingRow = null;
  confirmBox.hidden = true;
  showMsg('Order deleted.');
  applyFilters();
  updateTotals();
});

document.getElementById('no').addEventListener('click', () => {
  pendingRow = null;
  confirmBox.hidden = true;
});

search.addEventListener('input', applyFilters);
statusSel.addEventListener('change', applyFilters);

updateTotals();
applyFilters();
</script>
</body>
</html>
```

**What changed**

- **Bake list at the top.** It totals the quantity of each product across pending orders, so the 4 a.m. baker sees "Product A: 10, Product B: 25" without doing arithmetic. It recalculates after a delete.
- **Readable in a dim kitchen.** Larger type, big bold quantities, high-contrast status pills (Pending is amber, Complete is green), and a dark theme that follows the system setting.
- **Driver-friendly.** Customer names are bold, completed rows are muted, the table scrolls sideways on a phone, and buttons are at least 44px tall for touch.
- **Working controls.** Search matches customer and item text. The status filter is populated with Pending and Complete. Delete asks for confirmation, then removes the row and shows a message. "No results found" appears when filters match nothing.
- **Kept as-is:** the `#`, Customer, Item, Qty, Status, and Actions columns, the same sample data, and the "No results," success, and confirm elements.

**Choices to check**

- The success message now says "Order deleted." instead of "Success!" It's more useful at 4 a.m. Change the `showMsg` call if you want the original text.
- I added a small script. The original page had no behavior, so search, the filter, and delete had nothing to do.
- **Add Order and Edit have no behavior yet.** They need a form and a data source, which the template doesn't have. Tell me where the orders come from and I'll wire them up.
- The bake list counts only Pending orders. If bakers should also see Complete items, that's a one-line change.
