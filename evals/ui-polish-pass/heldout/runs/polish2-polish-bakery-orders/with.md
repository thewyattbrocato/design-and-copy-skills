I couldn't save the file because the Write tool is disabled in this session. Here is the full finished page to paste into `orders.html`. I haven't run it in a browser or tested it with a screen reader.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222;font-size:18px;line-height:1.4}
h1{margin:0 0 16px}
.wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:10px 8px;text-align:left;overflow-wrap:anywhere}
th{background:#f6f6f6}
td.qty,th.qty{text-align:right;font-variant-numeric:tabular-nums;font-weight:600}
.status{padding:2px 10px;border-radius:10px;background:#e5e7eb;white-space:nowrap}
.status.pending{background:#fde9b8;color:#4a3200}
.status.complete{background:#d4ecd8;color:#123d1c}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px}
.toolbar input{flex:1 1 200px}
input,select,button{font:inherit;padding:8px 12px;min-height:44px;box-sizing:border-box}
input,select{border:1px solid #767676;border-radius:4px;background:#fff;color:inherit}
button{cursor:pointer}
:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
td button+button{margin-left:4px}
#none,#empty{padding:16px 0}
#msg{margin-top:16px;padding:10px 14px;background:#d4ecd8;color:#123d1c;border-radius:4px}
#confirm{position:fixed;left:50%;top:30%;transform:translateX(-50%);width:min(420px,90vw);box-sizing:border-box;padding:20px;background:#fff;border:2px solid #222;border-radius:6px;box-shadow:0 8px 30px rgba(0,0,0,.3)}
#confirm button{margin-top:12px}
[hidden]{display:none!important}
@media (max-width:480px){body{padding:12px}}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar">
<input id="q" type="search" aria-label="Search orders" placeholder="Search customer or item">
<select id="f" aria-label="Filter by status"><option value="">All</option><option>Pending</option><option>Complete</option></select>
<button id="add">Add Order</button></div>
<div class="wrap"><table>
<thead><tr><th scope="col">#</th><th scope="col">Customer Name</th><th scope="col">Item</th><th scope="col" class="qty">Qty</th><th scope="col">Status</th><th scope="col">Actions</th></tr></thead>
<tbody id="rows">
<tr><td>1</td><td>Customer 1</td><td>Product A</td><td class="qty">10</td><td><span class="status pending">Pending</span></td><td><button data-act="edit">Edit</button> <button data-act="del">Delete</button></td></tr>
<tr><td>2</td><td>Customer 2</td><td>Product B</td><td class="qty">25</td><td><span class="status complete">Complete</span></td><td><button data-act="edit">Edit</button> <button data-act="del">Delete</button></td></tr>
</tbody></table></div>
<p id="empty" hidden>No orders yet. Use Add Order to enter the first one.</p>
<p id="none" hidden>No results found.</p>
<div id="msg" role="status" hidden>Success!</div>
<div id="confirm" role="alertdialog" aria-modal="true" aria-labelledby="ctext" hidden><span id="ctext">Are you sure you want to delete this?</span><br><button id="yes">Delete order</button> <button id="no">Keep it</button></div>
<script>
const $=id=>document.getElementById(id),rows=$('rows'),msg=$('msg'),box=$('confirm');
let target=null,opener=null,timer;
// Give each row's buttons a name that says which order they act on
function label(){[...rows.rows].forEach(r=>{const n=r.cells[0].textContent,c=r.cells[1].textContent;
 r.querySelector('[data-act=edit]').setAttribute('aria-label',`Edit order ${n}, ${c}`);
 r.querySelector('[data-act=del]').setAttribute('aria-label',`Delete order ${n}, ${c}`);});}
function filter(){const q=$('q').value.trim().toLowerCase(),s=$('f').value;let shown=0;
 [...rows.rows].forEach(r=>{const ok=(!q||r.textContent.toLowerCase().includes(q))&&(!s||r.cells[4].textContent.trim()===s);r.hidden=!ok;if(ok)shown++;});
 const total=rows.rows.length;
 $('empty').hidden=total>0;$('none').hidden=!(total>0&&shown===0);
 $('none').textContent=shown||!total?'':`No results found${q?` for “${$('q').value.trim()}”`:''}${s?` with status ${s}`:''}.`;}
function say(t){msg.textContent=t;msg.hidden=false;clearTimeout(timer);timer=setTimeout(()=>msg.hidden=true,5000);}
function close(){box.hidden=true;target=null;if(opener&&opener.isConnected)opener.focus();else $('q').focus();}
msg.hidden=true;label();filter();
$('q').addEventListener('input',filter);$('f').addEventListener('change',filter);
rows.addEventListener('click',e=>{const b=e.target.closest('[data-act=del]');if(!b)return;
 target=b.closest('tr');opener=b;
 $('ctext').textContent=`Delete order ${target.cells[0].textContent} for ${target.cells[1].textContent}? This can’t be undone.`;
 box.hidden=false;$('no').focus();});
$('yes').onclick=()=>{const n=target.cells[0].textContent;target.remove();opener=null;filter();close();say(`Order ${n} deleted.`);};
$('no').onclick=close;
box.addEventListener('keydown',e=>{if(e.key==='Escape')close();
 if(e.key==='Tab'){const b=[$('yes'),$('no')],i=b.indexOf(document.activeElement);
  if(e.shiftKey&&i<=0){e.preventDefault();b[1].focus();}else if(!e.shiftKey&&i===1){e.preventDefault();b[0].focus();}}});
</script>
</body></html>
```

**What changed, with the layout and column order kept as they were:**
- **Readability at 4 a.m.:**
  - Body text is 18px.
  - Quantities are right-aligned, bold and in tabular figures, so bakers can scan them.
  - Pending is amber and Complete is green. Each still has its word, so color isn't the only cue.
  - Controls are at least 44px tall, which helps with flour on your fingers.
- **Search and filter:** both now work. The filter options are Pending and Complete instead of "Status 1/2". The "No results found" message now names what was searched or filtered. A separate empty state shows if every order is deleted.
- **Delete:** it asks first, and the buttons say "Delete order" and "Keep it". It names the order and says it can't be undone. Focus starts on the safe button, Esc cancels, and focus returns to where you were. A "deleted" message confirms it and fades after 5 seconds.
- **Access and small screens:**
  - Edit and Delete buttons name their order, for example "Delete order 2, Customer 2".
  - Focus rings are visible.
  - The table scrolls sideways on a phone instead of breaking the page.
  - Long customer names wrap.

**Needs your decision:**
- **Add Order and Edit:** they still do nothing, as in your original. Wiring them up means designing an order form, which is a new feature, so I left it.
- **Delivery address:** the driver's route needs one, but the page has no such field. I didn't invent it.
- **Delete is not saved:** it only removes the row from the page, so a reload brings it back.
