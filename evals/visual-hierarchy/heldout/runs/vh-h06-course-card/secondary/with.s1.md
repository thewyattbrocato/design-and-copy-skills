The card had five things competing at once: a red badge overlapping the top edge, an icon in a bordered circle, a gradient with stacked shadows, a red seat count, and three identical solid buttons. Nothing ranked above anything else. The new version makes "Reserve a seat" the one solid action and the title the main read.

```html
<div class="card">
  <span class="badge">NEW</span>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30-9pm &middot; 6 weeks &middot; Studio B</p>
  <p class="price">$185</p>
  <p class="seats">3 seats left</p>
  <div class="actions">
    <button class="btn">Reserve a seat</button>
    <button class="btn-link">Wishlist</button>
    <button class="btn-link">Share</button>
  </div>
</div>
```

```css
.card { width: 320px; padding: 24px; border: 1px solid #e6d3c0; border-radius: 16px; background: #fff; box-shadow: 0 2px 8px rgba(0,0,0,.06); font-family: system-ui, sans-serif; color: #2b2119; }
.badge { display: inline-block; background: #fbe9dd; color: #8a4a1f; font-size: 12px; font-weight: 700; letter-spacing: .04em; padding: 3px 8px; border-radius: 99px; }
.card h3 { font-size: 22px; font-weight: 700; line-height: 1.25; margin: 12px 0 6px; }
.meta { font-size: 14px; color: #6b5a4c; margin: 0 0 12px; }
.price { font-size: 18px; font-weight: 700; margin: 0 0 4px; }
.seats { font-size: 14px; font-weight: 600; color: #b3361f; margin: 0 0 16px; }
.actions { display: flex; align-items: center; flex-wrap: wrap; gap: 12px; }
.btn { background: #a85a24; color: #fff; border: 0; border-radius: 10px; padding: 12px 18px; font-size: 15px; font-weight: 700; cursor: pointer; }
.btn-link { background: none; border: 0; padding: 0; font: inherit; font-size: 14px; font-weight: 600; color: #6b5a4c; text-decoration: underline; cursor: pointer; }
```

What changed and why:
- **Removed:** the icon circle, the gradient, the stacked shadows and the orange border. None of them told the viewer anything about the class.
- **Badge:** now an inline tinted label above the title instead of a red chip overlapping the edge. It still says NEW, but it no longer competes with the title.
- **Buttons:** one solid primary action. Wishlist and Share are text links, so they stay available without pulling focus from Reserve.
- **Button color:** I darkened the orange to `#a85a24` so white text meets the 4.5:1 contrast floor at 15px bold. The original `#c9783c` came out around 4.2:1.

Notes:
- The seat count is the only red text left, so it reads as the urgency cue. I kept it because it is real information from your card.
- Turning Wishlist and Share into links makes them easier to miss. If they matter a lot, a small outline button would work better than a link.
