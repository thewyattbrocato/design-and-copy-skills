Here's the cleaned-up card. The main problems were too many competing effects and too many emphasized elements.

**What was making it busy**
- **Too many effects at once:** a gradient background, two shadows on the card, a red glowing badge, and a bordered icon circle with its own shadow.
- **Competing accent colors:** orange, red, and brown were all used at full strength, so nothing stood out.
- **Three equal-weight buttons with 3D drop shadows:** the primary action looked the same as "Share."
- **Badge overlapping the title area:** it sat on the top edge and crowded the heading.

**What changed**
- A plain white card with one thin border and a soft shadow.
- One accent color (the orange) for the primary action. Red is kept only for the "3 seats left" urgency cue.
- Clear hierarchy: title, then meta, then price, then seats, then actions.
- One filled primary button and two quiet secondary buttons.
- The title gets right padding so it never runs under the badge.

```html
<div class="card">
  <span class="badge">NEW</span>
  <div class="icon" aria-hidden="true">&#127994;</div>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm &middot; 6 weeks &middot; Studio B</p>
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
  box-sizing: border-box;
  position: relative;
  width: 320px;
  max-width: 100%;
  padding: 20px;
  border: 1px solid #e6d5c3;
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, .08);
  font-family: system-ui, sans-serif;
  color: #2b2118;
}

.badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background: #d2412a;
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .04em;
  padding: 3px 8px;
  border-radius: 6px;
}

.icon {
  display: grid;
  place-items: center;
  width: 48px;
  height: 48px;
  margin-bottom: 12px;
  font-size: 24px;
  background: #fdf1e7;
  border-radius: 10px;
}

.card h3 {
  font-size: 18px;
  line-height: 1.3;
  margin: 0 0 4px;
  padding-right: 64px; /* keeps the title clear of the badge */
  font-weight: 700;
}

.meta {
  font-size: 14px;
  color: #6b5b4e;
  margin: 0 0 12px;
}

.price {
  font-size: 22px;
  font-weight: 700;
  margin: 0 0 2px;
}

.seats {
  font-size: 14px;
  font-weight: 600;
  color: #b3361f;
  margin: 0 0 16px;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.btn {
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  padding: 10px 14px;
  border: 1px solid #e6d5c3;
  border-radius: 8px;
  background: #fff;
  color: #6b5b4e;
  cursor: pointer;
}

.btn-primary {
  flex: 1 1 100%;
  background: #c9783c;
  border-color: #c9783c;
  color: #fff;
}
```

**Two notes**
- The original icon `&#127982;` is 🏮 (a paper lantern), not a pottery piece. I switched it to `&#127994;`, which is 🏺 (an amphora). If you'd rather have a different image, any emoji works.
- The seats color `#b3361f` is a slightly darker red than the badge so the text passes contrast on white. The price and title are the largest text, so they carry the card.
