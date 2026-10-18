I couldn't save a file because the Write tool is disabled in this session. The full page is below. I haven't run it in a browser or tested it with a screen reader.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222;font-size:18px;line-height:1.4}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:10px 8px;text-align:left;overflow-wrap:anywhere}
th{background:#f6f6f6}
td.qty,th.qty{text-align:right;font-variant-numeric:tabular-nums;font-weight:600}
.status{padding:2px 10px;border-radius:10px;background:#e5e7eb;white-space:nowrap}
.status.pending{background:#fde9b8;color:#4a3300}
.status.complete{background:#d4edda;color:#14401f}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px}
.toolbar input{flex:1 1 200px;min-width:0}
input,select,button{font:inherit;padding:6px 12px;min-height:44px;box-sizing:border-box}
input,select{border:1px solid #767676;border-radius:4px;background:#fff;color:inherit}
button{cursor:pointer}
:focus-visible{outline:3px solid #1a56db;outline-offset:2px}
.wrap{overflow-x:auto}
td.actions{white-space:nowrap}
#none{margin:16px 0}
#msg{margin-top:16px;padding:10px 14px;background:#d4edda;color:#14401f;border-radius:4px}
#confirm{position:fixed;left:50%;top:30%;transform:translateX(-50%);width:min(90vw,380px);padding:20px;background:#fff;border:2px solid #222;border-radius:6px;box-shadow:0 8px 30px rgba(0,0,0,.3)}
#confirm p{margin:0 0 16px}
[hidden]{display:none!important}
@media (max-width:600px){body{padding:12px}}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar">
<input id="q" type="search" aria-label="Search orders by customer or item" placeholder="Search...">
<select id="f" aria-label="Filter by status"><option value="">All</option><option>Pending</option><option>Complete</option></select>
<button id="add" type="button">Add Order</button></div>
<div class="wrap">
<table>
<caption style="text-align:left;padding-bottom:6px"><span id="count" aria-live="polite"></span></caption>
<thead><tr><th>#</th><th>Customer Name</th><th>Item</th><th class="qty">Qty</th><th>Status</th><th>Actions</th></tr></thead>
<tbody id="rows">
<tr><td>1</td><td>Customer 1</td><td>Product A</td><td class="qty">10</td><td><span class="status pending">Pending</span></td><td class="actions"><button type="button" class="edit">Edit</button> <button type="button" class="del">Delete</button></td></tr>
<tr><td>2</td><td>Customer 2</td><td>Product B</td><td class="qty">25</td><td><span class="status complete">Complete</span></td><td class="actions"><button type="button" class="edit">Edit</button> <button type="button" class="del">Delete</button></td></tr>
</tbody></table></div>
<p id="none" hidden role="status">No results found.</p>
<div id="msg" hidden role="status">Success!</div>
<div id="confirm" role="alertdialog" aria-modal="true" aria-labelledby="ctext" hidden><p id="ctext">Are you sure you want to delete this?</p><button type="button" id="yes">Delete order</button> <button type="button" id="no">Keep it</button></div>
<script>
const $=id=>document.getElementById(id),rows=$('rows'),none=$('none'),msg=$('msg'),box=$('confirm');
let target=null,opener=null,timer;
// name each button after its order so screen readers can tell them apart
function label(){[...rows.rows].forEach(r=>{const c=r.cells,w=c[1].textContent+', '+c[2].textContent;
r.querySelector('.edit').setAttribute('aria-label','Edit order '+c[0].textContent+': '+w);
r.querySelector('.del').setAttribute('aria-label','Delete order '+c[0].textContent+': '+w)})}
function filter(){const q=$('q').value.trim().toLowerCase(),s=$('f').value;let n=0;
[...rows.rows].forEach(r=>{const ok=(!s||r.cells[4].textContent.trim()===s)&&(!q||r.textContent.toLowerCase().includes(q));r.hidden=!ok;if(ok)n++});
none.hidden=n>0;
none.textContent=rows.rows.length?'No results found'+(q?' for “'+$('q').value.trim()+'”':'')+(s?' with status '+s:'')+'. Clear the search or filter to see all orders.':'No orders yet. Use Add Order to enter the first one.';
$('count').textContent=n+(n===1?' order shown':' orders shown')}
function toast(t){msg.textContent=t;msg.hidden=false;clearTimeout(timer);timer=setTimeout(()=>msg.hidden=true,5000)}
$('q').addEventListener('input',filter);$('f').addEventListener('change',filter);
rows.addEventListener('click',e=>{const b=e.target.closest('.del');if(!b)return;
target=b.closest('tr');opener=b;const c=target.cells;
$('ctext').textContent='Delete order '+c[0].textContent+' ('+c[1].textContent+', '+c[3].textContent+' × '+c[2].textContent+')? This can’t be undone.';
box.hidden=false;$('no').focus()});
function close(){box.hidden=true;target=null}
$('no').onclick=()=>{const o=opener;close();o.focus()};
$('yes').onclick=()=>{const r=target,next=[...rows.rows].find(x=>!x.hidden&&x!==r),num=r.cells[0].textContent;
r.remove();close();filter();toast('Order '+num+' deleted.');
(next?next.querySelector('.del'):$('add')).focus()};
box.addEventListener('keydown',e=>{if(e.key==='Escape')$('no').click();
if(e.key==='Tab'){const f=[$('yes'),$('no')],i=f.indexOf(document.activeElement);e.preventDefault();f[(i+(e.shiftKey?-1:1)+2)%2].focus()}});
label();filter();
</script>
</body></html>
```

I kept the layout, columns, colors and wording. The changes:

- **Filter and search:** the page had hidden "No results", "Success!" and "Are you sure" elements, but nothing used them. They now work. Search matches any text in a row, and the status filter offers All, Pending and Complete instead of "Status 1" and "Status 2". The "No results" message says what was searched and how to clear it. It also has a separate message for when no orders are left.
- **Delete:** the dialog names the order and its quantity, says it can't be undone, and uses the buttons "Delete order" and "Keep it". Focus starts on "Keep it", so a stray Enter at 4am doesn't delete anything. Escape cancels. Focus stays inside the dialog while it's open. Afterward focus moves to the next Delete button, and "Order N deleted." appears for 5 seconds.
- **Reading at 4am and on the route:**
  - Text is 18px.
  - Quantities are bold and right-aligned.
  - Pending and Complete are tinted as well as labeled.
  - The table scrolls sideways on narrow screens, and long names wrap.
- **Access:**
  - Search and filter have labels.
  - Each Edit and Delete button names its order.
  - There is a visible focus ring.
  - Buttons are at least 44px tall.
  - The count of orders shown is announced when it changes.

**Still open:**
- **Add Order and Edit:** these are still unwired. The original had no form for them, so I didn't invent one. Say what fields they need and I'll build it.
- **Sample rows:** they still read "Customer 1 / Product A".
