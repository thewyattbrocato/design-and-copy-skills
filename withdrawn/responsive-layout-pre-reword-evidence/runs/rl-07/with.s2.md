Your page is probably missing the viewport meta tag, so mobile browsers render it at a virtual desktop width (about 980px) and shrink it to fit. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it still looks small after that, check for fixed pixel widths in your CSS (like `width: 1000px`) and switch them to `max-width: 100%` or relative units.
