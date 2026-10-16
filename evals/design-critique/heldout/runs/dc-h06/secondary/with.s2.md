```css
.card { width: 260px; box-sizing: border-box; padding: 0 12px 12px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }
.card img { display: block; width: calc(100% + 24px); height: 160px; margin: 0 -12px 12px; object-fit: cover; }
.card h3 { margin: 0 0 4px; font-size: 18px; }
.card p { margin: 4px 0; font-size: 14px; color: #555; }
.card button { display: block; width: 100%; margin-top: 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The fixed `height: 310px` caused the overflow, so it's removed and the card now sizes to its content. The image gets a 12px gap below it, and the title is spaced from the image by that gap. The padding keeps the text and button off the border, and `overflow: hidden` clips the image to the rounded corners.
