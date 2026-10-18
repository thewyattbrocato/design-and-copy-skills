The hover rule swaps the background to a pale tint (`#e8f3f0`) but the text stays white. Make the hover background a darker shade of the green so the white text keeps its contrast:

```css
.save:hover { background: #185a4b; }
```

`#185a4b` is darker than the base `#1f6f5c`, so it reads as a hover state. White on it has a contrast ratio of roughly 8:1.

If you want the pale look on hover instead, change the text color too:

```css
.save:hover { background: #e8f3f0; color: #1f6f5c; }
```

That version needs a border or outline, because the pale button would otherwise nearly vanish against a white card.

I didn't edit any files, since the CSS only came through in your message. Paste the fix into your stylesheet.
