Here's the updated page. The look is unchanged, except for the keyboard focus ring, which I explain below.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Upcoming paddles – Events – Canoe club</title>
 <meta name="description" content="Upcoming canoe club paddles: evening estuary trips and weir runs for improvers.">
 <style>
  .nav a{margin-right:14px}
  .card{display:grid;grid-template-columns:1fr auto;gap:8px;border:1px solid #cfd8dc;padding:16px;border-radius:8px}
  /* h2 replaces h4 for a correct heading outline; these rules keep the old h4 look */
  .card h2{font-size:1em;margin:1.33em 0}
  .card .actions{display:contents}
  .card .book{grid-column:2;grid-row:1}
  .card .cancel{grid-column:1;grid-row:1}
  /* Keep a clearly visible focus indicator (the old faint shadow was too subtle) */
  a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid #0078c8;outline-offset:2px}
  .sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  .skip{position:absolute;left:-9999px}
  .skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:10}
 </style>
</head>
<body>
 <a class="skip" href="#main">Skip to main content</a>
 <header class="nav">
  <a href="/"><img src="/logo.svg" alt="Canoe club home"></a>
  <nav aria-label="Main" style="display:inline">
   <a href="/about">About</a><a href="/trips">Trips</a><a href="/kit">Kit hire</a>
   <a href="/safety">Safety</a><a href="/juniors">Juniors</a><a href="/coaching">Coaching</a>
   <a href="/news">News</a><a href="/gallery">Gallery</a><a href="/shop">Shop</a>
   <a href="/join">Join</a><a href="/contact">Contact</a><a href="/login">Member login</a>
  </nav>
  <form role="search" action="/search" style="display:inline">
   <input type="search" name="q" aria-label="Search the site">
  </form>
 </header>
 <main id="main">
  <h1>Upcoming paddles</h1>
  <article class="card">
   <h2>Estuary evening paddle</h2>
   <p>Thursday 7pm, flat water, all abilities.</p>
   <div class="actions">
    <button type="button" class="cancel">Cancel booking<span class="sr-only"> for Estuary evening paddle</span></button>
    <button type="button" class="book">Book a place<span class="sr-only"> on Estuary evening paddle</span></button>
   </div>
  </article>
  <article class="card">
   <h2>Weir run for improvers</h2>
   <p>Saturday 9am, moving water, helmet required.</p>
   <div class="actions">
    <button type="button" class="cancel">Cancel booking<span class="sr-only"> for Weir run for improvers</span></button>
    <button type="button" class="book">Book a place<span class="sr-only"> on Weir run for improvers</span></button>
   </div>
  </article>
 </main>
</body>
</html>
```

**What I changed**
- **Document basics:** I added the doctype and a viewport meta tag, which the page needs to work on phones. I also added a real title and a meta description, replacing "Untitled". The logo path is now `/logo.svg`, so it still loads when the page is served from `/events`.
- **Structure:** The links are now in a labelled `<nav>`, and the search box is in a `role="search"` form. I added a skip link that only shows when focused. Each event is an `<article>`, and the headings go h1 → h2 instead of skipping to h4. The h2 CSS reproduces the old h4 size and spacing, so nothing moves.
- **Buttons:** `.sr-only` was never defined, so "Reserve" was showing as visible text. I defined it. I replaced "Reserve" with hidden text naming the event, so screen readers hear "Book a place on Estuary evening paddle" instead of identical buttons. The visible label comes first in each name, which keeps voice-control users working. The buttons are also `type="button"`.
- **Focus:** `outline:none` plus a faint shadow made keyboard focus nearly invisible. It's now a 2px blue outline on `:focus-visible`, so it appears for keyboard users and not on mouse clicks. This is the only visible change.

**Things for you to decide or wire up**
- **Buttons do nothing yet:** There's no handler or form action. The booking and cancel logic still needs connecting. The search form posts to `/search`, which is my guess, so change it if the real URL differs.
- **Layout and reading order:** The grid puts the buttons above the title and description. A keyboard or screen-reader user meets them after the text, which is out of step with what sighted users see. I left it because you asked me not to restyle. If the committee is open to it, putting the title first would fix it.
- **Buttons shown together:** Every event shows both "Cancel booking" and "Book a place". Production should probably show only the one that applies to the member's state.
- **Logo size:** I didn't add `width` and `height` to the logo because I don't know its dimensions. Adding them stops the page jumping as it loads.
