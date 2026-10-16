Your card was busy because it had about six effects competing for attention, and nothing clearly ranked first. The gradient, two shadows, glowing red badge, and shadowed icon circle each added noise. Almost all the text was bold at nearly the same size. Three identical solid buttons gave equal weight to "Reserve," "Wishlist," and "Share." The red badge and red seats line also competed for the same urgency cue.

The new order is: class title, then Reserve a seat, then price and seats left, then schedule details, then wishlist and share, then the NEW tag.

```html
<div class="card">
  <div class="card-head">
    <h3>Wheel Throwing for Beginners</h3>
    <span class="tag">New</span>
  </div>
  <p class="meta">Tuesdays 6:30–9pm &middot; 6 weeks &middot; Studio B</p>
  <p class="price">$185</p>
  <p class="seats">3 seats left</p>
  <button class="btn btn-primary">Reserve a seat</button>
  <div class="secondary">
    <button class="btn btn-ghost">Add to wishlist</button>
    <button class="btn btn-ghost">Share</button>
  </div>
</div>
```

```css
.card {
  width: 320px;
  box-sizing: border-box;
  padding: 24px;
  background: #fff;
  border: 1px solid #e6d9cc;
  border-radius: 12px;
  font-family: system-ui, sans-serif;
  color: #2b2118;
}

.card-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.card h3 {
  font-size: 22px;
  line-height: 1.25;
  font-weight: 700;
  margin: 0;
}

.tag {
  flex-shrink: 0;
  font-size: 12px;
  font-weight: 700;
  color: #8a4a1f;
  background: #fbf1e8;
  padding: 2px 8px;
  border-radius: 99px;
}

.meta {
  font-size: 14px;
  color: #6b5a4c;
  margin: 8px 0 16px;
}

.price {
  font-size: 20px;
  font-weight: 700;
  margin: 0;
}

.seats {
  font-size: 14px;
  font-weight: 600;
  color: #b53a22;
  margin: 4px 0 20px;
}

.btn {
  font-family: inherit;
  cursor: pointer;
}

.btn-primary {
  display: block;
  width: 100%;
  background: #8a4a1f;
  color: #fff;
  border: 0;
  border-radius: 10px;
  padding: 12px 14px;
  font-size: 16px;
  font-weight: 700;
}

.secondary {
  display: flex;
  gap: 16px;
  margin-top: 12px;
}

.btn-ghost {
  background: none;
  border: 0;
  padding: 0;
  font-size: 14px;
  font-weight: 600;
  color: #6b5a4c;
  text-decoration: underline;
}
```

What changed and why:

- **One effect per surface.** The gradient, glow, and stacked shadows are gone. A 1px border and a plain white background do the job.
- **Decoration removed.** The icon circle had no information, so I dropped it. If the emoji carries brand identity for you, it can go back as a small inline mark beside the title.
- **One primary action.** Reserve is the only solid button. Wishlist and Share are quiet text links.
- **Clear steps.** The title is 22px, price is 20px, and the meta line is 14px in a muted color. The steps are visible without being dramatic.
- **One urgency cue.** "3 seats left" stays red as text. The badge is now a small, quiet tag.
- **Contrast.** The button color is darker than your original `#c9783c`, so the white label meets readable contrast. If you want the original orange back, the button will need a darker label color or a larger text size to pass.
