I haven't run this, and there's no file in the working directory, so here's the finished version to paste in. The problems were:

- **Keyboard users couldn't use the +/- controls.** They were `<div>`s with `onmousedown`, so they couldn't be tabbed to or activated.
- **Focus stayed on the old link after a view swap.** The link was also an `href='#'` that jumped the page. That's why she keeps losing her place.
- **Nothing said which page she was on.** The title never changed, and screen readers heard nothing.
- **The fares image had `alt=''`, so its prices were hidden from screen readers.**
- **"Pay now" wasn't in a `<form>`,** so Enter did nothing.

```html
<header class='top'><a href='/'>Harbourline Ferries</a></header>
<main id='app'>
  <section id='browse' aria-labelledby='h-browse'>
    <h1 id='h-browse' tabindex='-1'>Sailings from Pell Quay</h1>
    <img src='/img/fares.png' alt='Fares: Adult £14, Child £7' width='320'>
    <div class='row' role='group' aria-labelledby='l-adult'>
      <span id='l-adult'>Adult day return</span>
      <div class='qty'>
        <button type='button' class='btn' aria-label='Remove one adult ticket' onclick='step("adult",-1)'>-</button>
        <span id='q-adult' role='status' aria-label='Adult tickets'>0</span>
        <button type='button' class='btn' aria-label='Add one adult ticket' onclick='step("adult",1)'>+</button>
      </div>
    </div>
    <div class='row' role='group' aria-labelledby='l-child'>
      <span id='l-child'>Child day return</span>
      <div class='qty'>
        <button type='button' class='btn' aria-label='Remove one child ticket' onclick='step("child",-1)'>-</button>
        <span id='q-child' role='status' aria-label='Child tickets'>0</span>
        <button type='button' class='btn' aria-label='Add one child ticket' onclick='step("child",1)'>+</button>
      </div>
    </div>
    <a href='#checkout'>Go to checkout</a>
  </section>

  <section id='checkout' aria-labelledby='h-checkout' hidden>
    <h1 id='h-checkout' tabindex='-1'>Your details</h1>
    <form id='pay' onsubmit='return pay(event)'>
      <label for='nm'>Full name</label><input id='nm' autocomplete='name' required>
      <label for='em'>Email</label><input id='em' type='email' autocomplete='email' required>
      <button type='submit'>Pay now</button>
    </form>
  </section>
</main>
<div class='basket-bar' style='position:fixed;bottom:0;left:0;right:0'>
  Basket: <span id='total' role='status'>£0</span>
</div>

<script>
const PRICE = {adult: 14, child: 7};
const qty = {adult: 0, child: 0};
const TITLES = {browse: 'Sailings from Pell Quay', checkout: 'Your details'};

function step(kind, d){
  qty[kind] = Math.max(0, qty[kind] + d);
  document.getElementById('q-' + kind).textContent = qty[kind];
  const t = qty.adult * PRICE.adult + qty.child * PRICE.child;
  document.getElementById('total').textContent = '£' + t;
}

function show(id, moveFocus){
  if (!TITLES[id]) id = 'browse';
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  document.title = TITLES[id] + ' – Harbourline Ferries';
  if (moveFocus) {
    const h = document.querySelector('#' + id + ' h1');
    h.focus();
    window.scrollTo(0, 0);
  }
}

// Hash routing: Back/Forward work, and the link is a real link.
window.addEventListener('hashchange', () => show(location.hash.slice(1), true));
show(location.hash.slice(1), false);

function pay(e){
  e.preventDefault();
  // TODO: hook up real payment submission here
  return false;
}
</script>
```

Add two lines to your CSS. Neither changes how the page looks.

```css
html { scroll-padding-bottom: 4rem; }   /* focused fields don't hide behind the fixed basket bar */
main { padding-bottom: 4rem; }
```

Things to check before Friday:
- **`step()` wasn't in what you pasted.** I wrote one using £14 and £7. If you already have one, keep yours and just make sure it updates `#total`.
- **The `<button>` elements need your `.btn` styling to carry over.** Add `font: inherit` and check that the border, background and padding match the old divs. If the page used `div.btn` selectors, change them to `.btn`.
- **Don't remove focus outlines.** If your CSS has `outline: none` anywhere, replace it with a visible `:focus-visible` style. I couldn't see your CSS.
- **"Pay now" doesn't pay yet.** The `pay()` function is a placeholder, so wire in your real submission.
- **There's no "back to sailings" link on checkout.** The browser Back button now works, but a visible link would be kinder. I left it out to keep the look unchanged.
- **Test it with the keyboard.** Tab through the page, press Enter on "Go to checkout" and check that focus lands on "Your details". Then ask your customer to try it if you can.
