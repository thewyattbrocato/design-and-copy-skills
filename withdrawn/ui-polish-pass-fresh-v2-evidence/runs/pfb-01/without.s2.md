I couldn't save the file because the Write tool is disabled in this session. The full corrected page is below, so you can paste it over your current file. I haven't run it in a browser, so please do one Tab-only pass before launch.

**What was causing her to get lost**
- **Mouse-only controls:** `+` and `−` were `<div>`s that reacted to `mousedown`. A keyboard can't reach them or activate them. They are now real `<button>`s that respond to `click` (so Enter and Space work), with labels such as "Add one veg box".
- **Focus left behind on view changes:** when "View basket" or "Checkout" hid a section, focus stayed on a hidden element. Focus now moves to the new section's heading, and the page title updates.
- **Prices were invisible to screen readers:** the prices exist only as images with empty `alt`. I set the alt text to "Price: £8.50" and "Price: £6.00", taken from your `prices` object. Please check these match the images.
- **No feedback on quantity or total changes:** the quantities and total are now live regions, so changes get announced.
- **No way back:** I added "Back to boxes" and "Back to basket" buttons.
- **Fixed bar hiding content:** I added bottom padding so the basket bar doesn't cover the last content when tabbing or scrolling.
- **Focus outline:** I kept the browser's default outline, and the button reset keeps the circles looking as they do now.

**Things that were unfinished (you may want to check these)**
- **Basket list:** `#lines` was never filled, so the basket was always empty. It now lists each item, line totals and the overall total, with an "empty" message when there's nothing in it.
- **Place order:** it did nothing useful before. It now shows a "Thank you" view, but nothing is sent anywhere because there's no backend in what you shared. I left a `TODO` where the order needs to be submitted. Please don't launch with that unresolved.

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Order boxes – greenbarrow food co-op</title>
</head>
<body>
<header><h1>greenbarrow food co-op</h1></header>
<main>
 <section id="browse" aria-labelledby="h-browse">
  <h2 id="h-browse" tabindex="-1">This week's boxes</h2>
  <article class="item">
   <h3 id="n-veg">Veg box</h3>
   <img src="veg-box-price.png" alt="Price: £8.50">
   <div class="qty" role="group" aria-labelledby="n-veg">
    <button type="button" class="minus" data-id="veg" aria-label="Remove one veg box">-</button><span id="q-veg" aria-live="polite" aria-label="Veg boxes in basket">0</span><button type="button" class="plus" data-id="veg" aria-label="Add one veg box">+</button>
   </div>
  </article>
  <article class="item">
   <h3 id="n-eggs">Eggs and honey</h3>
   <img src="eggs-honey-price.png" alt="Price: £6.00">
   <div class="qty" role="group" aria-labelledby="n-eggs">
    <button type="button" class="minus" data-id="eggs" aria-label="Remove one eggs and honey box">-</button><span id="q-eggs" aria-live="polite" aria-label="Eggs and honey boxes in basket">0</span><button type="button" class="plus" data-id="eggs" aria-label="Add one eggs and honey box">+</button>
   </div>
  </article>
 </section>
 <section id="basket" aria-labelledby="h-basket" hidden>
  <h2 id="h-basket" tabindex="-1">Your basket</h2>
  <p id="empty" hidden>Your basket is empty.</p>
  <ul id="lines"></ul>
  <button type="button" id="back-browse">Back to boxes</button>
  <button type="button" id="to-checkout">Checkout</button>
 </section>
 <section id="checkout" aria-labelledby="h-checkout" hidden>
  <h2 id="h-checkout" tabindex="-1">Collection details</h2>
  <form>
   <label for="fname">Full name</label><input id="fname" autocomplete="name" required>
   <label for="phone">Phone</label><input id="phone" type="tel" autocomplete="tel" required>
   <button type="button" id="back-basket">Back to basket</button>
   <button type="submit">Place order</button>
  </form>
 </section>
 <section id="done" aria-labelledby="h-done" hidden>
  <h2 id="h-done" tabindex="-1">Thank you</h2>
  <p>Your order has been received. See you at collection.</p>
 </section>
</main>
<div class="basket-bar"><span id="total" role="status" aria-label="Basket total">£0.00</span><button type="button" id="go">View basket</button></div>
<script>
 const prices = {veg: 8.5, eggs: 6};
 const names = {veg: 'Veg box', eggs: 'Eggs and honey'};
 const qty = {veg: 0, eggs: 0};
 const money = n => '£' + n.toFixed(2);
 function total(){ let t = 0; for (const k in qty) t += qty[k]*prices[k]; return t; }
 function show(id){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  if (id === 'basket') renderBasket();
  const h = document.querySelector('#' + id + ' h2');
  h.focus();
  window.scrollTo(0, 0);
  document.title = h.textContent + ' – greenbarrow food co-op';
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
  document.getElementById('empty').hidden = !empty;
  document.getElementById('to-checkout').hidden = empty;
  if (!empty){
   const li = document.createElement('li');
   li.innerHTML = '<strong>Total: ' + money(total()) + '</strong>';
   ul.appendChild(li);
  }
 }
 document.querySelectorAll('.plus').forEach(b => b.addEventListener('click', () => { qty[b.dataset.id]++; refresh(); }));
 document.querySelectorAll('.minus').forEach(b => b.addEventListener('click', () => { if (qty[b.dataset.id] > 0) qty[b.dataset.id]--; refresh(); }));
 document.getElementById('go').onclick = () => show('basket');
 document.getElementById('to-checkout').onclick = () => show('checkout');
 document.getElementById('back-browse').onclick = () => show('browse');
 document.getElementById('back-basket').onclick = () => show('basket');
 document.querySelector('#checkout form').addEventListener('submit', e => {
  e.preventDefault();
  // TODO: send the order somewhere – there is no backend wired up yet.
  show('done');
 });
</script>
<style>
 main{padding-bottom:72px}
 .basket-bar{position:fixed;left:0;right:0;bottom:0;display:flex;justify-content:space-between;padding:12px 20px;background:#2f5d3a;color:#fff}
 .plus,.minus{display:inline-block;width:32px;height:32px;padding:0;font:inherit;color:inherit;background:none;line-height:32px;text-align:center;border:1px solid #2f5d3a;border-radius:50%;cursor:pointer}
 .basket-bar button:focus-visible{outline:2px solid #fff;outline-offset:2px}
 h2:focus{outline:none}
</style>
</body>
</html>
```

**Before the weekend**
1. Tab through the whole flow without a mouse: browse, add items, view basket, checkout, place order.
2. Ideally, get your member to try it. She'll catch things I can't.
3. Wire up order submission.

The browser Back button still doesn't move between views. I can add that if you want it.
