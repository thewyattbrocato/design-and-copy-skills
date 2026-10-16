```html
<div class="card">
  <span class="badge">New</span>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="offer">
    <p class="price">$185</p>
    <p class="seats">3 seats left</p>
  </div>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <button class="btn btn-secondary">Add to wishlist</button>
    <button class="btn btn-tertiary">Share</button>
  </div>
</div>
```

```css
.card {
  width: 320px;
  padding: 24px;
  border: 1px solid #e3d5c8;
  border-radius: 16px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(60, 40, 20, .08);
  font-family: system-ui, sans-serif;
  color: #2b2118;
}
.badge {
  display: inline-block;
  margin-bottom: 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #b3321f;
}
.card h3 { font-size: 22px; line-height: 1.25; margin: 0 0 8px; font-weight: 700; }
.meta { font-size: 14px; font-weight: 400; color: #5f5145; margin: 0 0 20px; }
.offer { display: flex; align-items: baseline; justify-content: space-between; margin: 0 0 20px; }
.price { font-size: 20px; font-weight: 700; margin: 0; }
.seats { font-size: 14px; font-weight: 400; color: #b3321f; margin: 0; }
.actions { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 12px; }
.btn { font: inherit; font-size: 14px; font-weight: 600; border-radius: 10px; padding: 10px 14px; cursor: pointer; }
.btn-primary { flex: 1 1 100%; background: #a8591f; color: #fff; border: 1px solid #a8591f; padding: 12px 14px; }
.btn-secondary { background: transparent; color: #7a4118; border: 1px solid #c9a98c; }
.btn-tertiary { background: transparent; color: #7a4118; border: 1px solid transparent; text-decoration: underline; }
.btn:focus-visible { outline: 2px solid #2b2118; outline-offset: 2px; }
```

**Why it looked busy:** everything was loud. The gradient, border, big colored shadow, icon circle, glowing badge and three identical solid buttons all competed. Every line of text was also bold, so nothing led.

**New order:**
1. The class title is largest.
2. The schedule is quieter regular text.
3. The price is bold, with "3 seats left" in red beside it.
4. "Reserve a seat" is the only solid button. Wishlist is outlined, and Share is a text link.

**Notes:**
- I removed the emoji circle because it carried no information. If you want it as a brand touch, add it back small and flat, with no border or shadow.
- "NEW" is now a small red label instead of a floating pill.
