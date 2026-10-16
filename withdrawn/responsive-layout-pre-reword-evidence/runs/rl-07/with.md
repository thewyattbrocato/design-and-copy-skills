Your page is missing the viewport meta tag, so mobile browsers assume a ~980px-wide desktop layout and scale it down to fit. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it's still tiny after that, check for fixed pixel widths (like `width: 1000px`) in your CSS, and switch them to `max-width: 100%` or relative units.
