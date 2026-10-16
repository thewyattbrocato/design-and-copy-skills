```css
.card { width: 260px; min-height: 310px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button { width: calc(100% - 24px); margin: auto 12px 12px; padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

- **Button overflow:** the fixed `height: 310px` is now `min-height`, so the card grows to fit its content. It's also a flex column, so the button sits at the bottom (`margin-top: auto`).
- **Title spacing:** `h3` now has a 12px top margin and 12px side margins, and `p` has matching side margins.
- **Button sizing:** the button's width is reduced by its side margins so it doesn't overflow horizontally.
- **Rounded corners:** `overflow: hidden` clips the image to the card's rounded corners.
