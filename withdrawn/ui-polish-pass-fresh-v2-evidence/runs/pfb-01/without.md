I couldn't save this to a file because the Write tool is disabled in this session. The full corrected page is below, so you can paste it over your current file. I haven't run it in a browser.

**What was trapping her**
- **The +/- controls were `<div>`s.** A keyboard can't reach or activate them. They're now real `<button>`s with labels like "Add one veg box". I also switched them from `mousedown` to `click`, because Enter and Space only fire `click`.
- **Focus was lost when the view changed.** Pressing "View basket" hid the section she was in, so focus fell back to the top of the page. Now each view change moves focus to that view's heading and updates the page title.
- **There was no way back.** I added "Back to boxes" and "Back to basket" buttons. These are the only visible additions.
- **The basket never showed anything.** `#lines` was never filled. It now lists the items and a total, and shows "Your basket is empty" with Checkout hidden when there's nothing in it.
- **"Place order" did nothing.** It now shows a "Thank you" view. It doesn't send the order anywhere yet, so there's a `TODO` for that.
- **The prices are only in images.** `alt=""` hid them from screen readers. I used "Price: £8.50" and "Price: £6.00" from your script. Please check these match what the images say.
- **Quantity changes were silent.** A polite live region now announces the new quantity and total.
- **The fixed bottom bar could cover focused content.** I added bottom padding and `scroll-padding` so it can't.
- I added a visible focus ring and a `lang`, `title` and viewport tag. The look is otherwise unchanged. The buttons are reset to match your old circles.

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Order – greenbarrow food co-op</title>
</head>
<body>
<header><h1>greenbarrow food co-op</h1></header>
<main>
 <section id="browse" aria-labelledby="h-browse">
  <h2 id="h-browse" tabindex="-1">This week's boxes</h2>
  <article class="item">
   <h3>Veg box</h3>
   <img src="veg-box-price.png" alt="Price: £8.50">
   <div class="qty" role="group" aria-label="Veg box quantity">
    <button type="button" class="minus" data-id="veg" aria-label="Remove one veg box">-</button>
    <span id="q-veg">0</span>
    <button type="button" class="plus" data-id="veg" aria-label="Add one veg box">+</button>
   </div>
  </article>
  <article class="item">
   <h3>Eggs and honey</h3>
   <img src="eggs-honey-price.png" alt="Price: £6.00">
   <div class="qty" role="group" aria-label="Eggs and honey quantity">
    <button type="button" class="minus" data-id="eggs" aria-label="Remove one eggs and honey">-</button>
    <span id="q-eggs">0</span>
    <button type="button" class="plus" data-id="eggs" aria-label="Add one eggs and honey">+</button>
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
  <p>Your order has been placed. We'll see you at collection.</p>
 </section>
</main>
<div class="basket-bar"><span id="total">£0.00</span><button type="button" id="go">View basket</button></div>
<div id="status" class="sr-only" role="status" aria-live="polite"></div>
<script>
 const prices = {veg: 8.5, eggs: 6};
 const names = {veg: 'Veg box', eggs: 'Eggs and honey'};
 const qty = {veg: 0, eggs: 0};
 const $ = id => document.getElementById(id);
 const money = n => '£' + n.toFixed(2);
 const total = () => Object.keys(qty).reduce((t, k) => t + qty[k] * prices[k], 0);

 function show(id){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  if (id === 'basket') renderBasket();
  const h = document.querySelector('#' + id + ' h2');
  h.focus();
  window.scrollTo(0, 0);
  document.title = h.textContent + ' – greenbarrow food co-op';
 }
 function refresh(changed){
  for (const k in qty) $('q-'+k).textContent = qty[k];
  $('total').textContent = money(total());
  if (changed) $('status').textContent = names[changed] + ': ' + qty[changed] + '. Basket total ' + money(total());
 }
 function renderBasket(){
  const ul = $('lines');
  ul.textContent = '';
  const keys = Object.keys(qty).filter(k => qty[k] > 0);
  keys.forEach(k => {
   const li = document.createElement('li');
   li.textContent = names[k] + ' × ' + qty[k] + ' – ' + money(qty[k] * prices[k]);
   ul.appendChild(li);
  });
  if (keys.length) {
   const li = document.createElement('li');
   li.textContent = 'Total: ' + money(total());
   ul.appendChild(li);
  }
  $('empty').hidden = keys.length > 0;
  $('to-checkout').hidden = keys.length === 0;
 }

 document.querySelectorAll('.plus').forEach(b => b.addEventListener('click', () => {
  qty[b.dataset.id]++; refresh(b.dataset.id);
 }));
 document.querySelectorAll('.minus').forEach(b => b.addEventListener('click', () => {
  if (qty[b.dataset.id] > 0) qty[b.dataset.id]--;
  refresh(b.dataset.id);
 }));
 $('go').onclick = () => show('basket');
 $('to-checkout').onclick = () => show('checkout');
 $('back-browse').onclick = () => show('browse');
 $('back-basket').onclick = () => show('basket');
 document.querySelector('#checkout form').addEventListener('submit', e => {
  e.preventDefault();
  // TODO: send the order to wherever the co-op collects orders.
  show('done');
 });
</script>
<style>
 .basket-bar{position:fixed;left:0;right:0;bottom:0;display:flex;justify-content:space-between;padding:12px 20px;background:#2f5d3a;color:#fff}
 main{padding-bottom:70px}
 html{scroll-padding-bottom:70px}
 .plus,.minus{display:inline-block;width:32px;height:32px;padding:0;font:inherit;color:inherit;background:none;line-height:32px;text-align:center;border:1px solid #2f5d3a;border-radius:50%;cursor:pointer}
 button:focus-visible,input:focus-visible{outline:3px solid #1a56db;outline-offset:2px}
 .basket-bar button:focus-visible{outline-color:#fff}
 h2:focus{outline:none}
 .sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
</style>
</body>
</html>
```

Before launch, ask your member to try it with Tab, Shift+Tab, Enter and Space. I haven't tested it with a screen reader. If any of your own CSS styles `button`, check that it doesn't change the circles or hide the focus ring.
