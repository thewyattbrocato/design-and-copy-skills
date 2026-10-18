```css
.card { width: 260px; min-height: 310px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; box-sizing: border-box; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button { width: calc(100% - 24px); margin: auto 12px 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The fixed `height` is now `min-height`, so the card grows to fit its content instead of letting the button spill out. The title and description now have side and top spacing, and the button is pinned to the bottom with matching margins.
