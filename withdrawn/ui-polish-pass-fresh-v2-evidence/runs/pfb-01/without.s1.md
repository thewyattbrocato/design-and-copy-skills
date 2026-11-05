I couldn't save the file. The Write tool is disabled in this session, so I haven't touched your page. Below is the finished version to paste over it (the `<style>` block can stay at the bottom, as in yours). I haven't run it in a browser.

**What was making her get lost**
- **The + and − controls were `<div>`s with `mousedown` handlers.** A keyboard can't reach or activate them, so she couldn't change a quantity at all. They're now real `<button>`s with labels like "Add one veg box", and they use `click`. A reset in the CSS keeps the round green look.
- **The prices were only in the images.** The `alt=""` meant a screen reader skipped them. I used the prices from your script (`Veg box, £8.50` and `Eggs and honey, £6.00`). Check these match what the PNGs say.
- **Switching views left focus on a button that had just been hidden.** Now `show()` moves focus to the new section's heading. The heading has `tabindex="-1"`, so a screen reader announces it.
- **There was no way back from the basket or checkout.** I added "Back" buttons, and the browser Back button now works too (via `pushState` and `popstate`).
- **The basket list was never filled in.** `#lines` was empty, so the basket page showed nothing. It now lists each item with its quantity and line total. An empty basket shows "Your basket is empty" and hides Checkout.
- **Nothing happened on "Place order".** It now shows a thank-you view. It doesn't send the order anywhere, because I don't know where orders should go. There's a `TODO` marking the spot.
- **Quantity and total changes weren't announced.** A visually hidden `role="status"` region now reads out e.g. "Veg box: 1. Total £8.50".
- **Focus indicators.** I added a visible `:focus-visible` ring in a yellow that shows on both the white page and the green bar.
- **The fixed basket bar covered the bottom of the page.** I added bottom padding on `main`.

**Replace the `<body>` markup and `<script>` with this:**

```html
<header><h1>greenbarrow food co-op</h1></header>
<main>
 <section id="browse" aria-labelledby="h-browse">
  <h2 id="h-browse" tabindex="-1">This week's boxes</h2>
  <article class="item">
   <h3>Veg box</h3>
   <img src="veg-box-price.png" alt="Veg box, £8.50">
   <div class="qty" role="group" aria-label="Veg box quantity">
    <button type="button" class="minus" data-id="veg" aria-label="Remove one veg box">-</button>
    <span id="q-veg">0</span>
    <button type="button" class="plus" data-id="veg" aria-label="Add one veg box">+</button>
   </div>
  </article>
  <article class="item">
   <h3>Eggs and honey</h3>
   <img src="eggs-honey-price.png" alt="Eggs and honey, £6.00">
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
  <button type="button" class="back" data-to="browse">Back to boxes</button>
  <button type="button" id="to-checkout">Checkout</button>
 </section>
 <section id="checkout" aria-labelledby="h-checkout" hidden>
  <h2 id="h-checkout" tabindex="-1">Collection details</h2>
  <form>
   <label for="fname">Full name</label><input id="fname" autocomplete="name" required>
   <label for="phone">Phone</label><input id="phone" type="tel" autocomplete="tel" required>
   <button type="button" class="back" data-to="basket">Back to basket</button>
   <button type="submit">Place order</button>
  </form>
 </section>
 <section id="done" aria-labelledby="h-done" hidden>
  <h2 id="h-done" tabindex="-1">Thank you</h2>
  <p id="done-msg"></p>
 </section>
</main>
<div class="basket-bar"><span id="total">£0.00</span><button type="button" id="go">View basket</button></div>
<div id="status" class="sr-only" role="status" aria-live="polite"></div>

<script>
 const prices = {veg: 8.5, eggs: 6};
 const names = {veg: 'Veg box', eggs: 'Eggs and honey'};
 const qty = {veg: 0, eggs: 0};
 const money = n => '£' + n.toFixed(2);
 const total = () => Object.keys(qty).reduce((t, k) => t + qty[k] * prices[k], 0);

 function show(id, opts = {}){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  if (id === 'basket') renderBasket();
  const h = document.querySelector('#' + id + ' h2');
  document.title = h.textContent + ' – Greenbarrow Food Co-op';
  if (!opts.noPush) history.pushState({view: id}, '', '#' + id);
  h.focus();
  window.scrollTo(0, 0);
 }
 function renderBasket(){
  const ul = document.getElementById('lines');
  ul.innerHTML = '';
  for (const k in qty){
   if (!qty[k]) continue;
   const li = document.createElement('li');
   li.textContent = `${names[k]} × ${qty[k]} – ${money(qty[k] * prices[k])}`;
   ul.appendChild(li);
  }
  const empty = total() === 0;
  document.getElementById('empty').hidden = !empty;
  document.getElementById('to-checkout').hidden = empty;
 }
 function refresh(changedId){
  for (const k in qty) document.getElementById('q-' + k).textContent = qty[k];
  document.getElementById('total').textContent = money(total());
  if (changedId) document.getElementById('status').textContent =
   `${names[changedId]}: ${qty[changedId]}. Total ${money(total())}`;
 }
 document.querySelectorAll('.plus').forEach(b => b.addEventListener('click', () => { qty[b.dataset.id]++; refresh(b.dataset.id); }));
 document.querySelectorAll('.minus').forEach(b => b.addEventListener('click', () => { if (qty[b.dataset.id] > 0) qty[b.dataset.id]--; refresh(b.dataset.id); }));
 document.querySelectorAll('.back').forEach(b => b.addEventListener('click', () => show(b.dataset.to)));
 document.getElementById('go').onclick = () => show('basket');
 document.getElementById('to-checkout').onclick = () => show('checkout');
 document.querySelector('#checkout form').addEventListener('submit', e => {
  e.preventDefault();
  document.getElementById('done-msg').textContent =
   `Thanks ${document.getElementById('fname').value}, your order of ${money(total())} is in. We'll text you about collection.`;
  show('done');
  // TODO: send the order to the co-op
 });
 addEventListener('popstate', e => show((e.state && e.state.view) || 'browse', {noPush: true}));
 history.replaceState({view: 'browse'}, '', '#browse');
</script>
```

**Replace your `<style>` with this:**

```html
<style>
 .basket-bar{position:fixed;left:0;right:0;bottom:0;display:flex;justify-content:space-between;padding:12px 20px;background:#2f5d3a;color:#fff}
 .plus,.minus{display:inline-block;width:32px;height:32px;line-height:32px;text-align:center;border:1px solid #2f5d3a;border-radius:50%;cursor:pointer;
  padding:0;margin:0;background:none;color:inherit;font:inherit}
 main{padding-bottom:70px}
 button:focus-visible,input:focus-visible{outline:3px solid #f2b705;outline-offset:2px}
 .basket-bar button:focus-visible{outline-color:#fff}
 [tabindex="-1"]:focus{outline:none}
 .sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
</style>
```

**Other things to check**
- **Page head.** If the full page doesn't already have one, put `<!DOCTYPE html>`, `<html lang="en-GB">`, a `<title>` and a viewport meta tag around it.
- **Colours.** The green bar and the white text are fine. I haven't checked how your page text and the + and − buttons look on the real background.
- **Testing with her.** Before launch, ask her to run through it: Tab to a +, press Enter or Space, then View basket, Checkout and Place order. If you can also try it with VoiceOver (Cmd+F5 on a Mac), that would help.

If you turn Write back on, or tell me where the file should live, I can save it directly.
