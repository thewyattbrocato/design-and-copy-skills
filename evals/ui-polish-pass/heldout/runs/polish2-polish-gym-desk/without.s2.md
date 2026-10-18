I couldn't save the file: the Write tool is disabled in this session, so nothing has been written to disk. Here's the finished page in full. Paste it into `index.html` and it will run as is.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Front Desk</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px}nav a{color:#fff;margin-right:20px;text-decoration:none}
nav a:hover,nav a:focus-visible{text-decoration:underline}
main{padding:24px;max-width:1100px;margin:0 auto}.cards{display:flex;gap:16px;margin-bottom:24px;flex-wrap:wrap}
.card{background:#fff;padding:16px;border-radius:8px;flex:1;min-width:180px;box-shadow:0 1px 2px rgba(0,0,0,.06)}.card b{display:block;font-size:28px}
table{width:100%;background:#fff;border-collapse:collapse;border-radius:8px;overflow:hidden}th,td{padding:10px;text-align:left;border-bottom:1px solid #eee}
th{background:#fafafa;font-size:13px;color:#555}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button:hover{background:#1d4ed8}
button.small{padding:4px 10px;font-size:13px;background:#fff;color:#2563eb;border:1px solid #2563eb}
button.small:hover{background:#eff6ff}
:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}
form{background:#fff;padding:16px;border-radius:8px;display:flex;gap:16px;flex-wrap:wrap;align-items:flex-end}
label{display:flex;flex-direction:column;font-size:13px;color:#555;gap:4px}
input[type=text],select{padding:8px;border:1px solid #ccc;border-radius:4px;font:inherit;min-width:200px}
label.check{flex-direction:row;align-items:center;gap:8px;font-size:15px;color:#222;padding-bottom:8px}
.badge{padding:2px 8px;border-radius:99px;font-size:13px;background:#e5e7eb}
.badge.out{background:#fef3c7;color:#92400e}.badge.in{background:#dcfce7;color:#166534}
#empty{color:#666}#err{background:#fee2e2;color:#991b1b;padding:10px;border-radius:4px}
#total{margin:12px 0 0;font-weight:600}
</style></head><body>
<nav><a href="#top">Dashboard</a><a href="#activity">Today's Activity</a><a href="#checkin">Check In</a></nav>
<main id="top">
<h1>Front Desk</h1>
<div class="cards">
<div class="card">Checked in today<b id="c-in">0</b></div>
<div class="card">Today's sales<b id="c-rev">$0</b></div>
<div class="card">Rental shoes out<b id="c-shoes">0</b></div>
</div>
<h2 id="activity">Today's Activity</h2>
<table id="tbl" hidden><thead><tr><th>Name</th><th>Item</th><th>Status</th><th>Time</th><th>Paid</th><th></th></tr></thead>
<tbody id="rows"></tbody></table>
<p id="empty">No check-ins yet today.</p>
<p id="err" role="alert" hidden>Something went wrong saving that. Please try again.</p>
<h2 id="checkin">Check In</h2>
<form id="f">
<label>Guest name<input type="text" id="name" required autocomplete="off" placeholder="First and last name"></label>
<label>Entry<select id="entry">
<option value="day">Day pass</option>
<option value="member">Member (already paid)</option>
</select></label>
<label class="check"><input type="checkbox" id="shoes"> Rent shoes</label>
<button type="submit">Check in</button>
</form>
<p id="total" aria-live="polite"></p>
</main>
<script>
// Prices in dollars. Change these to match the gym.
var PRICES={day:20,shoes:5};
var KEY='frontdesk.checkins';
var $=function(id){return document.getElementById(id)};
var money=function(n){return '$'+n.toLocaleString()};
var load=function(){try{return JSON.parse(localStorage.getItem(KEY))||[]}catch(e){return []}};
var save=function(d){localStorage.setItem(KEY,JSON.stringify(d))};
var sameDay=function(t){return new Date(t).toDateString()===new Date().toDateString()};
var data;
function status(e){return e.shoes&&!e.returned?'out':'in'}
function render(){
  var today=data.filter(function(e){return sameDay(e.t)});
  var tb=$('rows');tb.textContent='';
  today.slice().reverse().forEach(function(e){
    var tr=document.createElement('tr'),s=status(e);
    var cells=[e.name,(e.entry==='day'?'Day pass':'Member')+(e.shoes?' + shoes':'')];
    cells.forEach(function(v){var td=document.createElement('td');td.textContent=v;tr.appendChild(td)});
    var st=document.createElement('td'),b=document.createElement('span');
    b.className='badge '+s;b.textContent=s==='out'?'Shoes out':'Checked in';st.appendChild(b);tr.appendChild(st);
    var tm=document.createElement('td');tm.textContent=new Date(e.t).toLocaleTimeString([],{hour:'numeric',minute:'2-digit'});tr.appendChild(tm);
    var pd=document.createElement('td');pd.textContent=money(e.paid);tr.appendChild(pd);
    var ac=document.createElement('td');
    if(s==='out'){var btn=document.createElement('button');btn.className='small';btn.textContent='Shoes returned';
      btn.setAttribute('aria-label','Mark shoes returned for '+e.name);
      btn.onclick=function(){e.returned=true;persist()};ac.appendChild(btn)}
    tr.appendChild(ac);tb.appendChild(tr);
  });
  $('tbl').hidden=!today.length;$('empty').hidden=!!today.length;
  $('c-in').textContent=today.length;
  $('c-rev').textContent=money(today.reduce(function(a,e){return a+e.paid},0));
  $('c-shoes').textContent=data.filter(function(e){return status(e)==='out'}).length;
}
function persist(){
  try{save(data);$('err').hidden=true}catch(e){$('err').hidden=false}
  render();
}
function total(){
  var t=($('entry').value==='day'?PRICES.day:0)+($('shoes').checked?PRICES.shoes:0);
  $('total').textContent='Amount due: '+money(t);return t;
}
$('entry').onchange=$('shoes').onchange=total;
$('f').onsubmit=function(ev){
  ev.preventDefault();
  var name=$('name').value.trim();if(!name)return;
  var due=total();
  data.push({name:name,entry:$('entry').value,shoes:$('shoes').checked,paid:due,t:Date.now()});
  persist();
  $('f').reset();total();$('name').focus();
};
data=load();render();total();
</script>
</body></html>
```

I kept your layout, nav bar, cards, table and form, and filled in the parts that were placeholders:

- **Cards:** "Total Users / Revenue / Active Items" are now "Checked in today", "Today's sales" and "Rental shoes out". They update on their own.
- **Check-in form:** it has a name field, Day pass or Member, and a "Rent shoes" checkbox. It shows the amount due and logs the check-in.
- **Activity table:** the fake John and Jane rows are gone. It shows today's check-ins with the newest first. Rows with shoes out get a "Shoes returned" button.
- **Empty and error messages:** "No check-ins yet today" appears when the table is empty. The error message appears if saving fails.
- **Nav:** the four dead links are now three links that jump to sections of the page.
- **Polish:** form labels, keyboard focus outlines, and a layout that wraps on narrow screens.

Before Monday, check these:

1. **Prices are guesses.** I used $20 for a day pass and $5 for shoes. Change `PRICES` at the top of the script.
2. **Data is stored only in that browser.** It uses `localStorage`, so it survives refreshes but isn't shared between computers. It also disappears if someone clears the browser data. If you have more than one desk, or you need real records, it needs a backend. I can add one if you want.
3. **It doesn't take payments.** It records the amount due and doesn't charge anything.
4. **Members aren't looked up.** "Member" is just a choice in the dropdown. It doesn't check a membership list.
5. **I haven't opened it in a browser.** Please do a test check-in and a shoe return before the weekend.
