Here's the full page with the fixes applied. The visuals are unchanged: same card grid, spacing and button placement, with no new colors.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Upcoming paddles</title>
 <style>
  .nav a{margin-right:14px}
  .card{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px;border:1px solid #cfd8dc;padding:16px;border-radius:8px;overflow-wrap:anywhere}
  .card h2{font-size:1em;margin:1.33em 0}  /* same look as the old h4 */
  .card .actions{display:contents}
  .card .book{grid-column:2;grid-row:1}
  .card .cancel{grid-column:1;grid-row:1}
  .sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  .skip{position:absolute;left:-9999px}
  .skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:1}
  a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid #0b5cad;outline-offset:2px;box-shadow:0 0 4px rgba(0,120,200,.25)}
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
  <input type="search" aria-label="Search the site">
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

**What changed, most important first**
- **Button names:** the old `.sr-only` class was never defined, so "Reserve" showed on screen next to "Book a place". Screen-reader users also got identical "Book a place" and "Cancel booking" buttons on every card. Each button now has its visible label first, then the event name as hidden text.
- **Focus ring:** `outline: none` left only a 25%-opacity glow, which is nearly invisible. I switched to `:focus-visible` with a solid 2px outline and kept the original glow on top.
- **Page basics:** I added the doctype, a viewport meta tag, a real title (it was "Untitled"), and a skip link. The 12 links are now in a `<nav>` landmark.
- **Headings:** the `h4` under the `h1` skipped levels, so the cards now use `h2`. A one-line rule keeps them looking the same.
- **Long text:** `minmax(0,1fr)` and `overflow-wrap` stop long event names from breaking the card at narrow widths.
- **Button type:** the buttons are now `type="button"`, so they won't submit a form if they're ever placed in one.

**Still needs a decision from you**
- The buttons aren't connected to anything. Booking and cancelling need a busy state, a confirmation or error message, and Undo or a confirm step for cancel. I didn't invent your booking flow.
- "Cancel booking" appears on events nobody has booked yet. You may want to show it only for members who have booked.
- The title has no club name. Add it, for example "Upcoming paddles – [club name]".
- There's no empty state for a week with no events.

I haven't tested this in a browser or with a screen reader. I only read the code.
