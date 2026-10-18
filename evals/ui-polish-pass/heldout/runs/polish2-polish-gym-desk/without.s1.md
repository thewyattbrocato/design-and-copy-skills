I couldn't save the file. The Write tool is disabled in this session, and I have no other way to create files here. The full finished page is below, so you can paste it into `index.html` yourself. If you turn file writing back on, I'll save it directly.

I kept your layout, classes, nav, cards, table, the two hidden messages and the form. I changed the content and made it work for the desk:

- **Wording:** "Dashboard / Welcome / Total Users / Item 1" are now Front Desk, Checked in today, Sales today and Shoes out now.
- **Form:** the Submit button adds a row to the activity table.
  - The second input is now a dropdown: Member check-in, Day pass, Shoe rental, or Day pass + shoe rental.
  - An empty name shows an error and puts the cursor back in the name box.
- **Cards:** the three totals are worked out from the table, so they stay correct.
- **Shoes:** shoe rentals show a "Shoes out" status with a Return shoes button on the row.
- **Empty and error messages:** "No data available" now only shows before the first entry. The error message shows if the browser can't save.
- **Saving:** entries are kept in the browser per day, so a refresh doesn't wipe the desk's list. The list starts fresh each day.
- **Also added:** bigger tap targets, visible keyboard focus, text labels on the status badges, and a layout that works on a tablet.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Front Desk</title>
<style>
:root{--bg:#f5f5f5;--ink:#222;--muted:#5b6470;--line:#e5e7eb;--surface:#fff;--accent:#2563eb;--accent-d:#1d4ed8;--nav:#1f2937;--ok:#166534;--ok-bg:#dcfce7;--warn:#92400e;--warn-bg:#fef3c7;--bad:#991b1b;--bad-bg:#fee2e2}
*{box-sizing:border-box}
body{font-family:system-ui,sans-serif;margin:0;background:var(--bg);color:var(--ink)}
nav{background:var(--nav);padding:12px 24px}
nav a{color:#fff;margin-right:20px;text-decoration:none;padding:4px 0;border-bottom:2px solid transparent}
nav a:hover,nav a:focus-visible{border-bottom-color:#fff;outline:none}
nav a[aria-current=page]{border-bottom-color:#60a5fa;font-weight:600}
main{padding:24px;max-width:1100px;margin:0 auto}
h1{margin-top:0}
.cards{display:flex;gap:16px;margin-bottom:24px;flex-wrap:wrap}
.card{background:var(--surface);padding:16px;border-radius:8px;flex:1;min-width:180px;color:var(--muted)}
.card b{display:block;font-size:28px;color:var(--ink);font-variant-numeric:tabular-nums}
table{width:100%;background:var(--surface);border-collapse:collapse;border-radius:8px;overflow:hidden}
th,td{padding:10px;text-align:left;border-bottom:1px solid var(--line)}
th{font-size:13px;color:var(--muted);font-weight:600}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
.badge{display:inline-block;padding:2px 8px;border-radius:999px;font-size:13px;font-weight:600}
.badge.ok{background:var(--ok-bg);color:var(--ok)}
.badge.warn{background:var(--warn-bg);color:var(--warn)}
.badge.done{background:#e5e7eb;color:#374151}
button{padding:8px 16px;background:var(--accent);color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer;min-height:40px}
button:hover{background:var(--accent-d)}
button.small{padding:4px 12px;min-height:32px;background:#fff;color:var(--accent);border:1px solid var(--accent)}
button.small:hover{background:#eff6ff}
:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}
form{background:var(--surface);padding:16px;border-radius:8px;display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end}
label{display:flex;flex-direction:column;gap:4px;font-size:13px;color:var(--muted)}
input,select{font:inherit;padding:8px;border:1px solid #9ca3af;border-radius:4px;min-height:40px;min-width:200px;color:var(--ink);background:#fff}
#empty{background:var(--surface);padding:16px;border-radius:8px;color:var(--muted)}
#err,#formerr{background:var(--bad-bg);color:var(--bad);padding:10px 14px;border-radius:6px}
#formerr{flex-basis:100%;margin:0}
@media (max-width:600px){main{padding:16px}input,select{min-width:0;width:100%}label{flex:1 1 100%}}
</style></head><body>
<nav aria-label="Main">
<a href="#" aria-current="page">Front Desk</a><a href="#">Passes</a><a href="#">Members</a><a href="#">Settings</a>
</nav>
<main>
<h1>Front Desk</h1>
<div class="cards">
<div class="card">Checked in today<b id="s-in">0</b></div>
<div class="card">Sales today<b id="s-rev">$0</b></div>
<div class="card">Shoes out now<b id="s-shoes">0</b></div>
</div>

<h2>Today's Activity</h2>
<table id="tbl" hidden>
<thead><tr><th>Name</th><th>Item</th><th>Status</th><th>Time</th><th class="num">Price</th><th><span style="position:absolute;left:-9999px">Action</span></th></tr></thead>
<tbody id="rows"></tbody>
</table>
<p id="empty">No check-ins yet today.</p>
<p id="err" role="alert" hidden>Couldn't save to this browser. Entries will be lost if the page is reloaded.</p>

<h2>Add New</h2>
<form id="f" novalidate>
<label>Name<input id="name" autocomplete="off" placeholder="Enter name" required></label>
<label>Item
<select id="item">
<option>Member check-in</option>
<option>Day pass</option>
<option>Shoe rental</option>
<option>Day pass + shoe rental</option>
</select></label>
<button type="submit">Submit</button>
<p id="formerr" role="alert" hidden>Enter a name first.</p>
</form>
</main>
<script>
// Prices in dollars. Update these to match the gym's actual rates.
const PRICES={"Member check-in":0,"Day pass":20,"Shoe rental":6,"Day pass + shoe rental":26};
const KEY="frontdesk-"+new Date().toDateString();
const $=id=>document.getElementById(id);
const hasShoes=e=>e.item.includes("Shoe");
let entries=[];
try{entries=JSON.parse(localStorage.getItem(KEY)||"[]")}catch(_){$("err").hidden=false}

function save(){try{localStorage.setItem(KEY,JSON.stringify(entries));$("err").hidden=true}catch(_){$("err").hidden=false}}
const money=n=>"$"+n.toLocaleString();
const time=t=>new Date(t).toLocaleTimeString([],{hour:"numeric",minute:"2-digit"});

function render(){
  const rows=$("rows");rows.textContent="";
  [...entries].reverse().forEach(e=>{
    const tr=rows.insertRow();
    tr.insertCell().textContent=e.name;
    tr.insertCell().textContent=e.item;
    const st=tr.insertCell(),b=document.createElement("span");
    const out=hasShoes(e)&&!e.returned;
    b.className="badge "+(out?"warn":hasShoes(e)?"done":"ok");
    b.textContent=out?"Shoes out":hasShoes(e)?"Shoes returned":"Checked in";
    st.append(b);
    tr.insertCell().textContent=time(e.t);
    const p=tr.insertCell();p.className="num";p.textContent=money(PRICES[e.item]);
    const a=tr.insertCell();
    if(out){const r=document.createElement("button");r.className="small";r.textContent="Return shoes";
      r.setAttribute("aria-label","Return shoes for "+e.name);
      r.onclick=()=>{e.returned=true;save();render()};a.append(r)}
  });
  $("tbl").hidden=!entries.length;$("empty").hidden=!!entries.length;
  $("s-in").textContent=entries.length;
  $("s-rev").textContent=money(entries.reduce((s,e)=>s+PRICES[e.item],0));
  $("s-shoes").textContent=entries.filter(e=>hasShoes(e)&&!e.returned).length;
}

$("f").addEventListener("submit",ev=>{
  ev.preventDefault();
  const name=$("name").value.trim();
  $("formerr").hidden=!!name;
  if(!name){$("name").focus();return}
  entries.push({name,item:$("item").value,t:Date.now()});
  save();render();
  $("name").value="";$("name").focus();
});
render();
</script>
</body></html>
```

Check these before Monday:
- **Prices are placeholders.** The `PRICES` line at the top of the script has made-up numbers ($20 day pass, $6 shoes). Put in your real rates, or Sales today will be wrong.
- **Nav links go nowhere.** Passes, Members and Settings still point to `#`, as in your original, because there are no other pages to link to.
- **Saving is per browser.** The list lives in that one browser on that one machine. If two desk computers are in use, each shows only its own list.
- **Not tested.** I couldn't open the page, so I haven't seen it run. Try adding a day pass and a shoe rental, then press Return shoes.
