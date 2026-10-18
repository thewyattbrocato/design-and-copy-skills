```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:8px;text-align:left;vertical-align:top;overflow-wrap:anywhere}
th{white-space:nowrap}td:last-child{white-space:nowrap}
.scroll{overflow-x:auto}
.sub{display:block;font-size:13px;color:#555}
.status{padding:2px 8px;border-radius:10px;background:#e5e7eb;white-space:nowrap}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
button,input,select{font:inherit;padding:6px 12px}
input,select{border:1px solid #888;border-radius:4px}
button{cursor:pointer;border:1px solid #888;border-radius:4px;background:#fff}
button.primary{background:#222;color:#fff;border-color:#222}
:focus-visible{outline:3px solid #2563eb;outline-offset:2px}
#msg{margin:16px 0;padding:8px 12px;border-radius:4px;background:#e5e7eb}
#msg:focus{outline-offset:0}
#none,#empty{margin:16px 0}
dialog{border:1px solid #888;border-radius:6px;max-width:440px;width:calc(100% - 32px)}
dialog form{display:grid;gap:12px}
.field{display:grid;gap:4px;font-weight:600}
.field input,.field select{font-weight:400}
.err{color:#b91c1c;font-weight:400;font-size:14px}
.actions{display:flex;gap:8px;justify-content:flex-end}
</style></head>
<body>
<h1>Orders</h1>
<div class="toolbar">
<input id="q" type="search" placeholder="Search café or item" aria-label="Search orders">
<select id="filter" aria-label="Filter by status"><option value="">All statuses</option><option>Pending</option><option>Baking</option><option>Ready</option><option>Delivered</option></select>
<button class="primary" id="add">Add Order</button>
</div>
<div class="scroll">
<table id="orders">
<thead><tr><th>#</th><th>Café</th><th>Item</th><th>Qty</th><th>Status</th><th>Actions</th></tr></thead>
<tbody></tbody>
</table>
</div>
<p id="empty" hidden>No orders yet. <button id="add-first">Add the first order</button></p>
<p id="none" hidden>No orders match. <button id="clear">Show all orders</button></p>
<div id="msg" role="status" tabindex="-1" hidden></div>

<dialog id="editor" aria-labelledby="editor-title">
<form id="editor-form" novalidate>
<h2 id="editor-title">Add order</h2>
<div class="field"><label for="f-customer">Café</label><input id="f-customer" name="customer" autocomplete="off" aria-describedby="e-customer"><span class="err" id="e-customer" hidden></span></div>
<div class="field"><label for="f-address">Delivery address</label><input id="f-address" name="address" autocomplete="off" aria-describedby="e-address"><span class="err" id="e-address" hidden></span></div>
<div class="field"><label for="f-item">Item</label><input id="f-item" name="item" list="products" autocomplete="off" aria-describedby="e-item"><span class="err" id="e-item" hidden></span></div>
<div class="field"><label for="f-qty">Quantity</label><input id="f-qty" name="qty" type="number" min="1" step="1" aria-describedby="e-qty"><span class="err" id="e-qty" hidden></span></div>
<div class="field"><label for="f-status">Status</label><select id="f-status" name="status"><option>Pending</option><option>Baking</option><option>Ready</option><option>Delivered</option></select></div>
<div class="actions"><button type="button" id="e-cancel">Cancel</button><button class="primary">Save order</button></div>
</form>
</dialog>

<dialog id="confirm" aria-labelledby="confirm-text">
<form method="dialog">
<p id="confirm-text"></p>
<div class="actions"><button value="cancel">Keep order</button><button class="primary" value="ok">Delete order</button></div>
</form>
</dialog>

<datalist id="products"><option>Sourdough loaf</option><option>Baguette</option><option>Croissant</option><option>Pain au chocolat</option><option>Cinnamon roll</option><option>Rye loaf</option><option>Focaccia</option></datalist>

<script>
const $=s=>document.querySelector(s);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let orders=[
{id:1,customer:'Blue Door Café',address:'214 Mill St',item:'Sourdough loaf',qty:12,status:'Baking'},
{id:2,customer:'Hollis & Vine',address:'9 Orchard Ave',item:'Croissant',qty:48,status:'Pending'},
{id:3,customer:'Corner Perk',address:'77 Harbor Rd',item:'Pain au chocolat',qty:24,status:'Ready'},
{id:4,customer:'The Rye House Coffee',address:'1520 Pine Ct',item:'Rye loaf',qty:6,status:'Delivered'},
{id:5,customer:'Juniper Coffee Co.',address:'300 Elm Blvd, Suite 2',item:'Cinnamon roll',qty:18,status:'Pending'}
];
let nextId=6,editId=null,pendingId=null,msgTimer;

function render(){
  const q=$('#q').value.trim().toLowerCase(),st=$('#filter').value;
  const rows=orders.filter(o=>(!st||o.status===st)&&(!q||(o.customer+' '+o.item).toLowerCase().includes(q)));
  $('#orders tbody').innerHTML=rows.map(o=>`<tr>
<td>${o.id}</td>
<td>${esc(o.customer)}<span class="sub">${esc(o.address)}</span></td>
<td>${esc(o.item)}</td><td>${o.qty}</td>
<td><span class="status">${o.status}</span></td>
<td><button data-act="edit" data-id="${o.id}" aria-label="Edit order ${o.id} for ${esc(o.customer)}">Edit</button> <button data-act="delete" data-id="${o.id}" aria-label="Delete order ${o.id} for ${esc(o.customer)}">Delete</button></td></tr>`).join('');
  $('#orders').hidden=orders.length===0;
  $('#empty').hidden=orders.length>0;
  $('#none').hidden=!(orders.length>0&&rows.length===0);
}

function say(t){
  const m=$('#msg');m.textContent=t;m.hidden=false;m.focus();
  clearTimeout(msgTimer);msgTimer=setTimeout(()=>m.hidden=true,5000);
}

function clearErrors(){
  document.querySelectorAll('#editor-form .err').forEach(s=>s.hidden=true);
  document.querySelectorAll('#editor-form [aria-invalid]').forEach(i=>{i.removeAttribute('aria-invalid');i.removeAttribute('aria-describedby')});
  document.querySelectorAll('#editor-form input[aria-describedby]').forEach(i=>i.setAttribute('aria-describedby','e-'+i.name));
}

function openEditor(o){
  editId=o?o.id:null;
  const f=$('#editor-form');
  f.reset();clearErrors();
  $('#editor-title').textContent=o?`Edit order #${o.id}`:'Add order';
  if(o){f.customer.value=o.customer;f.address.value=o.address;f.item.value=o.item;f.qty.value=o.qty;f.status.value=o.status;}
  $('#editor').showModal();
  f.customer.focus();
}

function askDelete(o){
  pendingId=o.id;
  $('#confirm').returnValue='';
  $('#confirm-text').textContent=`Delete order #${o.id} for ${o.customer} (${o.qty} ${o.item})? It will be removed from the bake list and the route. This cannot be undone.`;
  $('#confirm').showModal();
}

$('#orders tbody').addEventListener('click',e=>{
  const b=e.target.closest('button');if(!b)return;
  const o=orders.find(x=>x.id==b.dataset.id);if(!o)return;
  if(b.dataset.act==='edit')openEditor(o);else askDelete(o);
});

$('#confirm').addEventListener('close',()=>{
  if($('#confirm').returnValue!=='ok'||pendingId==null)return;
  const o=orders.find(x=>x.id===pendingId);
  orders=orders.filter(x=>x.id!==pendingId);pendingId=null;
  render();say(`Order #${o.id} for ${o.customer} deleted.`);
});

$('#editor-form').addEventListener('submit',e=>{
  e.preventDefault();
  const f=e.target;clearErrors();
  const data={customer:f.customer.value.trim(),address:f.address.value.trim(),item:f.item.value.trim(),qty:Number(f.qty.value),status:f.status.value};
  const errs=[];
  if(!data.customer)errs.push(['customer','Enter the café name.']);
  if(!data.address)errs.push(['address','Enter the delivery address for the driver.']);
  if(!data.item)errs.push(['item','Enter what to bake.']);
  if(!Number.isInteger(data.qty)||data.qty<1)errs.push(['qty','Enter a quantity of 1 or more.']);
  if(errs.length){
    for(const [k,msg] of errs){
      const s=$('#e-'+k);s.textContent=msg;s.hidden=false;
      f.elements[k].setAttribute('aria-invalid','true');
    }
    f.elements[errs[0][0]].focus();
    return;
  }
  let text;
  if(editId==null){const id=nextId++;orders.push({id,...data});text=`Order #${id} added.`;}
  else{Object.assign(orders.find(o=>o.id===editId),data);text=`Order #${editId} saved.`;}
  $('#editor').close();
  render();say(text);
});

$('#e-cancel').onclick=()=>$('#editor').close();
$('#q').addEventListener('input',render);
$('#filter').addEventListener('change',render);
$('#add').onclick=$('#add-first').onclick=()=>openEditor(null);
$('#clear').onclick=()=>{$('#q').value='';$('#filter').value='';render();$('#q').focus();};
render();
</script>
</body></html>
```

What changed: the placeholders are now real café orders, with a delivery address under each café name for the driver. Statuses are Pending, Baking, Ready, and Delivered, which replaces the original "Complete". Search, the status filter, Add/Edit, and Delete all work. Delete asks for confirmation and names the order, and the success message is announced. The no-results and empty-list states now have a way out. Errors appear beside the field and move focus to the first problem. Every Edit and Delete button names its order. Visible focus rings are restored, and the table scrolls sideways on narrow screens. The look, palette, and layout are unchanged.

Not done: the page has no backend, so Add, Edit, and Delete only last until reload. I also didn't run it in a browser or with a screen reader, so those checks are still open. I also did not add a bake-totals summary, since that would be a new feature.
