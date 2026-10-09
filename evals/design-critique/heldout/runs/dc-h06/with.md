```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; padding-bottom: 12px; box-sizing: border-box; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button { display: block; width: calc(100% - 24px); margin: 0 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

Changes:
- Removed the fixed `height: 310px`, so the card grows to fit its content and the button stays inside.
- Set `overflow: hidden` so the image corners clip to the rounded border.
- Added side and top margins on the `h3` and `p`, which separates the title from the image.
- Gave the button `calc(100% - 24px)` width and 12px side margins so it lines up with the text.
