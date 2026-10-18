```css
.card {
  width: 260px;
  min-height: 310px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  padding-bottom: 12px;
}
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button {
  width: calc(100% - 24px);
  margin: auto 12px 0;
  padding: 10px;
  background: #1d4e89;
  color: #fff;
  border: 0;
  border-radius: 6px;
}
```

Changes:
- **Button overflow:** the fixed `height: 310px` is now `min-height`, so the card grows to fit its content. The card is also a flex column, which pins the button to the bottom with `margin-top: auto`.
- **Title spacing:** the `h3` now has a top margin of 12px. I added 12px of side margin to the text and button so they don't touch the card edges.
- **Clipping:** `overflow: hidden` keeps the image corners inside the rounded border. `box-sizing: border-box` keeps the width at 260px.
