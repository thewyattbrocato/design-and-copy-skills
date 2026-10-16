```css
.card { width: 260px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.card img { width: 100%; height: 160px; object-fit: cover; display: block; }
.card h3 { margin: 12px 12px 0; font-size: 18px; }
.card p { margin: 4px 12px 12px; font-size: 14px; color: #555; }
.card button { margin: auto 12px 12px; width: calc(100% - 24px); padding: 10px; background: #1d4e89; color: #fff; border: 0; border-radius: 6px; }
```

The fixed `height: 310px` was too short for the content, so the button overflowed. Removing it lets the card grow to fit. The card is now a flex column, and `margin: auto` on the button pushes it to the bottom if the card is ever taller than its content. The title gets 12px of top margin, and the inner elements are inset 12px so they line up with the card edges.
