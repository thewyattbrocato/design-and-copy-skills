```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 14px 16px 0; font-size: 18px; }
.card p { margin: 6px 16px 0; font-size: 14px; color: #555; }
.card button { margin: 14px 16px 16px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The fixed `height: 310px` is gone, so the card grows to fit its content. The text and button get side and top spacing, and `overflow: hidden` keeps the image inside the rounded corners.
