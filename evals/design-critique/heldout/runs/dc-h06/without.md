```css
.card {
  width: 260px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 0; padding: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 0 12px; padding: 0 12px; font-size: 14px; color: #555; }
.card button {
  width: calc(100% - 24px);
  margin: auto 12px 12px;
  padding: 10px;
  background: #1d4e89;
  color: #fff;
  border: 0;
  border-radius: 6px;
}
```

What changed: I removed the fixed `height` so the card grows to fit its content, which stops the button from hanging off the bottom. I also changed `overflow` to `hidden` so the image respects the rounded corners. The title and text now have padding, which moves the title away from the image. The button now has margins so it doesn't touch the card edges.
