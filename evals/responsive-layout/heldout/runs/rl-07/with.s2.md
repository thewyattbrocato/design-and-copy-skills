Your page is missing the viewport meta tag, so mobile browsers render it at a virtual desktop width (about 980px) and scale it down to fit the screen. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it still looks off after that, your CSS may use fixed pixel widths. Switching those to relative units or adding `@media` queries will fix it.
