## Why it feels busy

- **Everything is emphasized.** Nearly every text element is bold, so nothing stands out. The title, meta, price, and seats all compete.
- **Too many effects.** The card has a border, a gradient, a heavy orange glow, and a hard bottom edge. The badge, icon, and buttons each add their own border or shadow. That's about eight depth effects on one small card.
- **Three equal buttons.** "Reserve", "Wishlist", and "Share" look equally important, and they probably won't fit on one row at 320px.
- **Red is used twice.** The badge and the seats line both use it, so neither one reads as the urgent signal.
- **Contrast.** White text on `#c9783c` is about 3.5:1, which is below the 4.5:1 that WCAG AA asks for at this text size.

## Cleaned up

The fixes: one soft shadow, a flat background, a clear text hierarchy, and one primary action with two quiet secondary ones.

```html
<div class="card">
  <div class="top">
    <div class="icon" aria-hidden="true">&#127982;</div>
    <span class="badge">New</span>
  </div>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="info">
    <p class="price">$185</p>
    <p class="seats">3 seats left</p>
  </div>
  <button class="btn primary">Reserve a seat</button>
  <div class="secondary">
    <button class="btn ghost">Add to wishlist</button>
    <button class="btn ghost">Share</button>
  </div>
</div>
```

```css
.card {
  width: 320px;
  padding: 24px;
  border-radius: 16px;
  background: #fffaf5;
  box-shadow: 0 1px 3px rgba(60, 30, 10, .12), 0 8px 24px rgba(60, 30, 10, .08);
  font-family: system-ui, sans-serif;
  color: #2b1d14;
}
.top { display: flex; justify-content: space-between; align-items: flex-start; }
.icon { font-size: 40px; line-height: 1; }
.badge { background: #f6e3d3; color: #8a4a1f; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 99px; }
.card h3 { font-size: 20px; font-weight: 700; margin: 16px 0 4px; }
.meta { font-size: 14px; color: #6b5a4e; margin: 0 0 16px; }
.info { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 20px; }
.price { font-size: 24px; font-weight: 700; margin: 0; }
.seats { font-size: 14px; color: #b3321d; margin: 0; }
.btn { font: inherit; font-size: 14px; font-weight: 600; border-radius: 10px; padding: 10px 14px; cursor: pointer; }
.primary { width: 100%; background: #9a4f1d; color: #fff; border: 0; }
.primary:hover { background: #834116; }
.secondary { display: flex; gap: 8px; margin-top: 8px; }
.ghost { flex: 1; background: transparent; color: #8a4a1f; border: 1px solid #e3cdb9; }
.ghost:hover { background: #f6e3d3; }
.btn:focus-visible { outline: 2px solid #9a4f1d; outline-offset: 2px; }
```

## What changed

- **Hierarchy:** the title and price are bold, the meta line is regular and muted, and the seats line is regular weight in red. Red now appears only on the seats line, so it works as the urgency cue.
- **Depth:** one soft shadow on the card. The border, gradient, and the shadows on the icon, badge, and buttons are gone.
- **Badge and icon:** the badge sits in the top row next to the icon instead of being absolutely positioned. That also stops it from clipping if a parent has `overflow: hidden`.
- **Price and seats:** they share a row, which saves vertical space and ties the two facts together.
- **Actions:** "Reserve a seat" is a full-width filled button. Wishlist and Share are outlined and sit side by side below it. The primary button's color is darkened to about 6:1 contrast.
- **Small extras:** a focus ring and hover states, and the en dash in the time range (6:30–9pm).

I haven't rendered this in a browser, so check it visually. If it feels too plain, the easiest thing to add back is a very subtle `border: 1px solid #f0e0d0` on the card.
