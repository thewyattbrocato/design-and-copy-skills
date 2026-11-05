I couldn't save the file because the Write tool is disabled in this session, so the full page is below. I haven't opened it in a browser or tried it with a screen reader.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222;font-size:1.125rem;line-height:1.4}
h1{margin:0 0 16px}
.wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:10px 8px;text-align:left;overflow-wrap:anywhere}
th{background:#f6f6f6}
td.qty,th.qty{text-align:right;font-variant-numeric:tabular-nums;font-weight:600}
.status{padding:2px 10px;border-radius:10px;background:#e5e7eb;white-space:nowrap}
.status.pending{background:#fde9b8}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
input,select,button{font:inherit;padding:8px 12px;min-height:44px;box-sizing:border-box}
input,select{border:1px solid #767676;border-radius:4px;background:#fff;color:inherit}
button{cursor:pointer}
:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
.actions{white-space:nowrap}
#none{margin:16px 0}
#msg{position:fixed;left:24px;bottom:24px;background:#14532d;color:#fff;padding:12px 16px;border-radius:6px}
#confirm{position:fixed;inset:auto 24px 24px 24px;max-width:420px;background:#fff;border:2px solid #222;border-radius:6px;padding:16px}
#confirm button{margin-top:12px}
[hidden]{display:none!important}
@media (max-width:480px){body{padding:12px}}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar">
  <input id="q" type="search" aria-label="Search orders" placeholder="Search café or item">
  <select id="f" aria-label="Filter by status"><option value="">All</option><option>Pending</option><option>Complete</option></select>
  <button type="button">Add Order</button>
</div>
<div class="wrap">
<table>
<thead><tr><th scope="col">#</th><th scope="col">Café</th><th scope="col">Item</th><th scope="col" class="qty">Qty</th><th scope="col">Status</th><th scope="col">Actions</th></tr></thead>
<tbody id="rows">
<tr><td>1</td><td>Customer 1</td><td>Product A</td><td class="qty">10</td><td><span class="status pending">Pending</span></td><td class="actions"><button type="button" data-edit>Edit</button> <button type="button" data-del>Delete</button></td></tr>
<tr><td>2</td><td>Customer 2</td><td>Product B</td><td class="qty">25</td><td><span class="status">Complete</span></td><td class="actions"><button type="button" data-edit>Edit</button> <button type="button" data-del>Delete</button></td></tr>
</tbody>
</table>
</div>
<p id="none" role="status" hidden>No orders match your search. <button type="button" id="clear">Clear search</button></p>
<div id="msg" role="status" hidden>Order deleted.</div>
<div id="confirm" role="alertdialog" aria-modal="true" aria-labelledby="ctext" hidden>
  <span id="ctext">Delete this order? This can't be undone.</span><br>
  <button type="button" id="yes">Delete order</button> <button type="button" id="no">Keep order</button>
</div>
<script>
const $=s=>document.querySelector(s), rows=()=>[...document.querySelectorAll('#rows tr')];
function name(){rows().forEach(r=>{const c=r.cells,l=`order ${c[0].textContent}, ${c[1].textContent}`;
  r.querySelector('[data-edit]').setAttribute('aria-label','Edit '+l);
  r.querySelector('[data-del]').setAttribute('aria-label','Delete '+l);});}
name();
function filter(){
  const q=$('#q').value.trim().toLowerCase(), s=$('#f').value; let n=0;
  rows().forEach(r=>{const ok=(!q||r.textContent.toLowerCase().includes(q))&&(!s||r.querySelector('.status').textContent===s);
    r.hidden=!ok; if(ok)n++;});
  $('#none').hidden=n>0;
}
$('#q').oninput=$('#f').onchange=filter;
$('#clear').onclick=()=>{$('#q').value='';$('#f').value='';filter();$('#q').focus();};
let target=null,opener=null;
$('#rows').onclick=e=>{const b=e.target.closest('[data-del]'); if(!b)return;
  target=b.closest('tr');opener=b;$('#confirm').hidden=false;$('#no').focus();};
$('#no').onclick=()=>{$('#confirm').hidden=true;opener&&opener.focus();};
$('#yes').onclick=()=>{
  const all=rows().filter(r=>!r.hidden), i=all.indexOf(target), next=all[i+1]||all[i-1];
  target.remove();$('#confirm').hidden=true;name();filter();
  const m=$('#msg');m.hidden=false;setTimeout(()=>m.hidden=true,4000);
  (next?next.querySelector('[data-del]'):$('#q')).focus();
};
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!$('#confirm').hidden)$('#no').click();});
</script>
</body></html>
```

**What changed**
- **Look:** I kept the layout, colors and field order. The text is a bit larger, and the controls are at least 44px tall. Quantity is right-aligned in bold so the numbers are easy to scan at 4am. Pending now has a warm tint as well as its label.
- **Wording:** "Customer Name" is now "Café", and the placeholder "Status 1/2" options are now Pending and Complete.
- **Buttons:**
  - Each button names its order, for example "Delete order 1, Customer 1", instead of repeating "Edit" and "Delete".
  - Keyboard focus is clearly visible.
- **Search and filter:** They now filter the rows, and "No results" shows a Clear search button.
- **Delete:**
  - It still asks first, with buttons labeled "Delete order" and "Keep order", and Esc cancels.
  - After deleting, a short confirmation appears and focus moves to a neighbouring row.
- **Phones:** The viewport meta tag was missing, so I added it. The table scrolls sideways on narrow screens, and long café names wrap.

**What's left**
- **Add Order and Edit:** I left them doing nothing, as in your original.
- **Rows:** They are still your sample rows, and I didn't invent bakery data.
- **Route view:** The driver view needs delivery addresses or stops, and you haven't given me any.
