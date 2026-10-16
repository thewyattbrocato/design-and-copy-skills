Your page is probably missing the viewport meta tag, so mobile browsers pretend the screen is about 980px wide and shrink the whole page to fit. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it's already there, check for fixed pixel widths (like `width: 1000px`) on your containers. Those will also force the shrunken look, so switch them to `max-width: 100%` or relative units.
