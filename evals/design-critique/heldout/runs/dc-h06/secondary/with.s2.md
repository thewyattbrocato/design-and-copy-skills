```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px; font-size: 14px; color: #555; }
.card button { align-self: stretch; margin: 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The fixed `height: 310px` was forcing the card to end before the content did, so the button spilled out. Removing it lets the card grow to fit. The flex column with `align-self: stretch` keeps the button full-width inside the 12px margins without overflowing. `overflow: hidden` keeps the image corners clipped to the rounded border.
