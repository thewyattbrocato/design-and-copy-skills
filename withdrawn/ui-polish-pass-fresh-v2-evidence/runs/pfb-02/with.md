Here's the full file, since most of it changed. The layout, borders, spacing and wording are as you had them.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Upcoming paddles – Canoe club</title>
 <style>
  .nav a{margin-right:14px}
  .card{display:grid;grid-template-columns:1fr auto;gap:8px;border:1px solid #cfd8dc;padding:16px;border-radius:8px}
  .card h2{font-size:1em;margin:1.33em 0} /* same size as the old h4 */
  .card .actions{display:contents}
  .card .book{grid-column:2;grid-row:1}
  .card .cancel{grid-column:1;grid-row:1}

  /* visible focus ring (the old faint shadow was not enough) */
  a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid #0b5cad;outline-offset:2px}

  .sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  .skip{position:absolute;left:8px;top:-60px;background:#fff;padding:8px 12px;border:2px solid #0b5cad}
  .skip:focus{top:8px}
 </style>
</head>
<body>
 <a class="skip" href="#main">Skip to main content</a>
 <header>
  <nav class="nav" aria-label="Main">
   <a href="/"><img src="logo.svg" alt="Canoe club home"></a>
   <a href="/about">About</a><a href="/trips">Trips</a><a href="/kit">Kit hire</a>
   <a href="/safety">Safety</a><a href="/juniors">Juniors</a><a href="/coaching">Coaching</a>
   <a href="/news">News</a><a href="/gallery">Gallery</a><a href="/shop">Shop</a>
   <a href="/join">Join</a><a href="/contact">Contact</a><a href="/login">Member login</a>
   <input type="search" aria-label="Search the site">
  </nav>
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
- **Button names:** `.sr-only` was never defined, so "Reserve" would have shown as visible text next to "Book a place". Screen-reader users would also have heard four identical buttons. Each button now has its visible label first, then the event name. That keeps the visible text inside the accessible name, which voice-control users need.
- **Focus:** `outline: none` with a 25% blue shadow is nearly invisible. I replaced it with a 2px outline on `:focus-visible`. `#0b5cad` is a stand-in I picked, so swap in a brand blue if you prefer.
- **Headings:** the page jumped from h1 to h4, so I made the card titles h2. The CSS keeps them at the old h4 size and spacing.
- **Page basics:**
  - Added the doctype, a viewport meta tag and a real title.
  - Wrapped the links in a labelled `<nav>`.
  - Added a skip link, because there are 12 links before the content.
  - Added `type="button"` to the buttons.

**Still needs your input**
- **Buttons do nothing:** I didn't add booking behaviour because I don't know your backend. They still need handlers with a busy state, a result message and an error with retry. "Cancel booking" should only appear for events the member has booked, and should offer undo or a clear confirmation. As written, it shows on every card.
- **Search box:** it isn't in a form, so it can't submit anywhere. It needs a form with your search URL.

I only read the code. I didn't run it in a browser, test with a screen reader, or test at narrow widths.
