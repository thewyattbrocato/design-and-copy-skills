I've made the page keyboard- and screen-reader-friendly without changing how it looks. I haven't run any of this. Here is the whole file:

```html
<style>
  /* access additions only; nothing here changes the existing look */
  :focus-visible { outline: 3px solid #1a5fb4; outline-offset: 2px; }
  h1:focus { outline: none; }               /* script-focused heading, not a control */
  html { scroll-padding-bottom: 4rem; }     /* keep focused items clear of the fixed basket bar */
  main { padding-bottom: 4rem; }            /* so the last control can scroll above the bar */
</style>

<header class='top'><a href='/'>Harbourline Ferries</a></header>
<main id='app'>
  <section id='browse'>
    <h1 tabindex='-1'>Sailings from Pell Quay</h1>
    <img src='/img/fares.png' alt='Fares: Adult £14, Child £7' width='320'>
    <div class='row' role='group' aria-labelledby='l-adult'>
      <span id='l-adult'>Adult day return</span>
      <div class='qty'>
        <button type='button' class='btn' aria-label='Remove one adult ticket' onclick='step("adult",-1)'>-</button>
        <span id='q-adult' role='status'>0</span>
        <button type='button' class='btn' aria-label='Add one adult ticket' onclick='step("adult",1)'>+</button>
      </div>
    </div>
    <div class='row' role='group' aria-labelledby='l-child'>
      <span id='l-child'>Child day return</span>
      <div class='qty'>
        <button type='button' class='btn' aria-label='Remove one child ticket' onclick='step("child",-1)'>-</button>
        <span id='q-child' role='status'>0</span>
        <button type='button' class='btn' aria-label='Add one child ticket' onclick='step("child",1)'>+</button>
      </div>
    </div>
    <a href='#checkout' onclick='show("checkout"); return false;'>Go to checkout</a>
  </section>
  <section id='checkout' hidden>
    <h1 tabindex='-1'>Your details</h1>
    <form id='pay-form'>
      <label for='nm'>Full name</label><input id='nm' autocomplete='name' required>
      <label for='em'>Email</label><input id='em' type='email' autocomplete='email' required>
      <button type='submit'>Pay now</button>
    </form>
    <a href='#browse' onclick='show("browse"); return false;'>Back to sailings</a>
  </section>
</main>
<div class='basket-bar' style='position:fixed;bottom:0;left:0;right:0'>Basket: <span id='total' role='status'>£0</span></div>
<script>
var TITLES = {
  browse: 'Sailings from Pell Quay – Harbourline Ferries',
  checkout: 'Your details – Harbourline Ferries'
};
function show(id, fromHistory){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  document.title = TITLES[id];
  if (!fromHistory) history.pushState({view: id}, '', '#' + id);
  var h = document.querySelector('#' + id + ' h1');
  h.focus();
  window.scrollTo(0, 0);
}
// Browser Back/Forward move between views instead of leaving the site
window.addEventListener('popstate', function(e){
  show((e.state && e.state.view) || 'browse', true);
});
history.replaceState({view: 'browse'}, '', location.pathname + location.search);
document.title = TITLES.browse;
</script>
```

**What was breaking it for her, most harmful first**
1. **The +/- controls were `div`s with `onmousedown`.** They couldn't be tabbed to or activated from a keyboard. They are now real buttons that act on click, and each is named for what it does, such as "Add one adult ticket".
2. **Focus was lost on every view change.** When the page swapped views, focus stayed on a link that had just been hidden. `show()` now updates the page title and moves focus to the new view's heading, so she hears where she is.
3. **"Go to checkout" jumped to the top of the page.** It was `href='#'` with no `preventDefault`. It now goes to `#checkout` and doesn't jump.
4. **The only fare information was in the image.** Its `alt` was empty, so a screen reader skipped the prices. The alt now states them.
5. **The basket bar covered focused controls.** I added bottom padding and scroll padding so the focus ring never sits behind it.
6. **There was no focus indicator, and no way back from checkout.** I added a `:focus-visible` outline and a "Back to sailings" link. Browser Back now steps between views instead of leaving the site.
7. **Counts and total didn't announce changes.** The counts and total now announce updates politely.
8. **The checkout wasn't a form.** The inputs are now in a `<form>` and marked `required`.

**Still to do before Friday**
- **Payment isn't wired up.** I didn't invent a submit handler. Add `onsubmit` on `#pay-form` yourself, with a busy state on "Pay now" and a visible error that keeps what she typed if payment fails.
- **I couldn't see `step()` or your CSS.** Check that the `<button class='btn'>` elements match the old `div` buttons. If they show a default grey background or border, add `background:none;border:0;font:inherit;color:inherit` to `.btn`. Also check that `step()` updates `#total` and doesn't go below 0. I picked the focus-ring colour, so change it if it clashes.
- **I haven't tested any of it.** That means no keyboard walk-through, screen reader, 200% zoom or 320px width. A quick Tab-through of browse → checkout → back is worth doing.
