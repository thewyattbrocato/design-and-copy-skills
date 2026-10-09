```css
.card { display: flex; flex-direction: column; width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; flex-shrink: 0; }
.card h3 { margin: 14px 14px 0; font-size: 18px; }
.card p { margin: 6px 14px 14px; font-size: 14px; color: #555; }
.card button { margin: auto 14px 14px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The fixed `height` was the cause of the overflow. The card now grows to fit its content. The `img` is `flex-shrink: 0` so it keeps its height. The title and paragraph have padding, and the button sits at the bottom through `margin: auto`.
