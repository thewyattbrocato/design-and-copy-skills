I couldn't save the page. The Write tool is disabled in this session, so nothing has been created or changed on disk. Below is the full finished file. Save it as `index.html`, or turn Write back on and I'll save it.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222;font-size:1.125rem;line-height:1.4}
h1{margin-top:0}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:10px 8px;text-align:left;overflow-wrap:anywhere}
th{background:#f6f6f6}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
td.qty{font-weight:700;font-size:1.25rem}
.status{display:inline-block;padding:2px 10px;border-radius:10px;background:#e5e7eb;color:#222;white-space:nowrap}
.status.pending{background:#fde9b8;color:#4a3200}
.status.complete{background:#d4edda;color:#14381f}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.toolbar input{flex:1 1 200px}
input,select,button{font:inherit;padding:8px 12px;min-height:44px;box-sizing:border-box}
input,select{border:1px solid #767676;border-radius:4px;background:#fff;color:#222}
button{cursor:pointer}
:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
.wrap{overflow-x:auto}
#none{margin:16px 0}
#msg{position:fixed;left:24px;bottom:24px;background:#14381f;color:#fff;padding:12px 16px;border-radius:6px}
#msg[hidden]{display:none}
dialog{border:1px solid #767676;border-radius:8px;padding:20px;max-width:min(420px,calc(100vw - 32px))}
dialog::backdrop{background:rgba(0,0,0,.4)}
dialog label{display:block;margin-bottom:12px}
dialog label input,dialog label select{display:block;width:100%;margin-top:4px}
.err{color:#9b1c1c;margin:0 0 12px}
.actions{display:flex;gap:8px;justify-content:flex-end;margin-top:8px}
@media(max-width:600px){body{padding:12px}}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar">
  <input id="q" type="search" placeholder="Search customer or item" aria-label="Search orders by customer or item">
  <select id="f" aria-label="Filter by status"><option value="">All</option><option>Pending</option><option>Complete</option></select>
  <button id="add" type="button">Add Order</button>
</div>
<div class="wrap">
<table>
<thead><tr><th class="num">#</th><th>Customer Name</th><th>Item</th><th class="num">Qty</th><th>Status</th><th>Actions</th></tr></thead>
<tbody id="rows"></tbody>
</table>
</div>
<p id="none" hidden>No results found. <button id="clear" type="button">Clear search and filter</button></p>
<div id="msg" role="status" hidden>Success!</div>

<dialog id="confirm" aria-labelledby="ctitle">
  <form method="dialog">
    <p id="ctitle">Are you sure you want to delete this?<br><strong id="cwhat"></strong></p>
    <div class="actions"><button value="no" autofocus>No, keep it</button> <button value="yes">Yes, delete</button></div>
  </form>
</dialog>

<dialog id="edit" aria-labelledby="etitle">
  <form id="eform" method="dialog" novalidate>
    <h2 id="etitle" style="margin-top:0"></h2>
    <p class="err" id="eerr" role="alert" hidden></p>
    <label>Customer Name<input name="c" required></label>
    <label>Item<input name="i" required></label>
    <label>Qty<input name="n" type="number" min="1" step="1" inputmode="numeric" required></label>
    <label>Status<select name="s"><option>Pending</option><option>Complete</option></select></label>
    <div class="actions"><button type="button" id="ecancel">Cancel</button> <button type="submit">Save</button></div>
  </form>
</dialog>

<script>
let orders=[
 {id:1,c:"Customer 1",i:"Product A",n:10,s:"Pending"},
 {id:2,c:"Customer 2",i:"Product B",n:25,s:"Complete"}
], nextId=3, editing=null, last=null, timer;
const $=id=>document.getElementById(id), rows=$("rows");

function esc(t){const d=document.createElement("div");d.textContent=t;return d.innerHTML}
function render(){
  const q=$("q").value.trim().toLowerCase(), f=$("f").value;
  const list=orders.filter(o=>(!f||o.s===f)&&(!q||(o.c+" "+o.i).toLowerCase().includes(q)));
  rows.innerHTML=list.map(o=>`<tr><td class="num">${o.id}</td><td>${esc(o.c)}</td><td>${esc(o.i)}</td><td class="num qty">${o.n}</td>
   <td><span class="status ${o.s.toLowerCase()}">${o.s}</span></td>
   <td><button type="button" data-a="edit" data-id="${o.id}" aria-label="Edit order ${o.id}: ${esc(o.c)}, ${esc(o.i)}">Edit</button>
   <button type="button" data-a="del" data-id="${o.id}" aria-label="Delete order ${o.id}: ${esc(o.c)}, ${esc(o.i)}">Delete</button></td></tr>`).join("");
  const empty=!list.length;
  $("none").hidden=!empty;
  $("none").firstChild.textContent=orders.length?"No results found. ":"No orders yet. ";
  $("clear").hidden=!orders.length;
  document.querySelector("table").hidden=empty;
}
function say(t){clearTimeout(timer);const m=$("msg");m.textContent=t;m.hidden=false;timer=setTimeout(()=>m.hidden=true,4000)}

$("q").oninput=$("f").onchange=render;
$("clear").onclick=()=>{$("q").value="";$("f").value="";render();$("q").focus()};
$("add").onclick=()=>{last=null;openEdit(null)};
rows.onclick=e=>{
  const b=e.target.closest("button"); if(!b) return;
  const o=orders.find(x=>x.id==b.dataset.id); last=b;
  if(b.dataset.a==="edit") openEdit(o);
  else{editing=o;$("cwhat").textContent=`#${o.id} ${o.c}: ${o.n} × ${o.i}`;$("confirm").showModal()}
};
$("confirm").onclose=()=>{
  if($("confirm").returnValue==="yes"&&editing){
    orders=orders.filter(x=>x!==editing);render();say("Order deleted.");
    (rows.querySelector("button[data-a=del]")||$("add")).focus();
  } else if(last&&last.isConnected) last.focus();
  $("confirm").returnValue="";
};
function openEdit(o){
  editing=o;const f=$("eform");
  $("etitle").textContent=o?`Edit order #${o.id}`:"Add Order";
  f.c.value=o?o.c:"";f.i.value=o?o.i:"";f.n.value=o?o.n:"";f.s.value=o?o.s:"Pending";
  $("eerr").hidden=true;$("edit").showModal();
}
$("ecancel").onclick=()=>$("edit").close();
$("edit").onclose=()=>{(last&&last.isConnected?last:$("add")).focus()};
$("eform").onsubmit=e=>{
  e.preventDefault();const f=e.target,n=Number(f.n.value);
  const bad=!f.c.value.trim()?[f.c,"Enter the customer name."]:!f.i.value.trim()?[f.i,"Enter the item."]:
    !(Number.isInteger(n)&&n>0)?[f.n,"Enter a whole number of 1 or more for Qty."]:null;
  if(bad){$("eerr").textContent=bad[1];$("eerr").hidden=false;bad[0].focus();return}
  const v={c:f.c.value.trim(),i:f.i.value.trim(),n,s:f.s.value};
  const wasEdit=!!editing;
  if(editing)Object.assign(editing,v);else orders.push({id:nextId++,...v});
  $("edit").close();render();say(wasEdit?"Order saved.":"Order added.");
};
render();
</script>
</body></html>
```

**What I changed, keeping the look, layout and wording:**
- **Controls that did nothing now work.**
  - Search matches customer or item.
  - The filter options are now All, Pending and Complete, replacing "Status 1" and "Status 2".
  - Delete opens your confirm prompt, now as a real dialog. The buttons read "No, keep it" and "Yes, delete", and the dialog names the order.
  - Add Order and Edit open a small form with inline errors that keep what was typed.
  - Saves and deletes show the success message, which is now announced to screen readers.
- **No results.** The empty message offers "Clear search and filter". If every order has been deleted, it says "No orders yet." instead.
- **Early-morning reading.**
  - Text is larger.
  - Quantity is bold, right-aligned and has tabular figures.
  - Pending and Complete have distinct tints with dark text, and the status word is still there.
- **Access.**
  - Inputs have labels and there is a visible focus ring.
  - Buttons are at least 44px tall.
  - Each Edit and Delete button is named for its order.
  - Focus returns to a sensible place after a dialog closes or a row is deleted.
- **Narrow screens.** The table scrolls sideways and long names wrap.

**Open questions:**
- Orders live in memory only, so a reload resets them. Saving them needs your backend or `localStorage`, and I didn't want to guess which.
- I kept "Customer 1" and "Product A" as sample data. Swap in real café names and breads.
- I haven't run this in a browser or tested it with a screen reader.
