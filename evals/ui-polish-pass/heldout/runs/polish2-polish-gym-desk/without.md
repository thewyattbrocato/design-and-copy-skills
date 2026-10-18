I couldn't save the file because the Write tool is disabled in this session, and I have no other way to create files. I haven't run or tested the page. The full file is below, so you can save it as `index.html` and open it in a browser.

I kept your structure: the nav, the three stat cards, the activity table, the empty and error messages, and the add form. I changed what each part does so it fits the front desk. The dataviz skill didn't apply because the page has no charts, only stat tiles.

**What changed**
- **Cards:** they now show *In the gym now*, *Today's sales* and *Shoes out*, calculated from the entries.
- **Form:** it takes a name and a type (member check-in, day pass or shoe rental). It shows the price and adds a row to the table.
- **Table:**
  - Each row has a *Check out* or *Return* button, which updates the cards.
  - It shows the latest 50 entries.
  - The "No data available." message appears when the list is empty.
- **Error message:** it appears if the browser can't save.
- **Nav:** I replaced Items, Users and Settings with Dashboard, Check-ins, Day passes and Shoe rentals. Those filter the table, so no link is dead.
- **Accessibility:** the layout works on a narrower screen, keyboard focus is visible, and the error message is announced to screen readers.

Before Monday, check two things:
1. **Prices are placeholders:** day pass $22 and shoes $6. Change them in the `TYPES` object at the top of the script.
2. **Data lives in that one browser (`localStorage`):** it isn't shared between desk computers and is lost if the browser data is cleared. If you need a shared record, that needs a backend.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Front Desk</title>
<style>
:root{--ink:#222;--muted:#6b7280;--blue:#2563eb;--blue-d:#1d4ed8}
*{box-sizing:border-box}
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:var(--ink)}
nav{background:#1f2937;padding:0 24px;display:flex;gap:4px}
nav a{color:#d1d5db;padding:14px 12px;text-decoration:none;border-bottom:3px solid transparent}
nav a:hover{color:#fff}
nav a[aria-current="page"]{color:#fff;border-bottom-color:#60a5fa}
nav a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}
main{padding:24px;max-width:1100px;margin:0 auto}
h1{margin:0 0 4px}.sub{color:var(--muted);margin:0 0 20px}
h2{margin:28px 0 12px}
.cards{display:flex;gap:16px;margin-bottom:8px;flex-wrap:wrap}
.card{background:#fff;padding:16px;border-radius:8px;flex:1;min-width:180px;color:var(--muted)}
.card b{display:block;font-size:28px;color:var(--ink);font-variant-numeric:tabular-nums}
.panel{background:#fff;border-radius:8px;padding:16px}
table{width:100%;background:#fff;border-collapse:collapse;border-radius:8px;overflow:hidden}
th,td{padding:10px;text-align:left;border-bottom:1px solid #eee}
th{font-size:13px;color:var(--muted);font-weight:600}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
.badge{display:inline-block;padding:2px 10px;border-radius:99px;font-size:13px;font-weight:600}
.in{background:#dcfce7;color:#166534}.out{background:#fef3c7;color:#92400e}
.done{background:#e5e7eb;color:#374151}
form{display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end}
label{display:flex;flex-direction:column;font-size:13px;color:var(--muted);gap:4px}
input,select{padding:9px 10px;border:1px solid #d1d5db;border-radius:4px;font:inherit;color:var(--ink);background:#fff;min-width:200px}
button{padding:9px 16px;background:var(--blue);color:#fff;border:0;border-radius:4px;font:inherit;font-weight:600;cursor:pointer}
button:hover{background:var(--blue-d)}
button.ghost{background:#fff;color:var(--blue);border:1px solid var(--blue);padding:5px 12px;font-size:14px}
button.ghost:hover{background:#eff6ff}
#empty,#err{padding:16px;border-radius:8px;margin:12px 0}
#empty{background:#fff;color:var(--muted);text-align:center}
#err{background:#fee2e2;color:#991b1b}
.total{margin-left:auto;align-self:center;font-size:18px;font-variant-numeric:tabular-nums}
</style></head><body>
<nav aria-label="Views">
<a href="#all" data-f="all">Dashboard</a>
<a href="#in" data-f="in">Check-ins</a>
<a href="#pass" data-f="pass">Day passes</a>
<a href="#shoes" data-f="shoes">Shoe rentals</a>
</nav>
<main>
<h1>Front Desk</h1>
<p class="sub" id="today"></p>
<div class="cards">
<div class="card">In the gym now<b id="c-in">0</b></div>
<div class="card">Today's sales<b id="c-rev">$0.00</b></div>
<div class="card">Shoes out<b id="c-shoes">0</b></div>
</div>

<h2>New entry</h2>
<div class="panel">
<form id="form">
<label>Name<input id="name" placeholder="Enter name" autocomplete="off" required></label>
<label>Type<select id="type"></select></label>
<span class="total" id="price" aria-live="polite"></span>
<button type="submit">Submit</button>
</form>
</div>

<h2 id="h-act">Recent Activity</h2>
<p id="err" role="alert" hidden>An error occurred. Please try again.</p>
<table id="tbl"><thead><tr><th>Name</th><th>Item</th><th>Status</th><th>Time</th><th class="num">Price</th><th><span style="position:absolute;left:-9999px">Action</span></th></tr></thead>
<tbody id="rows"></tbody></table>
<p id="empty" hidden>No data available.</p>
</main>
<script>
// Edit prices here (dollars).
const TYPES={
  checkin:{label:'Member check-in',price:0,open:'In',close:'Left',btn:'Check out'},
  pass:{label:'Day pass',price:22,open:'In',close:'Left',btn:'Check out'},
  shoes:{label:'Shoe rental',price:6,open:'Out',close:'Returned',btn:'Return'}
};
const FILTERS={all:null,in:'checkin',pass:'pass',shoes:'shoes'};
const KEY='frontdesk-v1';
const $=id=>document.getElementById(id);
const money=n=>'$'+n.toFixed(2);
const dayKey=d=>new Date(d).toDateString();
let entries=[],filter='all';

function load(){
  try{entries=JSON.parse(localStorage.getItem(KEY)||'[]');$('err').hidden=true}
  catch(e){entries=[];$('err').hidden=false}
}
function save(){
  try{localStorage.setItem(KEY,JSON.stringify(entries));$('err').hidden=true}
  catch(e){$('err').hidden=false}
}

function render(){
  const today=entries.filter(e=>dayKey(e.t)===dayKey(Date.now()));
  $('c-in').textContent=today.filter(e=>e.type!=='shoes'&&!e.done).length;
  $('c-shoes').textContent=today.filter(e=>e.type==='shoes'&&!e.done).length;
  $('c-rev').textContent=money(today.reduce((s,e)=>s+e.price,0));

  const t=FILTERS[filter];
  const list=entries.filter(e=>!t||e.type===t).slice().reverse().slice(0,50);
  const body=$('rows');body.textContent='';
  list.forEach(e=>{
    const T=TYPES[e.type],tr=document.createElement('tr');
    const cell=(txt,cls)=>{const td=document.createElement('td');td.textContent=txt;if(cls)td.className=cls;tr.appendChild(td);return td};
    cell(e.name);cell(T.label);
    const st=cell('');const b=document.createElement('span');
    b.className='badge '+(e.done?'done':e.type==='shoes'?'out':'in');
    b.textContent=e.done?T.close:T.open;st.appendChild(b);
    cell(new Date(e.t).toLocaleString([], {month:'short',day:'numeric',hour:'numeric',minute:'2-digit'}));
    cell(money(e.price),'num');
    const act=cell('');
    if(!e.done){
      const btn=document.createElement('button');btn.className='ghost';btn.textContent=T.btn;
      btn.setAttribute('aria-label',T.btn+' '+e.name);
      btn.onclick=()=>{e.done=true;save();render()};act.appendChild(btn);
    }
    body.appendChild(tr);
  });
  $('tbl').hidden=!list.length;
  $('empty').hidden=!!list.length;
  document.querySelectorAll('nav a').forEach(a=>{
    if(a.dataset.f===filter)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');
  });
  $('h-act').textContent=filter==='all'?'Recent Activity':document.querySelector('nav a[aria-current]').textContent;
}

function route(){
  const h=location.hash.slice(1);filter=h in FILTERS?h:'all';render();
}

const sel=$('type');
Object.entries(TYPES).forEach(([k,v])=>{const o=document.createElement('option');o.value=k;o.textContent=v.label;sel.appendChild(o)});
const showPrice=()=>{$('price').textContent=money(TYPES[sel.value].price)};
sel.onchange=showPrice;showPrice();

$('form').onsubmit=ev=>{
  ev.preventDefault();
  const name=$('name').value.trim();
  if(!name){$('name').focus();return}
  const type=sel.value;
  entries.push({name,type,price:TYPES[type].price,t:Date.now(),done:false});
  save();$('name').value='';$('name').focus();render();
};

$('today').textContent=new Date().toLocaleDateString([], {weekday:'long',month:'long',day:'numeric'});
window.addEventListener('hashchange',route);
load();route();
</script>
</body></html>
```

If you re-enable file writing, I can save it and open it to check it in a browser. I'd also adjust the items and prices to match what you actually sell, such as punch cards, memberships or chalk.
