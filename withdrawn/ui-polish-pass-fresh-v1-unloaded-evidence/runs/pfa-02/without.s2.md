I couldn't save the file because the Write tool is disabled in this session. Here is the full page instead, so you can paste it into place. I haven't previewed it in a browser.

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Upcoming walks | Tarn Valley Ramblers</title>
  <style>
    a:focus-visible, button:focus-visible, input:focus-visible { outline: 2px solid #345; outline-offset: 2px; box-shadow: 0 0 4px #bcd; }
    /* Cancel is first in the DOM so tab order matches the visual order; same look as before. */
    .actions { display: flex; flex-direction: row; justify-content: flex-start; gap: 8px; }
    /* Headings are h2 for correct structure, sized to match the old h4 look. */
    .card h2 { font-size: 1em; margin: 1.33em 0; }
  </style>
</head>
<body>
<header>
  <a href="/"><img src="/logo.svg" alt="Tarn Valley Ramblers home"></a>
  <nav aria-label="Main">
    <a href="/about">About</a><a href="/walks" aria-current="page">Walks</a><a href="/grades">Grades</a>
    <a href="/kit">Kit list</a><a href="/safety">Safety</a><a href="/news">News</a>
    <a href="/photos">Photos</a><a href="/join">Join</a><a href="/members">Members</a>
    <a href="/contact">Contact</a><a href="/faq">FAQ</a><a href="/links">Links</a>
  </nav>
  <form role="search">
    <input type="search" placeholder="Search walks" aria-label="Search walks">
  </form>
</header>
<main>
  <h1>Upcoming walks</h1>
  <article class="card" aria-labelledby="walk1">
    <h2 id="walk1">Sunday 9 March: Hollin Crag circuit</h2>
    <p>11 km, moderate, meet at the Lower Mill car park at 9:30.</p>
    <div class="actions">
      <button type="button" aria-label="Cancel booking for Hollin Crag circuit, Sunday 9 March">Cancel booking</button>
      <button type="button" aria-label="Book a place on Hollin Crag circuit, Sunday 9 March">Book a place</button>
    </div>
  </article>
  <article class="card" aria-labelledby="walk2">
    <h2 id="walk2">Saturday 15 March: Beck Head to Ashby</h2>
    <p>7 km, easy, meet at the Beck Head bus stop at 10:00.</p>
    <div class="actions">
      <button type="button" aria-label="Cancel booking for Beck Head to Ashby, Saturday 15 March">Cancel booking</button>
      <button type="button" aria-label="Book a place on Beck Head to Ashby, Saturday 15 March">Book a place</button>
    </div>
  </article>
</main>
</body>
</html>
```

**What I changed (the layout should look the same):**
- **Document basics:** I added the doctype, `lang`, charset and viewport meta tags. I replaced the "Untitled" title with "Upcoming walks | Tarn Valley Ramblers".
- **Focus outline:** The old CSS removed the outline and left only a faint glow, so keyboard users couldn't see where they were. It now shows a clear outline on `:focus-visible`, and the glow is kept.
- **Button order:** `row-reverse` made the screen order (Cancel, then Book) differ from the tab order (Book, then Cancel). I swapped the buttons in the HTML and switched to a normal row, so it looks identical and tabs in the order you see.
- **Button labels:** `aria-label="Reserve"` didn't match the visible text "Book a place", which breaks voice control and confuses screen readers. Each button's label now starts with its visible text and names the walk, so the two cards' buttons are no longer identical.
- **Headings:** The walk titles jumped from `h1` to `h4`. They are now `h2`, with CSS that keeps the old `h4` size and spacing.
- **Other accessibility fixes:**
  - The logo's alt text is now "Tarn Valley Ramblers home" instead of "logo".
  - The search box now has a label and is a proper search input.
  - The nav is labelled, and the current page is marked.

**Things I left alone because they'd change the look or need your input:**
- **Nav spacing:** The nav links have no whitespace or spacing between them, so they may run together visually ("AboutWalksGrades…"). This may be handled by your site-wide stylesheet, which isn't in this snippet.
- **Buttons do nothing yet:** They have no handlers or form actions. They need wiring to your booking system before launch.
- **Dates:** The walks are 9 and 15 March, and today is 4 November 2026, so these look out of date unless they're next year's.
- **Missing files:** I assumed `/logo.svg` and the linked pages exist on the live site.

If you give me a file path, or enable writing, I can save this straight to disk.
