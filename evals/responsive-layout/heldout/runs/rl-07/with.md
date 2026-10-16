Your page is missing the viewport meta tag, so mobile browsers assume a ~980px-wide desktop layout and shrink it to fit. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it's still off after that, check for fixed pixel widths on your containers, since those can also force the page wider than the phone screen.
