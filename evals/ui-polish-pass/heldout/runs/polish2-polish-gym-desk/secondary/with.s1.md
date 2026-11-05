The skill's reference files cover more than this screen needs, so I've applied the relevant checks directly. The page is a single HTML file, so I'm returning the full file.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Front desk</title>
<style>
[hidden]{display:none!important}
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
.skip{position:absolute;left:-9999px}
.skip:focus{left:12px;top:12px;background:#fff;color:#222;padding:8px 12px;border-radius:4px;z-index:1}
nav{background:#1f2937;padding:12px 24px;display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center}
nav a{color:#fff;text-decoration:none;padding:4px 2px}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}
main{padding:24px;max-width:1100px}
h1{margin-top:0}
.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 200px}
.card b{display:block;font-size:28px;margin-top:4px}
.table-wrap{overflow-x:auto;background:#fff;border-radius:8px}
table{width:100%;background:#fff;border-collapse:collapse}
th,td{padding:10px;text-align:left;border-bottom:1px solid #eee}
th{font-weight:600}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button:hover:not(:disabled){background:#1d4ed8}
button:disabled{background:#9ca3af;cursor:not-allowed}
input{padding:8px 10px;border:1px solid #6b7280;border-radius:4px;font:inherit;background:#fff;min-width:0}
input[aria-invalid="true"]{border-color:#b91c1c}
.form{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end;background:#fff;padding:16px;border-radius:8px}
.field{display:flex;flex-direction:column;gap:4px;flex:1 1 200px}
.field-error{color:#b91c1c;font-size:14px}
.msg{margin:12px 0}
.msg.err{color:#b91c1c;font-weight:600}
.msg.ok{color:#166534;font-weight:600}
</style></head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav aria-label="Main">
<a href="#" aria-current="page">Dashboard</a><a href="#">Check-in</a><a href="#">Day passes</a><a href="#">Shoe rental</a><a href="#">Settings</a>
</nav>
<main id="main" tabindex="-1">
<h1>Front desk</h1>
<div class="cards">
<div class="card">Checked in today<b>—</b></div>
<div class="card">Day passes sold<b>—</b></div>
<div class="card">Shoes out on rental<b>—</b></div>
</div>

<h2 id="recent-h">Recent activity</h2>
<div class="table-wrap" id="table-wrap">
<table aria-labelledby="recent-h">
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody id="activity">
<tr><td>John Doe</td><td>Item 1</td><td>Active</td><td>01/01/2024</td></tr>
<tr><td>Jane Smith</td><td>Item 2</td><td>Pending</td><td>01/02/2024</td></tr>
</tbody>
</table>
</div>
<p id="empty" class="msg" hidden>No activity yet. New check-ins, day passes and shoe rentals will appear here.</p>

<h2 id="add-h">Add new</h2>
<form id="add" class="form" aria-labelledby="add-h" novalidate>
<div class="field">
<label for="f-name">Name</label>
<input id="f-name" name="name" autocomplete="off" required aria-describedby="name-err">
<span id="name-err" class="field-error" hidden>Enter a name to continue.</span>
</div>
<div class="field">
<label for="f-value">Value</label>
<input id="f-value" name="value" autocomplete="off">
</div>
<button type="submit" id="submit">Save entry</button>
</form>
<p id="ok" class="msg ok" role="status" hidden></p>
<p id="err" class="msg err" role="alert" hidden>Couldn't save this entry. Your name and value are still filled in. Try again, or ask a supervisor if it keeps failing.</p>
</main>
<script>
(function(){
  var form=document.getElementById('add'),
      nameIn=document.getElementById('f-name'),
      valueIn=document.getElementById('f-value'),
      btn=document.getElementById('submit'),
      nameErr=document.getElementById('name-err'),
      err=document.getElementById('err'),
      ok=document.getElementById('ok'),
      tbody=document.getElementById('activity'),
      empty=document.getElementById('empty'),
      wrap=document.getElementById('table-wrap');

  function syncEmpty(){
    var none=tbody.rows.length===0;
    empty.hidden=!none;
    wrap.hidden=none;
  }
  function cell(row,text){
    var td=document.createElement('td');
    td.textContent=text;
    row.appendChild(td);
  }
  function today(){
    return new Date().toLocaleDateString('en-US',{month:'2-digit',day:'2-digit',year:'numeric'});
  }

  syncEmpty();

  form.addEventListener('submit', async function(e){
    e.preventDefault();
    err.hidden=true; ok.hidden=true;

    var name=nameIn.value.trim(), value=valueIn.value.trim();
    if(!name){
      nameErr.hidden=false;
      nameIn.setAttribute('aria-invalid','true');
      nameIn.focus();
      return;
    }
    nameErr.hidden=true;
    nameIn.removeAttribute('aria-invalid');

    // Saving is wired to window.submitEntry({name, value}), which must return a promise.
    // Until that is connected, saves show the error message instead of pretending to succeed.
    if(typeof window.submitEntry!=='function'){
      err.hidden=false;
      return;
    }

    btn.disabled=true; btn.textContent='Saving…';
    form.setAttribute('aria-busy','true');
    try{
      await window.submitEntry({name:name, value:value});
      var row=document.createElement('tr');
      cell(row,name); cell(row,value); cell(row,'Active'); cell(row,today());
      tbody.appendChild(row);
      nameIn.value=''; valueIn.value='';
      syncEmpty();
      ok.textContent='Saved '+name+'.';
      ok.hidden=false;
      nameIn.focus();
    }catch(_){
      err.hidden=false;
    }finally{
      btn.disabled=false; btn.textContent='Save entry';
      form.removeAttribute('aria-busy');
    }
  });
})();
</script>
</body></html>
```

**What changed**
- **Save flow:** labelled fields, required-name validation with an inline message beside the field, a busy state that blocks double-submit, a visible success line, and a failure message that keeps what was typed. Saved rows are added with text content, not HTML.
- **Empty state:** the "No activity yet" message now shows when the table has no rows, and the table hides.
- **Access:** skip link, `lang`, meaningful title and h1, `scope` on headers, named table and form, visible focus rings, and the "Dashboard" link marked as current.
- **Responsive:** nav and cards wrap, the table scrolls sideways on small screens, and the form stacks.
- **Copy:** "Users", "Revenue" and "Items" are replaced with terms from your three jobs (check-in, day passes, shoe rental).

**Needs your input before Monday**
- The stat cards show "—". The old numbers were placeholders, so I removed them rather than let staff see fake figures. Wire them to real counts.
- Until `window.submitEntry` is defined, every save shows the error. This is deliberate so nothing looks saved when it isn't. Connect it to your check-in system.
- Nav links are still `href="#"`, and "Value" is kept as the field name. Tell me the real routes and what the value field should hold and I'll fix both.

Not checked: I did not test with a screen reader, on a real device, or in a browser.
