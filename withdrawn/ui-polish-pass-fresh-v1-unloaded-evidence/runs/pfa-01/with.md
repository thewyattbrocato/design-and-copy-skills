I've fixed the keyboard and screen-reader problems below. I haven't run any of it, so please tab through it once yourself before Friday.

```html
<style>
  /* keep the look: native buttons inherit the page font, nothing else changes */
  :where(button.btn){font:inherit}
  a:focus-visible, button:focus-visible, input:focus-visible,
  h1:focus-visible { outline:2px solid currentColor; outline-offset:2px }
  h1[tabindex='-1']:focus { outline:none }            /* heading is only a focus target, not a control */
  html { scroll-padding-bottom:4rem }                 /* focused items never sit under the basket bar */
  main { padding-bottom:4rem }
</style>

<header class='top'><a href='/'>Harbourline Ferries</a></header>
<main id='app'>
  <section id='browse'>
    <h1 tabindex='-1'>Sailings from Pell Quay</h1>
    <img src='/img/fares.png' alt='Fares: Adult £14, Child £7' width='320'>
    <div class='row'>
      <span id='l-adult'>Adult day return</span>
      <div class='qty' role='group' aria-labelledby='l-adult'>
        <button type='button' class='btn' aria-label='Remove one adult day return' onclick='step("adult",-1)'>-</button>
        <span id='q-adult' aria-live='polite'>0</span>
        <button type='button' class='btn' aria-label='Add one adult day return' onclick='step("adult",1)'>+</button>
      </div>
    </div>
    <div class='row'>
      <span id='l-child'>Child day return</span>
      <div class='qty' role='group' aria-labelledby='l-child'>
        <button type='button' class='btn' aria-label='Remove one child day return' onclick='step("child",-1)'>-</button>
        <span id='q-child' aria-live='polite'>0</span>
        <button type='button' class='btn' aria-label='Add one child day return' onclick='step("child",1)'>+</button>
      </div>
    </div>
    <a href='#checkout'>Go to checkout</a>
  </section>
  <section id='checkout' hidden>
    <a href='#browse'>Back to sailings</a>
    <h1 tabindex='-1'>Your details</h1>
    <label for='nm'>Full name</label><input id='nm' autocomplete='name'>
    <label for='em'>Email</label><input id='em' type='email' autocomplete='email'>
    <button type='submit'>Pay now</button>
  </section>
</main>
<div class='basket-bar' style='position:fixed;bottom:0;left:0;right:0'>Basket: <span id='total' role='status'>£0</span></div>
<script>
var PRICE = {adult:14, child:7}, qty = {adult:0, child:0};
var TITLES = {browse:'Sailings from Pell Quay', checkout:'Your details'};

function step(kind, d){
  qty[kind] = Math.max(0, qty[kind] + d);
  document.getElementById('q-' + kind).textContent = qty[kind];
  document.getElementById('total').textContent =
    '£' + (qty.adult * PRICE.adult + qty.child * PRICE.child);
}

function show(id, moveFocus){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  document.title = TITLES[id] + ' – Harbourline Ferries';
  if (moveFocus) document.querySelector('#' + id + ' h1').focus();
}

function fromHash(){
  var id = location.hash.slice(1);
  return TITLES[id] ? id : 'browse';
}
window.addEventListener('hashchange', () => show(fromHash(), true));
show(fromHash(), false);   // first load: set title/view, don't steal focus
</script>
```

**What was wrong and what I changed, worst first**
1. **The +/- controls were `div`s with `onmousedown`.** A keyboard user couldn't reach or press them. They're now real `<button>`s that act on click. Each has a name that says what it does, such as "Add one adult day return". The quantity is announced when it changes.
2. **`step()` wasn't defined in what you sent.** If it's defined elsewhere, drop my version. If not, the buttons would have thrown errors. I used the £14 and £7 fares from your image comment.
3. **Switching views left focus and the page title where they were.** `show()` now updates the title and moves focus to the new page's heading, so a screen reader announces where she is. On first load it doesn't move focus.
4. **"Go to checkout" was `href='#'` with an `onclick`.** It's now a real `#checkout` link, so the browser's Back button works. That means a keyboard user can go back without losing the basket. I added a "Back to sailings" link on checkout, because the header link reloads the page and empties the basket.
5. **The fares were only inside an image with empty alt text.** Screen-reader users couldn't get the prices, so I put them in the alt text.
6. **The fixed basket bar could cover whatever had focus.** I added bottom padding and scroll margin. The total is also a live region, so changes are announced.
7. **Focus rings.** I couldn't see your CSS. I added a `:focus-visible` outline in the current text colour in case yours was missing or removed. Delete it if you already have one.

**Still open**
- **"Pay now" isn't wired up.** There's no `<form>` or handler, so it does nothing. I didn't invent payment behaviour. The fields also have no validation or error messages yet.
- **Check the +/- buttons against your `.btn` CSS.** Native buttons can pick up default padding or borders if your `.btn` rule doesn't set them. I couldn't see the stylesheet, so I couldn't confirm the look is unchanged.
- **Not checked:** a screen-reader pass, 200% zoom or a 320px width, and forced-colours mode.
