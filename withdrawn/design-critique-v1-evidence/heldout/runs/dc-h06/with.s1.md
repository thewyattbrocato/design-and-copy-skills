```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; padding-bottom: 12px; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button { display: block; width: calc(100% - 24px); margin: 0 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

- **Button overflow:** I removed the fixed `height: 310px`. The content was taller than that, so the card now sizes to its content. I also added `padding-bottom` so the button doesn't sit on the bottom border.
- **Title against the image:** `h3` now has a 12px top margin, and the title and description have 12px side margins.
- **Button width:** The button width is `calc(100% - 24px)` with matching 12px side margins, so it lines up with the text.
- **Rounded corners:** I changed `overflow` to `hidden` so the image is clipped to the card's rounded corners.
