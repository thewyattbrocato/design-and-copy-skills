I couldn't save the file because the Write tool is disabled in this session. The full finished page is below, so you can paste it over your current file. I haven't opened it in a browser.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Front desk</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px}nav a{color:#fff;margin-right:20px;text-decoration:none;display:inline-block;padding:6px 0;border-bottom:2px solid transparent}
nav a[aria-current=page]{border-bottom-color:#fff;font-weight:600}
main{padding:24px}.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 160px}.card b{display:block;font-size:28px}
.tablewrap{overflow-x:auto}
table{width:100%;background:#fff;border-collapse:collapse}th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
caption{text-align:left;position:absolute;left:-9999px}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;min-height:36px;cursor:pointer}
button.link{background:none;color:#1d4ed8;text-decoration:underline;padding:8px 4px}
button[aria-disabled=true]{background:#6b7280;cursor:progress}
:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
nav :focus-visible{outline-color:#fff}
.msg{background:#fff;border-left:4px solid #6b7280;padding:12px 16px;border-radius:4px;margin:12px 0}
.msg.err{border-left-color:#b91c1c}.msg.ok{border-left-color:#15803d}
.msg.err strong{color:#b91c1c}
.skel td span{display:block;height:14px;border-radius:4px;background:#e5e7eb}
form{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end}
label{display:flex;flex-direction:column;gap:4px;font-size:14px}
input,select{padding:8px;border:1px solid #6b7280;border-radius:4px;font:inherit;min-height:20px;background:#fff}
input[aria-invalid=true]{border-color:#b91c1c}
.fielderr{color:#b91c1c;font-size:13px;min-height:1em}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;background:#6b7280}
.dot.good{background:#15803d}.dot.wait{background:#b45309}
@media (prefers-reduced-motion:no-preference){.skel td span{animation:p 1.2s ease-in-out infinite}@keyframes p{50%{opacity:.5}}}
</style></head><body>
<nav aria-label="Main"><a href="#" aria-current="page">Dashboard</a><a href="#">Items</a><a href="#">Users</a><a href="#">Settings</a></nav>
<main>
<h1>Front desk</h1>
<div class="cards" aria-label="Today at a glance">
<div class="card">Checked in today<b id="c-in">–</b></div>
<div class="card">Day passes sold<b id="c-pass">–</b></div>
<div class="card">Shoes rented<b id="c-shoes">–</b></div>
</div>
<h2>Recent Activity</h2>
<div class="tablewrap"><table>
<caption>Recent check-ins, day passes and shoe rentals</caption>
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody id="rows"></tbody>
</table></div>
<p id="empty" class="msg" hidden>Nothing at the desk yet. Check someone in, sell a day pass or rent shoes with the form below.</p>
<div id="err" class="msg err" role="alert" hidden><strong>Couldn't load recent activity.</strong> The list may be out of date. <button type="button" class="link" id="retry">Try again</button></div>
<h2>Add New</h2>
<form id="f" novalidate>
<label>Name<input id="name" name="name" autocomplete="off" aria-describedby="name-err" placeholder="e.g. Jane Smith"><span class="fielderr" id="name-err"></span></label>
<label>Item<select id="item" name="item"><option>Check-in</option><option>Day pass</option><option>Shoe rental</option></select><span class="fielderr"></span></label>
<span><button type="submit" id="go">Submit</button><span class="fielderr"></span></span>
</form>
<div id="status" class="msg" role="status" hidden></div>
<div id="fail" class="msg err" role="alert" hidden></div>
</main>
<script>
const $=id=>document.getElementById(id);
let data=[];
// TODO: replace these two stubs with the desk's real backend calls.
const api={
  list:async()=>[
    {name:"John Doe",item:"Day pass",at:"2024-01-01T10:15"},
    {name:"Jane Smith",item:"Shoe rental",at:"2024-01-02T11:40"}],
  add:async e=>e
};
const statusOf={"Check-in":["Checked in","good"],"Day pass":["Paid","good"],"Shoe rental":["Out","wait"]};
const fmt=s=>new Date(s).toLocaleString([], {dateStyle:"medium",timeStyle:"short"});
function render(){
  const body=$("rows");body.textContent="";
  for(const r of data){
    const tr=body.insertRow();
    tr.insertCell().textContent=r.name;
    tr.insertCell().textContent=r.item;
    const [w,c]=statusOf[r.item]||[r.item,""];
    const td=tr.insertCell();const d=document.createElement("span");
    d.className="dot "+c;d.setAttribute("aria-hidden","true");td.append(d,w);
    tr.insertCell().textContent=fmt(r.at);
  }
  $("empty").hidden=data.length>0;
  const n=i=>data.filter(r=>r.item===i).length;
  $("c-in").textContent=n("Check-in");$("c-pass").textContent=n("Day pass");$("c-shoes").textContent=n("Shoe rental");
}
function skeleton(){
  $("rows").innerHTML=Array(3).fill('<tr class="skel"><td><span></span></td><td><span></span></td><td><span></span></td><td><span></span></td></tr>').join("");
  $("empty").hidden=true;
}
async function load(){
  $("err").hidden=true;
  if(!data.length)skeleton();
  try{data=await api.list();render()}
  catch(e){render();$("err").hidden=false}
}
$("retry").onclick=load;
$("f").onsubmit=async ev=>{
  ev.preventDefault();
  const btn=$("go");if(btn.getAttribute("aria-disabled")==="true")return;
  const name=$("name"),v=name.value.trim();
  $("fail").hidden=true;$("status").hidden=true;
  if(!v){name.setAttribute("aria-invalid","true");$("name-err").textContent="Enter the climber's name.";name.focus();return}
  name.removeAttribute("aria-invalid");$("name-err").textContent="";
  btn.setAttribute("aria-disabled","true");btn.textContent="Saving…";
  const entry={name:v,item:$("item").value,at:new Date().toISOString()};
  try{
    await api.add(entry);
    data.unshift(entry);render();
    $("status").textContent=`${entry.item} saved for ${v}.`;$("status").hidden=false;
    name.value="";name.focus();
  }catch(e){
    $("fail").textContent=`Couldn't save ${entry.item.toLowerCase()} for ${v}. Nothing was recorded. Check the connection and press Submit again.`;
    $("fail").hidden=false;
  }finally{btn.removeAttribute("aria-disabled");btn.textContent="Submit"}
};
load();
</script>
</body></html>
```

I kept your nav, card, table and form layout, colors, fonts and nav links. What changed:

- **Gym wording:** the page is now "Front desk". The cards read Checked in today, Day passes sold and Shoes rented. They count the rows in the table, so they can't disagree with it. I dropped the Revenue card because I don't have your prices. The "Enter value" field is now an Item dropdown with Check-in, Day pass and Shoe rental.
- **Submit:**
  - A blank name shows an error next to the field and puts the cursor there.
  - While saving, the button reads "Saving…" and can't be pressed twice.
  - On success a message says what was saved, the new row appears at the top, and the name field is cleared and focused for the next person.
  - On failure a message says nothing was recorded, and the typed name stays in the field.
- **Loading, empty and error states:** the table shows placeholder rows while loading. An empty list tells staff what to do next. A failed load shows a "Try again" button.
- **Status column:** each status has a word as well as a colored dot.
- **Accessibility and small screens:** there are visible keyboard focus outlines, real labels on the inputs, and a marker for the current nav page. Cards wrap, and the table scrolls sideways on narrow screens.

Things for you to check before Monday:

- **The data is still fake.** `api.list` and `api.add` at the top of the script are stubs that return the two sample rows, and new entries are only held in the page. Reloading loses them. Swap in your real calls, and make them throw on failure so the error messages appear.
- **Statuses are my guess.** Check-in shows "Checked in", day pass shows "Paid" and shoe rental shows "Out". There's no way to mark shoes as returned yet. Edit the `statusOf` line to match how the desk works.
- **Not tested:** I haven't run it in a browser or with a screen reader. The sample rows are dated January 2024, so you'll want real data.
