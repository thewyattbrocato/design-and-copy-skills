```html
<div class="card">
  <p class="eyebrow"><span class="badge">New</span> Evening class</p>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30–9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="buy">
    <p class="price">$185</p>
    <p class="seats">3 seats left</p>
  </div>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <button class="btn btn-secondary">Add to wishlist</button>
    <button class="btn btn-link">Share</button>
  </div>
</div>
```

```css
.card {
  width: 320px;
  padding: 24px;
  border: 1px solid #ead9c6;
  border-radius: 16px;
  background: #fffaf4;
  box-shadow: 0 2px 8px rgba(80, 50, 20, .08);
  font-family: system-ui, sans-serif;
  color: #2b1d12;
}
.eyebrow { display: flex; align-items: center; gap: 8px; margin: 0 0 8px; font-size: 13px; color: #6b5543; }
.badge { background: #8a4a1f; color: #fff; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .04em; padding: 2px 8px; border-radius: 99px; }
.card h3 { font-size: 24px; line-height: 1.2; font-weight: 700; margin: 0 0 8px; }
.meta { font-size: 14px; font-weight: 400; color: #5f4a38; margin: 0 0 20px; }
.buy { display: flex; align-items: baseline; justify-content: space-between; margin: 0 0 20px; }
.price { font-size: 32px; font-weight: 700; line-height: 1; margin: 0; }
.seats { font-size: 14px; font-weight: 600; color: #b3361f; margin: 0; }
.actions { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; }
.btn { font: inherit; font-size: 14px; font-weight: 600; border-radius: 10px; padding: 10px 14px; cursor: pointer; }
.btn-primary { flex: 1 1 100%; padding: 12px 14px; background: #8a4a1f; color: #fff; border: 1px solid #8a4a1f; }
.btn-secondary { background: transparent; color: #8a4a1f; border: 1px solid #c9a98a; }
.btn-link { background: none; border: 1px solid transparent; color: #6b5543; text-decoration: underline; }
.btn:focus-visible { outline: 2px solid #8a4a1f; outline-offset: 2px; }
```

**Why it looked busy:** nearly everything competed.
- Three identical solid buttons, a bold meta line, a bold price, a bold seats line, a floating badge, and a circled icon with its own shadow, border and glow were all loud at once.
- The card also stacked a gradient, a 2px border and two shadows.

**What I changed:**
- **Order:** the title comes first, then the price, then one solid "Reserve a seat" button. The meta line is now regular weight and muted. Wishlist is an outline button and Share is a text link.
- **Removed decoration:** I cut the emoji circle, the gradient and the stacked shadows. The badge is now a small inline "New" tag.
- **Contrast:** the old white-on-orange button text was too low-contrast, so I darkened the button to `#8a4a1f`.

I assumed the pottery emoji wasn't carrying the brand. If it is, bring it back as a small unframed glyph next to "Evening class".
