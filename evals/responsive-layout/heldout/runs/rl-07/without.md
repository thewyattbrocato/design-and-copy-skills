Your page is missing the viewport meta tag, so mobile browsers assume a ~980px-wide desktop layout and scale it down to fit the screen. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it still looks small after that, check for fixed pixel widths on your containers and use `max-width` or percentage/responsive CSS (media queries) instead.
