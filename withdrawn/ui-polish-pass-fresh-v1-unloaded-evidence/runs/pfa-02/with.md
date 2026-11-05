The page is pasted into the chat rather than saved as a file, so here is the full updated version. The look is unchanged.

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Upcoming walks – Tarn Valley Ramblers</title>
  <style>
    a:focus-visible, button:focus-visible, input:focus-visible { outline: 2px solid #1a4f8a; outline-offset: 2px; box-shadow: 0 0 4px #bcd; }
    .actions { display: flex; flex-direction: row; justify-content: flex-start; gap: 8px; flex-wrap: wrap; }
    .card h2 { font-size: 1em; margin: 1.33em 0; } /* was h4; same size */
    .skip { position: absolute; left: -9999px; }
    .skip:focus { position: static; }
  </style>
</head>
<body>
<a class='skip' href='#main'>Skip to main content</a>
<header>
  <a href='/'><img src='/logo.svg' alt='Tarn Valley Ramblers home'></a>
  <nav aria-label='Main'>
    <a href='/about'>About</a><a href='/walks' aria-current='page'>Walks</a><a href='/grades'>Grades</a>
    <a href='/kit'>Kit list</a><a href='/safety'>Safety</a><a href='/news'>News</a>
    <a href='/photos'>Photos</a><a href='/join'>Join</a><a href='/members'>Members</a>
    <a href='/contact'>Contact</a><a href='/faq'>FAQ</a><a href='/links'>Links</a>
  </nav>
  <form role='search'><input type='search' aria-label='Search walks' placeholder='Search walks'></form>
</header>
<main id='main'>
  <h1>Upcoming walks</h1>
  <article class='card'>
    <h2>Sunday 9 March: Hollin Crag circuit</h2>
    <p>11 km, moderate, meet at the Lower Mill car park at 9:30.</p>
    <div class='actions'>
      <button type='button' aria-label='Cancel booking: Hollin Crag circuit, 9 March'>Cancel booking</button>
      <button type='button' aria-label='Book a place: Hollin Crag circuit, 9 March'>Book a place</button>
    </div>
  </article>
  <article class='card'>
    <h2>Saturday 15 March: Beck Head to Ashby</h2>
    <p>7 km, easy, meet at the Beck Head bus stop at 10:00.</p>
    <div class='actions'>
      <button type='button' aria-label='Cancel booking: Beck Head to Ashby, 15 March'>Cancel booking</button>
      <button type='button' aria-label='Book a place: Beck Head to Ashby, 15 March'>Book a place</button>
    </div>
  </article>
</main>
</body>
</html>
```

**What I changed**
- **Page basics:** I replaced the "Untitled" title with a real one. I added the doctype, `lang` and viewport tag, which the page was missing.
- **Focus:** `outline: none` with a pale `#bcd` glow was nearly invisible. Keyboard focus now gets a clear 2px ring, and the glow stays.
- **Button order:** `row-reverse` made the tab order the opposite of what you see. I put the buttons in the DOM in their visual order (Cancel, then Book) and used a normal row, so nothing moves on screen.
- **Button names:** `aria-label='Reserve'` didn't match the visible "Book a place", and it didn't say which walk. Each button's name now starts with its visible text and ends with the walk and date. "Cancel booking" gets the same treatment.
- **Headings:** `h1` followed by `h4` skipped levels. The walk titles are now `h2`, styled to match the old size and spacing.
- **Navigation and search:** the logo alt text is now "Tarn Valley Ramblers home". The search box has a label. I added a skip link, a label on the nav, and `aria-current` on Walks.

**Still open**
- The buttons have no behaviour yet. Booking and cancelling need a handler that shows a result, such as "Booked: Hollin Crag circuit", and an error with retry if it fails. I didn't invent those without your booking endpoint.
- I haven't checked the page in a browser or with a screen reader. I also haven't checked the 12 nav links at narrow widths. They run together with no spacing, so they may be cramped on small screens.
- The `#1a4f8a` focus colour is my choice, so swap it for a club colour if you prefer.
