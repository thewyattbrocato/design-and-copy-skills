The hover rule changes only the background, so the white text stays on a near-white fill. Keep the dark background on hover and darken it slightly instead:

```css
.save:hover { background: #185a4b; }
```

White text on `#185a4b` has a contrast ratio of roughly 8:1, so it stays readable. If you want to keep the pale hover look, change the text color too, for example `.save:hover { background: #e8f3f0; color: #1f6f5c; }`. That's a bigger visual change, so I went with the darker fill.
