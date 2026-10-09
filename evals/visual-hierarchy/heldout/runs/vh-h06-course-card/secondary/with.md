The card's problem is that nearly every element is asking for attention at once. The red badge, the gradient, the heavy shadows, the emoji in a shadowed circle, the bold meta line, the price at the same size as the title, and three identical solid buttons all compete. Reserving a seat is the job, so the title, price, seats and main button should lead, and the rest should step back.

```html
<div class="card">
  <span class="badge">New</span>
  <h3>Wheel Throwing for Beginners</h3>
  <p class="meta">Tuesdays 6:30-9pm &middot; 6 weeks &middot; Studio B</p>
  <div class="facts">
    <p class="price">$185</p>
    <p class="seats">3 seats left</p>
  </div>
  <div class="actions">
    <button class="btn btn-primary">Reserve a seat</button>
    <button class="btn btn-quiet">Add to wishlist</button>
    <button class="btn btn-text">Share</button>
  </div>
</div>
```

```css
.card { width: 320px; padding: 24px; border: 1px solid #e6d5c3; border-radius: 12px; background: #fff; color: #2b2622; font-family: system-ui, sans-serif; }

.badge { display: inline-block; font-size: 12px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: #8a4a1f; background: #fbeee3; padding: 3px 8px; border-radius: 4px; margin: 0 0 12px; }
.card h3 { font-size: 22px; font-weight: 700; line-height: 1.3; margin: 0 0 6px; }
.meta { font-size: 14px; color: #6b625b; margin: 0 0 16px; }

.facts { display: flex; justify-content: space-between; align-items: baseline; margin: 0 0 20px; }
.price { font-size: 18px; font-weight: 700; margin: 0; }
.seats { font-size: 14px; font-weight: 600; color: #a8371f; margin: 0; }

.actions { display: flex; flex-wrap: wrap; gap: 8px; }
.btn { font: inherit; font-size: 15px; font-weight: 600; border-radius: 8px; padding: 10px 16px; cursor: pointer; }
.btn-primary { flex: 1 1 100%; background: #a35a24; color: #fff; border: 1px solid #a35a24; }
.btn-quiet { background: #fff; color: #2b2622; border: 1px solid #cfc3b7; }
.btn-text { background: none; border: none; color: #6b625b; text-decoration: underline; padding: 10px 4px; }
```

What changed and why:

- **One primary action.** "Reserve a seat" is the only solid button and spans the full width. Wishlist is an outline button and Share is a text link, so the card has a single clear next step.
- **Title leads, price follows.** The title is the largest element, and the price drops from 20px to 18px so it no longer competes with it.
- **One accent.** The red badge and red seats count were both emphasis. The badge is now a quiet neutral tag, and the red stays on "3 seats left" because it's the one piece of urgency worth noticing.
- **Decoration removed.** The gradient, the stacked shadows, the emoji circle and the overlapping badge had no job, so I cut them. A thin neutral border and a 12px radius do the framing. If the emoji is part of your brand, it can go inline before the title at a small size.
- **Contrast.** I darkened the button fill to `#a35a24` so white text meets the 4.5:1 contrast floor. The original `#c9783c` was about 3.4:1.

I kept your copy as written. The wishlist and share buttons sit on their own row so the labels don't crowd each other at 320px.
