Here is the finished screen. It's one file, so I've returned the whole thing. Layout, colors, and type are unchanged. The gym's own nouns replace the placeholders, and the missing states, form handling, and access fixes are added.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Front desk</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #fbbf24;outline-offset:2px}
.skip{position:absolute;left:8px;top:-48px;background:#fff;padding:8px 12px;border-radius:4px;z-index:10}.skip:focus{top:8px}
nav{background:#1f2937;padding:12px 24px}nav a{color:#fff;margin-right:20px;text-decoration:none}nav a[aria-current]{text-decoration:underline}
main{padding:24px;max-width:1100px}
.cards{display:flex;gap:16px;margin-bottom:24px;flex-wrap:wrap}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 200px}.card b{display:block;font-size:28px}
.table-wrap{overflow-x:auto;background:#fff;border-radius:8px}
table{width:100%;border-collapse:collapse}th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button:disabled{opacity:.6;cursor:progress}
input{padding:8px;border:1px solid #6b7280;border-radius:4px;font:inherit}
.form{display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end;background:#fff;padding:16px;border-radius:8px}
.field{display:flex;flex-direction:column;gap:4px;min-width:220px;flex:1}
.msg{color:#b91c1c;font-size:14px;min-height:1em}
.notice{padding:12px 16px;border-radius:6px;margin:0 0 16px}
.notice.err{background:#fef2f2;color:#991b1b;border:1px solid #fca5a5}
.notice.ok{background:#f0fdf4;color:#166534;border:1px solid #86efac}
[hidden]{display:none!important}
@media (max-width:600px){main{padding:16px}nav{padding:12px 16px}nav a{display:inline-block;margin:4px 16px 4px 0}}
</style></head><body>
<a class="skip" href="#main">Skip to content</a>
<nav aria-label="Main"><a href="#" aria-current="page">Dashboard</a><a href="#">Check-in</a><a href="#">Day passes</a><a href="#">Shoe rental</a><a href="#">Settings</a></nav>
<main id="main">
<h1>Front desk</h1>
<div class="cards">
<div class="card">Members<b>1,234</b></div>
<div class="card">Revenue<b>$12,345</b></div>
<div class="card">Shoes out<b>56</b></div>
</div>

<h2>Recent activity</h2>
<p id="err" class="notice err" role="alert" hidden>Couldn't load recent activity. <button type="button" onclick="location.reload()">Try again</button></p>
<div class="table-wrap">
<table>
<caption class="sr-only" style="position:absolute;left:-9999px">Recent check-ins, passes and rentals</caption>
<thead><tr><th scope="col">Name</th><th scope="col">Pass or rental</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody>
<tr><td>John Doe</td><td>Day pass</td><td>Active</td><td>01/01/2024</td></tr>
<tr><td>Jane Smith</td><td>Shoe rental</td><td>Pending</td><td>01/02/2024</td></tr>
</tbody>
</table>
</div>
<p id="empty" hidden>No check-ins, passes or rentals yet today.</p>

<h2 id="add-h">Add entry</h2>
<form id="add" class="form" novalidate aria-labelledby="add-h">
<div class="field">
<label for="name">Name</label>
<input id="name" name="name" autocomplete="off" placeholder="Member or guest name" aria-describedby="name-err">
<span class="msg" id="name-err"></span>
</div>
<div class="field">
<label for="value">Pass or rental</label>
<input id="value" name="value" autocomplete="off" placeholder="e.g. Day pass, Shoe rental">
<span class="msg" id="value-err"></span>
</div>
<button type="submit" id="submit">Save</button>
</form>
<p id="result" class="notice" role="status" hidden></p>
</main>

<script>
const form = document.getElementById('add');
const nameIn = document.getElementById('name');
const valueIn = document.getElementById('value');
const nameErr = document.getElementById('name-err');
const submit = document.getElementById('submit');
const result = document.getElementById('result');

// Replace the body with the desk system call. It must throw on failure.
async function saveEntry(entry) {
  throw new Error('the desk system is not connected yet');
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  nameErr.textContent = '';
  nameIn.removeAttribute('aria-invalid');
  if (!nameIn.value.trim()) {
    nameErr.textContent = 'Enter a name to check in or sell.';
    nameIn.setAttribute('aria-invalid', 'true');
    nameIn.focus();
    return;
  }
  const entry = { name: nameIn.value.trim(), value: valueIn.value.trim() };
  submit.disabled = true;
  submit.textContent = 'Saving…';
  form.setAttribute('aria-busy', 'true');
  result.hidden = true;
  try {
    await saveEntry(entry);
    result.className = 'notice ok';
    result.textContent = 'Saved ' + entry.name + '.';
    form.reset();
    nameIn.focus();
  } catch (err) {
    // Keep what was typed so the desk can retry.
    result.className = 'notice err';
    result.textContent = 'Not saved: ' + err.message + '. Your entry is still here.';
  } finally {
    result.hidden = false;
    submit.disabled = false;
    submit.textContent = 'Save';
    form.removeAttribute('aria-busy');
  }
});
</script>
</body></html>
```

**What changed**
- **Labels and wording:** the nav, cards, table headers, and sample rows now use the desk's nouns (check-in, day passes, shoe rental). The old "Users", "Items", and "Submit" are gone.
- **Form:** the inputs now have real labels and a required-name check. An error appears beside the field, and focus moves to it. The Save button shows "Saving…" and is disabled while it runs. A failure keeps the typed values and says why. Success says who was saved.
- **Empty and error states:** a message for an empty table and an alert with Try again for a failed load. Both are hidden until something wires them up.
- **Access:** a skip link, `aria-current` on the active nav item, table captions and column headers, visible focus rings, and labelled inputs.
- **Small screens:** the table scrolls sideways instead of breaking the layout, the cards wrap, and the nav stacks.

**Needs you before Monday**
- `saveEntry()` is a stub that always fails, so Save will show "Not saved" until you connect it to the desk system. The failure message is shown as it would be in real use.
- The numbers (1,234 members, $12,345, 56 shoes) and the table rows are still sample values. I didn't change them because I don't have the real figures.

**Not checked:** I only read the code. I did not test it with a screen reader, on a real device, at 200% text size, or in a browser.
