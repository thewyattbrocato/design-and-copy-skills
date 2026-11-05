I couldn't save the file because the Write tool is disabled in this session. The full updated page is below instead. It has not been run in a browser or tested with a screen reader.

**What was wrong for her**
- **Mouse-only controls:** `+` and `−` were `<div>`s that reacted to `mousedown`, so a keyboard could never reach them. They're now real `<button>`s with names like "Add one veg box", and they act on click.
- **No way to move around:** Basket and Checkout had no Back buttons, and focus stayed on the button that had just been hidden. Each view change now moves focus to the new heading and updates the page title.
- **Empty basket list:** `#lines` was never filled in. It now lists each box with its price and a total, and says so when the basket is empty.
- **Form submit:** the form had no handler, so pressing Place order just reloaded the page. It now has a submit handler with a busy state and an error message that keeps what she typed.
- **Small fixes:**
  - The price images had `alt=""`, so the price was invisible to a screen reader. Their alt text is now the price (I couldn't see the images, so check these match).
  - Quantities are announced when they change.
  - There's a visible focus ring.
  - The fixed bottom bar is hidden outside Browse, and the page has bottom padding so the bar can't cover focused items.

The look is unchanged. The buttons are styled to match the old circles.

**Before the weekend:** the file has no order endpoint, so I added `const ORDER_URL = ''`. While it's empty, Place order shows "Your order hasn't been sent". It never shows a false success. Set it to wherever orders should go. I assumed a JSON `POST` of `{name, phone, items}`.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>This week's boxes – greenbarrow food co-op</title>
</head>
<body>
<header><h1>greenbarrow food co-op</h1></header>
<main>
 <section id="browse">
  <h2 tabindex="-1">This week's boxes</h2>
  <article class="item">
   <h3 id="h-veg">Veg box</h3>
   <img src="veg-box-price.png" alt="£8.50">
   <div class="qty" role="group" aria-labelledby="h-veg"><button type="button" class="minus" data-id="veg" aria-label="Remove one veg box">-</button><span id="q-veg" aria-live="polite">0</span><button type="button" class="plus" data-id="veg" aria-label="Add one veg box">+</button></div>
  </article>
  <article class="item">
   <h3 id="h-eggs">Eggs and honey</h3>
   <img src="eggs-honey-price.png" alt="£6.00">
   <div class="qty" role="group" aria-labelledby="h-eggs"><button type="button" class="minus" data-id="eggs" aria-label="Remove one eggs and honey">-</button><span id="q-eggs" aria-live="polite">0</span><button type="button" class="plus" data-id="eggs" aria-label="Add one eggs and honey">+</button></div>
  </article>
 </section>
 <section id="basket" hidden>
  <h2 tabindex="-1">Your basket</h2>
  <p id="basket-empty" hidden>Your basket is empty. Choose a box to get started.</p>
  <ul id="lines"></ul>
  <p id="basket-total"></p>
  <button type="button" id="basket-back">Back to boxes</button>
  <button type="button" id="to-checkout">Checkout</button>
 </section>
 <section id="checkout" hidden>
  <h2 tabindex="-1">Collection details</h2>
  <form>
   <label for="fname">Full name</label><input id="fname" autocomplete="name" required>
   <label for="phone">Phone</label><input id="phone" type="tel" autocomplete="tel" required>
   <p id="form-error" role="alert" hidden></p>
   <button type="button" id="checkout-back">Back to basket</button>
   <button type="submit">Place order</button>
  </form>
 </section>
 <section id="done" hidden>
  <h2 tabindex="-1">Order sent</h2>
  <p id="done-msg"></p>
 </section>
</main>
<div class="basket-bar"><span id="total">£0.00</span><button id="go">View basket</button></div>
<script>
 const ORDER_URL = ''; // [order endpoint] – set this to where orders should be sent
 const prices = {veg: 8.5, eggs: 6};
 const names = {veg: 'Veg box', eggs: 'Eggs and honey'};
 const titles = {browse: "This week's boxes", basket: 'Your basket', checkout: 'Collection details', done: 'Order sent'};
 const qty = {veg: 0, eggs: 0};
 const money = n => '£' + n.toFixed(2);
 const total = () => Object.keys(qty).reduce((t, k) => t + qty[k]*prices[k], 0);
 function show(id, focus = true){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  document.querySelector('.basket-bar').hidden = id !== 'browse';
  document.title = titles[id] + ' – greenbarrow food co-op';
  if (focus){ document.querySelector('#' + id + ' h2').focus(); window.scrollTo(0, 0); }
 }
 function refresh(){
  for (const k in qty) document.getElementById('q-'+k).textContent = qty[k];
  document.getElementById('total').textContent = money(total());
 }
 function renderBasket(){
  const ul = document.getElementById('lines');
  ul.textContent = '';
  for (const k in qty){
   if (!qty[k]) continue;
   const li = document.createElement('li');
   li.textContent = names[k] + ' × ' + qty[k] + ' – ' + money(qty[k]*prices[k]);
   ul.appendChild(li);
  }
  const empty = total() === 0;
  document.getElementById('basket-empty').hidden = !empty;
  document.getElementById('basket-total').hidden = empty;
  document.getElementById('basket-total').textContent = 'Total: ' + money(total());
  document.getElementById('to-checkout').hidden = empty;
 }
 document.querySelectorAll('.plus').forEach(b => b.addEventListener('click', () => { qty[b.dataset.id]++; refresh(); }));
 document.querySelectorAll('.minus').forEach(b => b.addEventListener('click', () => { if (qty[b.dataset.id] > 0) qty[b.dataset.id]--; refresh(); }));
 document.getElementById('go').onclick = () => { renderBasket(); show('basket'); };
 document.getElementById('basket-back').onclick = () => show('browse');
 document.getElementById('to-checkout').onclick = () => show('checkout');
 document.getElementById('checkout-back').onclick = () => show('basket');

 const form = document.querySelector('form');
 const err = document.getElementById('form-error');
 form.addEventListener('submit', async e => {
  e.preventDefault();
  const btn = form.querySelector('[type=submit]');
  if (btn.disabled) return;
  btn.disabled = true; btn.textContent = 'Sending…'; err.hidden = true;
  try {
   if (!ORDER_URL) throw new Error('no endpoint');
   const r = await fetch(ORDER_URL, {method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({name: form.fname.value, phone: form.phone.value, items: qty})});
   if (!r.ok) throw new Error(r.status);
   document.getElementById('done-msg').textContent = 'Thank you, ' + form.fname.value + '. Your order of ' + money(total()) + ' has been sent.';
   for (const k in qty) qty[k] = 0;
   refresh(); form.reset(); show('done');
  } catch {
   err.textContent = "Your order hasn't been sent. Your details are still here, so you can press Place order to try again.";
   err.hidden = false;
  } finally {
   btn.disabled = false; btn.textContent = 'Place order';
  }
 });
</script>
<style>
 html{scroll-padding-bottom:80px}
 body{padding-bottom:80px}
 .basket-bar{position:fixed;left:0;right:0;bottom:0;display:flex;justify-content:space-between;padding:12px 20px;background:#2f5d3a;color:#fff}
 .basket-bar[hidden]{display:none}
 .plus,.minus{display:inline-block;box-sizing:content-box;width:32px;height:32px;padding:0;font:inherit;line-height:32px;text-align:center;border:1px solid #2f5d3a;border-radius:50%;background:none;color:inherit;cursor:pointer}
 :focus-visible{outline:3px solid #2f5d3a;outline-offset:2px}
 .basket-bar :focus-visible{outline-color:#fff}
</style>
</body>
</html>
```

**Not checked**
- I haven't tabbed through it, tested with a screen reader, or tried 200% zoom or a 320px width.
- The browser Back button still leaves the page rather than going to the previous view. Fixing that is a design decision.
- The "Order sent" wording is mine. Add collection time and place once you've settled them.

Ask your member to try it with the keyboard before launch.
