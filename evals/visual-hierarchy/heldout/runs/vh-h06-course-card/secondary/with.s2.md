Here's the cleaned-up card. The busy look came from about six effects competing at once: a gradient background, two stacked shadows, a glowing red badge, a shadowed icon circle, and three identical solid buttons. None of them ranked the content, so everything fought for attention.

```html
<div class="card">
  <span class="badge">NEW</span>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm · 6 weeks · Studio B</p>
  <p class="price">$185</p>
  <p class="seats">3 seats left</p>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <div class="secondary">
      <button class="btn-link">Add to wishlist</button>
      <button class="btn-link">Share</button>
    </div>
  </div>
</div>
```

```css
.card {
  width: 320px;
  padding: 24px;
  border: 1px solid #e3d5c7;
  border-radius: 12px;
  background: #fff;
  color: #2b2119;
  font-family: system-ui, sans-serif;
}

.badge {
  display: inline-block;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .06em;
  color: #b5552b;
  border: 1.5px solid #b5552b;
  border-radius: 99px;
  padding: 2px 8px;
}

.card h3 { font-size: 24px; line-height: 1.2; margin: 10px 0 8px; font-weight: 700; }
.meta { font-size: 14px; color: #6b5a4c; margin: 0 0 12px; }
.price { font-size: 18px; font-weight: 700; margin: 0 0 2px; }
.seats { font-size: 14px; font-weight: 600; color: #b3361f; margin: 0 0 20px; }

.actions { display: flex; flex-direction: column; gap: 12px; }

.btn-primary {
  background: #b5552b;
  color: #fff;
  border: 0;
  border-radius: 8px;
  padding: 12px 18px;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
}

.secondary { display: flex; gap: 16px; }

.btn-link {
  background: none;
  border: 0;
  padding: 0;
  color: #6b5a4c;
  font-size: 14px;
  font-weight: 600;
  text-decoration: underline;
  cursor: pointer;
}
```

What changed and why:
- **Order:** the title leads, then the schedule, price, and seat count. Reserve is the one solid button; wishlist and share drop to quiet text links.
- **One loud thing per group:** the terracotta fill goes to the Reserve action. Red is reserved for the "3 seats left" urgency cue, and the NEW badge is now an outline tag with no glow.
- **Removed:** the gradient, the double shadow, the 3D button shadows, and the 80px icon circle. The emoji carried no information the title doesn't already give, so I dropped it. If it's part of your brand, add it back small beside the title.
