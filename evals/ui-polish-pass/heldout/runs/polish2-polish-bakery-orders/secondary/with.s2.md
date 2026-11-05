The orders page is finished below. I returned the whole file because most of it changed. Search, the status filter, delete with confirmation, the success message and the empty and no-results states now work. Add and Edit have no handlers yet because the page has no backend, so they stay as buttons only.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222;line-height:1.4}
h1{margin:0 0 16px}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px}
.toolbar input,.toolbar select{padding:8px;font:inherit;border:1px solid #767676;border-radius:4px;min-height:40px}
.table-wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%}
th,td{border:1px solid #ddd;padding:8px;text-align:left;vertical-align:top;overflow-wrap:anywhere}
th{background:#f5f5f5}
td.qty{text-align:right;font-variant-numeric:tabular-nums}
.status{padding:2px 8px;border-radius:10px;background:#e5e7eb;white-space:nowrap}
.actions{white-space:nowrap}
button{padding:8px 12px;font:inherit;min-height:40px;border:1px solid #767676;background:#fff;border-radius:4px;cursor:pointer}
button:hover{background:#f3f4f6}
button.danger{border-color:#b42318;color:#b42318}
button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
.state{margin:16px 0;padding:16px;border:1px solid #ddd;border-radius:6px}
.state p{margin:0 0 12px}
#msg{margin:16px 0;padding:12px;border-radius:6px;background:#ecfdf3;border:1px solid #027a48;color:#054f31}
#confirm{margin:16px 0;padding:16px;border:2px solid #b42318;border-radius:6px;background:#fff}
#confirm p{margin:0 0 12px}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
[hidden]{display:none!important}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style></head><body>
<main>
<h1>Orders</h1>
<div class="toolbar" role="search">
  <label class="sr-only" for="q">Search orders</label>
  <input id="q" type="search" placeholder="Search customer, item or #">
  <label class="sr-only" for="status">Filter by status</label>
  <select id="status"><option>All</option><option>Pending</option><option>Complete</option></select>
  <button type="button">Add Order</button>
</div>
<div class="table-wrap">
<table>
<caption class="sr-only">Orders to bake and deliver</caption>
<thead><tr><th scope="col">#</th><th scope="col">Customer Name</th><th scope="col">Item</th><th scope="col">Qty</th><th scope="col">Status</th><th scope="col">Actions</th></tr></thead>
<tbody id="rows">
<tr data-status="Pending"><td>1</td><td>Customer 1</td><td>Product A</td><td class="qty">10</td><td><span class="status">Pending</span></td><td class="actions"><button type="button" aria-label="Edit order 1">Edit</button> <button type="button" class="danger" data-delete aria-label="Delete order 1">Delete</button></td></tr>
<tr data-status="Complete"><td>2</td><td>Customer 2</td><td>Product B</td><td class="qty">25</td><td><span class="status">Complete</span></td><td class="actions"><button type="button" aria-label="Edit order 2">Edit</button> <button type="button" class="danger" data-delete aria-label="Delete order 2">Delete</button></td></tr>
</tbody>
</table>
</div>
<div id="empty" class="state" hidden><p>No orders yet.</p><button type="button">Add Order</button></div>
<div id="none" class="state" hidden><p>No orders match your search or filter.</p><button type="button" id="clear">Clear search and filter</button></div>
<div id="msg" role="status" hidden>Order deleted.</div>
<div id="confirm" role="alertdialog" aria-labelledby="confirm-text" hidden>
  <p id="confirm-text">Delete this order? This can't be undone.</p>
  <button type="button" class="danger" id="yes">Delete order</button> <button type="button" id="no">Keep order</button>
</div>
</main>
<script>
const tbody=document.getElementById('rows'),q=document.getElementById('q'),st=document.getElementById('status');
const empty=document.getElementById('empty'),none=document.getElementById('none'),msg=document.getElementById('msg');
const dlg=document.getElementById('confirm'),yes=document.getElementById('yes'),no=document.getElementById('no');
let pendingRow=null,opener=null,msgTimer=null;

function applyFilters(){
  const term=q.value.trim().toLowerCase(),s=st.value,all=[...tbody.rows];
  let shown=0;
  all.forEach(r=>{
    const text=[...r.cells].slice(0,4).map(c=>c.textContent).join(' ').toLowerCase();
    const match=(!term||text.includes(term))&&(s==='All'||r.dataset.status===s);
    r.hidden=!match; if(match) shown++;
  });
  empty.hidden=all.length>0;
  none.hidden=all.length===0||shown>0;
}
q.addEventListener('input',applyFilters);
st.addEventListener('change',applyFilters);
document.getElementById('clear').addEventListener('click',()=>{q.value='';st.value='All';applyFilters();q.focus();});

tbody.addEventListener('click',e=>{
  const b=e.target.closest('button[data-delete]'); if(!b) return;
  pendingRow=b.closest('tr'); opener=b;
  const n=pendingRow.cells[0].textContent, c=pendingRow.cells[1].textContent;
  document.getElementById('confirm-text').textContent=`Delete order ${n} for ${c}? This can't be undone.`;
  dlg.hidden=false; yes.focus();
});
function closeConfirm(focusTarget){
  dlg.hidden=true; pendingRow=null;
  if(focusTarget&&focusTarget.isConnected) focusTarget.focus();
  else if(opener&&opener.isConnected) opener.focus();
  else document.querySelector('h1').focus();
  opener=null;
}
no.addEventListener('click',()=>closeConfirm());
yes.addEventListener('click',()=>{
  const row=pendingRow; if(!row) return;
  const next=row.nextElementSibling||row.previousElementSibling;
  row.remove();
  applyFilters();
  closeConfirm(next?next.querySelector('[data-delete]'):null);
  msg.hidden=false; clearTimeout(msgTimer);
  msgTimer=setTimeout(()=>{msg.hidden=true;},6000);
});
dlg.addEventListener('keydown',e=>{
  if(e.key==='Escape'){e.preventDefault();closeConfirm();}
  if(e.key==='Tab'){
    const f=[yes,no];
    if(e.shiftKey&&document.activeElement===f[0]){e.preventDefault();f[1].focus();}
    else if(!e.shiftKey&&document.activeElement===f[1]){e.preventDefault();f[0].focus();}
  }
});
</script>
</body></html>
```

What changed and why:
- **Filter options:** "Status 1" and "Status 2" are now Pending and Complete, the two statuses in the data. If the bakery has more stages, such as Baking or Out for delivery, tell me and I'll add them.
- **Delete confirmation:** "Are you sure?" and Yes/No are now "Delete order" and "Keep order", with the order number and customer named. Focus moves into the dialog, Tab stays inside it, Escape cancels, and focus returns to the row afterward.
- **Success message:** "Success!" is now "Order deleted.", announced to screen readers and cleared after six seconds.
- **Empty and no-results states:** an empty list says "No orders yet." with an Add Order button. A search or filter with no matches says so and offers a button to clear them.
- **Narrow screens:** the table scrolls sideways instead of breaking the layout, and long names wrap.
- **Reading at 4am:** quantities are right-aligned, and the buttons have visible focus rings and larger hit areas.
- **Row buttons:** Edit and Delete now name their order, so a screen reader doesn't just hear "Delete" three times.

Not checked: I didn't run this in a browser or with a screen reader, so the keyboard and screen-reader behavior is from reading the code only. Add Order and Edit still do nothing because there's no backend. Those need a form and a save step before they can be finished.
