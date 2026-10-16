Your page is missing the viewport meta tag, so mobile browsers render it at a virtual ~980px desktop width and shrink it to fit. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it still looks off after that, you likely have fixed pixel widths in your CSS. Switch those to `max-width: 100%` or relative units, and add `@media` queries for narrow screens.
