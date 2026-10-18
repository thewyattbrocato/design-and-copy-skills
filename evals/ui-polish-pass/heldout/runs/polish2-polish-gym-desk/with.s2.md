I couldn't save the file because the Write tool is disabled in this session. Here is the finished page. Save it as `index.html`.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Front desk</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px}nav a{color:#fff;margin-right:20px;text-decoration:none;display:inline-block;padding:4px 0}
nav a[aria-current]{border-bottom:2px solid #fff}
main{padding:24px}.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 160px}.card b{display:block;font-size:28px}
.table-wrap{overflow-x:auto}
table{width:100%;background:#fff;border-collapse:collapse}th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
caption{text-align:left;position:absolute;left:-9999px}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
nav a:focus-visible{outline-color:#fff}
form{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start;background:#fff;padding:16px;border-radius:8px}
.field{display:flex;flex-direction:column;gap:4px;flex:1 1 200px}
label{font-size:14px;font-weight:600}
input,select{padding:8px;border:1px solid #6b7280;border-radius:4px;font:inherit;background:#fff;min-width:0}
input[aria-invalid=true]{border-color:#b91c1c;border-width:2px}
.field-err{color:#b91c1c;font-size:14px;margin:0}
form button{align-self:flex-end}
#empty{background:#fff;padding:16px;border-radius:8px}
#err{background:#fef2f2;color:#991b1b;border:1px solid #b91c1c;padding:12px;border-radius:8px}
#ok{color:#166534;font-weight:600;min-height:1.5em}
</style></head><body>
<nav><a href="#" aria-current="page">Dashboard</a><a href="#">Items</a><a href="#">Users</a><a href="#">Settings</a></nav>
<main>
<h1>Front desk</h1>
<div class="cards">
<div class="card">Check-ins today<b id="c-in">0</b></div>
<div class="card">Day passes sold today<b id="c-pass">0</b></div>
<div class="card">Shoes rented today<b id="c-shoe">0</b></div>
</div>
<h2>Recent Activity</h2>
<div class="table-wrap"><table id="tbl" hidden><caption>Recent front desk activity, newest first</caption>
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody id="rows"></tbody>
</table></div>
<p id="empty">Nothing at the desk yet today. Check someone in, sell a day pass or rent shoes below and it will show up here.</p>
<p id="err" role="alert" hidden>That entry wasn't saved on this device. What you entered is still in the form. Press Submit to try again.</p>
<h2>Add New</h2>
<form id="f" novalidate>
<div class="field"><label for="name">Name</label>
<input id="name" autocomplete="off" aria-describedby="name-err">
<p class="field-err" id="name-err" hidden>Enter the customer's name.</p></div>
<div class="field"><label for="item">Item</label>
<select id="item"><option>Check-in</option><option>Day pass</option><option>Shoe rental</option></select></div>
<button type="submit">Submit</button>
</form>
<p id="ok" role="status"></p>
</main>
<script>
var KEY='frontdesk-activity',STATUS={'Check-in':'Checked in','Day pass':'Sold','Shoe rental':'Rented'},SHOW=25;
var $=function(i){return document.getElementById(i)};
var list=[];
try{list=JSON.parse(localStorage.getItem(KEY)||'[]')}catch(e){list=[]}
function sameDay(a,b){return new Date(a).toDateString()===new Date(b).toDateString()}
function render(){
  var now=Date.now(),rows=$('rows');rows.textContent='';
  list.slice(0,SHOW).forEach(function(r){
    var tr=rows.insertRow();
    [r.name,r.item,STATUS[r.item],new Date(r.t).toLocaleString([],{dateStyle:'short',timeStyle:'short'})]
      .forEach(function(v){tr.insertCell().textContent=v});
  });
  $('tbl').hidden=!list.length;$('empty').hidden=!!list.length;
  var today=list.filter(function(r){return sameDay(r.t,now)});
  function n(item){return today.filter(function(r){return r.item===item}).length}
  $('c-in').textContent=n('Check-in');$('c-pass').textContent=n('Day pass');$('c-shoe').textContent=n('Shoe rental');
}
$('f').addEventListener('submit',function(e){
  e.preventDefault();
  var name=$('name').value.trim(),bad=!name;
  $('name-err').hidden=!bad;$('name').setAttribute('aria-invalid',bad);
  $('ok').textContent='';
  if(bad){$('name').focus();return}
  var entry={name:name,item:$('item').value,t:Date.now()},next=[entry].concat(list);
  try{localStorage.setItem(KEY,JSON.stringify(next))}
  catch(x){$('err').hidden=false;return}
  list=next;$('err').hidden=true;render();
  $('ok').textContent='Added '+name+' – '+entry.item+'.';
  $('name').value='';$('name').focus();
});
$('name').addEventListener('input',function(){$('name-err').hidden=true;this.removeAttribute('aria-invalid')});
render();
</script>
</body></html>
```

I kept the layout, colors, nav and table. These are the changes:

- **Placeholder content is gone.** The "John Doe / Item 1" rows, "Total Users 1,234", "Revenue $12,345" and "Active Items 56" were template data.
  - The cards now count today's check-ins, day passes sold and shoes rented from what the desk enters.
  - I dropped Revenue because I have no prices. If you give me the pass and rental prices, I can add it back.
  - The form's "value" box is now an Item dropdown (Check-in, Day pass, Shoe rental), and the Status column is derived from it.
  - The title and heading now say "Front desk".
- **Submit now works.** Before, the button did nothing.
  - An empty name shows an error beside the field and puts focus there.
  - A successful add shows "Added Jane – Day pass.", clears the name and returns focus to it for the next customer.
  - Entries are saved in the browser, so a reload keeps them. If saving fails, the error message appears and the form keeps what was typed.
- **The empty and error messages are used.** The empty message appears until the first entry. The table shows the newest 25 entries.
- **Accessibility and small screens.**
  - Inputs have visible labels.
  - Keyboard focus is visible on every control.
  - The table has a caption and column headers.
  - The current nav page is marked.
  - The cards wrap, long names wrap, and the table scrolls sideways on narrow screens.

I haven't opened this in a browser or tested it with a screen reader.

Two things to decide before Monday:
- **Corrections and returns.** There's no way to remove a mistaken entry or mark shoes as returned. I left both out because they'd be new features.
- **Shared data.** Data is stored per browser, so it won't be shared between two desk machines.
