I couldn't save a file because the Write tool is disabled in this session. The full page is below, so you can paste it into `index.html`. I haven't run it in a browser or tested it with a screen reader.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222;font-size:18px;line-height:1.4}
h1{margin:0 0 16px}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:10px 8px;text-align:left;overflow-wrap:anywhere}
th{background:#f6f6f6;font-size:.85em}
td.qty{font-size:1.25em;font-weight:700;font-variant-numeric:tabular-nums}
.wrap{overflow-x:auto}
.status{padding:2px 10px;border-radius:10px;background:#e5e7eb;white-space:nowrap;display:inline-block}
.status.pending{background:#fde9b8;color:#4a3300}
.status.complete{background:#d4ecd8;color:#124a1d}
.status.complete::before{content:"\2713\00a0"}
.toolbar{margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px}
.toolbar input{flex:1 1 200px}
input,select,button,textarea{font:inherit;color:inherit}
input,select{padding:6px 8px;border:1px solid #767676;border-radius:4px;background:#fff}
button{padding:6px 12px;min-height:40px;border:1px solid #767676;border-radius:4px;background:#f3f3f3;cursor:pointer}
button.primary{background:#222;color:#fff;border-color:#222}
button:hover{background:#e6e6e6}button.primary:hover{background:#000}
:focus-visible{outline:3px solid #1a56db;outline-offset:2px}
td.actions{white-space:nowrap}
#none{padding:24px 0}
#msg{position:fixed;left:24px;right:24px;bottom:24px;max-width:480px;padding:12px 16px;background:#124a1d;color:#fff;border-radius:6px;display:flex;gap:12px;align-items:center;justify-content:space-between}
#msg[hidden],#none[hidden],#confirm[hidden]{display:none}
#msg button{background:#fff;color:#222;min-height:36px}
dialog{border:1px solid #767676;border-radius:8px;padding:20px;max-width:360px;width:calc(100% - 48px)}
dialog::backdrop{background:rgba(0,0,0,.4)}
dialog label{display:block;margin-bottom:12px}
dialog input,dialog select{display:block;width:100%;box-sizing:border-box;margin-top:4px}
.err{color:#9b1c1c;font-size:.9em;margin:0 0 8px}
.row{display:flex;gap:8px;justify-content:flex-end;margin-top:8px}
@media (max-width:600px){body{padding:12px}}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar"><input id="q" type="search" aria-label="Search orders" placeholder="Search café or item"> <select id="f" aria-label="Filter by status"><option value="">All</option><option>Pending</option><option>Complete</option></select> <button id="add" class="primary">Add Order</button></div>
<div class="wrap"><table>
<thead><tr><th scope="col">#</th><th scope="col">Customer Name</th><th scope="col">Item</th><th scope="col">Qty</th><th scope="col">Status</th><th scope="col">Actions</th></tr></thead>
<tbody id="rows"></tbody>
</table></div>
<p id="none" hidden role="status"></p>
<div id="msg" hidden role="status"><span id="msgtext">Success!</span> <button id="undo" hidden>Undo</button></div>
<div id="confirm" hidden>Are you sure you want to delete this?<br><button>Yes</button> <button>No</button></div>

<dialog id="dlg" aria-labelledby="dtitle"><form method="dialog" id="form" novalidate>
<h2 id="dtitle" style="margin-top:0"></h2>
<p class="err" id="err" role="alert" hidden></p>
<label>Customer<input name="c" required></label>
<label>Item<input name="i" required></label>
<label>Qty<input name="q" type="number" min="1" step="1" inputmode="numeric" required></label>
<label>Status<select name="s"><option>Pending</option><option>Complete</option></select></label>
<div class="row"><button type="button" id="cancel">Cancel</button><button class="primary" id="save">Save order</button></div>
</form></dialog>

<script>
var orders=[{id:1,c:"Customer 1",i:"Product A",q:10,s:"Pending"},{id:2,c:"Customer 2",i:"Product B",q:25,s:"Complete"}],
nextId=3,editing=null,timer,last=null,opener=null;
var $=function(s){return document.querySelector(s)},rows=$("#rows"),q=$("#q"),f=$("#f");
function esc(t){var d=document.createElement("div");d.textContent=t;return d.innerHTML.replace(/"/g,"&quot;")}
function render(){
 var t=q.value.trim().toLowerCase(),s=f.value;
 var list=orders.filter(function(o){return(!s||o.s===s)&&(!t||(o.c+" "+o.i).toLowerCase().indexOf(t)>-1)});
 rows.innerHTML=list.map(function(o){var n=esc(o.c+", "+o.i);
  return '<tr><td>'+o.id+'</td><td>'+esc(o.c)+'</td><td>'+esc(o.i)+'</td><td class="qty">'+o.q+'</td><td><span class="status '+o.s.toLowerCase()+'">'+o.s+'</span></td><td class="actions"><button data-e="'+o.id+'" aria-label="Edit order '+o.id+': '+n+'">Edit</button> <button data-d="'+o.id+'" aria-label="Delete order '+o.id+': '+n+'">Delete</button></td></tr>'}).join("");
 var none=$("#none"),empty=!list.length;
 $("table").hidden=empty;none.hidden=!empty;
 if(empty)none.innerHTML=orders.length?'No orders match your search or filter. <button id="clr">Clear search</button>':'No orders yet. Use Add Order to enter the first one.';
}
function say(text,canUndo){clearTimeout(timer);$("#msgtext").textContent=text;$("#undo").hidden=!canUndo;$("#msg").hidden=false;timer=setTimeout(function(){$("#msg").hidden=true;last=null},canUndo?8000:3000)}
function openDlg(o,btn){editing=o;opener=btn;$("#dtitle").textContent=o?"Edit order "+o.id:"Add order";$("#err").hidden=true;
 var e=$("#form").elements;e.c.value=o?o.c:"";e.i.value=o?o.i:"";e.q.value=o?o.q:"";e.s.value=o?o.s:"Pending";$("#dlg").showModal();e.c.focus()}
$("#add").onclick=function(){openDlg(null,this)};
$("#cancel").onclick=function(){$("#dlg").close()};
$("#dlg").addEventListener("close",function(){if(opener&&document.contains(opener))opener.focus();else $("#add").focus()});
$("#form").addEventListener("submit",function(ev){
 var e=this.elements,c=e.c.value.trim(),i=e.i.value.trim(),n=parseInt(e.q.value,10);
 if(!c||!i||!(n>0)){ev.preventDefault();var er=$("#err");er.textContent="Enter a customer, an item and a quantity of 1 or more.";er.hidden=false;(!c?e.c:!i?e.i:e.q).focus();return}
 if(editing){editing.c=c;editing.i=i;editing.q=n;editing.s=e.s.value;say("Order "+editing.id+" saved.")}
 else{orders.push({id:nextId++,c:c,i:i,q:n,s:e.s.value});say("Order added.")}
 render()});
rows.addEventListener("click",function(ev){
 var b=ev.target.closest("button");if(!b)return;
 if(b.dataset.e){openDlg(orders.filter(function(o){return o.id==b.dataset.e})[0],b)}
 if(b.dataset.d){var idx=orders.findIndex(function(o){return o.id==b.dataset.d});last={o:orders[idx],idx:idx};orders.splice(idx,1);render();say("Order "+last.o.id+" deleted.",true);
  var nb=rows.querySelector("button");(nb||q).focus()}});
$("#undo").onclick=function(){if(!last)return;orders.splice(last.idx,0,last.o);last=null;render();say("Order restored.");q.focus()};
$("#none").addEventListener("click",function(ev){if(ev.target.id==="clr"){q.value="";f.value="";render();q.focus()}});
q.oninput=f.onchange=render;
render();
</script>
</body></html>
```

I kept the layout, colors, column order and wording. The page was static before, so every control did nothing. Now:

- **Search and filter work.** The status filter lists Pending and Complete instead of "Status 1/2". If nothing matches, the page says so and offers "Clear search". It also has a message for an empty list.
- **Delete undoes instead of asking.** Deleting removes the row and shows "Order N deleted" with Undo for 8 seconds, so there's no "Are you sure?" step. The old `#confirm` block is still in the markup but hidden. Delete it if you don't want it.
- **Add and Edit open a small dialog.** It checks the fields, shows the error inside the dialog and keeps what was typed. After saving, a short "saved" message appears. Focus returns to the button you used.
- **Easier to read at 4 a.m.** Text is 18px, quantities are large and bold, and buttons are at least 40px tall. Pending and Complete have different colors, and Complete also has a ✓ plus the word, so color isn't the only cue.
- **Accessibility.** Focus rings are visible. Edit and Delete buttons name their order. The search box and filter have labels, the table has proper headers, and messages are announced to screen readers. The table scrolls sideways on narrow screens instead of breaking.

- **Needs your input:** Customer 1 / Product A are still the sample data, and changes live only in the page and reset on reload. Persisting them needs a backend or `localStorage`.
- **Not checked:** I didn't try the page at 320px or with large text.
- **Not built:** the driver's route view. I don't know what the page should show for them, such as address or delivery order.
