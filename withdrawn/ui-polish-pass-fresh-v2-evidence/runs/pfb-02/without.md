I've fixed the accessibility, semantics and robustness problems and left the visual design alone. I haven't run this in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Upcoming paddles – Canoe Club</title>
 <meta name="description" content="Upcoming canoe club paddles: evening estuary trips and weir runs for improvers. Book a place online.">
 <style>
  .nav a{margin-right:14px}
  .nav form{display:inline}
  .card{display:grid;grid-template-columns:1fr auto;gap:8px;border:1px solid #cfd8dc;padding:16px;border-radius:8px}
  .card h2{font-size:1em;margin:1.33em 0}
  .card .actions{display:contents}
  .card .book{grid-column:2;grid-row:1}
  .card .cancel{grid-column:1;grid-row:1}

  /* Keep a clearly visible keyboard focus indicator (the old one was near-invisible) */
  a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid #0078c8;outline-offset:2px}

  /* Visually hidden, still read by screen readers (class was used but never defined) */
  .sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  .skip{position:absolute;left:-9999px}
  .skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:10}
 </style>
</head>
<body>
 <a class="skip" href="#main">Skip to main content</a>
 <header class="nav">
  <nav aria-label="Main">
   <a href="/"><img src="logo.svg" alt="Canoe club home"></a>
   <a href="/about">About</a><a href="/trips">Trips</a><a href="/kit">Kit hire</a>
   <a href="/safety">Safety</a><a href="/juniors">Juniors</a><a href="/coaching">Coaching</a>
   <a href="/news">News</a><a href="/gallery">Gallery</a><a href="/shop">Shop</a>
   <a href="/join">Join</a><a href="/contact">Contact</a><a href="/login">Member login</a>
  </nav>
  <form role="search" action="/search" method="get">
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
- **Document basics:** I added the doctype and a viewport meta tag. The page title was "Untitled", so it now has a real one, plus a meta description.
- **Undefined `.sr-only`:** the class was used but never defined, so "Reserve" was showing as visible text in the buttons. I defined it. The hidden text now names the event, for example "Book a place on Estuary evening paddle". Before, every button on the page read the same to a screen reader.
- **Focus styles:** `outline:none` plus a faint 25% shadow made keyboard focus nearly invisible. I replaced it with a `:focus-visible` outline. Mouse users won't see it.
- **Heading order:** the page jumped from `h1` to `h4`. The cards now use `h2`, with CSS that keeps the original `h4` size and spacing.
- **Landmarks and semantics:** the nav links are in a `<nav>`, the search is a `role="search"` form, and each card is an `<article>`. I added a skip link that only appears on keyboard focus, which helps with 12 nav links.
- **Buttons:** I added `type="button"` so they won't submit a form by accident.

**Things I left alone or need your input on**
- **Button order:** the grid rules put the buttons visually above the title and text, but they come after them in the HTML. I kept that because it's the look the committee approved. A screen reader reads the title first, which is fine.
- **Placeholders:** the buttons have no behavior, and the search form posts to `/search?q=`. I guessed that URL, so check it against your backend.
- **Booking logic:** every event shows both "Cancel booking" and "Book a place". You probably want to show only one, depending on whether the member has booked. That needs your booking logic.
- **Logo:** set `width` and `height` on `logo.svg` to avoid layout shift.
- **Mobile layout:** I haven't tested the nav on narrow screens. With 12 links plus search it will probably wrap awkwardly. Fixing that would change the look, so I left it.
