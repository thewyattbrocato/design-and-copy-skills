I've finished the page for keyboard use and left the look alone. I haven't run it or tried it with a screen reader. Here's the whole file, since most of it changed:

```html
<body>
<header><h1>greenbarrow food co-op</h1></header>
<main>
 <section id="browse">
  <h2 tabindex="-1">This week's boxes</h2>
  <article class="item">
   <h3>Veg box</h3>
   <img src="veg-box-price.png" alt="£8.50">
   <div class="qty" role="group" aria-label="Veg box quantity">
    <button type="button" class="minus" data-id="veg" aria-label="Remove one veg box">-</button>
    <span id="q-veg" aria-live="polite">0</span>
    <button type="button" class="plus" data-id="veg" aria-label="Add one veg box">+</button>
   </div>
  </article>
  <article class="item">
   <h3>Eggs and honey</h3>
   <img src="eggs-honey-price.png" alt="£6.00">
   <div class="qty" role="group" aria-label="Eggs and honey quantity">
    <button type="button" class="minus" data-id="eggs" aria-label="Remove one eggs and honey">-</button>
    <span id="q-eggs" aria-live="polite">0</span>
    <button type="button" class="plus" data-id="eggs" aria-label="Add one eggs and honey">+</button>
   </div>
  </article>
 </section>
 <section id="basket" hidden>
  <h2 tabindex="-1">Your basket</h2>
  <p id="empty">Your basket is empty. Add a box to get started.</p>
  <ul id="lines"></ul>
  <button type="button" id="keep-shopping">Back to boxes</button>
  <button type="button" id="to-checkout">Checkout</button>
 </section>
 <section id="checkout" hidden>
  <h2 tabindex="-1">Collection details</h2>
  <form>
   <label for="fname">Full name</label><input id="fname" autocomplete="name" required>
   <label for="phone">Phone</label><input id="phone" type="tel" autocomplete="tel" required>
   <p id="form-status" role="status"></p>
   <button type="button" id="back-basket">Back to basket</button>
   <button type="submit">Place order</button>
  </form>
 </section>
</main>
<div class="basket-bar"><span>Total: <span id="total" aria-live="polite">£0.00</span></span><button type="button" id="go">View basket</button></div>
<script>
 const prices = {veg: 8.5, eggs: 6};
 const names = {veg: 'Veg box', eggs: 'Eggs and honey'};
 const qty = {veg: 0, eggs: 0};
 const money = n => '£' + n.toFixed(2);

 function show(id, push = true){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  if (id === 'basket') renderBasket();
  if (push) history.pushState({v: id}, '');
  const h = document.querySelector('#' + id + ' h2');
  h.focus(); h.scrollIntoView({block: 'start'});
 }
 window.addEventListener('popstate', e => show((e.state && e.state.v) || 'browse', false));
 history.replaceState({v: 'browse'}, '');

 function refresh(){
  let t = 0;
  for (const k in qty){ document.getElementById('q-'+k).textContent = qty[k]; t += qty[k]*prices[k]; }
  document.getElementById('total').textContent = money(t);
  return t;
 }
 function renderBasket(){
  const ul = document.getElementById('lines');
  ul.innerHTML = '';
  let any = false;
  for (const k in qty){
   if (!qty[k]) continue;
   any = true;
   const li = document.createElement('li');
   li.textContent = names[k] + ' × ' + qty[k] + ' — ' + money(qty[k]*prices[k]);
   ul.appendChild(li);
  }
  document.getElementById('empty').hidden = any;
  document.getElementById('to-checkout').hidden = !any;
 }

 document.querySelectorAll('.plus').forEach(b => b.addEventListener('click', () => { qty[b.dataset.id]++; refresh(); }));
 document.querySelectorAll('.minus').forEach(b => b.addEventListener('click', () => { if (qty[b.dataset.id] > 0) qty[b.dataset.id]--; refresh(); }));
 document.getElementById('go').onclick = () => show('basket');
 document.getElementById('keep-shopping').onclick = () => show('browse');
 document.getElementById('to-checkout').onclick = () => show('checkout');
 document.getElementById('back-basket').onclick = () => show('basket');

 // TODO before launch: send the order somewhere (email, sheet, backend).
 async function placeOrder(order){ /* not connected yet */ }
 document.querySelector('#checkout form').addEventListener('submit', async e => {
  e.preventDefault();
  const btn = e.submitter, status = document.getElementById('form-status');
  btn.disabled = true; status.textContent = 'Placing your order…';
  try {
   await placeOrder({qty, name: fname.value, phone: phone.value});
   status.textContent = 'Thank you, ' + fname.value + '. Your order is placed.';
  } catch (err) {
   status.textContent = 'We could not place your order. Your details are kept; please try again.';
   btn.disabled = false;
  }
 });
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

**What was wrong for her, in order of harm**
- **The + and − were `div`s that only reacted to `mousedown`.** She couldn't reach or press them with a keyboard at all. They're now real buttons with names like "Add one veg box". They use `click`, so Enter and Space work. The look is unchanged, with the browser's default button styling reset.
- **Switching views left focus on the old button, which was then hidden.** Focus now moves to the new view's heading. I also added browser Back support, so Back returns to the previous view and not off the page.
- **Basket and checkout were dead ends.** I added "Back to boxes" and "Back to basket" buttons. These are the only new visible elements.
- **The basket list was never filled in.** It now lists each line with its price, and shows an empty message with no Checkout button when there's nothing in it.
- **Submit reloaded the page and lost her details.** It now has a handler with a "Placing your order…" state, a thank-you message and an error message that keeps what she typed.
- **The prices live only in images with empty alt text.** I gave them alt text (£8.50 and £6.00), taken from your `prices` object. Please check that they match the pictures.
- **The fixed bottom bar could cover focused items.** `main` now has bottom padding, and I added a visible focus ring in the existing green (white on the bar).
- **Quantity and total changes are now announced by a screen reader.**

**Before the weekend**
- **`placeOrder` is a stub.** It does nothing, so the page will say "Your order is placed" without sending anything. Wire it to wherever orders go before launch. I didn't want to invent that.
- **The snippet has no `<html lang="en">`, `<title>` or viewport meta tag.** Add them in the document head if they aren't already there.
- **Test it yourself with Tab, Shift+Tab, Enter and Space.** Ideally ask her to try it too.
