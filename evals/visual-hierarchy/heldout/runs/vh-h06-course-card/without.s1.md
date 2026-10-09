The card looks busy because every element is competing for attention.

**What was causing it**
- **Too much decoration.** The card has a gradient, a 2px border and a large orange glow, all at once. The icon circle adds its own border and shadow, and the badge has a glow too.
- **No type hierarchy.** The title, meta line, price and seats are all bold (700) at 14-20px, so nothing stands out.
- **Three identical buttons.** Each has a heavy 3D shadow, so "Reserve" looks no more important than "Share".
- **Red used twice.** It marks both "NEW" and "3 seats left", so they compete.

**What I changed**
- The card is flat, with a 1px border and a soft shadow.
- The icon sits in a plain tinted tile.
- The title is semibold, the meta line is regular and muted, and the price is the largest text.
- The price and seats share one row. Red is used only for the seats warning.
- "Reserve" is the one solid button. The other two are quiet outline buttons.
- I added a visible keyboard focus style.

```html
<div class="card">
  <span class="badge">New</span>
  <div class="icon" aria-hidden="true">&#127982;</div>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="offer">
    <span class="price">$185</span>
    <span class="seats">3 seats left</span>
  </div>
  <div class="actions">
    <button type="button" class="btn btn-primary">Reserve a seat</button>
    <button type="button" class="btn btn-secondary">Add to wishlist</button>
    <button type="button" class="btn btn-secondary">Share</button>
  </div>
</div>
```

```css
.card {
  position: relative;
  width: 320px;
  padding: 24px;
  background: #fffaf5;
  border: 1px solid #ead9c8;
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(60, 40, 20, .08);
  font-family: system-ui, sans-serif;
  color: #2b2118;
}

.badge {
  position: absolute;
  top: 16px;
  right: 16px;
  padding: 2px 10px;
  border-radius: 99px;
  background: #f3e1cf;
  color: #8a4a1f;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .04em;
  text-transform: uppercase;
}

.icon {
  display: grid;
  place-items: center;
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: #f3e1cf;
  font-size: 30px;
}

.card h3 {
  margin: 16px 0 4px;
  font-size: 20px;
  font-weight: 600;
  line-height: 1.25;
}

.meta {
  margin: 0 0 16px;
  font-size: 14px;
  color: #6b5a4d;
}

.offer {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 20px;
}

.price {
  font-size: 28px;
  font-weight: 700;
}

.seats {
  font-size: 14px;
  font-weight: 600;
  color: #b3321d;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.btn {
  padding: 10px 14px;
  border-radius: 10px;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}

.btn-primary {
  flex: 1 0 100%;
  background: #9a4f1c;
  border: 1px solid #9a4f1c;
  color: #fff;
}

.btn-secondary {
  flex: 1;
  background: transparent;
  border: 1px solid #d9c4b0;
  color: #5a3a20;
}

.btn-primary:hover { background: #823f13; }
.btn-secondary:hover { background: #f6ebe0; }
.btn:focus-visible { outline: 2px solid #9a4f1c; outline-offset: 2px; }
```

I haven't rendered this. If any spacing looks off in your page, tell me and I'll adjust it.
