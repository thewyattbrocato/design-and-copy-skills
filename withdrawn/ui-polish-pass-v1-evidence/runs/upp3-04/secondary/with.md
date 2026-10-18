The hover rule changes only the background, so the text stays white and sits on a pale green. Keep the background dark on hover instead:

```css
.save:hover { background: #18594a; }
```

`#18594a` is a slightly darker shade of `#1f6f5c`, so the white text stays high-contrast on hover.

If you want the hover to visibly change the button's color, you can also set the text color explicitly, but that needs a background that still contrasts with it. Darkening is the simpler fix.
