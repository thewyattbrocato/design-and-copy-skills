The card had about eight things competing at once: a gradient, two shadows, a glowing red badge, a bordered icon disc, a red seat count, bold text in every line, and three identical solid buttons. Here is a version with one visible order: title, then the reserve action, then price and seats, with the rest quieter.

```html
<article class="card">
  <span class="tag">New</span>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm · 6 weeks · Studio B</p>
  <p class="price">$185</p>
  <p class="seats">3 seats left</p>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <button class="btn btn-secondary">Wishlist</button>
    <button class="btn btn-text">Share</button>
  </div>
</article>
```

```css
.card {
  width: 320px;
  padding: 24px;
  border: 1px solid #eadacb;
  border-radius: 12px;
  background: #fff;
  color: #2b2118;
  font-family: system-ui, sans-serif;
}

.tag {
  display: inline-block;
  margin-bottom: 10px;
  padding: 2px 8px;
  border-radius: 4px;
  background: #fbeee3;
  color: #8a4a1f;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .04em;
  text-transform: uppercase;
}

.card h3 {
  margin: 0 0 6px;
  font-size: 22px;
  font-weight: 700;
  line-height: 1.25;
}

.meta {
  margin: 0 0 16px;
  font-size: 14px;
  color: #6b5a4c;
}

.price {
  margin: 0 0 4px;
  font-size: 18px;
  font-weight: 600;
}

.seats {
  margin: 0 0 20px;
  font-size: 14px;
  font-weight: 600;
  color: #b8361f;
}

.actions {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.btn {
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  border-radius: 8px;
  padding: 10px 14px;
  cursor: pointer;
}

.btn-primary {
  flex: 1 1 100%;
  border: 0;
  background: #a85d26;
  color: #fff;
  padding: 12px 14px;
}

.btn-secondary {
  border: 1px solid #d8c3ae;
  background: #fff;
  color: #2b2118;
}

.btn-text {
  border: 0;
  background: none;
  color: #6b5a4c;
  text-decoration: underline;
  padding-inline: 4px;
}
```

What changed and why:

- **One boss:** "Reserve a seat" is the only solid button and spans the full width. Wishlist is outlined and Share is a text link, so they stay available without competing.
- **Clear order:** the title is the largest and heaviest line. Price drops to 18px at a lighter weight, and the meta line is muted gray. Every line was bold before, which flattened the order.
- **Removed:** the gradient, the stacked shadows, the glowing badge, the bordered icon disc, and the emoji. The emoji carried no information, so I dropped it. If the card needs a visual identity, a single quiet image above the title would do that job better.
- **One emphasis:** the seat count is the only colored text. The badge is now a small inline tag instead of a red pill overlapping the edge.
- **Contrast:** I darkened the button and seat colors so white and red text clear the 4.5:1 floor for small text. Check the exact values against your brand palette.
