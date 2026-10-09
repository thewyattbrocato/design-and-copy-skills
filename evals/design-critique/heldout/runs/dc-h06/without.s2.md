```css
.card {
  width: 260px;
  min-height: 310px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-sizing: border-box;
  padding-bottom: 12px;
}
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button {
  display: block;
  width: calc(100% - 24px);
  margin: 0 12px;
  padding: 10px;
  background: #1d4e89;
  color: #fff;
  border: 0;
  border-radius: 6px;
}
```

Changes:
- The fixed `height: 310px` became `min-height`, so the card grows to fit its content and the button stays inside.
- `overflow: hidden` clips the image to the rounded corners.
- `box-sizing: border-box` and bottom padding keep the button off the border.
- The title and paragraph now have a 12px side margin and a 12px top margin on the title, so the title no longer touches the image.
- The button has matching side margins so it lines up with the text.
