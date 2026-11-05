The main problem is that your member can't reach the + and − controls at all. They're `div`s that only respond to `mousedown`, so the keyboard can't focus or press them. Fixing that exposed several related problems, which I've fixed too. The look is unchanged.

**What was wrong, most harmful first**
1. **+/− are unreachable by keyboard** and have no names. They're now real buttons named "Add one Veg box" and so on. They use `click`, so Enter and Space work.
2. **The price exists only in the images, which have `alt=""`.** A screen-reader user never hears it. The alt text now carries the price.
3. **Switching views lost her place.** The old section vanished and focus fell back to the top of the page. Focus now moves to the new section's heading, and the page title updates.
4. **No way back.** There was no route from checkout to basket or from basket to browse. I added two plain "Back" buttons.
5. **The basket list was never filled in.** `#lines` stayed empty. It now lists each box with its quantity and price, and shows a message when the basket is empty.
6. **The form did nothing useful.** It would reload the page and lose what she'd typed. It now has a submit handler with a busy state and an inline error that keeps her input.
7. **The fixed bar covered the last content, and nothing showed where focus was.** I added bottom padding and a visible focus ring, including a white one on the green bar.

```html
<body>
<header><h1>greenbarrow food co-op</h1></header>
<main>
 <section id="browse" aria-labelledby="h-browse">
  <h2 id="h-browse" tabindex="-1">This week's boxes</h2>
  <article class="item">
   <h3>Veg box</h3>
   <img src="veg-box-price.png" alt="£8.50">
   <div class="qty">
    <button type="button" class="minus" data-id="veg" aria-label="Remove one Veg box">-</button>
    <span id="q-veg" role="status" aria-label="Veg box quantity">0</span>
    <button type="button" class="plus" data-id="veg" aria-label="Add one Veg box">+</button>
   </div>
  </article>
  <article class="item">
   <h3>Eggs and honey</h3>
   <img src="eggs-honey-price.png" alt="£6.00">
   <div class="qty">
    <button type="button" class="minus" data-id="eggs" aria-label="Remove one Eggs and honey">-</button>
    <span id="q-eggs" role="status" aria-label="Eggs and honey quantity">0</span>
    <button type="button" class="plus" data-id="eggs" aria-label="Add one Eggs and honey">+</button>
   </div>
  </article>
 </section>
 <section id="basket" hidden aria-labelledby="h-basket">
  <h2 id="h-basket" tabindex="-1">Your basket</h2>
  <p id="empty" hidden>Nothing in your basket yet. Pick a box first.</p>
  <ul id="lines"></ul>
  <button type="button" id="back-browse">Back to boxes</button>
  <button type="button" id="to-checkout">Checkout</button>
 </section>
 <section id="checkout" hidden aria-labelledby="h-checkout">
  <h2 id="h-checkout" tabindex="-1">Collection details</h2>
  <form id="order-form">
   <label for="fname">Full name</label><input id="fname" autocomplete="name" required>
   <label for="phone">Phone</label><input id="phone" type="tel" autocomplete="tel" required>
   <p id="order-error" role="alert" hidden></p>
   <button type="button" id="back-basket">Back to basket</button>
   <button type="submit" id="place">Place order</button>
  </form>
  <p id="done" role="status" hidden></p>
 </section>
</main>
<div class="basket-bar"><span>Total: <span id="total">£0.00</span></span><button id="go">View basket</button></div>
<script>
 const prices = {veg: 8.5, eggs: 6};
 const names = {veg: 'Veg box', eggs: 'Eggs and honey'};
 const qty = {veg: 0, eggs: 0};
 const money = n => '£' + n.toFixed(2);

 function show(id){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  const h = document.querySelector('#' + id + ' h2');
  document.title = h.textContent + ' – greenbarrow food co-op';
  h.focus();
  window.scrollTo(0, 0);
 }
 function renderBasket(){
  const ul = document.getElementById('lines');
  ul.textContent = '';
  let n = 0;
  for (const k in qty){
   if (!qty[k]) continue;
   n++;
   const li = document.createElement('li');
   li.textContent = names[k] + ' × ' + qty[k] + ' – ' + money(qty[k] * prices[k]);
   ul.appendChild(li);
  }
  document.getElementById('empty').hidden = n > 0;
  document.getElementById('to-checkout').hidden = n === 0;
 }
 function refresh(){
  let t = 0;
  for (const k in qty){ document.getElementById('q-'+k).textContent = qty[k]; t += qty[k]*prices[k]; }
  document.getElementById('total').textContent = money(t);
 }
 document.querySelectorAll('.plus').forEach(b => b.addEventListener('click', () => { qty[b.dataset.id]++; refresh(); }));
 document.querySelectorAll('.minus').forEach(b => b.addEventListener('click', () => { if (qty[b.dataset.id] > 0) qty[b.dataset.id]--; refresh(); }));
 document.getElementById('go').onclick = () => { renderBasket(); show('basket'); };
 document.getElementById('back-browse').onclick = () => show('browse');
 document.getElementById('to-checkout').onclick = () => show('checkout');
 document.getElementById('back-basket').onclick = () => { renderBasket(); show('basket'); };

 // TODO: replace with the real order endpoint. Nothing is sent until you do.
 async function submitOrder(order){ throw new Error('not connected'); }

 document.getElementById('order-form').addEventListener('submit', async e => {
  e.preventDefault();
  const btn = document.getElementById('place'), err = document.getElementById('order-error');
  err.hidden = true;
  btn.disabled = true; btn.textContent = 'Placing order…';
  try {
   await submitOrder({name: fname.value, phone: phone.value, qty});
   e.target.hidden = true;
   const done = document.getElementById('done');
   done.textContent = 'Thanks, ' + fname.value + ' – your order is placed.';
   done.hidden = false;
  } catch (x) {
   err.textContent = "Your order wasn't sent. Your details are still here – please try again.";
   err.hidden = false;
  } finally {
   btn.disabled = false; btn.textContent = 'Place order';
  }
 });
 refresh();
</script>
<style>
 main{padding-bottom:72px}
 .basket-bar{position:fixed;left:0;right:0;bottom:0;display:flex;justify-content:space-between;padding:12px 20px;background:#2f5d3a;color:#fff}
 .plus,.minus{display:inline-block;width:32px;height:32px;line-height:32px;padding:0;font:inherit;color:inherit;background:none;text-align:center;border:1px solid #2f5d3a;border-radius:50%;cursor:pointer}
 :focus-visible{outline:3px solid #2f5d3a;outline-offset:2px}
 .basket-bar :focus-visible{outline-color:#fff}
 h2:focus{outline:none}
</style>
</body>
```

**Still needed**
- **Orders are not sent yet.** `submitOrder` is a placeholder that always fails, so the form currently shows the "wasn't sent" message. Point it at your real order endpoint before launch. I didn't make up an endpoint, and I didn't want a fake "order placed" message to go live.
- **Your snippet is only the `<body>`.** Make sure the page has `<html lang="en">`, a `<title>` and `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- **I haven't run any of this.** I haven't tried it in a browser or with a screen reader. Please have your keyboard-only member try it before the weekend.
