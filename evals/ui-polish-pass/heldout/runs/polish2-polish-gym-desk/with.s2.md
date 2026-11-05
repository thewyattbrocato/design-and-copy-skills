I couldn't save the file because the Write tool is disabled in this session. The full updated page is below, so you can paste it over your current file. I haven't opened it in a browser.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Front desk – Dashboard</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px;display:flex;flex-wrap:wrap;gap:4px 20px}nav a{color:#fff;text-decoration:none;padding:4px 0}
nav a:hover{text-decoration:underline}nav a[aria-current=page]{font-weight:600;border-bottom:2px solid #fff}
main{padding:24px}.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 180px}.card b{display:block;font-size:28px}
.tablewrap{overflow-x:auto}
table{width:100%;background:#fff;border-collapse:collapse}th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
caption{text-align:left;position:absolute;left:-9999px}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button:disabled{background:#6b7280;cursor:progress}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
nav a:focus-visible{outline-color:#fff}
.skip{position:absolute;left:-9999px;background:#fff;padding:8px;z-index:1}.skip:focus{left:8px;top:8px}
form{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start}
.field{display:flex;flex-direction:column;gap:4px;flex:1 1 200px}
input{padding:8px;border:1px solid #6b7280;border-radius:4px;font:inherit;min-width:0}
input[aria-invalid=true]{border-color:#b91c1c}
.fe{color:#b91c1c;font-size:14px;margin:0}
#err{background:#fef2f2;border:1px solid #b91c1c;color:#7f1d1d;padding:12px;border-radius:4px;margin-bottom:12px}
#msg{margin:12px 0 0;color:#166534;min-height:1.2em}
#empty{background:#fff;padding:16px;border-radius:8px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style></head><body>
<a class="skip" href="#main">Skip to content</a>
<nav aria-label="Main"><a href="#" aria-current="page">Dashboard</a><a href="#">Items</a><a href="#">Users</a><a href="#">Settings</a></nav>
<main id="main">
<h1>Front desk</h1>
<div class="cards">
<div class="card">Total Users<b>1,234</b></div>
<div class="card">Revenue<b>$12,345</b></div>
<div class="card">Active Items<b>56</b></div>
</div>
<h2>Recent Activity</h2>
<div id="err" role="alert" hidden>Couldn't save that entry, so it was not added. What you typed is still in the form below. <button type="button" id="retry">Try again</button></div>
<div class="tablewrap">
<table id="tbl"><caption>Recent activity</caption>
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody id="rows">
<tr><td>John Doe</td><td>Item 1</td><td>Active</td><td>01/01/2024</td></tr>
<tr><td>Jane Smith</td><td>Item 2</td><td>Pending</td><td>01/02/2024</td></tr>
</tbody></table>
</div>
<p id="empty" hidden>No activity yet. Add the first entry below.</p>
<h2>Add New</h2>
<form id="f" novalidate>
<div class="field"><label for="name">Name</label><input id="name" autocomplete="off" placeholder="Enter name" aria-describedby="nameErr"><p class="fe" id="nameErr" hidden>Enter a name.</p></div>
<div class="field"><label for="val">Value</label><input id="val" autocomplete="off" placeholder="Enter value" aria-describedby="valErr"><p class="fe" id="valErr" hidden>Enter a value.</p></div>
<button type="submit" id="go" style="align-self:flex-end">Submit</button>
</form>
<p id="msg" role="status"></p>
</main>
<script>
const $=id=>document.getElementById(id),f=$('f'),rows=$('rows'),go=$('go');
function sync(){const none=!rows.children.length;$('empty').hidden=!none;$('tbl').hidden=none}
function bad(el,errEl,on){el.setAttribute('aria-invalid',on);errEl.hidden=!on}
// Replace with a real request (fetch) when the backend exists; it should reject on failure.
async function save(entry){return entry}
async function submit(){
  $('err').hidden=true;$('msg').textContent='';
  const n=$('name'),v=$('val'),nv=n.value.trim(),vv=v.value.trim();
  bad(n,$('nameErr'),!nv);bad(v,$('valErr'),!vv);
  if(!nv||!vv){(!nv?n:v).focus();return}
  go.disabled=true;go.textContent='Saving…';
  try{
    await save({nv,vv});
    const tr=rows.insertRow(0),d=new Date();
    [nv,vv,'Active',d.toLocaleDateString('en-US',{month:'2-digit',day:'2-digit',year:'numeric'})].forEach(t=>tr.insertCell().textContent=t);
    f.reset();sync();$('msg').textContent='Added '+nv+'.';n.focus();
  }catch(e){$('err').hidden=false;$('retry').focus()}
  finally{go.disabled=false;go.textContent='Submit'}
}
f.addEventListener('submit',e=>{e.preventDefault();submit()});
$('retry').addEventListener('click',submit);
sync();
</script>
</body></html>
```

I kept your layout, colors and fields. This is what I added:
- **Form:**
  - Every input has a real label.
  - Empty fields show an inline error and focus goes to the first one.
  - Submit shows "Saving…" and is disabled while it runs, so a double-click can't add an entry twice.
  - A confirmation line says what was added.
  - On failure, the error banner has a Try again button and keeps what was typed.
- **Table:** it has a header row and caption. It scrolls sideways on narrow screens and wraps long names. When it has no rows, it's replaced by the "No activity yet" message.
- **Page:** I added a skip link, a viewport tag, a real title and an h1, and the Dashboard link is marked as the current page. Focus rings show on every control, and the nav and cards wrap on small screens.

**Needs your input before Monday:**
- **Sample data:** the cards (1,234 users, $12,345 revenue, 56 items) and the two table rows are still your placeholders. I didn't relabel them because I don't know your real numbers. Please don't show them to customers as they are.
- **Saving:** there's no backend yet. Submit only adds a row in the browser, and a refresh loses it. The `save()` function is the one place to put your real request.
- **Labels:** "Item 1", "Value" and the nav names are still generic. Tell me the real ones (day pass, shoe rental, check-in, prices) and I'll swap them in.

I haven't tried it with a screen reader or on a phone.
