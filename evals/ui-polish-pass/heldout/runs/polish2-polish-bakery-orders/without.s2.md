I couldn't save the file because the Write tool is disabled in this session. Nothing has been written to disk. Here is the finished page. Save it as `index.html`, or turn Write back on and I'll create it.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orders</title>
<style>
:root{
  --bg:#fbf6ee;--panel:#fff;--ink:#2b2118;--muted:#6f6254;--line:#e6dccb;
  --accent:#8a4b1f;--accent-ink:#fff;--danger:#a32a1d;
  --pend-bg:#fde7b0;--pend-ink:#5c3d00;--done-bg:#d5ebd2;--done-ink:#1d4a1a;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#17120e;--panel:#221b15;--ink:#f4ece1;--muted:#b4a595;--line:#3a2f26;
  --accent:#e9a066;--accent-ink:#1a1008;--danger:#ff8b7a;
  --pend-bg:#5a4210;--pend-ink:#ffe3a0;--done-bg:#24452a;--done-ink:#c8f0c8;
}}
*{box-sizing:border-box}
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:var(--bg);color:var(--ink);font-size:18px;line-height:1.4}
main{max-width:1000px;margin:0 auto}
h1{font-family:Georgia,"Times New Roman",serif;font-size:2.2rem;margin:0 0 16px;letter-spacing:.01em}
.toolbar{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px}
input,select,button{font:inherit;color:inherit}
input,select{padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--panel)}
#q{flex:1 1 220px;min-width:0}
button{padding:10px 16px;border:1px solid var(--line);border-radius:8px;background:var(--panel);cursor:pointer;min-height:44px}
button:hover{border-color:var(--accent)}
button.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent);font-weight:600}
button.danger{color:var(--danger)}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.table-wrap{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow-x:auto}
table{border-collapse:collapse;width:100%}
th,td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line)}
tr:last-child td{border-bottom:0}
th{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);background:var(--bg)}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
td.qty{font-size:1.5rem;font-weight:700}
td.cust{font-weight:600}
.status{display:inline-block;padding:3px 12px;border-radius:999px;font-size:.85rem;font-weight:600}
.status.pending{background:var(--pend-bg);color:var(--pend-ink)}
.status.complete{background:var(--done-bg);color:var(--done-ink)}
tr.done td:not(.act){color:var(--muted)}
td.act{white-space:nowrap}
td.act button{padding:6px 12px;min-height:40px}
#none{padding:24px;text-align:center;color:var(--muted)}
#msg{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--done-bg);color:var(--done-ink);padding:12px 22px;border-radius:10px;font-weight:600;box-shadow:0 4px 16px #0004}
dialog{border:1px solid var(--line);border-radius:12px;background:var(--panel);color:var(--ink);padding:24px;max-width:420px;width:calc(100% - 32px)}
dialog::backdrop{background:#0008}
dialog label{display:block;margin-bottom:12px;font-size:.9rem;color:var(--muted)}
dialog label input,dialog label select{display:block;width:100%;margin-top:4px;color:var(--ink);font-size:1rem}
.btns{display:flex;gap:10px;justify-content:flex-end;margin-top:16px}
[hidden]{display:none!important}
</style></head><body>
<main>
<h1>Orders</h1>
<div class="toolbar">
  <input id="q" type="search" placeholder="Search customer or item…" aria-label="Search orders">
  <select id="filter" aria-label="Filter by status"><option>All</option><option>Pending</option><option>Complete</option></select>
  <button id="add" class="primary">Add Order</button>
</div>
<div class="table-wrap">
<table>
<thead><tr><th class="num">#</th><th>Customer</th><th>Item</th><th class="num">Qty</th><th>Status</th><th>Actions</th></tr></thead>
<tbody id="rows"></tbody>
</table>
<p id="none" hidden>No results found.</p>
</div>
</main>

<div id="msg" role="status" hidden>Success!</div>

<dialog id="confirm">
  <p id="confirmText">Are you sure you want to delete this?</p>
  <div class="btns"><button id="no">No</button> <button id="yes" class="danger">Yes</button></div>
</dialog>

<dialog id="form">
  <form method="dialog" id="orderForm">
    <label>Customer<input name="customer" required></label>
    <label>Item<input name="item" required></label>
    <label>Qty<input name="qty" type="number" min="1" required></label>
    <label>Status<select name="status"><option>Pending</option><option>Complete</option></select></label>
    <div class="btns"><button type="button" id="cancel">Cancel</button> <button class="primary">Save</button></div>
  </form>
</dialog>

<script>
let orders=[
  {id:1,customer:"Customer 1",item:"Product A",qty:10,status:"Pending"},
  {id:2,customer:"Customer 2",item:"Product B",qty:25,status:"Complete"}
];
let nextId=3,editing=null,deleting=null,timer;
const $=id=>document.getElementById(id);
const rows=$("rows");

function esc(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}

function render(){
  const q=$("q").value.trim().toLowerCase(),f=$("filter").value;
  const list=orders.filter(o=>(f==="All"||o.status===f)&&(o.customer+" "+o.item).toLowerCase().includes(q));
  rows.innerHTML=list.map(o=>`<tr class="${o.status==="Complete"?"done":""}" data-id="${o.id}">
    <td class="num">${o.id}</td><td class="cust">${esc(o.customer)}</td><td>${esc(o.item)}</td>
    <td class="num qty">${o.qty}</td>
    <td><span class="status ${o.status.toLowerCase()}">${o.status}</span></td>
    <td class="act"><button data-a="edit">Edit</button> <button data-a="del" class="danger">Delete</button></td></tr>`).join("");
  $("none").hidden=list.length>0;
}

function flash(text){
  const m=$("msg");m.textContent=text;m.hidden=false;
  clearTimeout(timer);timer=setTimeout(()=>m.hidden=true,2500);
}

rows.addEventListener("click",e=>{
  const b=e.target.closest("button");if(!b)return;
  const id=+b.closest("tr").dataset.id,o=orders.find(x=>x.id===id);
  if(b.dataset.a==="edit")openForm(o);
  else{deleting=id;$("confirmText").textContent=`Are you sure you want to delete order ${id} (${o.customer})?`;$("confirm").showModal();}
});
$("yes").onclick=()=>{orders=orders.filter(o=>o.id!==deleting);$("confirm").close();render();flash("Order deleted.");};
$("no").onclick=()=>$("confirm").close();

function openForm(o){
  editing=o;const f=$("orderForm");f.reset();
  if(o){f.customer.value=o.customer;f.item.value=o.item;f.qty.value=o.qty;f.status.value=o.status;}
  $("form").showModal();f.customer.focus();
}
$("add").onclick=()=>openForm(null);
$("cancel").onclick=()=>$("form").close();
$("orderForm").addEventListener("submit",()=>{
  const f=$("orderForm"),d={customer:f.customer.value.trim(),item:f.item.value.trim(),qty:+f.qty.value,status:f.status.value};
  const wasEdit=!!editing;
  if(editing)Object.assign(editing,d);else orders.push({id:nextId++,...d});
  render();flash(wasEdit?"Order updated.":"Order added.");
});

$("q").addEventListener("input",render);
$("filter").addEventListener("change",render);
render();
</script>
</body></html>
```

I haven't opened it in a browser.

**What I added**
- The hidden pieces in your markup are now wired up:
  - **Search and status filter:** search matches customer and item. The filter offers All, Pending and Complete instead of "Status 1/2".
  - **"No results found."** shows when nothing matches.
  - **Success message:** it appears briefly after a change and then disappears.
  - **Delete:** it asks for confirmation first, and the question names the order.
  - **Add and Edit:** both open a small form.
- Search and filter work together, and orders are still numbered the same way.

**Design, for 4am and the driver**
- **Quantity:** it is the largest thing in each row, since it's what the bakers need.
- **Completed orders:** they fade back so the pending ones stand out. Status is shown as text as well as color.
- **Dark mode:** it follows the device setting, so it's easier on the eyes at 4am.
- **Touch targets:** buttons are large and the table scrolls sideways on a phone.

**What I didn't change**
- **Sample data:** the two rows are still your placeholders ("Customer 1", "Product A"). Swap in real data.
- **Persistence:** like your original, nothing is saved, so a reload resets the list. Saving to a server or `localStorage` would be the next step.
- **Route info:** I didn't add delivery address or stop order for the driver. I'd need to know what you want to show there.
