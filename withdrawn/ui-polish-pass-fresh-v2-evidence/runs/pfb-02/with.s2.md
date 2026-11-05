Here's the full file, since most of the head and markup changed. Colours, spacing, card layout and copy are the same as before.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Upcoming paddles</title>
 <style>
  .nav a{margin-right:14px}
  .card{display:grid;grid-template-columns:1fr auto;gap:8px;border:1px solid #cfd8dc;padding:16px;border-radius:8px}
  .card > *{min-width:0;overflow-wrap:anywhere}
  .card h2{font-size:1em;margin:1.33em 0}
  .card .actions{display:contents}
  .card .book{grid-column:2;grid-row:1}
  .card .cancel{grid-column:1;grid-row:1}
  .nav form{display:inline}

  /* focus: replaces the faint glow, which was too weak to see */
  a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid #0b5cad;outline-offset:2px;box-shadow:0 0 0 4px rgba(11,92,173,.25)}

  .sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  .skip{position:absolute;left:8px;top:-48px;background:#fff;padding:8px 12px;border:1px solid #0b5cad;z-index:10}
  .skip:focus{top:8px}
 </style>
</head>
<body>
 <a class="skip" href="#main">Skip to main content</a>
 <header class="nav">
  <a href="/"><img src="logo.svg" alt="Canoe club home"></a>
  <nav aria-label="Main" style="display:inline">
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
  <div class="card">
   <h2>Estuary evening paddle</h2>
   <p>Thursday 7pm, flat water, all abilities.</p>
   <div class="actions">
    <button type="button" class="cancel">Cancel booking<span class="sr-only"> for Estuary evening paddle</span></button>
    <button type="button" class="book">Book a place<span class="sr-only"> on Estuary evening paddle</span></button>
   </div>
  </div>
  <div class="card">
   <h2>Weir run for improvers</h2>
   <p>Saturday 9am, moving water, helmet required.</p>
   <div class="actions">
    <button type="button" class="cancel">Cancel booking<span class="sr-only"> for Weir run for improvers</span></button>
    <button type="button" class="book">Book a place<span class="sr-only"> on Weir run for improvers</span></button>
   </div>
  </div>
 </main>
</body>
</html>
```

**What I changed, most harmful first**
- **Button names:** `.sr-only` was never defined, so "Reserve" showed on screen and ran into the label ("ReserveBook a place"). I removed it. Each button's name now ends with the event, so a screen reader user can tell the two cards apart. The visible text is still the start of the name.
- **Focus:** `outline:none` plus a faint glow was close to invisible. It's now a clear ring on `:focus-visible`.
- **Headings:** the page jumped from h1 to h4. The cards now use h2, with CSS that keeps them looking as they did.
- **Navigation:** I added a skip link and a `nav` landmark. I wrapped the search box in a `role="search"` form so Enter submits it.
- **Head:** I added the doctype and viewport meta, and replaced the "Untitled" title.
- **Long text:** card text now wraps instead of overflowing.

**Needs your input**
- **Unwired buttons:** Book and Cancel don't do anything yet, and I didn't invent a booking endpoint. When you connect them, each needs a busy state, a written result and a retry on failure. Cancel needs either an undo or a confirm that names the event.
- **Search endpoint:** `/search` with `?q=` is a guess, so please check it against your site.
- **Cancel button position:** Cancel shows on every event, whether or not the person has booked. I left that as is.
- **Reading order:** the buttons sit above the title on screen but come after it in the markup. I kept the look, so keyboard and screen reader order differs slightly from what people see.

I haven't run this in a browser or tested it with a screen reader.
