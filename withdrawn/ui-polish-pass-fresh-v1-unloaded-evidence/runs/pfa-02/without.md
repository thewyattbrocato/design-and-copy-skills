I've made a few small fixes and left the layout and look as they were. Your page was pasted into the chat rather than saved as a file, so the full updated version is below.

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Upcoming walks – Tarn Valley Ramblers</title>
  <style>
    a:focus-visible, button:focus-visible, input:focus-visible { outline: 2px solid #1a4d8f; outline-offset: 2px; }
    .actions { display: flex; flex-direction: row; justify-content: flex-start; gap: 8px; }
    .card h2 { font-size: 1em; margin: 1.33em 0; }
  </style>
</head>
<body>
<header>
  <a href='/'><img src='/logo.svg' alt='Tarn Valley Ramblers home'></a>
  <nav aria-label='Main'>
    <a href='/about'>About</a><a href='/walks' aria-current='page'>Walks</a><a href='/grades'>Grades</a>
    <a href='/kit'>Kit list</a><a href='/safety'>Safety</a><a href='/news'>News</a>
    <a href='/photos'>Photos</a><a href='/join'>Join</a><a href='/members'>Members</a>
    <a href='/contact'>Contact</a><a href='/faq'>FAQ</a><a href='/links'>Links</a>
  </nav>
  <form role='search'><input type='text' placeholder='Search walks' aria-label='Search walks'></form>
</header>
<main>
  <h1>Upcoming walks</h1>
  <article class='card'>
    <h2>Sunday 9 March: Hollin Crag circuit</h2>
    <p>11 km, moderate, meet at the Lower Mill car park at 9:30.</p>
    <div class='actions'>
      <button type='button'>Cancel booking</button>
      <button type='button'>Book a place</button>
    </div>
  </article>
  <article class='card'>
    <h2>Saturday 15 March: Beck Head to Ashby</h2>
    <p>7 km, easy, meet at the Beck Head bus stop at 10:00.</p>
    <div class='actions'>
      <button type='button'>Cancel booking</button>
      <button type='button'>Book a place</button>
    </div>
  </article>
</main>
</body>
</html>
```

**What I changed**
- **Page basics:** I added the doctype, `lang`, charset and viewport tags. I replaced the "Untitled" title with "Upcoming walks – Tarn Valley Ramblers".
- **Focus outline:** The old style removed the outline and left only a faint `#bcd` glow, which keyboard users can barely see. It's now a clear outline that shows for keyboard focus only. This is the one visible change, and mouse users won't see it.
- **Button labels:** `aria-label='Reserve'` didn't match the visible text "Book a place", so voice-control users saying the button's name wouldn't have reached it. I removed it, and the visible text is now the button's name.
- **Button order:** `row-reverse` made the tab order the opposite of the visual order. I put the buttons in the DOM in the order they appear and switched to a normal `row`. They look the same.
- **Headings:** The walk titles jumped from `h1` to `h4`. They're now `h2`, and a small rule keeps them the same size as before.
- **Labels:** I gave the search box an `aria-label`. I changed the logo alt text from "logo" to "Tarn Valley Ramblers home". I marked Walks as the current page and labelled the nav.

**What I left alone**
- **Nav spacing:** The nav links have no whitespace or CSS between them within each line, so they may run together visually ("AboutWalksGrades"). Your stylesheet probably handles this elsewhere, so I didn't touch it.
- **Booking buttons:** Both buttons on each walk are always shown, including "Cancel booking" for someone who hasn't booked. That's a design choice, so I left it.
- **Logo path:** `/logo.svg` and the other root-relative links need to resolve on the live domain.
