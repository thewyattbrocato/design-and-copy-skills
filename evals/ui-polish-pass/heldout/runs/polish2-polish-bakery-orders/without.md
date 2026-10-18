I couldn't save this to a file because the Write tool is disabled in this session. The full page is below, and I haven't opened or run it in a browser. Save it as `orders.html`.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orders</title>
<style>
:root{
  --bg:#faf6ef;--surface:#fff;--text:#2b2118;--muted:#6b5d50;--line:#e3d9c8;
  --accent:#8a4b12;--accent-text:#fff;--focus:#1d4ed8;
  --pending-bg:#fde9b8;--pending-fg:#5c3a00;
  --done-bg:#d5ecd4;--done-fg:#174a1c;
  --danger:#a32020;
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#16120e;--surface:#211b15;--text:#f3ebdf;--muted:#b3a593;--line:#3a3128;
    --accent:#f0b25e;--accent-text:#1a1208;--focus:#8db4ff;
    --pending-bg:#4a3606;--pending-fg:#ffdf9a;
    --done-bg:#16391a;--done-fg:#b7e6b5;
    --danger:#ff9a9a;
  }
}
*{box-sizing:border-box}
body{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:18px;line-height:1.4;
  margin:0;padding:24px;background:var(--bg);color:var(--text)}
main{max-width:1000px;margin:0 auto}
h1{font-family:Georgia,"Times New Roman",serif;font-size:2.2rem;margin:0 0 16px;letter-spacing:.01em}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px}

.toolbar{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px}
input,select,button{font:inherit;color:var(--text);min-height:44px;border-radius:8px;border:1.5px solid var(--line);background:var(--surface);padding:6px 12px}
.toolbar input{flex:1 1 220px}
button{cursor:pointer;font-weight:600}
button:hover{border-color:var(--muted)}
button.primary{background:var(--accent);color:var(--accent-text);border-color:var(--accent)}
button.danger{color:var(--danger)}

.table-wrap{background:var(--surface);border:1px solid var(--line);border-radius:12px;overflow-x:auto}
table{border-collapse:collapse;width:100%}
th,td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line);vertical-align:middle}
tbody tr:last-child td{border-bottom:0}
th{font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);background:var(--bg)}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
td.qty{font-size:1.5rem;font-weight:700}
td.item{font-weight:600}
td.actions{white-space:nowrap}
td.actions button{min-height:40px;padding:4px 12px}

.status{display:inline-flex;align-items:center;gap:6px;padding:3px 12px;border-radius:999px;font-weight:600;font-size:.9rem}
.status::before{content:"";width:.6em;height:.6em;border-radius:50%;background:currentColor}
.status.pending{background:var(--pending-bg);color:var(--pending-fg)}
.status.pending::before{border-radius:0;transform:rotate(45deg)}
.status.complete{background:var(--done-bg);color:var(--done-fg)}

#none{padding:32px;text-align:center;color:var(--muted);font-size:1.1rem}
#msg{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--done-bg);color:var(--done-fg);
  border:1.5px solid currentColor;padding:12px 20px;border-radius:10px;font-weight:600;box-shadow:0 4px 16px rgb(0 0 0/.25)}
#confirm,#form{position:fixed;inset:0;margin:auto;height:fit-content;width:min(92vw,400px);
  background:var(--surface);color:var(--text);border:1px solid var(--line);border-radius:14px;padding:24px;box-shadow:0 12px 40px rgb(0 0 0/.35)}
#confirm::backdrop,#form::backdrop{background:rgb(0 0 0/.5)}
#confirm p{margin:0 0 20px;font-size:1.1rem}
#form label{display:block;font-weight:600;margin-bottom:12px}
#form input,#form select{display:block;width:100%;margin-top:4px}
.row{display:flex;gap:10px;justify-content:flex-end;margin-top:8px}
[hidden]{display:none!important}

@media (max-width:640px){
  body{padding:12px}
  th:first-child,td:first-child{display:none}
  td.actions{white-space:normal}
}
</style></head><body>
<main>
<h1>Orders</h1>
<div class="toolbar">
  <input id="q" type="search" placeholder="Search..." aria-label="Search orders">
  <select id="filter" aria-label="Filter by status"><option>All</option><option>Pending</option><option>Complete</option></select>
  <button id="add" class="primary">Add Order</button>
</div>

<div class="table-wrap">
<table>
<thead><tr><th>#</th><th>Customer Name</th><th>Item</th><th class="num">Qty</th><th>Status</th><th>Actions</th></tr></thead>
<tbody id="rows">
<tr><td>1</td><td>Customer 1</td><td class="item">Product A</td><td class="num qty">10</td><td><span class="status pending">Pending</span></td><td class="actions"><button>Edit</button> <button class="danger">Delete</button></td></tr>
<tr><td>2</td><td>Customer 2</td><td class="item">Product B</td><td class="num qty">25</td><td><span class="status complete">Complete</span></td><td class="actions"><button>Edit</button> <button class="danger">Delete</button></td></tr>
</tbody>
</table>
<p id="none" hidden>No results found.</p>
</div>

<div id="msg" role="status" hidden>Success!</div>

<dialog id="confirm">
  <p>Are you sure you want to delete this?</p>
  <div class="row"><button id="no" autofocus>No</button> <button id="yes" class="primary">Yes</button></div>
</dialog>

<dialog id="form">
  <form method="dialog" id="orderForm">
    <label>Customer Name<input name="customer" required></label>
    <label>Item<input name="item" required></label>
    <label>Qty<input name="qty" type="number" min="1" required></label>
    <label>Status<select name="status"><option>Pending</option><option>Complete</option></select></label>
    <div class="row"><button type="button" id="cancel">Cancel</button> <button class="primary">Save</button></div>
  </form>
</dialog>
</main>

<script>
const $ = id => document.getElementById(id);
const rows = $('rows'), q = $('q'), filter = $('filter'), none = $('none');
const confirmDlg = $('confirm'), formDlg = $('form'), form = $('orderForm');
let target = null, editing = null, timer;

function toast(text){
  const m = $('msg'); m.textContent = text; m.hidden = false;
  clearTimeout(timer); timer = setTimeout(() => m.hidden = true, 2500);
}
function apply(){
  const term = q.value.trim().toLowerCase(), st = filter.value;
  let shown = 0;
  for (const tr of rows.rows){
    const ok = tr.textContent.toLowerCase().includes(term) &&
      (st === 'All' || tr.querySelector('.status').textContent === st);
    tr.hidden = !ok; if (ok) shown++;
  }
  none.hidden = shown > 0;
}
function renumber(){ [...rows.rows].forEach((tr,i) => tr.cells[0].textContent = i + 1); }
function fill(tr, d){
  tr.cells[1].textContent = d.customer;
  tr.cells[2].textContent = d.item;
  tr.cells[3].textContent = d.qty;
  const s = tr.querySelector('.status');
  s.textContent = d.status; s.className = 'status ' + d.status.toLowerCase();
}

q.addEventListener('input', apply);
filter.addEventListener('change', apply);

$('add').onclick = () => { editing = null; form.reset(); formDlg.showModal(); };
$('cancel').onclick = () => formDlg.close();
form.addEventListener('submit', () => {
  const d = Object.fromEntries(new FormData(form));
  let tr = editing;
  if (!tr){
    tr = rows.rows[0].cloneNode(true);
    rows.append(tr); renumber();
  }
  fill(tr, d); apply(); toast('Success!');
});

rows.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  const tr = b.closest('tr');
  if (b.textContent === 'Delete'){ target = tr; confirmDlg.showModal(); }
  else {
    editing = tr; form.reset();
    form.customer.value = tr.cells[1].textContent;
    form.item.value = tr.cells[2].textContent;
    form.qty.value = tr.cells[3].textContent;
    form.status.value = tr.querySelector('.status').textContent;
    formDlg.showModal();
  }
});
$('no').onclick = () => { target = null; confirmDlg.close(); };
$('yes').onclick = () => {
  if (target){ target.remove(); renumber(); apply(); toast('Success!'); }
  target = null; confirmDlg.close();
};
</script>
</body></html>
```

**Design choices**
- **4 AM readability:** the page has a warm paper look with high contrast, and it switches to a dark theme automatically when the device is set to dark. Type is large, and quantity is the biggest thing in each row so bakers see it first.
- **Status:** the pills now use a diamond marker for Pending and a dot for Complete. Colour isn't the only signal.
- **Touch targets:** buttons and inputs are at least 40–44px tall, which suits a driver using a phone. On narrow screens the table scrolls sideways and the `#` column is hidden.

**Behaviour**
- **Filter:** "Status 1" and "Status 2" in the dropdown were placeholders. I changed them to Pending and Complete to match the data.
- **Search and filter:** search matches any text in the row and works together with the status filter. "No results found." appears when nothing matches.
- **Add and Edit:** both open a small form. Add appends a row and Edit updates the row in place.
- **Delete:** it asks "Are you sure you want to delete this?" first. The default focus is on **No**, so a stray tap won't delete an order.
- **Success message:** "Success!" shows for 2.5 seconds after a save or delete.
- **Persistence:** like the original, nothing is saved, so a refresh resets the list. To keep orders you'd need to add storage or a backend.

I didn't add delivery address or route fields. You didn't give me that data, and I didn't want to invent it. If you tell me what the driver needs, I can add a route column or sort order.
