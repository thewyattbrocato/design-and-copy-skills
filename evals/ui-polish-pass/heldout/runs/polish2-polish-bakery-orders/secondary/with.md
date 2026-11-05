I couldn't save the file: the Write tool is disabled in this session, and I have no shell to write it another way. The complete page is below so you can save it as `orders.html`. I didn't open the reference files, so the checks are from the skill summary and my own read of the code. I haven't rendered it or tested it with a screen reader.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Orders</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;padding:24px;background:#fff;color:#222;line-height:1.4}
h1{margin:0 0 16px;font-size:1.75rem}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px}
.toolbar label{font-weight:600}
input,select,button{font:inherit;padding:8px 12px;border:1px solid #767676;border-radius:6px;background:#fff;color:#222}
input[type=search]{min-width:200px;flex:1 1 200px}
button{cursor:pointer}
button.primary{background:#1f4e79;border-color:#1f4e79;color:#fff;font-weight:600}
button.danger{border-color:#9b1c1c;color:#9b1c1c}
button:hover{filter:brightness(0.95)}
:focus-visible{outline:3px solid #1a56db;outline-offset:2px}
.table-wrap{overflow-x:auto;border:1px solid #ccc;border-radius:6px}
table{border-collapse:collapse;width:100%;min-width:560px}
caption{text-align:left;padding:0 0 8px;font-weight:600}
th,td{border-bottom:1px solid #ddd;padding:10px 12px;text-align:left;vertical-align:middle}
thead th{background:#f3f4f6;position:sticky;top:0;font-size:0.9rem;text-transform:uppercase;letter-spacing:.03em}
tbody tr:last-child td{border-bottom:none}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
.actions{white-space:nowrap}
.actions button{margin-right:4px}
.status{display:inline-block;padding:2px 10px;border-radius:10px;font-size:0.9rem;font-weight:600;border:1px solid transparent}
.status.pending{background:#fef3c7;color:#78350f;border-color:#d97706}
.status.complete{background:#dcfce7;color:#14532d;border-color:#15803d}
.empty{margin:16px 0;padding:12px 16px;border:1px dashed #767676;border-radius:6px}
.notice{margin:16px 0;padding:12px 16px;border-radius:6px;background:#dcfce7;color:#14532d;border:1px solid #15803d;font-weight:600}
.confirm{margin-top:16px;padding:16px;border:2px solid #9b1c1c;border-radius:8px;max-width:520px}
.confirm p{margin:0 0 12px}
.confirm button{margin-right:6px}
@media (max-width:480px){body{padding:16px}h1{font-size:1.5rem}}
</style></head><body>
<h1>Orders</h1>
<div class="toolbar">
  <label for="search" class="sr-only">Search orders</label>
  <input id="search" type="search" placeholder="Search customer or item">
  <label for="status">Status</label>
  <select id="status"><option>All</option><option>Pending</option><option>Complete</option></select>
  <button class="primary" type="button">Add order</button>
</div>
<div class="table-wrap">
<table>
  <caption>Bakery orders</caption>
  <thead><tr><th scope="col">#</th><th scope="col">Customer name</th><th scope="col">Item</th><th scope="col" class="num">Qty</th><th scope="col">Status</th><th scope="col">Actions</th></tr></thead>
  <tbody>
  <tr><td>1</td><td>Customer 1</td><td>Product A</td><td class="num">10</td><td><span class="status pending">Pending</span></td><td class="actions"><button type="button" aria-label="Edit order 1">Edit</button> <button type="button" class="danger" aria-label="Delete order 1">Delete</button></td></tr>
  <tr><td>2</td><td>Customer 2</td><td>Product B</td><td class="num">25</td><td><span class="status complete">Complete</span></td><td class="actions"><button type="button" aria-label="Edit order 2">Edit</button> <button type="button" class="danger" aria-label="Delete order 2">Delete</button></td></tr>
  </tbody>
</table>
</div>
<p id="none" class="empty" hidden>No orders match your search or status. Clear the search or set Status back to All.</p>
<div id="msg" class="notice" role="status" hidden>Order saved.</div>
<div id="confirm" class="confirm" role="alertdialog" aria-labelledby="confirm-text" hidden>
  <p id="confirm-text"><strong>Delete this order?</strong> This can't be undone.</p>
  <button type="button" class="danger">Delete order</button> <button type="button">Keep order</button>
</div>
</body></html>
```

**What changed**
- **Names for assistive tech:** the search box, status select, and each Edit/Delete button now have accessible names that say which order they act on.
- **Status:** Pending is amber and Complete is green, but each keeps its word, so meaning doesn't rest on color. The filter options now use your real statuses instead of "Status 1" and "Status 2".
- **Baking view:** the header stays visible while scrolling, Qty is right-aligned with tabular numbers, and the table scrolls sideways on narrow screens instead of breaking the layout.
- **Empty and confirm copy:** the empty state says what was filtered and how to clear it. The confirm no longer says "Are you sure?" and names the consequence with verb buttons. The success message is now "Order saved.", which is my guess; change it if it also covers deletes.
- **Focus and roles:** visible focus rings, `role="status"` on the success notice, and `role="alertdialog"` on the confirm.

**Not done**
- Nothing is wired up: the original had no script, so Add, Edit, Delete, search, and the show/hide of the hidden elements still need your app code.
- I didn't check contrast values, 200% zoom, or screen reader behavior by running them.
