**Why it looked busy:** every element was emphasized. The card had a gradient, a border, a heavy shadow, a floating badge, a circled icon, and three identical solid 3D buttons. Everything was bold, and the title, meta line, price, and seat count were all 14–20px. Nothing was ranked.

**Ranking I used:**
1. Title
2. Price and the Reserve button
3. Schedule details and seats left
4. Wishlist and Share

```html
<div class="card">
  <p class="eyebrow">New</p>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm · 6 weeks · Studio B</p>
  <p class="price">$185 <span class="seats">· 3 seats left</span></p>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <button class="btn btn-quiet">Add to wishlist</button>
    <button class="btn btn-quiet">Share</button>
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
  font-family: system-ui, sans-serif;
  color: #2b2118;
}
.eyebrow {
  margin: 0 0 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #b4532a;
}
.card h3 {
  margin: 0 0 8px;
  font-size: 24px;
  line-height: 1.2;
  font-weight: 700;
}
.meta {
  margin: 0 0 20px;
  font-size: 14px;
  color: #6b5d50;
}
.price {
  margin: 0 0 16px;
  font-size: 20px;
  font-weight: 700;
}
.seats {
  font-size: 14px;
  font-weight: 600;
  color: #b4532a;
}
.actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px 16px;
}
.btn {
  font: inherit;
  font-size: 14px;
  cursor: pointer;
}
.btn-primary {
  flex: 1 0 100%;
  padding: 12px 16px;
  border: 0;
  border-radius: 8px;
  background: #b4532a;
  color: #fff;
  font-weight: 600;
}
.btn-quiet {
  padding: 4px 0;
  border: 0;
  background: none;
  color: #6b5d50;
  text-decoration: underline;
  text-underline-offset: 3px;
}
```

**What changed:**
- **Title:** it's now the largest and heaviest text. The schedule line dropped to regular weight in a softer color, so it reads as support.
- **Price and seats:** price is the second-boldest item. "3 seats left" sits beside it as the only colored text, which is enough urgency without a badge.
- **Buttons:** Reserve is the one solid, full-width button. Wishlist and Share are plain text links.
- **Removed:** the gradient, heavy shadows, and floating badge are gone. So are the circled icon and the 3D button borders, none of which carried information. The 🍮 emoji was a custard, not pottery; if you want an icon, use a real pottery one, quieter than the title.
- **NEW:** it's now a small label above the title instead of a badge.

I kept your orange as the single accent, darkened to `#b4532a` so the white button text and the small text have enough contrast. I also changed the hyphen in the time range to an en dash, and swapped the `&middot;` entities for literal `·` characters.
