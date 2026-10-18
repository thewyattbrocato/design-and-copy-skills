I couldn't save the file: the Write tool is disabled in this session, and I have no shell available to create files. The complete page is below. Save it as `orders.html` and open it in a browser.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orders</title>
<style>
:root{--ink:#1f2328;--muted:#5b6370;--line:#d9dde3;--pending:#fde68a;--pending-ink:#713f12;--done:#bbf7d0;--done-ink:#14532d}
*{box-sizing:border-box}
[hidden]{display:none!important}
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:var(--ink);font-size:16px}
h1{margin:0 0 16px}
h2{font-size:18px;margin:32px 0 8px}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px}
.toolbar input{flex:1 1 240px;padding:8px 10px;font:inherit;border:1px solid #9aa3ad;border-radius:6px}
select,button,.btn{font:inherit;padding:8px 12px;border-radius:6px;border:1px solid #9aa3ad;background:#fff;cursor:pointer}
button.primary{background:var(--ink);color:#fff;border-color:var(--ink)}
button.danger{color:#9b1c1c;border-color:#e5a5a5}
table{border-collapse:collapse;width:100%}
th,td{border-bottom:1px solid var(--line);padding:10px 8px;text-align:left;vertical-align:middle}
th{background:#f3f4f6;font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}
.num{text-align:right;font-variant-numeric:tabular-nums}
tr.done td{color:var(--muted)}
.status{display:inline-block;padding:2px 10px;border-radius:10px;font-size:14px;font-weight:600}
.status.Pending{background:var(--pending);color:var(--pending-ink)}
.status.Complete{background:var(--done);color:var(--done-ink)}
.actions{white-space:nowrap}
.actions button+button{margin-left:4px}
#none{color:var(--muted);padding:16px 0}
#msg{position:fixed;top:16px;right:16px;background:#14532d;color:#fff;padding:10px 16px;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,.2)}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center}
.dialog{background:#fff;padding:20px;border-radius:8px;width:min(420px,92vw);box-shadow:0 8px 24px rgba(0,0,0,.25)}
.dialog label{display:block;margin-bottom:12px;font-size:14px;color:var(--muted)}
.dialog input,.dialog select{display:block;width:100%;margin-top:4px;padding:8px 10px;font:inherit;font-size:16px;color:var(--ink);border:1px solid #9aa3ad;border-radius:6px}
.dialog .row{display:flex;gap:8px;justify-content:flex-end;margin-top:16px}
.err{color:#9b1c1c;font-size:14px;min-height:1em}
.bake{max-width:420px}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar">
  <input id="search" type="search" placeholder="Search customer, item, or #" aria-label="Search orders">
  <select id="filter" aria-label="Filter by status">
    <option value="">All statuses</option>
    <option>Pending</option>
    <option>Complete</option>
  </select>
  <button id="add" class="primary">Add Order</button>
</div>
<table>
  <thead><tr><th>#</th><th>Customer</th><th>Item</th><th class="num">Qty</th><th>Status</th><th>Actions</th></tr></thead>
  <tbody id="rows"></tbody>
</table>
<p id="none" hidden>No results found.</p>

<h2>To bake (pending)</h2>
<table class="bake">
  <thead><tr><th>Item</th><th class="num">Total</th></tr></thead>
  <tbody id="bake"></tbody>
</table>

<div id="form" class="overlay" hidden>
  <div class="dialog" role="dialog" aria-modal="true" aria-labelledby="form-title">
    <h2 id="form-title" style="margin-top:0">Add Order</h2>
    <label>Customer <input id="f-customer" required></label>
    <label>Item <input id="f-item" required></label>
    <label>Qty <input id="f-qty" type="number" min="1" step="1" required></label>
    <label>Status <select id="f-status"><option>Pending</option><option>Complete</option></select></label>
    <div id="f-err" class="err"></div>
    <div class="row"><button id="f-cancel">Cancel</button><button id="f-save" class="primary">Save</button></div>
  </div>
</div>

<div id="confirm" class="overlay" hidden>
  <div class="dialog" role="alertdialog" aria-labelledby="confirm-text">
    <p id="confirm-text" style="margin-top:0">Are you sure you want to delete this?</p>
    <div class="row"><button id="c-no">No</button><button id="c-yes" class="danger">Yes</button></div>
  </div>
</div>

<div id="msg" hidden>Success!</div>

<script>
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

// Sample data for layout only; replace with real orders.
let orders = [
  {id:1, customer:'Maple Street Café', item:'Sourdough loaf', qty:10, status:'Pending'},
  {id:2, customer:'Harbor Coffee Co.', item:'Croissant (box of 12)', qty:25, status:'Complete'},
  {id:3, customer:'Juniper & Co.', item:'Sourdough loaf', qty:6, status:'Pending'},
  {id:4, customer:'Corner Bean', item:'Cinnamon roll', qty:24, status:'Pending'},
  {id:5, customer:'Oak Table Café', item:'Baguette', qty:12, status:'Complete'},
];
let nextId = 6, editingId = null, deletingId = null, msgTimer = null;

function visible() {
  const q = $('#search').value.trim().toLowerCase();
  const st = $('#filter').value;
  return orders.filter(o =>
    (!st || o.status === st) &&
    (!q || [o.customer, o.item, String(o.id)].some(v => v.toLowerCase().includes(q))));
}

function render() {
  const list = visible();
  $('#rows').innerHTML = list.map(o => `
    <tr class="${o.status === 'Complete' ? 'done' : ''}">
      <td>${o.id}</td>
      <td>${esc(o.customer)}</td>
      <td>${esc(o.item)}</td>
      <td class="num">${o.qty}</td>
      <td><span class="status ${o.status}">${o.status}</span></td>
      <td class="actions"><button data-edit="${o.id}">Edit</button><button class="danger" data-del="${o.id}">Delete</button></td>
    </tr>`).join('');
  $('#none').hidden = list.length > 0;
  renderBake();
}

// Totals of pending items, so bakers see what to make regardless of filters.
function renderBake() {
  const totals = {};
  orders.filter(o => o.status === 'Pending').forEach(o => totals[o.item] = (totals[o.item] || 0) + o.qty);
  const rows = Object.entries(totals).sort((a, b) => a[0].localeCompare(b[0]));
  $('#bake').innerHTML = rows.length
    ? rows.map(([item, q]) => `<tr><td>${esc(item)}</td><td class="num">${q}</td></tr>`).join('')
    : '<tr><td colspan="2">Nothing pending to bake.</td></tr>';
}

function showMsg(text) {
  $('#msg').textContent = text;
  $('#msg').hidden = false;
  clearTimeout(msgTimer);
  msgTimer = setTimeout(() => $('#msg').hidden = true, 2500);
}

function openForm(id) {
  editingId = id;
  const o = id ? orders.find(x => x.id === id) : {customer:'', item:'', qty:'', status:'Pending'};
  $('#form-title').textContent = id ? `Edit order #${id}` : 'Add Order';
  $('#f-customer').value = o.customer;
  $('#f-item').value = o.item;
  $('#f-qty').value = o.qty;
  $('#f-status').value = o.status;
  $('#f-err').textContent = '';
  $('#form').hidden = false;
  $('#f-customer').focus();
}

function closeForm() { $('#form').hidden = true; editingId = null; }

function saveForm() {
  const data = {
    customer: $('#f-customer').value.trim(),
    item: $('#f-item').value.trim(),
    qty: parseInt($('#f-qty').value, 10),
    status: $('#f-status').value,
  };
  if (!data.customer || !data.item || !(data.qty > 0)) {
    $('#f-err').textContent = 'Customer, item, and a quantity of at least 1 are required.';
    return;
  }
  if (editingId) {
    Object.assign(orders.find(x => x.id === editingId), data);
    showMsg(`Order #${editingId} saved.`);
  } else {
    orders.push({id: nextId++, ...data});
    showMsg('Order added.');
  }
  closeForm();
  render();
}

function askDelete(id) {
  deletingId = id;
  const o = orders.find(x => x.id === id);
  $('#confirm-text').textContent = `Delete order #${id} for ${o.customer} (${o.item})?`;
  $('#confirm').hidden = false;
  $('#c-no').focus();
}

function confirmDelete() {
  orders = orders.filter(o => o.id !== deletingId);
  showMsg(`Order #${deletingId} deleted.`);
  deletingId = null;
  $('#confirm').hidden = true;
  render();
}

$('#search').addEventListener('input', render);
$('#filter').addEventListener('change', render);
$('#add').addEventListener('click', () => openForm(null));
$('#f-save').addEventListener('click', saveForm);
$('#f-cancel').addEventListener('click', closeForm);
$('#c-yes').addEventListener('click', confirmDelete);
$('#c-no').addEventListener('click', () => { deletingId = null; $('#confirm').hidden = true; });
$('#rows').addEventListener('click', e => {
  const edit = e.target.closest('[data-edit]');
  const del = e.target.closest('[data-del]');
  if (edit) openForm(Number(edit.dataset.edit));
  if (del) askDelete(Number(del.dataset.del));
});
document.addEventListener('keydown', e => {
  if (e.key !== 'Escape') return;
  if (!$('#confirm').hidden) { deletingId = null; $('#confirm').hidden = true; }
  else if (!$('#form').hidden) closeForm();
});

render();
</script>
</body></html>
```

**What changed**

- **Behavior that was only a mockup now works.** Search filters rows by customer, item, or order number. The status dropdown filters by Pending or Complete, and the "No results found" message appears when nothing matches. Add Order and Edit open a form with validation. Delete asks for confirmation and names the order, then the "Success!" message reports the result and fades after a few seconds.
- **A "To bake (pending)" table** sums pending quantities by item. It ignores the search and status filters, so bakers see the full production list at 4 a.m.
- **Readability:** larger text, higher-contrast status badges that carry a label as well as color, right-aligned quantities, and completed rows greyed out.

**Choices I made that you may want to change**

- Statuses are still just Pending and Complete, as in your original. If the driver needs "Out for delivery" or "Ready," add it to the form and filter lists.
- The data is sample data, and nothing is saved. Refreshing the page resets it. Persistence needs a backend or at least `localStorage`, which I left out because you asked to keep it working the way it does.
- I did not run this in a browser. I checked it by reading the code, so please open it once and try add, edit, delete, and search.
