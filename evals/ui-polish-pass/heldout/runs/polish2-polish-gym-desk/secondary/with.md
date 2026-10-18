I couldn't save the file: the Write tool is disabled in this session. The finished file is below, so you can paste it over your current copy as `front-desk.html`. Most of the file changed, so this is the whole thing. The look, layout, colors, and wording are unchanged except where noted.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Front desk · Dashboard</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px;display:flex;flex-wrap:wrap;gap:4px 20px}
nav a{color:#fff;text-decoration:none;padding:4px 0;border-bottom:2px solid transparent}
nav a[aria-current="page"]{border-bottom-color:#fff}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}
main{padding:24px;max-width:1100px}
.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 200px}
.card b{display:block;font-size:28px}
.table-wrap{overflow-x:auto;background:#fff;border-radius:8px}
table{width:100%;background:#fff;border-collapse:collapse}
th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button[aria-disabled="true"]{opacity:.6;cursor:progress}
.form{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end}
.field{display:flex;flex-direction:column;gap:4px}
.field input{padding:8px;border:1px solid #6b7280;border-radius:4px;font:inherit;min-width:200px}
.field input[aria-invalid="true"]{border-color:#b91c1c}
.hint-error{color:#b91c1c;font-size:14px}
.msg{margin:12px 0}
.error{color:#b91c1c}
.success{color:#166534}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
</style></head><body>
<nav aria-label="Main"><a href="#" aria-current="page">Dashboard</a><a href="#">Items</a><a href="#">Users</a><a href="#">Settings</a></nav>
<main>
<h1>Front desk</h1>
<div class="cards">
<div class="card">Total Users<b>1,234</b></div>
<div class="card">Revenue<b>$12,345</b></div>
<div class="card">Active Items<b>56</b></div>
</div>
<h2>Recent Activity</h2>
<div id="err" role="alert" hidden><p class="error">Couldn't load recent activity. Check the connection, then try again. <button type="button" id="retry">Retry</button></p></div>
<div class="table-wrap">
<table>
<caption class="sr-only">Recent activity</caption>
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody>
<tr><td>John Doe</td><td>Day pass</td><td>Active</td><td>01/01/2024</td></tr>
<tr><td>Jane Smith</td><td>Shoe rental</td><td>Pending</td><td>01/02/2024</td></tr>
</tbody>
</table>
</div>
<p id="empty" role="status" hidden>No activity yet. Check someone in or sell a day pass to see it here.</p>
<h2>Add New</h2>
<form id="add" novalidate>
<div class="form">
<div class="field">
<label for="name">Name</label>
<input id="name" name="name" autocomplete="off" required aria-describedby="name-err">
<span id="name-err" class="hint-error" hidden>Enter a name.</span>
</div>
<div class="field">
<label for="value">Value</label>
<input id="value" name="value" autocomplete="off">
</div>
<button type="submit" id="submit">Submit</button>
</div>
<p id="form-msg" class="msg" role="status" hidden></p>
</form>
</main>
<script>
const form = document.getElementById('add');
const name = document.getElementById('name');
const value = document.getElementById('value');
const submit = document.getElementById('submit');
const msg = document.getElementById('form-msg');
const nameErr = document.getElementById('name-err');
let busy = false;

document.getElementById('retry').addEventListener('click', () => location.reload());

name.addEventListener('input', () => {
  if (name.value.trim()) {
    name.removeAttribute('aria-invalid');
    nameErr.hidden = true;
  }
});

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  if (busy) return;

  if (!name.value.trim()) {
    name.setAttribute('aria-invalid', 'true');
    nameErr.hidden = false;
    name.focus();
    return;
  }

  busy = true;
  submit.setAttribute('aria-disabled', 'true');
  submit.textContent = 'Saving…';
  msg.hidden = true;

  const entry = { name: name.value.trim(), value: value.value.trim() };
  try {
    if (typeof window.saveEntry !== 'function') {
      throw new Error('Saving is not connected on this screen.');
    }
    await window.saveEntry(entry);
    msg.className = 'msg success';
    msg.textContent = 'Saved ' + entry.name + '.';
    form.reset();
    name.focus();
  } catch (err) {
    msg.className = 'msg error';
    msg.textContent = "Couldn't save. Your entry is still filled in, so you can try again. " + err.message;
  } finally {
    msg.hidden = false;
    busy = false;
    submit.removeAttribute('aria-disabled');
    submit.textContent = 'Submit';
  }
});
</script>
</body></html>
```

**What changed**
- **Submit:** the form now validates the name, shows the error beside the field, and moves focus to it. While saving, the button is marked busy and double-submits are blocked. On failure the typed values stay. Success and failure both show a message in words.
- **Save hook:** the form calls `window.saveEntry({name, value})`, which is not in the pasted file. Your existing desk code needs to define it. Until it does, Submit reports that saving isn't connected.
- **Error and empty states:** the error has a Retry button, which reloads the page. The empty message says what the screen is for. Both use `role="alert"` or `role="status"`, so they are announced. Your existing code must show and hide them via their ids.
- **Access:** inputs have visible labels (the placeholders were the only label before), the nav has a label and marks the current page, table headers have `scope`, the table has a caption, and focus rings are visible.
- **Layout:** cards wrap, the table scrolls sideways on narrow screens, and long names wrap.
- **Wording:** "Welcome" is now "Front desk". The sample items use "Day pass" and "Shoe rental" from your description.

**Not done or not checked**
- I did not open this in a browser or test it with a screen reader. I only read the code.
- The card numbers (1,234 users, $12,345 revenue, 56 items) are still hardcoded samples. Wire them to real data before Monday, or the desk will see fake numbers.
