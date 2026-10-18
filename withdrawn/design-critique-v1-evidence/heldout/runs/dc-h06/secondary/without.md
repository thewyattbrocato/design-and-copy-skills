```css
.card { width: 260px; min-height: 310px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 14px 12px 0; font-size: 18px; }
.card p { margin: 6px 12px; font-size: 14px; color: #555; }
.card button { margin: auto 12px 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

- **Button overflow:** `height: 310px` was fixed, so the content had nowhere to go. It's now `min-height`, and the card is a flex column. The button gets `margin-top: auto`, which pins it to the bottom and lets the card grow if the text needs more room.
- **Cramped title:** the `h3` had `margin: 0`. It now has 14px of top spacing and 12px side padding, which also lines up the text with the button.
- **Clipping:** `overflow` is now `hidden` so the rounded corners clip the image. Without this, the square image would poke past the 8px radius.
