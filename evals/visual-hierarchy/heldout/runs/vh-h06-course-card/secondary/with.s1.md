Main job: get someone to reserve a seat. So the order is the title and price, then the seats left and the Reserve button, then the schedule. Wishlist and Share drop to quiet secondary actions. The gradient, the double shadow, the glowing icon circle and the red badge with its own shadow all compete with that order, so I removed them. The seats-left line is the one accent color.

```html
<div class="card">
  <div class="card-top">
    <span class="icon" aria-hidden="true">&#127982;</span>
    <span class="badge">New</span>
  </div>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="price">$185</p>
  <p class="seats">3 seats left</p>
  <p class="meta">Tuesdays 6:30&ndash;9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <button class="btn btn-secondary">Wishlist</button>
    <button class="btn btn-link">Share</button>
  </div>
</div>
```

```css
.card {
  width: 320px;
  padding: 24px;
  border: 1px solid #e6d5c3;
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .06);
  font-family: system-ui, sans-serif;
  color: #2b2118;
}

.card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.icon {
  font-size: 28px;
  line-height: 1;
}

.badge {
  font-size: 12px;
  font-weight: 600;
  color: #6b5a4a;
  background: #f4ece3;
  padding: 3px 8px;
  border-radius: 4px;
}

.card h3 {
  font-size: 20px;
  font-weight: 700;
  line-height: 1.3;
  margin: 0 0 8px;
}

.price {
  font-size: 18px;
  font-weight: 700;
  margin: 0 0 4px;
}

.seats {
  font-size: 14px;
  font-weight: 700;
  color: #a8431f;
  margin: 0 0 12px;
}

.meta {
  font-size: 14px;
  color: #6b5a4a;
  margin: 0 0 20px;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}

.btn {
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  border-radius: 8px;
  padding: 10px 16px;
  cursor: pointer;
}

.btn-primary {
  background: #a8431f;
  color: #fff;
  border: 1px solid #a8431f;
}

.btn-secondary {
  background: transparent;
  color: #2b2118;
  border: 1px solid #c9b8a6;
}

.btn-link {
  background: none;
  border: none;
  color: #6b5a4a;
  padding: 10px 4px;
  text-decoration: underline;
}
```

Notes:
- The seats-left line is the only urgency signal, so it's the one place the accent color appears besides the button. If you'd rather have the button carry all the color, make `.seats` the same dark text as the title.
- I kept the 🏺 icon small and unboxed as the one identity mark. If you don't need it, delete the `.icon` span and the `.card-top` will just hold the badge.
