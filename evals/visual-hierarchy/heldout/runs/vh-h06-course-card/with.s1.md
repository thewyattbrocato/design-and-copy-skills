I cut the effects and ranked the content. The card now reads title, then price and the Reserve button, then schedule and seats, then the two minor actions.

```html
<div class="card">
  <div class="top">
    <span class="icon" aria-hidden="true">&#127982;</span>
    <span class="badge">New</span>
  </div>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30-9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="buy">
    <p class="price">$185</p>
    <p class="seats">3 seats left</p>
  </div>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <div class="secondary">
      <button class="btn btn-secondary">Add to wishlist</button>
      <button class="btn btn-link">Share</button>
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
  box-shadow: 0 2px 8px rgba(60, 40, 20, .08);
  font-family: system-ui, sans-serif;
  color: #2b1d12;
}
.top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
.icon { font-size: 28px; line-height: 1; }
.badge { font-size: 12px; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; color: #8a4a1f; background: #f5e3d0; padding: 3px 8px; border-radius: 99px; }
.card h3 { font-size: 22px; font-weight: 700; line-height: 1.25; margin: 0 0 6px; }
.meta { font-size: 14px; font-weight: 400; color: #5f4b3b; margin: 0 0 20px; }
.buy { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 16px; }
.price { font-size: 28px; font-weight: 700; margin: 0; }
.seats { font-size: 14px; font-weight: 600; color: #b3321d; margin: 0; }
.actions { display: flex; flex-direction: column; gap: 8px; }
.secondary { display: flex; justify-content: space-between; align-items: center; }
.btn { font: inherit; font-size: 14px; font-weight: 600; border-radius: 8px; padding: 8px 12px; cursor: pointer; }
.btn-primary { font-size: 16px; padding: 12px 16px; background: #a85a24; color: #fff; border: 0; }
.btn-secondary { background: transparent; color: #8a4a1f; border: 1px solid #c9a98c; }
.btn-link { background: transparent; color: #8a4a1f; border: 0; text-decoration: underline; }
```

**Why it looked busy:**
- **Competing emphasis:** The 2px border, gradient, big colored shadow, glowing badge, ringed icon circle and three identical 3D buttons were all shouting at once. Nothing was the main thing.
- **Flat text:** The title, price and bold meta line were all about the same size and weight.
- **Three equal buttons:** "Share" looked as important as "Reserve a seat".

**What changed:**
- **Decoration:** I removed the gradient, double border, heavy shadows and icon circle. The emoji stays as a small mark.
- **Badge:** It now sits in the top row instead of floating off the corner, and it is quieter.
- **Price and seats:** The price is larger, with "3 seats left" as the only red text, on the same row.
- **Buttons:** There is one solid button, one outline button and one text link.

I assumed "3 seats left" and the $185 price are real and kept them as written.
