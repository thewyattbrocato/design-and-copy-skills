I couldn't save the page. The Write tool is disabled in this session, and I have no other way to create files. I also haven't opened the page in a browser, so none of it has been tested. Below is the full finished page. Save it as `orders.html`.

Your original had no script, so I added the behavior your markup implied:
- **Search and filter:** The search box matches customer or item. The filter is now All, Pending or Complete, in place of "Status 1" and "Status 2".
- **Add and edit:** Add Order and Edit open a small form.
- **Delete:** Delete asks "Are you sure…?" first.
- **Messages:** "Success!" shows briefly after a save or delete. "No results found." shows when nothing matches.

Nothing is saved between page loads, same as before. Your two rows are still the sample data, so swap in real orders.

**Look and feel**
- **4 a.m. reading:** It follows the device's light or dark setting. Quantities are big and bold, so the baker sees how much to bake at a glance. Complete rows are dimmed.
- **Summary line:** A line under the title shows pending orders and total units to bake.
- **Status:** Status is shown with a ✓ or dot plus the word, not just color.
- **Phones and print:** The driver gets a stacked card layout on a phone. Printing hides the buttons.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orders</title>
<style>
:root{
  color-scheme:light dark;
  --bg:#faf6ef;--surface:#fffdf9;--ink:#2a2118;--muted:#6b5d4d;--line:#e4d9c7;
  --accent:#8a4b1c;--accent-ink:#fff;--danger:#a3261b;
  --pend-bg:#fde9c4;--pend-ink:#6a4300;--done-bg:#d9eed9;--done-ink:#1d5a28;
  --focus:#1d4ed8;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#17130f;--surface:#211b15;--ink:#f3ebde;--muted:#b3a58f;--line:#3a3025;
  --accent:#e8a463;--accent-ink:#1a1209;--danger:#ff8f84;
  --pend-bg:#4a3510;--pend-ink:#ffd58a;--done-bg:#1f3d25;--done-ink:#a7e3b0;
  --focus:#8ab4ff;
}}
*{box-sizing:border-box}
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:var(--bg);color:var(--ink);font-size:18px;line-height:1.4}
main{max-width:1000px;margin:0 auto}
h1{font-family:Georgia,"Iowan Old Style",serif;font-size:2.2rem;margin:0 0 4px;letter-spacing:-.01em}
.summary{margin:0 0 20px;color:var(--muted)}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.toolbar{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px}
input,select,button{font:inherit;color:inherit}
input,select{padding:10px 12px;border:1.5px solid var(--line);border-radius:8px;background:var(--surface);min-height:44px}
.toolbar input{flex:1 1 220px}
button{padding:8px 16px;min-height:44px;border:1.5px solid var(--line);border-radius:8px;background:var(--surface);cursor:pointer;font-weight:600}
button:hover{border-color:var(--accent)}
button.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
button.danger{color:var(--danger)}
.toolbar .primary{margin-left:auto}
.wrap{background:var(--surface);border:1px solid var(--line);border-radius:12px;overflow:hidden}
table{border-collapse:collapse;width:100%}
th,td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line);vertical-align:middle}
tr:last-child td{border-bottom:0}
th{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);background:var(--bg)}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
td.qty{font-size:1.5rem;font-weight:700}
td.id{color:var(--muted);font-variant-numeric:tabular-nums}
td.item{font-weight:600}
tr.done td:not(.actions){color:var(--muted)}
tr.done td.qty{font-weight:500}
.status{display:inline-flex;align-items:center;gap:6px;padding:3px 12px;border-radius:999px;font-size:.9rem;font-weight:600}
.status::before{content:"";width:8px;height:8px;border-radius:50%;background:currentColor}
.status.pending{background:var(--pend-bg);color:var(--pend-ink)}
.status.complete{background:var(--done-bg);color:var(--done-ink)}
.status.complete::before{content:"✓";width:auto;height:auto;background:none;font-size:.85em}
td.actions{white-space:nowrap}
td.actions button{padding:6px 12px;min-height:40px}
#none{text-align:center;color:var(--muted);padding:32px 0}
#msg{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:12px 22px;border-radius:999px;font-weight:600;box-shadow:0 4px 16px #0004}
dialog{border:1px solid var(--line);border-radius:12px;background:var(--surface);color:var(--ink);padding:24px;max-width:420px;width:calc(100% - 32px)}
dialog::backdrop{background:#0008}
dialog h2{margin:0 0 16px;font-family:Georgia,serif;font-size:1.4rem}
label{display:block;font-weight:600;font-size:.9rem;margin-bottom:12px}
label input,label select{display:block;width:100%;margin-top:4px;font-weight:400}
.btns{display:flex;gap:10px;justify-content:flex-end;margin-top:8px}
#confirm p{margin:0 0 16px}
@media (max-width:640px){
  body{padding:14px}
  thead{display:none}
  table,tbody,tr,td{display:block}
  tr{padding:12px 14px;border-bottom:1px solid var(--line);display:grid;grid-template-columns:1fr auto;gap:2px 12px}
  td{border:0;padding:2px 0}
  td.id{display:none}
  td.cust{grid-column:1;color:var(--muted)}
  td.item{grid-column:1;grid-row:2;font-size:1.15rem}
  td.qty{grid-column:2;grid-row:1/3;align-self:center}
  td.st{grid-column:1;margin-top:4px}
  td.actions{grid-column:1/3;margin-top:8px}
}
@media print{
  body{background:#fff;color:#000;padding:0}
  .toolbar,td.actions,th.actions,#msg{display:none}
  .wrap{border:0}
}
</style></head><body>
<main>
<h1>Orders</h1>
<p class="summary" id="summary"></p>
<div class="toolbar">
  <input id="q" type="search" placeholder="Search customer or item…" aria-label="Search orders">
  <select id="f" aria-label="Filter by status"><option value="">All</option><option>Pending</option><option>Complete</option></select>
  <button class="primary" id="add">Add Order</button>
</div>
<div class="wrap">
<table>
<thead><tr><th>#</th><th>Customer</th><th>Item</th><th class="num">Qty</th><th>Status</th><th class="actions">Actions</th></tr></thead>
<tbody id="rows"></tbody>
</table>
<p id="none" hidden>No results found.</p>
</div>
<div id="msg" role="status" hidden>Success!</div>
</main>

<dialog id="form">
  <form method="dialog" id="orderForm">
    <h2 id="formTitle">Add Order</h2>
    <label>Customer<input name="customer" required></label>
    <label>Item<input name="item" required></label>
    <label>Qty<input name="qty" type="number" min="1" step="1" required inputmode="numeric"></label>
    <label>Status<select name="status"><option>Pending</option><option>Complete</option></select></label>
    <div class="btns"><button type="button" id="cancel">Cancel</button><button class="primary" type="submit">Save</button></div>
  </form>
</dialog>

<dialog id="confirm">
  <p>Are you sure you want to delete this?</p>
  <div class="btns"><button id="no">No</button> <button class="danger" id="yes">Yes</button></div>
</dialog>

<script>
let orders=[
  {id:1,customer:"Customer 1",item:"Product A",qty:10,status:"Pending"},
  {id:2,customer:"Customer 2",item:"Product B",qty:25,status:"Complete"}
];
let nextId=3,editing=null,deleting=null,timer;
const $=id=>document.getElementById(id);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));

function render(){
  const q=$("q").value.trim().toLowerCase(), f=$("f").value;
  const list=orders.filter(o=>(!f||o.status===f)&&(!q||(o.customer+" "+o.item).toLowerCase().includes(q)));
  $("rows").innerHTML=list.map(o=>`<tr class="${o.status==="Complete"?"done":""}">
    <td class="id">${o.id}</td><td class="cust">${esc(o.customer)}</td><td class="item">${esc(o.item)}</td>
    <td class="num qty">${o.qty}</td>
    <td class="st"><span class="status ${o.status.toLowerCase()}">${o.status}</span></td>
    <td class="actions"><button data-edit="${o.id}" aria-label="Edit order ${o.id}">Edit</button> <button class="danger" data-del="${o.id}" aria-label="Delete order ${o.id}">Delete</button></td></tr>`).join("");
  $("none").hidden=list.length>0;
  const pending=orders.filter(o=>o.status==="Pending");
  $("summary").textContent=`${pending.length} pending · ${pending.reduce((n,o)=>n+o.qty,0)} units to bake · ${orders.length} orders total`;
}
function toast(t="Success!"){
  const m=$("msg");m.textContent=t;m.hidden=false;clearTimeout(timer);timer=setTimeout(()=>m.hidden=true,2500);
}
function openForm(o){
  editing=o;const F=$("orderForm");
  $("formTitle").textContent=o?"Edit Order":"Add Order";
  F.customer.value=o?o.customer:"";F.item.value=o?o.item:"";F.qty.value=o?o.qty:"";F.status.value=o?o.status:"Pending";
  $("form").showModal();
}
$("add").onclick=()=>openForm(null);
$("cancel").onclick=()=>$("form").close();
$("orderForm").onsubmit=e=>{
  const F=e.target,d={customer:F.customer.value.trim(),item:F.item.value.trim(),qty:+F.qty.value,status:F.status.value};
  if(editing)Object.assign(editing,d);else orders.push({id:nextId++,...d});
  render();toast();
};
$("rows").onclick=e=>{
  const b=e.target.closest("button");if(!b)return;
  if(b.dataset.edit)openForm(orders.find(o=>o.id==b.dataset.edit));
  if(b.dataset.del){deleting=+b.dataset.del;$("confirm").showModal();}
};
$("no").onclick=()=>$("confirm").close();
$("yes").onclick=()=>{orders=orders.filter(o=>o.id!==deleting);$("confirm").close();render();toast();};
$("q").oninput=$("f").onchange=render;
render();
</script>
</body></html>
```

If you'd like me to save it to a file, enable Write for the session and I'll do it.
