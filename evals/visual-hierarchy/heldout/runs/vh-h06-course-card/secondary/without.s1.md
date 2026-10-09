Here's the cleaned-up card. I didn't render it, so check it in a browser.

```html
<div class="card">
  <span class="badge">NEW</span>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30-9pm &middot; 6 weeks &middot; Studio B</p>
  <p class="price">$185</p>
  <p class="seats">3 seats left</p>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <button class="btn">Add to wishlist</button>
    <button class="btn">Share</button>
  </div>
</div>
```

```css
.card {
  width: 320px;
  max-width: 100%;
  padding: 20px;
  border: 1px solid #ead9c6;
  border-radius: 14px;
  background: #fff;
  box-shadow: 0 1px 2px rgba(0,0,0,.06), 0 4px 12px rgba(0,0,0,.06);
  font-family: system-ui, sans-serif;
  color: #2b2118;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.badge {
  align-self: flex-start;
  background: #fbe9e4;
  color: #b5321c;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .04em;
  padding: 3px 8px;
  border-radius: 99px;
}
.card h3 { margin: 4px 0 0; font-size: 20px; font-weight: 700; line-height: 1.25; }
.meta { margin: 0; font-size: 14px; color: #6b5a4a; }
.price { margin: 4px 0 0; font-size: 22px; font-weight: 700; }
.seats { margin: 0; font-size: 14px; font-weight: 600; color: #b5321c; }
.actions { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }
.btn {
  flex: 1 1 auto;
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  padding: 10px 14px;
  border: 1px solid #d8c3ad;
  border-radius: 10px;
  background: #fff;
  color: #2b2118;
  cursor: pointer;
}
.btn:hover { background: #fdf5ec; }
.btn-primary { flex-basis: 100%; background: #8a4a1f; border-color: #8a4a1f; color: #fff; }
.btn-primary:hover { background: #6f3a17; }
.btn:focus-visible { outline: 3px solid #e0a070; outline-offset: 2px; }
```

**Why it looked busy**

- **Too many effects competing.** The gradient, the 45px-offset glow, the inset ring, the icon's shadow, the badge's red glow, and the 3D button shadows all fought for attention. The card now has one flat surface and one soft shadow.
- **Too many accent colors.** Orange, red, and brown were all used at full strength. Orange is now only the primary button, red only for the badge and the seat count, and everything else is neutral.
- **Flat hierarchy.** The title, meta, and price were all bold at similar sizes. Now the title and price lead, meta is muted, and the seat count is the only semibold line.
- **Three equal buttons.** "Reserve" now has a clear primary treatment and the other two are secondary.
- **Floating decorations.** The icon circle and the overlapping badge added clutter. The badge now sits in the normal flow.

**Things I changed beyond styling**

- **Removed the icon.** `&#127982;` is 🏮 (a lantern), not pottery. If you want an icon, `&#127994;` is 🏺 and can go back above the title.
- **Fixed contrast.** The old orange button (`#c9783c`) with white text is about 3.4:1, below the 4.5:1 WCAG AA minimum for body text. The primary button is now `#8a4a1f` (about 6.8:1). The seat count is darkened from `#d2412a` (about 4.3:1 on the cream background) to `#b5321c`.
- **Added a focus style** so keyboard users can see which button is focused.
