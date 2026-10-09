```html
<div class="card">
  <p class="eyebrow">New</p>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm &middot; 6 weeks &middot; Studio B</p>
  <p class="price">$185 <span class="seats">3 seats left</span></p>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <div class="secondary">
      <button class="btn btn-text">Add to wishlist</button>
      <button class="btn btn-text">Share</button>
    </div>
  </div>
</div>
```

```css
.card {
  width: 320px;
  padding: 24px;
  border: 1px solid #e6d9cc;
  border-radius: 12px;
  background: #fff;
  color: #2b2118;
  font-family: system-ui, sans-serif;
}
.eyebrow {
  margin: 0 0 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #6b5b4e;
}
.card h3 { margin: 0 0 8px; font-size: 22px; line-height: 1.25; font-weight: 700; }
.meta { margin: 0 0 20px; font-size: 14px; color: #6b5b4e; }
.price {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin: 0 0 16px;
  font-size: 22px;
  font-weight: 700;
}
.seats { font-size: 14px; font-weight: 600; color: #b3341f; }
.btn { font: inherit; font-size: 14px; cursor: pointer; }
.btn-primary {
  width: 100%;
  padding: 12px 16px;
  background: #a8531f;
  color: #fff;
  border: 0;
  border-radius: 8px;
  font-weight: 600;
}
.btn-primary:hover { background: #8a4318; }
.secondary { display: flex; justify-content: space-between; margin-top: 8px; }
.btn-text {
  padding: 8px 0;
  background: none;
  border: 0;
  color: #6b5b4e;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.btn-text:hover { color: #2b2118; }
```

**Why it looked busy**
- Everything was loud at once: gradient, 2px border, big orange shadow, a glowing red badge, a shadowed icon circle, and three identical solid 3D buttons. Nothing could win.
- The meta line, price, and seats were all bold, with the title at 20px, so the text had no clear steps.

**What changed**
- The order is now title, then price and seats, then the single solid "Reserve a seat" button. Meta is quieter gray. "Add to wishlist" and "Share" are text links.
- Red now appears once, on the seat count. "NEW" is a small gray label instead of a second red badge.
- I removed the gradient, heavy shadows, and icon circle, since none of them carried information.

**Notes**
- The icon `&#127982;` renders as a red lantern, not pottery, so I dropped it. If you want an icon, a pot (🏺) would fit, but keep it small and unframed.
- Colors are my picks: the same terracotta family as your original, darkened so the white button text passes contrast.
