I haven't saved this to a file or run it, because I only have the snippet and not your CSS or `step()`. This is the updated markup:

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
        <span id='q-adult' aria-live='polite' aria-atomic='true'>0</span>
        <button type='button' class='btn' aria-label='Add one adult ticket' onclick='step("adult",1)'>+</button>
      </div>
    </div>
    <div class='row' role='group' aria-labelledby='l-child'>
      <span id='l-child'>Child day return</span>
      <div class='qty'>
        <button type='button' class='btn' aria-label='Remove one child ticket' onclick='step("child",-1)'>-</button>
        <span id='q-child' aria-live='polite' aria-atomic='true'>0</span>
        <button type='button' class='btn' aria-label='Add one child ticket' onclick='step("child",1)'>+</button>
      </div>
    </div>
    <a href='#checkout' onclick='event.preventDefault();show("checkout")'>Go to checkout</a>
  </section>

  <section id='checkout' hidden aria-labelledby='h-checkout'>
    <h1 id='h-checkout' tabindex='-1'>Your details</h1>
    <form id='pay-form'>
      <label for='nm'>Full name</label><input id='nm' autocomplete='name' required>
      <label for='em'>Email</label><input id='em' type='email' autocomplete='email' required>
      <button type='submit'>Pay now</button>
    </form>
  </section>
</main>
<div class='basket-bar' role='status' style='position:fixed;bottom:0;left:0;right:0'>Basket: <span id='total'>£0</span></div>

<style>
  html { scroll-padding-bottom: 4rem; }          /* focused items don't hide behind the fixed basket bar */
  h1:focus { outline: none; }                    /* heading is a focus target, not a control */
  a:focus-visible, button:focus-visible, input:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
</style>

<script>
const TITLES = {
  browse:   'Sailings from Pell Quay – Harbourline Ferries',
  checkout: 'Your details – Harbourline Ferries'
};
function show(id, push = true){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  document.title = TITLES[id];
  document.querySelector('#' + id + ' h1').focus();   // moves keyboard + screen reader position to the new page
  window.scrollTo(0, 0);
  if (push) history.pushState({id}, '', '#' + id);
}
window.addEventListener('popstate', e => show((e.state && e.state.id) || 'browse', false));
history.replaceState({id:'browse'}, '', location.pathname);
document.title = TITLES.browse;
</script>
```

**What was wrong and what I changed**
- **Quantity buttons:** they were `<div>`s with `onmousedown`, so the keyboard couldn't reach or press them. They're now real `<button>`s using `onclick`, with labels such as "Add one adult ticket". Changes to the count and the basket total are announced to screen readers.
- **Losing her place:** switching sections left focus on a control that had just been hidden. `show()` now moves focus to the new page's heading, scrolls to the top, and updates `document.title`.
- **Not knowing which page she's on:** the title now changes per page. Browser Back and Forward also work between the sailings and checkout views. Previously they left the site.
- **Fares image:** it had `alt=''`, so the prices were only visible in the picture. The alt text now carries them. Putting the prices in real text would be better still.
- **Checkout link:** it's still an `<a>`, so it looks the same, but it now has a real `#checkout` target.
- **"Pay now":** it was a submit button with no form around it. It's now inside a `<form>`, and the fields are marked `required`.
- **Fixed basket bar:** it could cover the field she tabbed to. The `scroll-padding-bottom` rule fixes that without changing how anything looks.

**Things to check before Friday**
- **Button look:** I haven't seen your CSS, so check that `.btn` still looks right on a `<button>`. You may need `font: inherit` and a border or background reset.
- **Focus outlines:** make sure nothing in your CSS has `outline: none`. I added a `:focus-visible` outline, which only appears for keyboard users.
- **Payment submit:** `#pay-form` has no submit handler, so submitting will reload the page. Add `e.preventDefault()` and your payment call. The original button did nothing either.
- **`step()` and `#total`:** `step()` wasn't in what you pasted. It needs to update `#q-…` and `#total`.
- **Language:** the page needs `<lang="en">` on `<html>`. I couldn't see that part of the file.

Once it's deployed, ask her to try it, or tab through it yourself with a screen reader (VoiceOver is built into your Mac).
