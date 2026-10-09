```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px; font-size: 14px; color: #555; }
.card button { display: block; width: calc(100% - 24px); margin: auto 12px 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The button was overflowing because the card had a fixed `height: 310px` and its content is taller than that. I removed the height so the card grows to fit. The title now has top margin, and the button is pushed to the bottom with `margin: auto`.
