I couldn't save the file. Write and Bash are both disabled in this session, so the finished page is below. Copy it into `staff-desk.html` to use it.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Front Desk Dashboard</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px}nav a{color:#fff;margin-right:20px;text-decoration:none;padding:4px 0;display:inline-block}
nav a[aria-current="page"]{border-bottom:2px solid #60a5fa}
nav a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}
main{padding:24px;max-width:1100px}.cards{display:flex;gap:16px;margin-bottom:24px;flex-wrap:wrap}
.card{background:#fff;padding:16px;border-radius:8px;flex:1;min-width:180px}.card b{display:block;font-size:28px}
.table-wrap{overflow-x:auto;border-radius:8px;margin-bottom:24px}
table{width:100%;background:#fff;border-collapse:collapse}th,td{padding:10px;text-align:left;border-bottom:1px solid #eee}
th{background:#fafafa;font-size:14px;color:#555}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;cursor:pointer;font-size:14px}
button:hover{background:#1d4ed8}
input,select{padding:8px 10px;border:1px solid #cbd5e1;border-radius:4px;font-size:14px;background:#fff}
.form-row{display:flex;gap:12px;align-items:flex-end;flex-wrap:wrap;background:#fff;padding:16px;border-radius:8px}
.field{display:flex;flex-direction:column;gap:4px;font-size:13px;color:#555}
.field input,.field select{min-width:200px}
.msg{padding:12px 16px;border-radius:6px;margin:0 0 16px}
#empty{background:#f1f5f9;color:#475569}
#err{background:#fee2e2;color:#991b1b}
.hint{color:#64748b;font-size:13px;margin-top:8px}
</style></head><body>
<nav>
<a href="#" aria-current="page">Dashboard</a><a href="#">Items</a><a href="#">Users</a><a href="#">Settings</a>
</nav>
<main>
<h1>Front Desk</h1>
<div class="cards">
<div class="card">Total Users<b>1,234</b></div>
<div class="card">Revenue<b>$12,345</b></div>
<div class="card">Active Items<b>56</b></div>
</div>

<h2>Recent Activity</h2>
<p id="err" class="msg" role="alert" hidden>An error occurred. Please try again.</p>
<div class="table-wrap">
<table id="activity">
<caption style="text-align:left;padding:0 0 8px;color:#555">Latest check-ins, day passes and shoe rentals</caption>
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody>
<tr><td>John Doe</td><td>Item 1</td><td>Active</td><td>01/01/2024</td></tr>
<tr><td>Jane Smith</td><td>Item 2</td><td>Pending</td><td>01/02/2024</td></tr>
</tbody>
</table>
</div>
<p id="empty" class="msg" hidden>No data available.</p>

<h2>Add New</h2>
<form id="add-form" class="form-row" novalidate>
<label class="field">Type
<select id="type" name="type">
<option value="Check-in">Check-in</option>
<option value="Day pass">Day pass</option>
<option value="Shoe rental">Shoe rental</option>
</select>
</label>
<label class="field">Name
<input id="name" name="name" placeholder="Enter name" autocomplete="off" required>
</label>
<label class="field">Value
<input id="value" name="value" placeholder="Enter value" autocomplete="off" required>
</label>
<button type="submit">Submit</button>
</form>
<p class="hint">Entries are added to the table above. Name and value are both required.</p>
</main>

<script>
(function () {
  var table = document.getElementById('activity');
  var tbody = table.tBodies[0];
  var empty = document.getElementById('empty');
  var err = document.getElementById('err');
  var form = document.getElementById('add-form');
  var nameIn = document.getElementById('name');
  var valueIn = document.getElementById('value');
  var typeIn = document.getElementById('type');

  function today() {
    var d = new Date();
    var mm = String(d.getMonth() + 1).padStart(2, '0');
    var dd = String(d.getDate()).padStart(2, '0');
    return mm + '/' + dd + '/' + d.getFullYear();
  }

  function refreshEmpty() {
    empty.hidden = tbody.rows.length > 0;
    table.hidden = tbody.rows.length === 0;
  }

  function addRow(cells) {
    var tr = document.createElement('tr');
    cells.forEach(function (text) {
      var td = document.createElement('td');
      td.textContent = text; // textContent so typed input is never parsed as HTML
      tr.appendChild(td);
    });
    tbody.insertBefore(tr, tbody.firstChild);
    refreshEmpty();
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = nameIn.value.trim();
    var value = valueIn.value.trim();
    if (!name || !value) {
      err.textContent = 'Name and value are both required.';
      err.hidden = false;
      (name ? valueIn : nameIn).focus();
      return;
    }
    err.hidden = true;
    addRow([name, value, typeIn.value, today()]);
    form.reset();
    nameIn.focus();
  });

  refreshEmpty();
})();
</script>
</body></html>
```

**What I changed**
- **Submit works.** It validates name and value, shows the error message if either is blank, and otherwise adds a row to the top of Recent Activity dated today. Text is inserted with `textContent`, so typed input can't inject HTML.
- **Type dropdown** for Check-in, Day pass, or Shoe rental, so the form matches the desk's three jobs.
- **Empty and error states** now actually toggle. The "No data available" and error messages were hidden with no code to show them.
- **Layout:** the table scrolls sideways on narrow screens, the stat cards wrap, and the page has a max width.
- **Accessibility:** form fields have labels, the table has headers and a caption, the current nav item is marked, and focus rings are visible.
- **Nav** shows which page you're on. The other links still go to `#` because there are no other pages yet.

**Still needs your input before Monday**
- **The stat numbers and the John Doe / Jane Smith rows are template placeholders.** Revenue of $12,345 on the front desk is wrong, so I left them only because I have no data source. Tell me where the real numbers come from (an API, a CSV export, or your POS) and I'll wire them in.
- **Nothing is saved.** Refreshing the page clears new entries. Persistence needs a backend or at least `localStorage`. Tell me which you have.
- **I didn't test it in a browser** because I have no way to run one here. Open it once and try a check-in, a blank submit, and a shoe rental.
