Here is the finished page. It is still one file with no dependencies, and it keeps the original layout, colors, and control set. The rows now come from a small in-page list, so Add, Edit, and Delete can update the table.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222}
h1{margin:0 0 4px}
.count{margin:0 0 16px;color:#555}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
input,select,button{font:inherit;padding:6px 10px;border:1px solid #999;border-radius:4px;background:#fff;color:#222}
button{cursor:pointer}
button:hover{background:#f3f4f6}
:focus-visible{outline:3px solid #2563eb;outline-offset:2px}
.primary{background:#1d4ed8;border-color:#1d4ed8;color:#fff}
.primary:hover{background:#1e40af}
.danger{color:#b91c1c}
.scroll{overflow-x:auto}
table{border-collapse:collapse;width:100%;min-width:560px}
th,td{border:1px solid #ddd;padding:8px;text-align:left;vertical-align:middle;overflow-wrap:anywhere}
th{background:#f7f7f7}
td.num{text-align:right;font-variant-numeric:tabular-nums}
.status{display:inline-block;padding:2px 8px;border-radius:10px;background:#e5e7eb;white-space:nowrap}
.status[data-s=Pending]{background:#fde68a}
.status[data-s=Baking]{background:#fdba74}
.status[data-s=Ready]{background:#bbf7d0}
dialog{border:1px solid #bbb;border-radius:8px;padding:20px;width:min(420px,calc(100% - 32px))}
dialog::backdrop{background:rgb(0 0 0 / .35)}
dialog h2{margin:0 0 12px}
.field{display:grid;gap:4px;margin-bottom:12px}
.field input,.field select{width:100%;box-sizing:border-box}
.error{color:#b91c1c;font-size:.9em}
[aria-invalid=true]{border-color:#b91c1c}
.actions{display:flex;justify-content:flex-end;gap:8px;margin-top:16px}
.toast{position:fixed;left:16px;bottom:16px;padding:10px 14px;border-radius:6px;background:#166534;color:#fff}
.toast:empty{display:none}
</style></head><body>
<h1>Orders</h1>
<p class="count" id="count" aria-live="polite"></p>
<div class="toolbar">
<input id="search" type="search" placeholder="Search customer or item" aria-label="Search orders">
<select id="filter" aria-label="Filter by status"><option value="">All statuses</option><option>Pending</option><option>Baking</option><option>Ready</option><option>Delivered</option></select>
<button id="add" class="primary" type="button">Add Order</button>
</div>
<div class="scroll"><table aria-label="Orders">
<thead><tr><th scope="col">#</th><th scope="col">Customer Name</th><th scope="col">Item</th><th scope="col">Qty</th><th scope="col">Status</th><th scope="col">Actions</th></tr></thead>
<tbody id="rows"></tbody>
</table></div>
<p id="empty" hidden>No orders yet. Use Add Order to enter the first one.</p>
<p id="none" hidden><span id="none-text"></span> <button id="clear" type="button">Clear search and filter</button></p>
<div id="msg" class="toast" role="status"></div>

<dialog id="editor" aria-labelledby="editor-title">
<form id="form" novalidate>
<h2 id="editor-title">Add order</h2>
<div class="field"><label for="f-customer">Customer</label><input id="f-customer" autocomplete="off" aria-describedby="e-customer"><span class="error" id="e-customer" hidden></span></div>
<div class="field"><label for="f-item">Item</label><select id="f-item"><option>Sourdough loaf</option><option>Rye loaf</option><option>Baguette</option><option>Croissant</option><option>Almond croissant</option><option>Cinnamon roll</option><option>Muffin</option></select></div>
<div class="field"><label for="f-qty">Qty</label><input id="f-qty" type="number" min="1" step="1" inputmode="numeric" aria-describedby="e-qty"><span class="error" id="e-qty" hidden></span></div>
<div class="field"><label for="f-status">Status</label><select id="f-status"><option>Pending</option><option>Baking</option><option>Ready</option><option>Delivered</option></select></div>
<div class="actions"><button type="button" id="cancel">Cancel</button><button type="submit" class="primary">Save order</button></div>
</form>
</dialog>

<dialog id="confirm" aria-labelledby="confirm-title">
<h2 id="confirm-title">Delete this order?</h2>
<p id="confirm-text"></p>
<div class="actions"><button type="button" id="keep">Keep it</button><button type="button" id="remove" class="danger">Delete order</button></div>
</dialog>

<script>
const PRODUCTS=['Sourdough loaf','Rye loaf','Baguette','Croissant','Almond croissant','Cinnamon roll','Muffin'];
let orders=[
{id:1,customer:'Café Lumière',item:'Sourdough loaf',qty:12,status:'Baking'},
{id:2,customer:'Bluebird Coffee',item:'Croissant',qty:48,status:'Pending'},
{id:3,customer:'Harbor Grind',item:'Baguette',qty:20,status:'Ready'},
{id:4,customer:'Marigold Café',item:'Cinnamon roll',qty:24,status:'Delivered'},
{id:5,customer:'Station Espresso',item:'Rye loaf',qty:6,status:'Pending'},
{id:6,customer:'Oak & Milk',item:'Almond croissant',qty:18,status:'Pending'}
];

const $=id=>document.getElementById(id);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let editingId=null, pendingDeleteId=null, returnFocus=null, toastTimer;

function toast(text){
  $('msg').textContent=text;
  clearTimeout(toastTimer);
  toastTimer=setTimeout(()=>$('msg').textContent='',4000);
}
function restoreFocus(){
  (returnFocus&&returnFocus.isConnected?returnFocus:$('add')).focus();
}

function render(){
  const q=$('search').value.trim().toLowerCase(), st=$('filter').value;
  const shown=orders.filter(o=>(!st||o.status===st)&&(!q||`${o.id} ${o.customer} ${o.item}`.toLowerCase().includes(q)));
  $('rows').innerHTML=shown.map(o=>{
    const n=esc(o.customer);
    return `<tr><td>${o.id}</td><td>${n}</td><td>${esc(o.item)}</td><td class="num">${o.qty}</td><td><span class="status" data-s="${o.status}">${o.status}</span></td><td><button type="button" data-act="edit" data-id="${o.id}" aria-label="Edit order ${o.id} for ${n}">Edit</button> <button type="button" class="danger" data-act="delete" data-id="${o.id}" aria-label="Delete order ${o.id} for ${n}">Delete</button></td></tr>`;
  }).join('');
  const toBake=orders.filter(o=>o.status==='Pending'||o.status==='Baking').reduce((s,o)=>s+o.qty,0);
  $('count').textContent=`Showing ${shown.length} of ${orders.length} orders · ${toBake} to bake`;
  const none=orders.length===0;
  document.querySelector('table').hidden=none;
  $('empty').hidden=!none;
  $('none').hidden=none||shown.length>0;
  $('none-text').textContent=`No orders match${q?` “${$('search').value.trim()}”`:''}${st?` with status ${st}`:''}.`;
}

function setError(field,msg){
  $('e-'+field).textContent=msg;
  $('e-'+field).hidden=!msg;
  $('f-'+field).setAttribute('aria-invalid',msg?'true':'false');
}

function openEditor(id=null,trigger=$('add')){
  const o=id?orders.find(x=>x.id===id):null;
  editingId=o?o.id:null;
  returnFocus=trigger;
  $('editor-title').textContent=o?`Edit order ${o.id}`:'Add order';
  $('f-customer').value=o?o.customer:'';
  $('f-item').value=o?o.item:PRODUCTS[0];
  $('f-qty').value=o?o.qty:'';
  $('f-status').value=o?o.status:'Pending';
  setError('customer','');
  setError('qty','');
  $('editor').showModal();
}

function openConfirm(id,trigger){
  const o=orders.find(x=>x.id===id);
  pendingDeleteId=id;
  returnFocus=trigger;
  $('confirm-text').textContent=`Order ${o.id} for ${o.customer} (${o.qty} × ${o.item}) will be removed from the list. This can't be undone.`;
  $('confirm').showModal();
}

$('add').onclick=()=>openEditor(null,$('add'));
$('cancel').onclick=()=>$('editor').close();
$('keep').onclick=()=>{ $('confirm').close(); restoreFocus(); };

$('form').addEventListener('submit',e=>{
  e.preventDefault();
  const customer=$('f-customer').value.trim();
  const qty=Number($('f-qty').value);
  setError('customer',customer?'':'Enter the café or customer name.');
  setError('qty',Number.isInteger(qty)&&qty>=1?'':'Enter a whole number, 1 or more.');
  const bad=$('form').querySelector('[aria-invalid="true"]');
  if(bad){ bad.focus(); return; }
  const data={customer,item:$('f-item').value,qty,status:$('f-status').value};
  let text;
  if(editingId){
    Object.assign(orders.find(o=>o.id===editingId),data);
    text=`Order ${editingId} saved.`;
  }else{
    const id=Math.max(0,...orders.map(o=>o.id))+1;
    orders.push({id,...data});
    text=`Order ${id} added.`;
  }
  $('editor').close();
  render();
  toast(text);
  restoreFocus();
});

$('remove').onclick=()=>{
  orders=orders.filter(o=>o.id!==pendingDeleteId);
  $('confirm').close();
  render();
  toast(`Order ${pendingDeleteId} deleted.`);
  restoreFocus();
};

$('rows').addEventListener('click',e=>{
  const b=e.target.closest('button[data-act]');
  if(!b) return;
  const id=Number(b.dataset.id);
  if(b.dataset.act==='edit') openEditor(id,b);
  else openConfirm(id,b);
});

$('search').addEventListener('input',render);
$('filter').addEventListener('change',render);
$('clear').onclick=()=>{ $('search').value=''; $('filter').value=''; render(); $('search').focus(); };

render();
</script>
</body></html>
```

**What changed:** placeholder data is now bakery orders and the status set is Pending, Baking, Ready, Delivered (replacing "Complete", which I changed so the driver's view has a clear "done" state). Search and status filter work, with a count of units still to bake for the 4am read. Add and Edit share a dialog with inline validation that keeps what was typed. Delete asks for confirmation with "Keep it" focused by default. Save and delete show a short confirmation, and an empty list and a no-match state each have a next action.

**Not done:** there is no backend, so orders reset when the page reloads. Connecting it to real storage is the next step. I also haven't opened it in a browser or tested it with a screen reader, so the keyboard, focus, and 320px layout are checked by reading the code only. The customer names are sample data to replace.
