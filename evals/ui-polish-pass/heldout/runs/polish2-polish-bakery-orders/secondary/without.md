I can't save files in this session, so the complete page is below. I haven't opened it in a browser.

What changed:
- **Real statuses.** The `Status 1` and `Status 2` placeholders are now Pending and Complete.
- **"To bake" summary at the top.** It totals quantities by product across Pending orders, so the 4 a.m. baker sees the list first.
- **Working toolbar.** Search matches customer or item, the status filter works, and "No results found." shows when nothing matches.
- **Add and Edit** open a form. **Delete** asks for confirmation, and the confirmation names the order.
- **Success message** appears after each save or delete.
- **Visual pass.** Larger quantities, pending and complete pills in different colors, and completed rows dimmed.
- **Print.** Toolbar and action buttons are hidden, so the driver can print a clean list.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orders</title>
<style>
:root{--ink:#1f1f1f;--muted:#6b6b6b;--line:#e2e2e2;--pending:#fde68a;--complete:#bbf7d0}
[hidden]{display:none!important}
*{box-sizing:border-box}
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:var(--ink);font-size:16px}
h1{margin:0 0 16px;font-size:28px}
h2{margin:0 0 12px;font-size:20px}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px}
.toolbar input{flex:1 1 220px;padding:8px 10px}
input,select,button{font:inherit;padding:8px 12px;border:1px solid #bbb;border-radius:6px;background:#fff}
select{padding:8px}
button{cursor:pointer}
button:hover{filter:brightness(.95)}
button.primary{background:#222;color:#fff;border-color:#222}
button.danger{color:#b91c1c}
.bake{border:1px solid var(--line);border-radius:8px;padding:12px 16px;margin-bottom:16px;background:#fafafa}
.bake h2{font-size:18px}
.bake ul{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:8px 24px}
.bake li{font-size:18px}
.bake b{font-size:22px;margin-right:6px;font-variant-numeric:tabular-nums}
table{border-collapse:collapse;width:100%}
th,td{border-bottom:1px solid var(--line);padding:10px 8px;text-align:left;vertical-align:middle}
th{background:#f3f4f6;font-weight:600;border-top:1px solid var(--line)}
td.qty,th.qty{text-align:right}
td.qty{font-size:18px;font-weight:700;font-variant-numeric:tabular-nums}
tr[data-status="Complete"] td:not(.actions):not(.status-cell){color:var(--muted)}
.status{display:inline-block;padding:2px 10px;border-radius:10px;background:#e5e7eb;font-size:14px}
.status.pending{background:var(--pending)}
.status.complete{background:var(--complete)}
.actions button{margin-right:4px}
#none{color:var(--muted);font-size:18px;padding:16px 0}
#msg{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#166534;color:#fff;padding:10px 18px;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,.2)}
#confirm{position:fixed;inset:0;background:rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center}
#confirm .box{background:#fff;border-radius:10px;padding:20px;max-width:420px;width:92vw;box-shadow:0 8px 24px rgba(0,0,0,.25)}
#confirm-what{font-weight:600}
dialog{border:1px solid #bbb;border-radius:10px;padding:20px;width:min(420px,92vw)}
dialog label{display:block;margin-bottom:12px}
dialog label input,dialog label select{display:block;width:100%;margin-top:4px}
.form-buttons{display:flex;justify-content:flex-end;gap:8px;margin-top:8px}
@media print{.toolbar,.actions,th.actions,#msg,#confirm,dialog{display:none!important}body{padding:0}}
</style></head><body>
<h1>Orders</h1>

<section class="bake" aria-labelledby="bake-h">
<h2 id="bake-h">To bake (pending)</h2>
<ul id="bake"></ul>
</section>

<div class="toolbar"><input id="search" type="search" placeholder="Search customer or item..."> <select id="filter"><option value="">All</option><option>Pending</option><option>Complete</option></select> <button id="add" class="primary">Add Order</button></div>

<table>
<thead><tr><th>#</th><th>Customer Name</th><th>Item</th><th class="qty">Qty</th><th>Status</th><th class="actions">Actions</th></tr></thead>
<tbody id="rows">
<tr><td>1</td><td>Customer 1</td><td>Product A</td><td class="qty">10</td><td><span class="status pending">Pending</span></td><td class="actions"><button class="edit">Edit</button> <button class="delete danger">Delete</button></td></tr>
<tr><td>2</td><td>Customer 2</td><td>Product B</td><td class="qty">25</td><td><span class="status complete">Complete</span></td><td class="actions"><button class="edit">Edit</button> <button class="delete danger">Delete</button></td></tr>
</tbody>
</table>
<p id="none" hidden>No results found.</p>

<div id="msg" hidden>Success!</div>

<div id="confirm" hidden><div class="box">Are you sure you want to delete this?<br><span id="confirm-what"></span><br><br><button id="yes" class="danger">Yes</button> <button id="no">No</button></div></div>

<dialog id="form"><form id="order-form">
<h2 id="form-title">Add Order</h2>
<label>Customer Name <input id="f-customer" required></label>
<label>Item <input id="f-item" required></label>
<label>Qty <input id="f-qty" type="number" min="1" required></label>
<label>Status <select id="f-status"><option>Pending</option><option>Complete</option></select></label>
<div class="form-buttons"><button type="button" id="f-cancel">Cancel</button> <button class="primary" type="submit">Save</button></div>
</form></dialog>

<script>
const $ = s => document.querySelector(s);
const rows = $('#rows'), search = $('#search'), filter = $('#filter'), none = $('#none'), msg = $('#msg');
const confirmBox = $('#confirm'), form = $('#form'), fForm = $('#order-form');
let editing = null, doomed = null, toastTimer;

function toast(t) {
  msg.textContent = t; msg.hidden = false;
  clearTimeout(toastTimer); toastTimer = setTimeout(() => msg.hidden = true, 2500);
}

function readRow(tr) {
  const c = tr.cells;
  return { customer: c[1].textContent, item: c[2].textContent, qty: c[3].textContent, status: c[4].textContent.trim() };
}

function writeRow(tr, o) {
  const c = tr.cells;
  c[1].textContent = o.customer;
  c[2].textContent = o.item;
  c[3].textContent = o.qty;
  c[3].className = 'qty';
  const s = document.createElement('span');
  s.className = 'status ' + o.status.toLowerCase();
  s.textContent = o.status;
  c[4].replaceChildren(s);
  tr.dataset.status = o.status;
}

function nextNumber() {
  return Math.max(0, ...[...rows.rows].map(r => +r.cells[0].textContent)) + 1;
}

function newRow() {
  const tr = document.createElement('tr');
  for (let i = 0; i < 6; i++) tr.append(document.createElement('td'));
  tr.cells[0].textContent = nextNumber();
  tr.cells[5].className = 'actions';
  tr.cells[5].innerHTML = '<button class="edit">Edit</button> <button class="delete danger">Delete</button>';
  return tr;
}

function refresh() {
  const q = search.value.trim().toLowerCase(), st = filter.value;
  let shown = 0;
  const totals = new Map();
  for (const tr of rows.rows) {
    const o = readRow(tr);
    tr.dataset.status = o.status;
    const ok = (!st || o.status === st) && (!q || (o.customer + ' ' + o.item).toLowerCase().includes(q));
    tr.hidden = !ok;
    if (ok) shown++;
    if (o.status === 'Pending') totals.set(o.item, (totals.get(o.item) || 0) + (+o.qty || 0));
  }
  none.hidden = shown > 0;

  const bake = $('#bake');
  if (!totals.size) {
    const li = document.createElement('li');
    li.textContent = 'Nothing to bake.';
    bake.replaceChildren(li);
  } else {
    bake.replaceChildren(...[...totals].map(([item, n]) => {
      const li = document.createElement('li'), b = document.createElement('b');
      b.textContent = n;
      li.append(b, item);
      return li;
    }));
  }
}

function openForm(tr) {
  editing = tr;
  $('#form-title').textContent = tr ? 'Edit Order' : 'Add Order';
  const o = tr ? readRow(tr) : { customer: '', item: '', qty: '', status: 'Pending' };
  $('#f-customer').value = o.customer;
  $('#f-item').value = o.item;
  $('#f-qty').value = o.qty;
  $('#f-status').value = o.status;
  form.showModal();
  $('#f-customer').focus();
}

$('#add').onclick = () => openForm(null);
$('#f-cancel').onclick = () => form.close();
search.addEventListener('input', refresh);
filter.addEventListener('change', refresh);

rows.addEventListener('click', e => {
  const tr = e.target.closest('tr');
  if (!tr) return;
  if (e.target.matches('.edit')) openForm(tr);
  if (e.target.matches('.delete')) {
    doomed = tr;
    const o = readRow(tr);
    $('#confirm-what').textContent = `#${tr.cells[0].textContent} · ${o.customer} · ${o.qty} × ${o.item}`;
    confirmBox.hidden = false;
    $('#yes').focus();
  }
});

$('#no').onclick = () => { confirmBox.hidden = true; doomed = null; };
$('#yes').onclick = () => {
  if (doomed) doomed.remove();
  doomed = null;
  confirmBox.hidden = true;
  refresh();
  toast('Order deleted');
};

fForm.addEventListener('submit', e => {
  e.preventDefault();
  const o = {
    customer: $('#f-customer').value.trim(),
    item: $('#f-item').value.trim(),
    qty: $('#f-qty').value,
    status: $('#f-status').value
  };
  const isNew = !editing;
  const tr = editing || newRow();
  writeRow(tr, o);
  if (isNew) rows.append(tr);
  editing = null;
  form.close();
  refresh();
  toast(isNew ? 'Order added' : 'Order saved');
});

refresh();
</script>
</body></html>
```

Choices I made that you may want to change:
- The Add and Edit form is a native `<dialog>`, so it works without a library. It's fine on phones but not tested on old browsers.
- Delete removes the row immediately after confirmation. Nothing is saved anywhere, so a page reload resets the list. If the orders need to persist, that needs a backend, which I left out.
- Order numbers aren't renumbered after a delete, so the # column stays stable for the bakers and driver.
