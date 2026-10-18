I couldn't save the file because the Write tool is disabled in this session, so the complete file is below. Paste it into a `.html` file and open it in a browser. The check-in, day pass and shoe rental flow is in the `Record an entry` form.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Front desk</title>
<style>
[hidden]{display:none!important}
*{box-sizing:border-box}
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222;line-height:1.4}
nav{background:#1f2937;padding:12px 24px;display:flex;flex-wrap:wrap;gap:4px 20px}
nav a{color:#fff;text-decoration:none;padding:4px 0}
nav a[aria-current="page"]{text-decoration:underline;text-underline-offset:4px}
main{padding:24px;max-width:1100px}
h1{margin:0 0 20px}
h2{margin:32px 0 12px;font-size:20px}
.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 200px;color:#4b5563}
.card b{display:block;font-size:28px;color:#222;font-variant-numeric:tabular-nums;overflow-wrap:anywhere}
.table-wrap{overflow-x:auto;background:#fff;border-radius:8px}
table{width:100%;background:#fff;border-collapse:collapse;min-width:480px}
th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
th{color:#4b5563;font-size:14px}
.empty{background:#fff;padding:24px;border-radius:8px;color:#4b5563}
.msg{padding:12px 16px;border-radius:6px;margin:0 0 16px}
#err{background:#fef2f2;color:#991b1b;border:1px solid #fca5a5;display:flex;flex-wrap:wrap;align-items:center;gap:12px}
#status{color:#166534;min-height:1.4em;margin:12px 0 0}
.form{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end;background:#fff;padding:16px;border-radius:8px}
.field{display:flex;flex-direction:column;gap:4px;flex:1 1 200px;min-width:0}
.field-error{color:#991b1b;font-size:14px}
input,select{font:inherit;padding:8px 10px;border:1px solid #6b7280;border-radius:4px;background:#fff;min-width:0;width:100%}
input[aria-invalid="true"]{border:2px solid #991b1b}
button{font:inherit;padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;cursor:pointer}
button:hover{background:#1d4ed8}
button:disabled{background:#6b7fa8;cursor:wait}
:focus-visible{outline:3px solid #2563eb;outline-offset:2px}
nav :focus-visible{outline-color:#fff}
</style></head><body>
<nav aria-label="Main"><a href="#" aria-current="page">Dashboard</a><a href="#">Check-in</a><a href="#">Passes &amp; rentals</a><a href="#">Members</a><a href="#">Settings</a></nav>
<main>
<h1>Front desk</h1>
<div class="cards">
<div class="card">Total members<b>1,234</b></div>
<div class="card">Revenue<b>$12,345</b></div>
<div class="card">Active passes &amp; rentals<b>56</b></div>
</div>

<h2 id="activity-title">Recent activity</h2>
<p id="err" role="alert" hidden><span id="err-text"></span><button type="button" id="retry">Try again</button></p>
<div class="table-wrap" id="table-wrap">
<table aria-labelledby="activity-title">
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody id="rows"></tbody>
</table>
</div>
<div id="empty" class="empty" hidden>
<p>No activity yet. Record the first check-in, day pass or shoe rental below.</p>
<button type="button" id="empty-action">Record an entry</button>
</div>

<h2 id="add-title">Record an entry</h2>
<form id="entry" class="form" novalidate aria-labelledby="add-title">
<div class="field">
<label for="name">Name</label>
<input id="name" name="name" autocomplete="off" aria-describedby="name-error">
<span id="name-error" class="field-error" hidden></span>
</div>
<div class="field">
<label for="item">Item</label>
<select id="item" name="item"><option>Day pass</option><option>Shoe rental</option><option>Check-in</option></select>
</div>
<button type="submit" id="submit">Record</button>
</form>
<p id="status" role="status"></p>
</main>

<script>
const activity = [
  { name: 'John Doe', item: 'Day pass', status: 'Active', date: '01/01/2024' },
  { name: 'Jane Smith', item: 'Shoe rental', status: 'Pending', date: '01/02/2024' }
];

const form = document.getElementById('entry');
const nameIn = document.getElementById('name');
const nameErr = document.getElementById('name-error');
const itemIn = document.getElementById('item');
const submitBtn = document.getElementById('submit');
const rowsEl = document.getElementById('rows');
const tableWrap = document.getElementById('table-wrap');
const emptyEl = document.getElementById('empty');
const errEl = document.getElementById('err');
const errText = document.getElementById('err-text');
const statusEl = document.getElementById('status');

function render() {
  rowsEl.replaceChildren(...activity.map(r => {
    const tr = document.createElement('tr');
    for (const v of [r.name, r.item, r.status, r.date]) {
      const td = document.createElement('td');
      td.textContent = v;
      tr.append(td);
    }
    return tr;
  }));
  tableWrap.hidden = activity.length === 0;
  emptyEl.hidden = activity.length > 0;
}

function showError(message) {
  errText.textContent = message;
  errEl.hidden = false;
  document.getElementById('retry').focus();
}

function setNameError(message) {
  nameIn.setAttribute('aria-invalid', 'true');
  nameErr.textContent = message;
  nameErr.hidden = false;
}

function clearNameError() {
  nameIn.removeAttribute('aria-invalid');
  nameErr.hidden = true;
}

function setBusy(busy) {
  submitBtn.disabled = busy;
  submitBtn.textContent = busy ? 'Recording…' : 'Record';
  form.setAttribute('aria-busy', String(busy));
}

// Stand-in for the real save. There is no backend in this file yet, so entries
// last until the page is reloaded. Replace the body with the request to the
// desk's server; a rejected promise takes the error path below.
function saveEntry(entry) {
  return new Promise(resolve => setTimeout(() => resolve(entry), 300));
}

async function submitEntry() {
  const name = nameIn.value.trim();
  if (!name) {
    setNameError('Enter a name to record this entry.');
    nameIn.focus();
    return;
  }
  clearNameError();
  errEl.hidden = true;
  setBusy(true);
  const entry = { name, item: itemIn.value, status: 'Active', date: new Date().toLocaleDateString('en-US') };
  try {
    await saveEntry(entry);
    activity.unshift(entry);
    render();
    form.reset();
    statusEl.textContent = `Recorded ${entry.item} for ${entry.name}.`;
    nameIn.focus();
  } catch (err) {
    // Typed values stay in the form so nothing has to be entered again.
    showError("Couldn't record this entry. What you typed is still here.");
  } finally {
    setBusy(false);
  }
}

form.addEventListener('submit', e => {
  e.preventDefault();
  submitEntry();
});
nameIn.addEventListener('input', clearNameError);
document.getElementById('retry').addEventListener('click', () => form.requestSubmit());
document.getElementById('empty-action').addEventListener('click', () => nameIn.focus());

render();
</script>
</body></html>
```

**What changed**
- **Form works:** Record checks the name, shows an inline error and focuses the field when it's blank, disables the button while saving, and confirms the result in words. Typed values survive a failure, and a "Try again" button sits in the error banner.
- **Empty state:** the table is replaced by a message and a "Record an entry" button when there are no rows.
- **Accessibility:** labels on the inputs (placeholders alone aren't labels), named table headers, a current-page marker in the nav, visible focus rings, and `[hidden]` forced so hidden states stay hidden.
- **Layout:** cards wrap, the table scrolls sideways on narrow screens, and the form stacks.
- **Product words:** "Items" became "Passes & rentals", "Users" became "Members", and the sample rows use Day pass and Shoe rental. Colors, card and table styling, and the overall layout are unchanged.

**Before Monday**
- **Nothing is saved:** entries live in page memory and vanish on reload. Connect `saveEntry` to your real backend, which is the one place to change.
- **Stat numbers are still sample values** (1,234 / $12,345 / 56). Wire them to real data.
- **Nav links are `#` placeholders**, since the other pages don't exist in this file.
- **Not tested:** I haven't run this in a browser, with a screen reader, or on a phone.
