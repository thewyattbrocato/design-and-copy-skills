```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 14px 12px 0; font-size: 18px; }
.card p { margin: 6px 12px; font-size: 14px; color: #555; }
.card button { margin: auto 12px 12px; width: calc(100% - 24px); padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The fixed `height` was forcing the button past the bottom, so I removed it and let the card grow with its content. The button uses `margin-top: auto` so it stays at the bottom. The h3 and p now have 12px side padding and a top gap from the image. I also changed `overflow` to `hidden` so the image corners stay inside the rounded border.
