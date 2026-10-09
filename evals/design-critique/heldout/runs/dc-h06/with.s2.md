Fixed CSS: the fixed `height` was clipping the content, so I switched it to `min-height` (really, auto height). I also added padding for the text and button.

```css
.card {
  width: 260px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  padding-bottom: 12px;
}
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button { width: calc(100% - 24px); margin: auto 12px 0; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

- **Button overflow:** removed `height: 310px`, so the card grows to fit its content.
- **Title against image:** gave the `h3` a 12px top margin.
- **Side spacing:** text and button now have 12px side margins.
- **Corners:** `overflow: hidden` keeps the image inside the rounded corners.
