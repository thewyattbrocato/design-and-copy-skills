I couldn't save the file or run a syntax check: the Write and Bash tools are disabled in this session. The complete page is below. Copy it into a file such as `front-desk.html` and open it in a browser. I checked it by reading only, so please click through each form once before Monday.

**What I changed**
- **Placeholder data removed.** "Total Users", "Revenue", and the John Doe rows were fake. The cards and activity log now count real actions from the desk.
- **Desk functions wired up.** Check-in, Day Pass sales, and Shoe Rental (rent and return) all work. Nav links point to them.
- **Error and empty messages used.** The hidden `#err` and `#empty` elements now show validation errors and an empty-day message.
- **Prices are placeholders.** Set them in `CONFIG` at the top of the script. I did not know your prices.

**Decisions you should check**
- **Storage is per browser.** Data lives in localStorage, so it does not sync between desk computers and does not connect to member records. For Monday that is fine on one machine. Before you rely on it across machines, the `save`/load code needs to call your backend.
- **Shoe returns are not charged.** Renting records the rental fee. Returning logs a "Returned" line with no amount. Add a deposit or late fee if you use one.
- **Walk-in passes.** If no name is entered, the sale is recorded as "Walk-in".

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Front Desk</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f5f5f5;color:#222}
nav{background:#1f2937;padding:12px 24px}nav a{color:#fff;margin-right:20px;text-decoration:none}
main{padding:24px}.cards{display:flex;gap:16px;margin-bottom:24px}
.card{background:#fff;padding:16px;border-radius:8px;flex:1}.card b{display:block;font-size:28px}
section{background:#fff;padding:16px;border-radius:8px;margin-bottom:24px}
h2{margin-top:0}
form{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
input,select{padding:8px;border:1px solid #ccc;border-radius:4px;font-size:14px}
table{width:100%;background:#fff;border-collapse:collapse;margin-bottom:24px}th,td{padding:10px;text-align:left;border-bottom:1px solid #eee}
button{padding:8px 16px;background:#2563eb;color:#fff;border:0;border-radius:4px;cursor:pointer}
button.secondary{background:#6b7280}
.err{color:#b91c1c;font-weight:600}
</style></head><body>
<nav><a href="#checkin">Check-in</a><a href="#passes">Day Passes</a><a href="#shoes">Shoe Rental</a><a href="#activity">Activity</a></nav>
<main>
<h1>Front Desk</h1>
<div class="cards">
<div class="card">Checked In Today<b id="st-checkins">0</b></div>
<div class="card">Day Passes Sold<b id="st-passes">0</b></div>
<div class="card">Revenue Today<b id="st-revenue">$0.00</b></div>
<div class="card">Pairs Out<b id="st-shoes">0</b></div>
</div>
<p id="err" class="err" hidden></p>

<section id="checkin"><h2>Check In</h2>
<form id="checkin-form"><input id="ci-name" placeholder="Name or member ID"><button>Check in</button></form>
</section>

<section id="passes"><h2>Sell Day Pass</h2>
<form id="pass-form"><input id="dp-name" placeholder="Name (optional)"><select id="dp-type"></select><input id="dp-qty" type="number" min="1" value="1" style="width:70px"><button>Sell</button></form>
</section>

<section id="shoes"><h2>Shoe Rental</h2>
<form id="shoe-form"><input id="sr-name" placeholder="Name"><select id="sr-size" aria-label="Shoe size"></select><button id="rent-btn">Rent</button></form>
<h3>Shoes Out</h3>
<table><thead><tr><th>Name</th><th>Size</th><th>Since</th><th></th></tr></thead><tbody id="out"></tbody></table>
<p id="out-empty" hidden>No shoes out.</p>
</section>

<section id="activity"><h2>Today's Activity</h2>
<table><thead><tr><th>Name</th><th>Item</th><th>Status</th><th>Time</th><th>Amount</th></tr></thead><tbody id="log"></tbody></table>
<p id="empty" hidden>No activity yet today.</p>
</section>
</main>

<script>
// Prices are placeholders. Set them to match your price list before Monday.
const CONFIG = {
  passes: [
    {id: 'adult', label: 'Adult day pass', price: 25},
    {id: 'youth', label: 'Youth day pass', price: 18}
  ],
  shoeRental: {price: 6}
};
const SIZES = Array.from({length: 23}, (_, i) => String(3 + i * 0.5)); // 3 to 14, half sizes

// Data is kept in this browser's localStorage. Swap load/save for your backend when it is ready.
const KEY = 'frontDesk.v1';
let state = JSON.parse(localStorage.getItem(KEY)) || {log: [], shoesOut: []};

const $ = id => document.getElementById(id);
const save = () => localStorage.setItem(KEY, JSON.stringify(state));
const dayOf = iso => new Date(iso).toLocaleDateString();
const timeOf = iso => new Date(iso).toLocaleTimeString([], {hour: 'numeric', minute: '2-digit'});
const money = n => '$' + n.toFixed(2);
const showErr = msg => { $('err').textContent = msg; $('err').hidden = !msg; };
const cell = text => { const td = document.createElement('td'); td.textContent = text; return td; };

function record(kind, name, item, status, amount = 0) {
  state.log.unshift({kind, name, item, status, amount, time: new Date().toISOString()});
  save();
  render();
}

function checkIn(e) {
  e.preventDefault();
  const name = $('ci-name').value.trim();
  if (!name) return showErr('Enter a name or member ID to check in.');
  showErr('');
  record('checkin', name, 'Gym entry', 'Checked in');
  $('ci-name').value = '';
}

function sellPass(e) {
  e.preventDefault();
  const pass = CONFIG.passes.find(p => p.id === $('dp-type').value);
  const qty = parseInt($('dp-qty').value, 10);
  if (!(qty > 0)) return showErr('Quantity must be at least 1.');
  showErr('');
  record('pass', $('dp-name').value.trim() || 'Walk-in', `${qty} × ${pass.label}`, 'Paid', pass.price * qty);
  $('dp-name').value = '';
  $('dp-qty').value = 1;
}

function rentShoes(e) {
  e.preventDefault();
  const name = $('sr-name').value.trim();
  if (!name) return showErr('Enter a name for the shoe rental.');
  showErr('');
  const size = $('sr-size').value;
  state.shoesOut.push({name, size, since: new Date().toISOString()});
  record('rent', name, `Shoes (size ${size})`, 'Rented', CONFIG.shoeRental.price);
  $('sr-name').value = '';
}

function returnShoes(i) {
  const s = state.shoesOut.splice(i, 1)[0];
  record('return', s.name, `Shoes (size ${s.size})`, 'Returned');
  save();
}

function render() {
  const today = new Date().toLocaleDateString();
  const todays = state.log.filter(r => dayOf(r.time) === today);
  const count = kind => todays.filter(r => r.kind === kind).length;
  const revenue = todays.reduce((sum, r) => sum + r.amount, 0);

  $('st-checkins').textContent = count('checkin');
  $('st-passes').textContent = count('pass');
  $('st-revenue').textContent = money(revenue);
  $('st-shoes').textContent = state.shoesOut.length;

  $('log').replaceChildren(...todays.map(r => {
    const tr = document.createElement('tr');
    tr.append(cell(r.name), cell(r.item), cell(r.status), cell(timeOf(r.time)), cell(r.amount ? money(r.amount) : '—'));
    return tr;
  }));
  $('empty').hidden = todays.length > 0;

  $('out').replaceChildren(...state.shoesOut.map((s, i) => {
    const tr = document.createElement('tr');
    const btn = document.createElement('button');
    btn.textContent = 'Return';
    btn.className = 'secondary';
    btn.onclick = () => returnShoes(i);
    const actions = cell('');
    actions.appendChild(btn);
    tr.append(cell(s.name), cell(s.size), cell(timeOf(s.since)), actions);
    return tr;
  }));
  $('out-empty').hidden = state.shoesOut.length > 0;
}

CONFIG.passes.forEach(p => $('dp-type').add(new Option(`${p.label} (${money(p.price)})`, p.id)));
SIZES.forEach(s => $('sr-size').add(new Option(s, s)));
$('rent-btn').textContent = `Rent (${money(CONFIG.shoeRental.price)})`;

$('checkin-form').addEventListener('submit', checkIn);
$('pass-form').addEventListener('submit', sellPass);
$('shoe-form').addEventListener('submit', rentShoes);
render();
</script>
</body></html>
```

**Next steps:** Set your real prices in `CONFIG`. Then decide whether you need shared storage before Monday, since that is the one piece that needs your backend.
