I couldn't save the file: the Write tool is disabled in this session. The full page is below. Copy it into `orders.html` to use it.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:8px;text-align:left;vertical-align:top;overflow-wrap:anywhere}
th{white-space:nowrap}
th.qty,td.qty{text-align:right}
.table-wrap{overflow-x:auto}
.status{padding:2px 8px;border-radius:10px;background:#e5e7eb;white-space:nowrap}
.actions{white-space:nowrap}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.toolbar input{flex:1 1 220px;min-width:0;padding:6px 8px}
button{padding:6px 12px}
:focus-visible{outline:2px solid #1d4ed8;outline-offset:2px}
#msg{margin-bottom:16px;padding:8px 12px;border-radius:6px;background:#ecfdf5;border:1px solid #6ee7b7}
#msg:empty{display:none}
#empty,#none{padding:16px 0}
#empty p,#none p{margin:0 0 8px}
dialog{border:1px solid #ddd;border-radius:8px;padding:20px;width:min(420px,calc(100% - 32px));color:#222}
dialog::backdrop{background:rgba(0,0,0,.3)}
dialog h2{margin:0 0 12px;font-size:1.25rem}
.field{margin-bottom:12px}
.field label{display:block;font-weight:600;margin-bottom:4px}
.field input,.field select{box-sizing:border-box;width:100%;padding:6px 8px;border:1px solid #767676;border-radius:4px;font:inherit}
.field input[aria-invalid=true]{border-color:#b91c1c}
.error{color:#b91c1c;font-size:.9em;margin:4px 0 0}
.dialog-actions{display:flex;gap:8px;justify-content:flex-end;margin-top:16px}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar">
<input id="search" type="search" placeholder="Search customer or item" aria-label="Search customer or item">
<select id="filter" aria-label="Filter by status"><option value="All">All statuses</option><option>Pending</option><option>Complete</option></select>
<button type="button" id="add">Add Order</button>
</div>
<div id="msg" role="status"></div>
<div class="table-wrap" id="table-wrap">
<table>
<thead><tr><th>#</th><th>Customer Name</th><th>Item</th><th class="qty">Qty</th><th>Status</th><th>Actions</th></tr></thead>
<tbody id="rows"></tbody>
</table>
</div>
<div id="empty" hidden><p>No orders yet. Add one to start the bake list.</p><button type="button" id="add-first">Add Order</button></div>
<div id="none" hidden><p id="none-text"></p><button type="button" id="clear">Clear search and filter</button></div>

<dialog id="order-dialog" aria-labelledby="order-title">
<form id="order-form" novalidate>
<h2 id="order-title">Add order</h2>
<div class="field"><label for="f-customer">Customer name</label><input id="f-customer" autocomplete="off" aria-describedby="e-customer"><p class="error" id="e-customer" hidden></p></div>
<div class="field"><label for="f-item">Item</label><input id="f-item" list="products" autocomplete="off" aria-describedby="e-item"><p class="error" id="e-item" hidden></p></div>
<div class="field"><label for="f-qty">Qty</label><input id="f-qty" type="number" min="1" step="1" inputmode="numeric" aria-describedby="e-qty"><p class="error" id="e-qty" hidden></p></div>
<div class="field"><label for="f-status">Status</label><select id="f-status"><option>Pending</option><option>Complete</option></select></div>
<datalist id="products"><option>Almond croissant</option><option>Country sourdough loaf</option><option>Cinnamon roll</option><option>Baguette</option><option>Everything bagel</option></datalist>
<div class="dialog-actions"><button type="button" id="cancel">Cancel</button><button type="submit">Save order</button></div>
</form>
</dialog>

<dialog id="confirm" aria-labelledby="confirm-title" aria-describedby="confirm-text">
<h2 id="confirm-title">Delete this order?</h2>
<p id="confirm-text"></p>
<div class="dialog-actions"><button type="button" id="keep">Keep order</button><button type="button" id="confirm-delete">Delete order</button></div>
</dialog>

<script>
const $=id=>document.getElementById(id);
const rows=$('rows'), search=$('search'), filter=$('filter');
const orderDialog=$('order-dialog'), form=$('order-form'), confirmDialog=$('confirm');
let orders=[
 {id:1,customer:'Harbor Coffee Co.',item:'Almond croissant',qty:24,status:'Pending'},
 {id:2,customer:'Maple & Main Café',item:'Country sourdough loaf',qty:12,status:'Pending'},
 {id:3,customer:'Linden Street Espresso',item:'Cinnamon roll',qty:36,status:'Complete'},
 {id:4,customer:'Northside Bistro',item:'Everything bagel',qty:18,status:'Pending'}
];
let nextId=5, editingId=null, deletingId=null, msgTimer;

function button(label,name,className,onClick){
 const b=document.createElement('button');
 b.type='button'; b.className=className; b.textContent=label; b.setAttribute('aria-label',name);
 b.addEventListener('click',onClick); return b;
}
function cell(text,className){
 const td=document.createElement('td'); td.textContent=text; if(className) td.className=className; return td;
}
function rowFor(o){
 const tr=document.createElement('tr'); tr.dataset.id=o.id;
 const pill=document.createElement('span'); pill.className='status'; pill.textContent=o.status;
 const status=document.createElement('td'); status.append(pill);
 const actions=document.createElement('td'); actions.className='actions';
 actions.append(
  button('Edit',`Edit order ${o.id}, ${o.customer}`,'edit',()=>openForm(o)),
  ' ',
  button('Delete',`Delete order ${o.id}, ${o.customer}`,'delete',()=>askDelete(o))
 );
 tr.append(cell(o.id), cell(o.customer), cell(o.item), cell(o.qty,'qty'), status, actions);
 return tr;
}
function render(){
 const term=search.value.trim(), st=filter.value;
 const lower=term.toLowerCase();
 const shown=orders.filter(o=>(st==='All'||o.status===st)&&(o.customer+' '+o.item).toLowerCase().includes(lower));
 rows.replaceChildren(...shown.map(rowFor));
 $('table-wrap').hidden=orders.length===0;
 $('empty').hidden=orders.length>0;
 $('none').hidden=orders.length===0||shown.length>0;
 if(!$('none').hidden){
  const what=st==='All'?'':st.toLowerCase()+' ';
  $('none-text').textContent=term?`No ${what}orders match “${term}”.`:`No ${what}orders.`;
 }
}
function showMsg(text){
 const m=$('msg'); m.textContent=text; clearTimeout(msgTimer);
 msgTimer=setTimeout(()=>{m.textContent='';},4000);
}
function focusRow(id){
 const tr=rows.querySelector(`tr[data-id="${id}"]`);
 (tr?tr.querySelector('.edit'):$('add')).focus();
}

function clearErrors(){
 ['customer','item','qty'].forEach(k=>{
  $('e-'+k).hidden=true; $('f-'+k).removeAttribute('aria-invalid');
 });
}
function openForm(o){
 editingId=o?o.id:null;
 $('order-title').textContent=o?`Edit order ${o.id}`:'Add order';
 $('f-customer').value=o?o.customer:'';
 $('f-item').value=o?o.item:'';
 $('f-qty').value=o?o.qty:'';
 $('f-status').value=o?o.status:'Pending';
 clearErrors();
 orderDialog.showModal();
}
function validate(){
 const qty=Number($('f-qty').value);
 const problems={
  customer:$('f-customer').value.trim()?'':'Enter the customer name.',
  item:$('f-item').value.trim()?'':'Enter the item, such as Almond croissant.',
  qty:Number.isInteger(qty)&&qty>=1?'':'Enter a quantity of 1 or more.'
 };
 let first=null;
 for(const k in problems){
  const input=$('f-'+k), err=$('e-'+k), msg=problems[k];
  err.textContent=msg; err.hidden=!msg;
  if(msg){ input.setAttribute('aria-invalid','true'); first=first||input; }
  else input.removeAttribute('aria-invalid');
 }
 if(first) first.focus();
 return !first;
}

form.addEventListener('submit',e=>{
 e.preventDefault();
 if(!validate()) return;
 const data={
  customer:$('f-customer').value.trim(),
  item:$('f-item').value.trim(),
  qty:Number($('f-qty').value),
  status:$('f-status').value
 };
 let id, text;
 if(editingId){
  Object.assign(orders.find(o=>o.id===editingId),data);
  id=editingId; text=`Order ${id} saved.`;
 } else {
  id=nextId++; orders.push({id,...data});
  text=`Order ${id} added for ${data.customer}.`;
 }
 orderDialog.close();
 render(); showMsg(text); focusRow(id);
});
$('cancel').addEventListener('click',()=>orderDialog.close());
$('add').addEventListener('click',()=>openForm(null));
$('add-first').addEventListener('click',()=>openForm(null));

function askDelete(o){
 deletingId=o.id;
 $('confirm-text').textContent=`This removes ${o.qty} × ${o.item} for ${o.customer} from the bake list and the route.`;
 confirmDialog.showModal();
}
$('keep').addEventListener('click',()=>confirmDialog.close());
$('confirm-delete').addEventListener('click',()=>{
 const pos=[...rows.children].findIndex(tr=>Number(tr.dataset.id)===deletingId);
 const removed=orders.find(o=>o.id===deletingId);
 orders=orders.filter(o=>o.id!==deletingId);
 confirmDialog.close(); deletingId=null;
 render();
 const after=[...rows.children];
 const next=after[pos]||after[pos-1];
 (next?next.querySelector('.edit'):$('add')).focus();
 showMsg(`Order ${removed.id} deleted.`);
});

$('clear').addEventListener('click',()=>{
 search.value=''; filter.value='All'; render(); search.focus();
});
search.addEventListener('input',render);
filter.addEventListener('change',render);
render();
</script>
</body></html>
```

**What changed**
- **Behavior:** The original had no script, so Search, the filter, Add, Edit and Delete did nothing. They now work, and the table is built from a small data array.
- **Add/Edit:** A dialog with customer, item, quantity and status. Errors show beside the field, the first bad field gets focus, and the typed values stay if validation fails.
- **Delete:** The confirm names the consequence ("This removes 24 × Almond croissant for Harbor Coffee Co. from the bake list and the route.") and uses "Delete order" / "Keep order". Focus moves to the next row after a delete.
- **Feedback:** Success shows in a status region ("Order 5 added for…") that clears after 4 seconds.
- **Empty states:** An empty list offers "Add Order". A search or filter with no matches says what was searched and offers "Clear search and filter".
- **Access and small screens:** Buttons are named by the order they act on. The focus ring is kept. The table scrolls sideways at 320px instead of breaking the layout. Long names wrap.
- **Look:** Colors, spacing, fonts and the gray status pills are unchanged.

**Decisions for you**
- I kept the statuses as Pending and Complete from the original. If bakers need "Baking" or "Out for delivery", that is a workflow change to make.
- The customers, items and quantities are invented sample data. The product list in the Item field is also a placeholder; swap in your real product names.

**Not checked:** I could not open this in a browser or run it with a screen reader, so the keyboard and screen-reader behavior is from reading the code only.
