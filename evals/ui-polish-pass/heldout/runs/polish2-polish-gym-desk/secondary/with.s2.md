The screen is small, so I'm returning the whole file. The changes cover focus, labels, live regions, the empty and error states, narrow screens, and the desk's own wording.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Front desk · Dashboard</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px;display:flex;flex-wrap:wrap;gap:4px 20px}
nav a{color:#fff;text-decoration:none}
nav a:hover,nav a[aria-current="page"]{text-decoration:underline}
nav a:focus-visible{outline:3px solid #fff;outline-offset:3px}
main{padding:24px}
.cards{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1 1 200px}
.card b{display:block;font-size:28px}
.table-wrap{overflow-x:auto}
table{width:100%;background:#fff;border-collapse:collapse}
th,td{padding:10px;text-align:left;border-bottom:1px solid #eee;overflow-wrap:anywhere}
th{font-weight:600}
#empty{color:#4b5563}
#err{color:#991b1b;background:#fef2f2;border:1px solid #fca5a5;padding:12px 16px;border-radius:6px}
#err button{margin-left:8px}
[hidden]{display:none!important}
form{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end}
.field{display:flex;flex-direction:column;gap:4px;font-size:14px}
input{padding:8px;border:1px solid #6b7280;border-radius:4px;font:inherit;background:#fff;color:#222}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;font:inherit;cursor:pointer}
button:hover{background:#1d4ed8}
button:focus-visible,input:focus-visible{outline:3px solid #1d4ed8;outline-offset:2px}
</style></head><body>
<nav>
<a href="#" aria-current="page">Dashboard</a>
<a href="#">Check-in</a>
<a href="#">Day passes</a>
<a href="#">Shoe rentals</a>
<a href="#">Settings</a>
</nav>
<main>
<h1>Front desk</h1>
<div class="cards">
<div class="card">Total Users<b>1,234</b></div>
<div class="card">Revenue<b>$12,345</b></div>
<div class="card">Active Items<b>56</b></div>
</div>
<h2 id="recent-h">Recent Activity</h2>
<p id="empty" role="status" hidden>No activity yet. Check-ins, day passes and shoe rentals will show up here.</p>
<p id="err" role="alert" hidden>Couldn't load recent activity. Check the connection, then <button type="button" onclick="location.reload()">Try again</button></p>
<div class="table-wrap">
<table aria-labelledby="recent-h">
<thead><tr><th scope="col">Name</th><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Date</th></tr></thead>
<tbody>
<tr><td>John Doe</td><td>Item 1</td><td>Active</td><td>01/01/2024</td></tr>
<tr><td>Jane Smith</td><td>Item 2</td><td>Pending</td><td>01/02/2024</td></tr>
</tbody>
</table>
</div>
<h2>Add New</h2>
<form id="add-new">
<label class="field">Name<input name="name" required autocomplete="off"></label>
<label class="field">Value<input name="value" required autocomplete="off"></label>
<button type="submit">Add</button>
</form>
</main></body></html>
```

**What changed**
- **Access:** Inputs now have real labels instead of placeholders. Table headers are scoped, and the table is named by its heading. The current page is marked in the nav with `aria-current` and underlined, so it isn't shown by color alone. Focus rings are visible on every control. The nav ring is white because blue disappears on the dark nav.
- **States:** The empty message says what the list is for. The error says what failed and offers "Try again", and it sits in a persistent alert region. Status and error are announced to assistive tech.
- **Layout:** Cards wrap instead of squeezing at narrow widths. The table scrolls sideways in its own box so the page doesn't overflow at 320px.
- **Copy:** Nav now uses the desk's own nouns: Check-in, Day passes, Shoe rentals. "Welcome" became "Front desk". The button is "Add" to match the "Add New" heading.

**Not done, and why**
- The file has no script, so nothing submits yet. The Add form needs a handler that disables the button while it saves, shows the result in words, and keeps the typed values if saving fails. I didn't invent that behavior.
- The card numbers and table rows are still static sample data, and the card labels ("Total Users", "Active Items") are unchanged. The real data and the item/rental wording need your confirmation.
- Not tested with a screen reader, on a real device, or at 200% zoom. I checked the contrast ratios and the layout by reading the code only.
