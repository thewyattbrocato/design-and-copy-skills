```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; padding-bottom: 12px; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button { display: block; width: calc(100% - 24px); margin: 0 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

Changes:
- Removed the fixed `height: 310px`, so the card grows to fit its content and the button no longer overflows.
- Set `overflow: hidden` so the image follows the rounded corners.
- Added side margins and top spacing on the title, so it no longer touches the image.
- Gave the paragraph and button matching side margins, and set the button width to `calc(100% - 24px)` so it fits inside them.
- Added bottom padding on the card.
