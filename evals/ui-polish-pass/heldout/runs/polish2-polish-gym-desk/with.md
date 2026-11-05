Here's the finished file. I kept the look, layout, colors and section order, and changed the wording and behavior that were generic or missing.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Front desk – Dashboard</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px;display:flex;flex-wrap:wrap;gap:4px 20px}
nav a{color:#fff;text-decoration:none;padding:4px 0}
nav a[aria-current="page"]{text-decoration:underline;text-underline-offset:6px}
main{padding:24px}
.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 160px}.card b{display:block;font-size:28px}
.table-wrap{overflow-x:auto}
table{width:100%;background:#fff;border-collapse:collapse}
th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
caption{text-align:left;position:absolute;left:-9999px}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button.small{padding:4px 10px}
button.link{background:none;color:#1d4ed8;text-decoration:underline;padding:4px}
button[aria-disabled="true"]{background:#6b7280;cursor:progress}
input,select{padding:8px;border:1px solid #6b7280;border-radius:4px;font:inherit;background:#fff;color:inherit;max-width:100%}
label{display:block;font-size:14px;margin-bottom:4px}
.field{display:inline-block;vertical-align:top;margin:0 8px 8px 0}
.field-err{color:#b91c1c;font-size:14px;margin:4px 0 0}
input[aria-invalid="true"]{border-color:#b91c1c}
#err{color:#b91c1c;margin:8px 0}
#msg{margin:8px 0;min-height:1.5em}
:focus-visible{outline:3px solid #f59e0b;outline-offset:2px}
nav :focus-visible{outline-color:#fff}
.skip{position:absolute;left:-9999px;background:#fff;padding:8px}
.skip:focus{left:8px;top:8px;z-index:1}
</style></head><body>
<a class="skip" href="#main">Skip to main content</a>
<nav aria-label="Main"><a href="#" aria-current="page">Dashboard</a><a href="#">Items</a><a href="#">Users</a><a href="#">Settings</a></nav>
<main id="main">
<h1>Front desk</h1>
<div class="cards">
<div class="card">Checked in today<b id="c-in">0</b></div>
<div class="card">Day passes sold today<b id="c-pass">0</b></div>
<div class="card">Shoes out now<b id="c-shoes">0</b></div>
</div>
<h2>Recent Activity</h2>
<div class="table-wrap">
<table><caption>Recent desk activity, newest first</caption>
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody id="rows"></tbody></table></div>
<p id="empty" hidden>Nothing at the desk yet today. Check someone in, sell a day pass or rent shoes below.</p>
<p id="err" role="alert" hidden>Couldn't save this entry. What you typed is still in the form. <button type="button" class="link" id="retry">Try again</button></p>
<p id="msg" role="status"></p>
<h2>Add New</h2>
<form id="f" novalidate>
<div class="field"><label for="name">Name</label>
<input id="name" autocomplete="off" aria-describedby="name-err" required>
<p class="field-err" id="name-err" hidden>Enter the person's name.</p></div>
<div class="field"><label for="kind">What for</label>
<select id="kind"><option>Check-in</option><option>Day pass</option><option>Shoe rental</option></select></div>
<div class="field"><label>&nbsp;</label><button id="go">Submit</button></div>
</form>
</main>
<script>
// Entries are kept in this browser only (localStorage). Swap load()/save() for your backend when there is one.
const KEY='frontdesk-log';
const $=id=>document.getElementById(id);
let log=[];try{log=JSON.parse(localStorage.getItem(KEY))||[]}catch(e){}
let undoTimer,pending=null;
const today=()=>new Date().toLocaleDateString();
function save(){localStorage.setItem(KEY,JSON.stringify(log))}
function render(){
  const t=today(),rows=$('rows');rows.textContent='';
  log.slice().reverse().slice(0,50).forEach(e=>{
    const tr=rows.insertRow();
    tr.insertCell().textContent=e.name;
    tr.insertCell().textContent=e.kind;
    const s=tr.insertCell();
    if(e.kind==='Shoe rental'&&!e.returned){
      s.append('Out ');
      const b=document.createElement('button');b.type='button';b.className='small';
      b.textContent='Mark returned';b.setAttribute('aria-label','Mark shoes returned: '+e.name);
      b.onclick=()=>{e.returned=true;try{save()}catch(x){e.returned=false;$('msg').textContent='Couldn\u2019t save. Try again.';return}render();$('msg').textContent='Shoes returned: '+e.name+'.'};
      s.append(b);
    }else s.textContent=e.kind==='Shoe rental'?'Returned':'Done';
    tr.insertCell().textContent=e.date;
  });
  $('empty').hidden=log.length>0;
  document.querySelector('.table-wrap').hidden=log.length===0;
  const td=log.filter(e=>e.date===t);
  $('c-in').textContent=td.filter(e=>e.kind==='Check-in').length;
  $('c-pass').textContent=td.filter(e=>e.kind==='Day pass').length;
  $('c-shoes').textContent=log.filter(e=>e.kind==='Shoe rental'&&!e.returned).length;
}
function submit(){
  const n=$('name'),name=n.value.trim();
  $('err').hidden=true;
  if(!name){n.setAttribute('aria-invalid','true');$('name-err').hidden=false;n.focus();return}
  n.removeAttribute('aria-invalid');$('name-err').hidden=true;
  const btn=$('go');btn.setAttribute('aria-disabled','true');btn.textContent='Saving…';
  const entry={name,kind:$('kind').value,date:today(),returned:false};
  log.push(entry);
  try{save()}catch(e){
    log.pop();$('err').hidden=false;$('retry').focus();
    btn.removeAttribute('aria-disabled');btn.textContent='Submit';return;
  }
  btn.removeAttribute('aria-disabled');btn.textContent='Submit';
  n.value='';n.focus();render();
  const m=$('msg');m.textContent='Added: '+name+', '+entry.kind+'. ';
  const u=document.createElement('button');u.type='button';u.className='link';u.textContent='Undo';
  u.onclick=()=>{log=log.filter(x=>x!==entry);try{save()}catch(x){}render();m.textContent='Removed: '+name+'.';clearTimeout(undoTimer)};
  m.append(u);clearTimeout(undoTimer);undoTimer=setTimeout(()=>{m.textContent=''},8000);
}
$('f').addEventListener('submit',e=>{e.preventDefault();if($('go').getAttribute('aria-disabled')!=='true')submit()});
$('retry').onclick=submit;
render();
</script>
</body></html>
```

**What changed**
- **Wording:** the generic "Users / Revenue / Active Items" cards and "Enter value" field are now gym terms. The cards are Checked in today, Day passes sold today and Shoes out now. The form takes a name and a choice of Check-in, Day pass or Shoe rental.
- **Submit:** the form now adds a row, shows a "Saving…" state that blocks double-submits, and confirms in words. The confirmation has an 8-second Undo. A blank name gets an inline error and focus. A failed save keeps what was typed and offers "Try again".
- **Shoes:** rentals show "Out" with a "Mark returned" button, and the button names the person.
- **Empty state:** the table starts empty and explains what to do. The "No data available" and "An error occurred" lines are replaced by specific messages.
- **Access and small screens:**
  - Real labels on the form fields.
  - Visible focus rings.
  - A skip link.
  - Table headers with scope.
  - The current nav item is marked.
  - Darker input borders.
  - Cards wrap and the table scrolls sideways on narrow screens.
  - Long names wrap.

**Decisions for you**
- I removed the John Doe and Jane Smith sample rows, the 1,234 and 56 figures, and the Revenue card. I don't know your prices, and fake numbers on a live desk would mislead. Add Revenue back once you tell me the day-pass and rental prices.
- Entries are saved in the browser on that desk computer only. They don't sync between machines or survive clearing browser data. The `save()` function is where a real backend would go.
- The nav links (Items, Users, Settings) still go nowhere, as in your original.

I haven't run this in a browser or tested it with a screen reader.
