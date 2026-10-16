Here's the cleaned-up card.

```html
<div class="card">
  <span class="badge">New</span>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30-9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="offer">
    <p class="price">$185</p>
    <p class="seats">3 seats left</p>
  </div>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <div class="secondary">
      <button class="btn btn-secondary">Add to wishlist</button>
      <button class="btn btn-tertiary">Share</button>
    </div>
  </div>
</div>
```

```css
.card {
  width: 320px;
  padding: 24px;
  border: 1px solid #e6d5c3;
  border-radius: 12px;
  background: #fffaf5;
  box-shadow: 0 1px 3px rgba(60, 40, 20, .08);
  font-family: system-ui, sans-serif;
  color: #2b2018;
}
.badge {
  display: inline-block;
  margin-bottom: 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: #8a4a1f;
}
.card h3 { font-size: 22px; line-height: 1.25; margin: 0 0 6px; font-weight: 700; }
.meta { font-size: 14px; font-weight: 400; color: #6b5a4c; margin: 0 0 20px; }
.offer { display: flex; align-items: baseline; justify-content: space-between; margin: 0 0 20px; }
.price { font-size: 20px; font-weight: 700; margin: 0; }
.seats { font-size: 14px; font-weight: 600; color: #b8341f; margin: 0; }

.actions { display: grid; gap: 8px; }
.secondary { display: flex; justify-content: space-between; align-items: center; }
.btn { font: inherit; font-size: 14px; font-weight: 600; border-radius: 8px; padding: 10px 14px; cursor: pointer; }
.btn:focus-visible { outline: 2px solid #2b2018; outline-offset: 2px; }
.btn-primary { width: 100%; padding: 12px 14px; font-size: 16px; background: #9a4a1c; color: #fff; border: 0; }
.btn-secondary { background: transparent; color: #8a4a1f; border: 1px solid #c9a98a; }
.btn-tertiary { background: transparent; color: #6b5a4c; border: 0; text-decoration: underline; }
```

**Why it looked busy:**
- Everything was shouting. Three identical solid buttons, a red badge, red seat count, bold on every line, and a thick border all competed for attention.
- Several effects stacked up: a gradient, a coloured glow shadow, a hard edge shadow, a bordered icon circle, and shadowed buttons. None of them told the viewer anything.

**What I changed:**
- The title now leads, then the schedule in quiet regular weight, then price and seats on one line.
- "Reserve a seat" is the only solid button. Wishlist is an outline button and Share is a text link.
- The NEW badge is now small label text instead of a floating red pill. The seat count is the only red on the card.
- I flattened the background and shadow, and darkened the button brown so white text passes contrast. The old `#c9783c` was too light.

**Notes:**
- I removed the icon. The code `&#127982;` renders as a pudding emoji (🍮), which doesn't say pottery. If you want an icon, a pottery one would be worth adding, kept small and quiet.
- Copy and facts are unchanged. I only lowercased "NEW" in the HTML, and the CSS uppercases it again.
