```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 16px 0; font-size: 18px; }
.card p { margin: 6px 16px 16px; font-size: 14px; color: #555; }
.card button { margin: auto 16px 16px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The fixed `height: 310px` was too short for the content, so I removed it and let the card grow. The card is now a flex column, and `margin: auto` pushes the button to the bottom. The title and text get 16px side padding, and `overflow: hidden` keeps the image corners inside the border radius.
