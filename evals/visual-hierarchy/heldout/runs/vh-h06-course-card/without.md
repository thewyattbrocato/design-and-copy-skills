The card looks busy because nothing is quieter than anything else. Specifically:

- **Everything is bold.** The title, meta, price, seats, badge and buttons are all 700 or 800 weight, so nothing stands out.
- **Too many effects.** The card has a gradient, a 2px border and two shadows. The badge, icon and buttons each add their own shadow or border.
- **Three identical buttons.** "Reserve" competes with "Wishlist" and "Share" even though it's the only action that matters.
- **Scattered details.** Price and seats sit on separate lines, though they're the two facts people use to decide.
- **Low contrast.** White text on `#c9783c` is about 3.6:1, which is below the 4.5:1 minimum for body text.

The version below uses a flat surface with one soft shadow, one primary button, and quiet secondary actions. Bold is kept for the title and price.

```html
<div class="card">
  <span class="badge">New</span>
  <div class="icon" aria-hidden="true">&#127982;</div>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="status">
    <span class="price">$185</span>
    <span class="seats">3 seats left</span>
  </div>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <button class="btn btn-ghost">Add to wishlist</button>
    <button class="btn btn-ghost">Share</button>
  </div>
</div>
```

```css
.card {
  position: relative;
  width: 320px;
  padding: 24px;
  border-radius: 16px;
  background: #fff6ec;
  box-shadow: 0 1px 2px rgba(138, 74, 31, .12), 0 8px 24px rgba(138, 74, 31, .12);
  font-family: system-ui, sans-serif;
  color: #3a2a1e;
}

.badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background: #b83222;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .04em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 99px;
}

.icon {
  display: grid;
  place-items: center;
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: #ffe0c2;
  font-size: 32px;
}

.card h3 {
  margin: 16px 0 4px;
  font-size: 20px;
  font-weight: 700;
  line-height: 1.25;
}

.meta {
  margin: 0 0 16px;
  font-size: 14px;
  font-weight: 400;
  color: #6b5442;
}

.status {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 20px;
}

.price {
  font-size: 24px;
  font-weight: 700;
}

.seats {
  font-size: 14px;
  font-weight: 500;
  color: #b83222;
}

.actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.btn {
  font: inherit;
  font-size: 14px;
  padding: 10px 14px;
  border-radius: 10px;
  cursor: pointer;
}

.btn-primary {
  grid-column: 1 / -1;
  background: #a85a22;
  color: #fff;
  border: 0;
  font-weight: 600;
}
.btn-primary:hover { background: #8a4a1f; }

.btn-ghost {
  background: transparent;
  color: #8a4a1f;
  border: 1px solid #e3c4a6;
  font-weight: 500;
}
.btn-ghost:hover { background: #ffe9d3; }

.btn:focus-visible { outline: 2px solid #8a4a1f; outline-offset: 2px; }
```

Changes beyond the cleanup:
- The primary button now has the strongest fill. The two secondary buttons share a row beneath it, so they no longer wrap or need `margin-right`.
- Price and seats-left are on one line, and the red is only used for urgency.
- I changed the button color from `#c9783c` to `#a85a22` (about 5:1 contrast with white). I also darkened the badge red for the same reason. The palette is still the same warm terracotta.
- I added `aria-hidden` on the emoji, since it's decorative, and a visible keyboard focus style.
- I used a proper en dash in "6:30–9pm" and set the badge text in CSS rather than all caps in the markup.

If you want a bit more warmth, put the gradient back on the card. It's the one effect I'd add first, and it doesn't clutter the layout.
