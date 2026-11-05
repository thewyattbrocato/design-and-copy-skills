I fixed the keyboard and screen-reader problems and added the missing `step()` logic. I haven't run it in a browser, and I couldn't see your stylesheet.

```html
<a class='skip' href='#app'>Skip to main content</a>
<header class='top'><a href='/'>Harbourline Ferries</a></header>
<main id='app'>
  <section id='browse' aria-labelledby='h-browse'>
    <h1 id='h-browse' tabindex='-1'>Sailings from Pell Quay</h1>
    <img src='/img/fares.png' alt='Fares: Adult £14, Child £7' width='320'>
    <div class='row'>
      <span id='l-adult'>Adult day return</span>
      <div class='qty' role='group' aria-labelledby='l-adult'>
        <button type='button' class='btn' aria-label='Remove one adult ticket' onclick='step("adult",-1)'><span aria-hidden='true'>-</span></button>
        <span id='q-adult' role='status'>0</span>
        <button type='button' class='btn' aria-label='Add one adult ticket' onclick='step("adult",1)'><span aria-hidden='true'>+</span></button>
      </div>
    </div>
    <div class='row'>
      <span id='l-child'>Child day return</span>
      <div class='qty' role='group' aria-labelledby='l-child'>
        <button type='button' class='btn' aria-label='Remove one child ticket' onclick='step("child",-1)'><span aria-hidden='true'>-</span></button>
        <span id='q-child' role='status'>0</span>
        <button type='button' class='btn' aria-label='Add one child ticket' onclick='step("child",1)'><span aria-hidden='true'>+</span></button>
      </div>
    </div>
    <a href='#checkout'>Go to checkout</a>
  </section>

  <section id='checkout' aria-labelledby='h-checkout' hidden>
    <h1 id='h-checkout' tabindex='-1'>Your details</h1>
    <form id='pay' onsubmit='return pay(event)'>
      <label for='nm'>Full name</label>
      <input id='nm' autocomplete='name' required>
      <label for='em'>Email</label>
      <input id='em' type='email' autocomplete='email' required>
      <button type='submit'>Pay now</button>
    </form>
  </section>
</main>
<div class='basket-bar' style='position:fixed;bottom:0;left:0;right:0'>
  Basket: <span id='total' role='status'>£0</span>
</div>

<style>
  /* accessibility only: no visual change to the existing design */
  .skip{position:absolute;left:-9999px}
  .skip:focus{left:8px;top:8px;background:#fff;padding:.5em;z-index:10}
  button.btn{font:inherit;color:inherit;cursor:pointer}   /* make real buttons match the old divs */
  button.btn[aria-disabled='true']{opacity:.5;cursor:default}
  :focus-visible{outline:3px solid #005fcc;outline-offset:2px}
  h1:focus{outline:none}                                   /* heading is only a focus target for the view change */
  html{scroll-padding-bottom:4rem}                         /* stops the fixed basket bar covering focused items */
  main{padding-bottom:4rem}
</style>

<script>
const PRICE = {adult:14, child:7};
const qty   = {adult:0, child:0};
const TITLES = {browse:'Sailings from Pell Quay', checkout:'Your details'};
const SITE = 'Harbourline Ferries';

function step(kind, d){
  qty[kind] = Math.max(0, qty[kind] + d);
  document.getElementById('q-' + kind).textContent = qty[kind];
  document.getElementById('total').textContent =
    '£' + (qty.adult*PRICE.adult + qty.child*PRICE.child);
  // use aria-disabled (not disabled) so focus isn't dropped when hitting 0
  document.querySelectorAll('#browse .qty').forEach(g => {
    const k = g.querySelector('[id^=q-]').id.slice(2);
    g.querySelector('button').setAttribute('aria-disabled', qty[k] === 0);
  });
}

function show(id, moveFocus){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  document.title = TITLES[id] + ' – ' + SITE;
  if (moveFocus){
    const h = document.querySelector('#' + id + ' h1');
    h.focus();
    window.scrollTo(0, 0);
  }
}

// hash routing: the link works with keyboard, Back button works, and the view is linkable
function route(moveFocus){
  show(location.hash === '#checkout' ? 'checkout' : 'browse', moveFocus);
}
window.addEventListener('hashchange', () => route(true));
route(false);
step('adult', 0); step('child', 0);

function pay(e){
  e.preventDefault();
  // TODO: hook up real payment submission
  return false;
}
</script>
```

**What was wrong, and what I changed**
- **Losing her place:** switching views hid one section and showed another, so focus stayed on a link that had just vanished. `show()` now moves focus to the new page's heading.
- **Not knowing what page she's on:**
  - The page title now changes with each view.
  - The heading receives focus, so a screen reader announces it.
  - The views use hash routing (`#checkout`), so the browser Back button works too.
- **+/- controls:** these were `div`s with `onmousedown`, so they couldn't be tabbed to or pressed with Enter or Space. They are now real `<button>`s with labels like "Add one adult ticket".
- **Counts and total:** these are now `role="status"`, so changes are announced. The minus button uses `aria-disabled` at 0 rather than `disabled`, so focus isn't dropped.
- **"Go to checkout":** this was `href="#"` plus JS, which jumped to the top of the page. It's now a real link to `#checkout`.
- **Checkout form:** "Pay now" wasn't inside a `<form>`, so Enter did nothing. It is now, with `required` fields.
- **Fares image:** it had empty alt text, but the fares exist only in the image. It now has the fares as alt text.
- **Smaller fixes:**
  - There's a skip link.
  - A visible focus ring appears on keyboard focus only.
  - The fixed basket bar no longer covers focused elements.

**Things to check before Friday**
1. **Missing `step()`:** it wasn't in what you pasted, so I wrote one using £14 and £7. If you already have one, merge the `aria-disabled` bit and drop mine.
2. **Pay now does nothing:** the `pay()` handler is a placeholder. Payment still needs wiring up, so make sure that exists elsewhere.
3. **Look:** I couldn't see your CSS, so the `button.btn` reset is a guess. If the buttons look different, adjust that rule.
4. **Focus ring:** if your CSS has `outline: none` on links or buttons, it will override my focus ring, so remove it.
5. **Page setup:** make sure the page has `<html lang="en">` and a `<title>`.
6. **Test:** tab through it yourself with a keyboard, and ideally ask the customer to try it.
