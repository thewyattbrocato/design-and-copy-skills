The finished page is below. The request was to finish the screen, not redesign it, so the layout, palette and type are unchanged. The changes are the states, the form, the placeholder content and the access fixes.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Front desk · Staff dashboard</title>
<style>
*{box-sizing:border-box}
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222;line-height:1.5}
.skip{position:absolute;left:-9999px;top:auto}
.skip:focus{left:12px;top:12px;background:#fff;color:#222;padding:8px 12px;border-radius:4px;z-index:10}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
nav{background:#1f2937;padding:12px 24px;display:flex;flex-wrap:wrap;gap:4px 20px;align-items:center}
nav a{color:#fff;text-decoration:none;padding:4px 0}
nav a[aria-current="page"]{text-decoration:underline;text-underline-offset:4px}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}
main{padding:24px;max-width:1100px}
.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 200px}
.card b{display:block;font-size:28px}
.table-wrap{overflow-x:auto;border-radius:8px}
table{width:100%;background:#fff;border-collapse:collapse}
th,td{padding:10px;text-align:left;border-bottom:1px solid #eee}
td.empty-cell{color:#555;text-align:center;padding:24px}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button:disabled{background:#64748b;cursor:wait}
p.msg{margin:12px 0;padding:12px 16px;border-radius:6px}
.alert{background:#fef2f2;color:#991b1b;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}
.notice{background:#ecfdf5;color:#065f46}
.notice:empty{display:none}
.field{display:flex;flex-direction:column;gap:4px;margin-bottom:12px;max-width:320px}
.field label{font-weight:600}
.field input{padding:8px;border:1px solid #6b7280;border-radius:4px;font:inherit}
.field input[aria-invalid="true"]{border-color:#b91c1c}
.field .err{color:#991b1b;font-size:14px}
.field .err:empty{display:none}
</style></head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav aria-label="Main">
  <a href="#" aria-current="page">Dashboard</a>
  <a href="#">Check-in</a>
  <a href="#">Day passes</a>
  <a href="#">Shoe rental</a>
  <a href="#">Members</a>
  <a href="#">Settings</a>
</nav>
<main id="main">
<h1>Front desk</h1>
<div class="cards">
  <div class="card">Members<b id="stat-members">—</b></div>
  <div class="card">Revenue<b id="stat-revenue">—</b></div>
  <div class="card">Active items<b id="stat-items">—</b></div>
</div>

<h2>Recent activity</h2>
<div class="table-wrap">
<table>
  <caption class="sr-only">Recent check-ins, day passes and shoe rentals</caption>
  <thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
  <tbody id="activity"></tbody>
</table>
</div>
<p id="empty" class="msg" hidden>No activity yet today. Check-ins, day passes and rentals will appear here.</p>
<div id="err" class="msg alert" role="alert" hidden>
  <span id="err-text">Recent activity didn't load.</span>
  <button id="retry" type="button">Try again</button>
</div>

<h2>Add new</h2>
<form id="add-form" novalidate>
  <div class="field">
    <label for="f-name">Name</label>
    <input id="f-name" name="name" autocomplete="off" required aria-describedby="f-name-err">
    <span id="f-name-err" class="err"></span>
  </div>
  <div class="field">
    <label for="f-value">Value</label>
    <input id="f-value" name="value" autocomplete="off" required aria-describedby="f-value-err">
    <span id="f-value-err" class="err"></span>
  </div>
  <button id="submit-btn" type="submit">Submit</button>
  <p id="form-status" class="msg notice" role="status"></p>
</form>
</main>

<script>
// Set these to the real endpoints. Until they are set, the page says so instead of pretending it worked.
const LOAD_URL = '';   // recent activity (GET, returns JSON array of {name, item, status, date})
const SAVE_URL = '';   // add new (POST, JSON body {name, value})

const $ = id => document.getElementById(id);
const tbody = $('activity'), emptyMsg = $('empty'), errBox = $('err'), errText = $('err-text');

function showActivity(state, rows = [], message = '') {
  tbody.textContent = '';
  emptyMsg.hidden = state !== 'empty';
  errBox.hidden = state !== 'error';
  errText.textContent = message;
  if (state === 'loading') {
    const td = document.createElement('td');
    td.colSpan = 4; td.className = 'empty-cell'; td.textContent = 'Loading recent activity…';
    const tr = document.createElement('tr'); tr.append(td); tbody.append(tr);
  }
  if (state === 'ready') {
    for (const r of rows) {
      const tr = document.createElement('tr');
      for (const v of [r.name, r.item, r.status, r.date]) {
        const td = document.createElement('td'); td.textContent = v; tr.append(td);
      }
      tbody.append(tr);
    }
  }
}

async function loadActivity() {
  showActivity('loading');
  try {
    if (!LOAD_URL) throw new Error('not-configured');
    const res = await fetch(LOAD_URL, { headers: { Accept: 'application/json' } });
    if (!res.ok) throw new Error('http ' + res.status);
    const rows = await res.json();
    showActivity(rows.length ? 'ready' : 'empty', rows);
  } catch (e) {
    showActivity('error', [], e.message === 'not-configured'
      ? "Recent activity isn't connected yet."
      : "Recent activity didn't load. Check the connection, then try again.");
  }
}
$('retry').addEventListener('click', loadActivity);

const form = $('add-form'), btn = $('submit-btn'), status = $('form-status');
const name = $('f-name'), value = $('f-value');

function fieldError(input, msg) {
  const span = $(input.id + '-err');
  input.setAttribute('aria-invalid', msg ? 'true' : 'false');
  span.textContent = msg;
  return !msg;
}

form.addEventListener('submit', async e => {
  e.preventDefault();
  if (btn.disabled) return;
  const n = name.value.trim(), v = value.value.trim();
  const ok = [
    fieldError(name, n ? '' : 'Enter a name.'),
    fieldError(value, v ? '' : 'Enter a value.')
  ].every(Boolean);
  if (!ok) { (n ? value : name).focus(); status.textContent = ''; return; }

  btn.disabled = true; btn.textContent = 'Saving…';
  status.textContent = '';
  try {
    if (!SAVE_URL) throw new Error('not-configured');
    const res = await fetch(SAVE_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: n, value: v })
    });
    if (!res.ok) throw new Error('http ' + res.status);
    form.reset();
    status.textContent = 'Saved. ' + n + ' was added.';
    name.focus();
  } catch (err) {
    status.textContent = err.message === 'not-configured'
      ? "Saving isn't connected yet. Your entries are still here."
      : 'Not saved. Your entries are still here. Check the connection and press Submit to try again.';
  } finally {
    btn.disabled = false; btn.textContent = 'Submit';
  }
});

loadActivity();
</script>
</body>
</html>
```

**Changes**
- **Placeholder content:** "Welcome" is now the h1 "Front desk". Nav uses the desk's jobs (Check-in, Day passes, Shoe rental) and "Users" is now "Members". The fake numbers and sample rows are gone, so the cards show "—" until they have real data.
- **Activity states:** loading, empty, error with Try again (in `role="alert"`), and ready. Rows are built with `textContent`, so names from the database can't inject HTML.
- **Add new form:** labels on both fields, required validation with messages beside each field, focus moved to the first problem, a Saving… state that blocks double-submit, a success message, and failure that keeps what was typed.
- **Access:** skip link, a page title, `aria-current` on the nav, table caption and column scopes, visible focus rings, and a wrapping layout with horizontal scroll on the table for narrow screens.

**Needs your input before Monday**
- `LOAD_URL` and `SAVE_URL` are empty. Until you set them, the activity area says it isn't connected and Submit says nothing was saved, so nothing shows a false success.
- The stat cards need a data source, and the nav links are still `#`.
- "Name" and "Value" are generic. Tell me what Add new is meant to create and I'll name the fields for it.

I have not run this in a browser or tested it with a screen reader. I only checked it by reading the code.
