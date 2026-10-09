The card looks busy because too many elements compete for attention:

- **Five decorative effects at once:** a gradient background, a 2px border, two stacked shadows (one a heavy orange glow), a red badge with its own glow, and an icon with a border and shadow.
- **Everything is bold:** the title, meta, price, seats, and buttons all use weight 700, so nothing stands out.
- **Three equal buttons:** they all look like primary actions, and the 3D bottom-shadow effect adds visual weight.
- **Two accent colors:** orange and red both compete for attention.

Here's a cleaned-up version. It keeps the same content and structure, with one small HTML change: the buttons get modifier classes so the main action stands out.

```html
<div class="card">
  <span class="badge">NEW</span>
  <div class="icon">&#127982;</div>
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
  --accent: #a85a26;
  --ink: #2b2118;
  --muted: #6e6257;
  --line: #e7dfd6;

  width: 320px;
  max-width: 100%;
  box-sizing: border-box;
  padding: 24px;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, .08);
  font-family: system-ui, sans-serif;
  color: var(--ink);
  position: relative;
}

.badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background: var(--accent);
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .04em;
  padding: 3px 8px;
  border-radius: 99px;
}

.icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: #f6ede4;
  display: grid;
  place-items: center;
  font-size: 28px;
}

.card h3 {
  font-size: 20px;
  font-weight: 600;
  line-height: 1.3;
  margin: 16px 0 8px;
}

.meta {
  font-size: 14px;
  color: var(--muted);
  margin: 0 0 16px;
}

.price {
  font-size: 24px;
  font-weight: 600;
  margin: 0 0 4px;
}

.seats {
  font-size: 14px;
  font-weight: 500;
  color: var(--accent);
  margin: 0 0 20px;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.btn {
  flex: 1 1 auto;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  padding: 10px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  cursor: pointer;
}

.btn:hover {
  background: #faf6f1;
}

.btn-primary {
  flex: 1 1 100%;
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.btn-primary:hover {
  background: #8f4c20;
}

.btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
```

**What changed:**

- **One accent color** (`--accent`) is used for the badge, seats count, and primary button. The gradient, glows, and 3D button shadows are gone.
- **Clear hierarchy:** the title is 600 weight, the price is the largest text, and the meta line is muted gray.
- **One primary action:** "Reserve a seat" is a full-width filled button. The other two are outlined and share the row below it.
- **Quieter icon:** a soft tinted circle instead of a bordered, shadowed disc.
- **Better contrast:** the accent is slightly darker than the original, so white text on it passes WCAG AA at 14px.
- **Accessibility and robustness:** I added hover and focus-visible states, and `max-width: 100%` so the card doesn't overflow on narrow screens.
