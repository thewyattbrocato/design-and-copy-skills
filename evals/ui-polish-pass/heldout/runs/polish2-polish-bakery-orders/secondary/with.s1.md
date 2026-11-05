```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222;line-height:1.4}
h1{margin:0 0 16px;font-size:1.6rem}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px}
input,select,button{font:inherit;padding:8px 12px;border:1px solid #767676;border-radius:6px;background:#fff;color:#222}
input{flex:1 1 220px;min-width:0}
button{cursor:pointer}
button:hover{background:#f3f4f6}
.danger{background:#b91c1c;color:#fff;border-color:#b91c1c}
.danger:hover{background:#991b1b}
:focus-visible{outline:3px solid #2563eb;outline-offset:2px}
.table-wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%}
th,td{border-bottom:1px solid #ddd;padding:10px 8px;text-align:left;vertical-align:middle}
th{font-size:.85rem;text-transform:uppercase;letter-spacing:.03em;color:#555;border-bottom:2px solid #bbb}
.num{text-align:right;font-variant-numeric:tabular-nums}
.status{display:inline-block;padding:2px 10px;border-radius:10px;background:#e5e7eb;font-size:.9rem;white-space:nowrap}
.actions{white-space:nowrap}
.actions button{padding:4px 10px;font-size:.9rem}
.note{padding:16px 8px;color:#444}
.msg{margin-top:16px;padding:10px 12px;border-radius:6px;background:#e5e7eb}
dialog{border:1px solid #888;border-radius:8px;padding:20px;max-width:420px;color:#222}
dialog::backdrop{background:rgba(0,0,0,.4)}
.dialog-actions{display:flex;gap:8px;justify-content:flex-end;margin-top:16px}
.visually-hidden{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (prefers-reduced-motion: reduce){*{transition:none!important;animation:none!important}}
</style></head>
<body>
<h1>Orders</h1>

<div class="toolbar" role="search">
  <input id="q" type="search" placeholder="Search café, item or order #" aria-label="Search orders">
  <select id="status" aria-label="Filter by status">
    <option value="all">All statuses</option>
    <option value="pending">Pending</option>
    <option value="complete">Complete</option>
  </select>
  <button type="button" id="add" class="primary">Add Order</button>
</div>

<div class="table-wrap" tabindex="0" aria-label="Orders table, scrolls sideways on small screens">
<table>
  <thead>
    <tr><th scope="col">#</th><th scope="col">Café</th><th scope="col">Item</th><th scope="col" class="num">Qty</th><th scope="col">Status</th><th scope="col">Actions</th></tr>
  </thead>
  <tbody id="rows">
    <tr data-status="pending"><td>1</td><td>Harbor Café</td><td>Sourdough loaf</td><td class="num">10</td><td><span class="status">Pending</span></td>
      <td class="actions"><button type="button" aria-label="Edit order 1 for Harbor Café">Edit</button> <button type="button" class="danger" data-delete aria-label="Delete order 1 for Harbor Café">Delete</button></td></tr>
    <tr data-status="complete"><td>2</td><td>Main St Café</td><td>Croissant</td><td class="num">25</td><td><span class="status">Complete</span></td>
      <td class="actions"><button type="button" aria-label="Edit order 2 for Main St Café">Edit</button> <button type="button" class="danger" data-delete aria-label="Delete order 2 for Main St Café">Delete</button></td></tr>
  </tbody>
</table>
</div>

<p id="empty" class="note" hidden>No orders yet. Add the first order to start today's bake list.</p>
<p id="none" class="note" hidden>No orders match your search. <button type="button" id="clear">Clear search and filter</button></p>
<div id="msg" class="msg" role="status" hidden></div>

<dialog id="confirm" aria-labelledby="confirm-title">
  <h2 id="confirm-title" style="font-size:1.1rem;margin:0 0 8px">Delete this order?</h2>
  <p id="confirm-text" style="margin:0"></p>
  <div class="dialog-actions">
    <button type="button" id="keep" autofocus>Keep order</button>
    <button type="button" id="do-delete" class="danger">Delete order</button>
  </div>
</dialog>

<script>
const q = document.getElementById('q'), statusSel = document.getElementById('status');
const rows = document.getElementById('rows'), none = document.getElementById('none'), empty = document.getElementById('empty');
const msg = document.getElementById('msg'), dlg = document.getElementById('confirm'), dlgText = document.getElementById('confirm-text');
let pendingRow = null, opener = null;

function applyFilters() {
  const term = q.value.trim().toLowerCase(), s = statusSel.value;
  let shown = 0;
  for (const r of rows.rows) {
    const ok = (!term || r.textContent.toLowerCase().includes(term)) && (s === 'all' || r.dataset.status === s);
    r.hidden = !ok;
    if (ok) shown++;
  }
  empty.hidden = rows.rows.length > 0;
  none.hidden = rows.rows.length === 0 || shown > 0;
}

q.addEventListener('input', applyFilters);
statusSel.addEventListener('change', applyFilters);
document.getElementById('clear').addEventListener('click', () => { q.value = ''; statusSel.value = 'all'; applyFilters(); q.focus(); });

rows.addEventListener('click', e => {
  const b = e.target.closest('button[data-delete]');
  if (!b) return;
  opener = b;
  pendingRow = b.closest('tr');
  const c = pendingRow.cells;
  dlgText.textContent = `${c[0].textContent}: ${c[3].textContent} × ${c[2].textContent} for ${c[1].textContent}. This can't be undone.`;
  dlg.showModal();
});

document.getElementById('keep').addEventListener('click', () => dlg.close());
dlg.addEventListener('close', () => { if (opener && opener.isConnected) opener.focus(); });

document.getElementById('do-delete').addEventListener('click', () => {
  const id = pendingRow.cells[0].textContent;
  pendingRow.remove();
  pendingRow = null; opener = null;
  dlg.close();
  applyFilters();
  msg.textContent = `Order ${id} deleted.`;
  msg.hidden = false;
  document.getElementById('add').focus();
});

applyFilters();
</script>
</body></html>
```

**What changed**
- Columns now name the bakery's nouns: "Café" instead of "Customer Name". Sample rows use placeholder cafés and products; replace them with real data.
- Qty is right-aligned with tabular numbers so the column scans at 4am.
- Status filter options are real statuses. Search and filter work together, and the "No results" message offers a one-click clear.
- Empty list shows a first-use message instead of an empty table.
- Edit and Delete have names that include the order and café, so they're distinct to a screen reader.
- Delete opens a real modal dialog (native, so Escape and focus handling work). It states the consequence and uses the verbs "Delete order" / "Keep order". Keep is focused by default. Focus returns to the row's Delete button on cancel and to Add Order after a delete.
- The success message is a live region and names the deleted order.
- The table scrolls sideways on narrow screens instead of breaking the layout. Focus rings are visible on every control.

**Notes**
- Kept the original neutral palette, type and layout. The only new color is the red Delete button, because it's a destructive action.
- Edit and Add Order had no defined behavior, so they're still unwired. Tell me what they should do and I'll add it.
- Not tested in a browser or with a screen reader. I checked the code by reading it.
