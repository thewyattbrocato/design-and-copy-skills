I can't write files in this session, so the finished page is below. Save it over your `orders.html`.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222}
.wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:8px;text-align:left;overflow-wrap:anywhere}
td.qty{font-size:1.25rem;font-weight:700;font-variant-numeric:tabular-nums}
.status{padding:2px 8px;border-radius:10px;background:#e5e7eb;white-space:nowrap}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px}
input,select,button{font:inherit}
input,select{padding:6px 8px;border:1px solid #767676;border-radius:3px;min-width:0}
button{padding:6px 12px;min-height:36px}
:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
#msg,#confirm,#none{margin-top:16px;padding:12px;border-radius:4px}
#msg{background:#e5e7eb}
#confirm{border:2px solid #222}
#none{border:1px dashed #767676}
[hidden]{display:none!important}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar">
<label class="sr" for="q">Search orders</label><input id="q" type="search" placeholder="Search...">
<label class="sr" for="st">Filter by status</label>
<select id="st"><option value="">All</option><option>Pending</option><option>Complete</option></select>
<button id="add">Add Order</button></div>
<div class="wrap"><table>
<thead><tr><th scope="col">#</th><th scope="col">Customer Name</th><th scope="col">Item</th><th scope="col">Qty</th><th scope="col">Status</th><th scope="col">Actions</th></tr></thead>
<tbody id="rows">
<tr><td>1</td><td>Customer 1</td><td>Product A</td><td class="qty">10</td><td><span class="status">Pending</span></td><td><button aria-label="Edit order 1, Customer 1">Edit</button> <button class="del" aria-label="Delete order 1, Customer 1">Delete</button></td></tr>
<tr><td>2</td><td>Customer 2</td><td>Product B</td><td class="qty">25</td><td><span class="status">Complete</span></td><td><button aria-label="Edit order 2, Customer 2">Edit</button> <button class="del" aria-label="Delete order 2, Customer 2">Delete</button></td></tr>
</tbody></table></div>
<p id="none" hidden></p>
<div id="msg" role="status" hidden></div>
<div id="confirm" role="alertdialog" aria-labelledby="ctext" hidden><span id="ctext"></span><br><br><button id="yes">Delete order</button> <button id="no">Keep it</button></div>
<script>
const $=id=>document.getElementById(id),rows=[...$('rows').rows];
let target=null,opener=null;
function filter(){
  const q=$('q').value.trim().toLowerCase(),s=$('st').value;let shown=0;
  rows.forEach(r=>{if(!r.isConnected)return;
    const ok=r.textContent.toLowerCase().includes(q)&&(!s||r.querySelector('.status').textContent===s);
    r.hidden=!ok;if(ok)shown++;});
  const none=$('none'),left=rows.some(r=>r.isConnected);
  none.hidden=shown>0;
  if(!left)none.textContent='No orders yet. Use Add Order to enter the first one.';
  else if(!shown)none.textContent='No results found'+(q?' for "'+$('q').value.trim()+'"':'')+(s?' with status '+s:'')+'. Clear the search or choose All to see every order.';
}
$('q').addEventListener('input',filter);$('st').addEventListener('change',filter);
$('rows').addEventListener('click',e=>{
  const b=e.target.closest('.del');if(!b)return;
  target=b.closest('tr');opener=b;
  const c=target.cells;
  $('ctext').textContent='Delete order '+c[0].textContent+' ('+c[2].textContent+' ×'+c[3].textContent+' for '+c[1].textContent+')? This can’t be undone.';
  $('msg').hidden=true;$('confirm').hidden=false;$('no').focus();
});
function closeConfirm(){$('confirm').hidden=true;}
$('no').onclick=()=>{closeConfirm();opener&&opener.focus();target=null;};
$('yes').onclick=()=>{
  const n=target.cells[0].textContent;
  const next=rows.find(r=>r!==target&&r.isConnected&&!r.hidden);
  target.remove();target=null;closeConfirm();filter();
  $('msg').textContent='Order '+n+' deleted.';$('msg').hidden=false;
  (next?next.querySelector('button'):$('q')).focus();
};
$('confirm').addEventListener('keydown',e=>{if(e.key==='Escape')$('no').click();});
</script>
</body></html>
```

**What I changed:**
- **Search and status filter:** they now work. The status options are Pending and Complete instead of "Status 1/2". If nothing matches, the page shows "No results found" with your search term and how to clear it. After the last order is deleted, it shows an empty-list message instead.
- **Delete:** it uses your existing confirm box. The text names the order and says it can't be undone. The buttons read "Delete order" and "Keep it", and focus starts on "Keep it". Esc cancels. After a delete, your success box says "Order N deleted." and focus moves to the next row, so keyboard users don't lose their place.
- **Access:**
  - Search and filter have labels.
  - Each Edit and Delete button names its order.
  - There is a visible focus ring.
  - Table headers are marked as column headers.
- **Reading at a glance:** quantity is larger and bold, since it's the number bakers need at 4 a.m. The table scrolls sideways on a narrow screen and long names wrap. A viewport tag is added.

Your palette, layout and wording are unchanged.

**Left alone:**
- **Edit and Add Order:** they still do nothing, as before. There's no form or backend to connect them to.
- **Dark theme:** I didn't add one. If bakers read this in a dark kitchen, that is a design decision for you.

I haven't run this in a browser or tested it with a screen reader.
