Here are the changed pieces. Everything visual is untouched: same markup structure, classes and copy.

**Quantity controls: now real buttons, working by keyboard, with names**
```html
<div class='row'>
  <span id='l-adult'>Adult day return</span>
  <div class='qty' role='group' aria-labelledby='l-adult'>
    <button type='button' class='btn' aria-label='Remove one adult ticket' onclick='step("adult",-1)'>-</button>
    <span id='q-adult' aria-live='polite'>0</span>
    <button type='button' class='btn' aria-label='Add one adult ticket' onclick='step("adult",1)'>+</button>
  </div>
</div>
<div class='row'>
  <span id='l-child'>Child day return</span>
  <div class='qty' role='group' aria-labelledby='l-child'>
    <button type='button' class='btn' aria-label='Remove one child ticket' onclick='step("child",-1)'>-</button>
    <span id='q-child' aria-live='polite'>0</span>
    <button type='button' class='btn' aria-label='Add one child ticket' onclick='step("child",1)'>+</button>
  </div>
</div>
```

**Fares image: the prices were invisible to screen readers**
```html
<img src='/img/fares.png' alt='Fares: Adult £14, Child £7' width='320'>
```

**Navigation: a button instead of a `#` link, plus a skip link, headings that take focus, and a space for the fixed bar**
```html
<a class='skip' href='#app'>Skip to main content</a>
<header class='top'><a href='/'>Harbourline Ferries</a></header>
...
<button type='button' onclick='show("checkout")'>Go to checkout</button>
...
<h1 tabindex='-1'>Sailings from Pell Quay</h1>   <!-- and the same tabindex on the checkout h1 -->
...
<div class='basket-bar' style='position:fixed;bottom:0;left:0;right:0' role='status'>Basket: <span id='total'>£0</span></div>
```
If the checkout link was styled as a link, `button` will need a small style rule to match.

```css
.skip{position:absolute;left:-999px}
.skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:10}
:focus-visible{outline:3px solid #005fcc;outline-offset:2px}
h1:focus{outline:none}              /* programmatic focus only, not a tab stop */
main{padding-bottom:4rem}           /* keeps the last control clear of the fixed basket bar */
html{scroll-padding-bottom:4rem}    /* focused fields don't scroll under it */
button.btn{font:inherit;color:inherit}
```
Pick the focus colour to suit your palette. It needs a 3:1 contrast against the background.

**Script: page changes now move focus, update the title and work with Back**
```js
const TITLES = {browse:'Sailings', checkout:'Your details'};
const FARES = {adult:14, child:7};
const qty = {adult:0, child:0};

function show(id, push = true){
  document.querySelectorAll('main section').forEach(s => s.hidden = s.id !== id);
  document.title = TITLES[id] + ' – Harbourline Ferries';
  if (push) history.pushState({id}, '', '#' + id);
  const h = document.querySelector('#' + id + ' h1');
  h.focus();
  window.scrollTo(0, 0);
}
addEventListener('popstate', e => show(e.state ? e.state.id : 'browse', false));
history.replaceState({id:'browse'}, '');

function step(k, d){
  qty[k] = Math.max(0, qty[k] + d);
  document.getElementById('q-' + k).textContent = qty[k];
  document.getElementById('total').textContent =
    '£' + (qty.adult*FARES.adult + qty.child*FARES.child);
}
```
Your snippet only had `show()`, so `step()` must live elsewhere. Keep yours and just add the two `aria-live` regions above. The one here is a stand-in, with the fares taken from your image comment.

**What was wrong for your customer**
- The `+`/`-` controls were `div`s with `onmousedown`, so keyboard users could neither reach nor use them. This was the main blocker.
- Switching pages left focus on a hidden link, which is why she kept losing her place. Focus now moves to the new page's heading.
- Nothing told her which page she was on. The title and heading focus now announce it.
- Quantity and total changes weren't announced.
- The fixed basket bar could cover focused controls.

**Not done or not checked**
- **Pay now:** it isn't inside a `<form>` and has no handler, so it does nothing. I left it alone because I don't know what payment should do. Wrap it in a form with your submit handler. Add inline errors for the name and email fields too.
- **Testing:** I haven't run this in a browser or with a screen reader. Tab through it once, then try it with VoiceOver, before Friday.
