I couldn't save the file because the Write tool is disabled in this session. The full updated page is below, so you can paste it over `events.html`. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Upcoming paddles | Canoe club</title>
 <meta name="description" content="Upcoming paddles and events at our canoe club: book a place on evening paddles and improver weir runs.">
 <style>
  .nav a{margin-right:14px}
  .card{display:grid;grid-template-columns:1fr auto;gap:8px;border:1px solid #cfd8dc;padding:16px;border-radius:8px}
  .card h2{font-size:1em;margin:1.33em 0} /* keeps the original h4 appearance */
  .card .actions{display:contents}
  .card .book{grid-column:2;grid-row:1}
  .card .cancel{grid-column:1;grid-row:1}
  /* Visible keyboard focus (replaces outline:none + faint shadow) */
  a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid #0b5cad;outline-offset:2px;box-shadow:0 0 4px rgba(0,120,200,.25)}
  .sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  .skip-link{position:absolute;left:-9999px}
  .skip-link:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:10}
 </style>
</head>
<body>
 <a class="skip-link" href="#main">Skip to main content</a>
 <header class="nav">
  <nav aria-label="Main">
   <a href="/"><img src="logo.svg" alt="Canoe club home"></a>
   <a href="/about">About</a><a href="/trips">Trips</a><a href="/kit">Kit hire</a>
   <a href="/safety">Safety</a><a href="/juniors">Juniors</a><a href="/coaching">Coaching</a>
   <a href="/news">News</a><a href="/gallery">Gallery</a><a href="/shop">Shop</a>
   <a href="/join">Join</a><a href="/contact">Contact</a><a href="/login">Member login</a>
  </nav>
  <input type="search" name="q" aria-label="Search the site">
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

**What I changed (the styling is untouched)**
- **Document basics:** I added `<!DOCTYPE html>`, a viewport meta tag and a meta description. I replaced the "Untitled" title with "Upcoming paddles | Canoe club".
- **Visible text bug:** `.sr-only` was never defined, so "Reserve" was showing next to "Book a place". It's now defined. The visually hidden text now names the event, so a screen reader hears "Book a place on Weir run for improvers" instead of two identical buttons.
- **Keyboard focus:** `outline:none` with a faint shadow made focus almost invisible. It's now a clear outline on `:focus-visible`, so mouse users see no change.
- **Headings:** The page jumped from h1 to h4, so I changed the card titles to h2. A small CSS rule keeps them looking exactly like the old h4s.
- **Landmarks and structure:** The links are now in a `<nav>`, each card is an `<article>`, and there's a skip-to-content link that only appears on keyboard focus.
- **Buttons:** They now have `type="button"`, so they won't submit a form if one is added later.

**Things for you to check or decide**
- **Club name:** Put your real club name in the `<title>`.
- **Buttons don't work yet:** Nothing happens when you click Book or Cancel. They need a backend or form, and I don't know your booking system.
- **Cancel on every card:** "Cancel booking" shows on every event, even for people with no booking. It should probably only show for a member who has booked.
- **Search box:** It isn't connected to anything, because I don't know your search endpoint. It should be a `<form role="search" action="…">`.
- **Logo size:** `logo.svg` has no `width` and `height`, so the page may shift while it loads. Add them once you know its size.
- **Reading order:** In each card the buttons appear above the title on screen, but they come after it in the HTML. Screen reader and tab order therefore differs from what sighted users see. Fixing it would change the layout, so I left it for you to decide.
