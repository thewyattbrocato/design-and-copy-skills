I couldn't save this to a file because the Write tool is disabled in this session. Here is the full finished page to paste over your current one. I haven't opened it in a browser.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Front desk</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px}nav a{color:#fff;margin-right:20px;text-decoration:none;display:inline-block;padding:6px 0}
nav a[aria-current]{border-bottom:2px solid #fff;font-weight:600}
main{padding:24px}.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 180px}.card b{display:block;font-size:28px}
.tablewrap{overflow-x:auto}
table{width:100%;background:#fff;border-collapse:collapse}th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
.status::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;background:#15803d}
.status.pending::before{background:#fff;border:2px solid #b45309;box-sizing:border-box}
button{padding:8px 16px;min-height:40px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button:hover{background:#1d4ed8}
button.link{background:none;color:#1d4ed8;text-decoration:underline;padding:4px 8px;min-height:0}
:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
nav :focus-visible{outline-color:#fff}
form{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start}
.field{display:flex;flex-direction:column;gap:4px;min-width:200px}
label{font-size:14px;font-weight:600}
input,select{padding:8px;min-height:40px;box-sizing:border-box;border:1px solid #6b7280;border-radius:4px;font:inherit;background:#fff}
input[aria-invalid=true]{border-color:#b91c1c;border-width:2px}
.msg{color:#b91c1c;font-size:14px;margin:0}
#ok{color:#15803d;font-weight:600;margin:12px 0 0}
#empty,#err{background:#fff;padding:16px;border-radius:8px}
#err{border-left:4px solid #b91c1c}
</style></head><body>
<nav aria-label="Main"><a href="#" aria-current="page">Dashboard</a><a href="#">Items</a><a href="#">Users</a><a href="#">Settings</a></nav>
<main>
<h1>Front desk</h1>
<div class="cards">
<div class="card">Members<b>1,234</b></div>
<div class="card">Revenue<b>$12,345</b></div>
<div class="card">Rental shoes out<b>56</b></div>
</div>
<h2 id="recent">Recent Activity</h2>
<div class="tablewrap" id="tablewrap">
<table aria-labelledby="recent"><thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody id="rows"></tbody></table>
</div>
<div id="empty" hidden>No check-ins, day passes or shoe rentals yet today. Add the first one below.</div>
<div id="err" role="alert" hidden>Couldn't load recent activity. Check the connection, then <button type="button" class="link" id="retry">try again</button>.</div>
<h2>Add New</h2>
<form id="f" novalidate>
<div class="field"><label for="name">Name</label><input id="name" autocomplete="off" aria-describedby="nameErr">
<p class="msg" id="nameErr" hidden>Enter the customer's name.</p></div>
<div class="field"><label for="item">Item</label>
<select id="item"><option>Check-in</option><option>Day pass</option><option>Shoe rental</option></select></div>
<div class="field"><label>&nbsp;</label><button type="submit">Submit</button></div>
</form>
<p id="ok" role="status"></p>
</main>
<script>
// Sample data. Replace with the real source; load() is where a failed fetch should call show("error").
var data=[
{name:"John Doe",item:"Day pass",status:"Active",date:"01/01/2024"},
{name:"Jane Smith",item:"Shoe rental",status:"Pending",date:"01/02/2024"}];
var $=function(id){return document.getElementById(id)};
function show(state){
  $("tablewrap").hidden=state!=="rows";
  $("empty").hidden=state!=="empty";
  $("err").hidden=state!=="error";
}
function render(){
  var tb=$("rows");tb.textContent="";
  data.forEach(function(r){
    var tr=tb.insertRow();
    [r.name,r.item,r.status,r.date].forEach(function(v,i){
      var td=tr.insertCell();
      if(i===2){var s=document.createElement("span");s.className="status "+v.toLowerCase();s.textContent=v;td.appendChild(s)}
      else td.textContent=v;
    });
  });
  show(data.length?"rows":"empty");
}
function load(){render()}
$("retry").onclick=function(){load()};
$("f").onsubmit=function(e){
  e.preventDefault();
  var n=$("name"),v=n.value.trim();
  $("ok").textContent="";
  if(!v){n.setAttribute("aria-invalid","true");$("nameErr").hidden=false;n.focus();return}
  n.removeAttribute("aria-invalid");$("nameErr").hidden=true;
  var d=new Date(),p=function(x){return String(x).padStart(2,"0")};
  data.unshift({name:v,item:$("item").value,status:"Active",date:p(d.getMonth()+1)+"/"+p(d.getDate())+"/"+d.getFullYear()});
  render();
  $("ok").textContent="Added: "+v+", "+$("item").value+".";
  n.value="";n.focus();
};
$("name").oninput=function(){if(this.value.trim()){this.removeAttribute("aria-invalid");$("nameErr").hidden=true}};
load();
</script>
</body></html>
```

I kept your colors, layout and type, and changed these things:

- **Form:**
  - Name and Item now have real labels. Your "Enter value" box became an Item dropdown (Check-in, Day pass, Shoe rental), because that is what the desk actually enters.
  - An empty name shows an error beside the field and puts the cursor back in it.
  - A successful submit adds a row at the top of the table, shows "Added: …" and clears the box ready for the next person.
- **Table and empty/error messages:**
  - The "No data available." and "An error occurred." messages that were hidden in your page now work. The empty message says what to do next. The error message has a "try again" button.
  - Status is shown with a word and a marker, not by color alone.
  - The table scrolls sideways on a narrow screen, and long names wrap.
- **Navigation and focus:**
  - The current page is marked in the nav.
  - Every control has a visible focus ring.
  - Buttons and inputs are bigger for touch.
- **Wording:** "Welcome" became "Front desk", and the cards now read Members, Revenue and Rental shoes out.

**Still needed from you:**
- The card numbers and the two table rows are still your placeholder sample data. Nothing is saved or loaded yet, and a page refresh loses anything added. When you have a real data source, put it in `load()`. A failed request should call `show("error")`.
- The Items, Users and Settings links still go nowhere.

I didn't test with a screen reader or on a tablet.
