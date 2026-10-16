Your page is probably missing the viewport meta tag, so mobile browsers render it at a ~980px desktop width and scale it down. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it still looks off after that, check that your CSS uses relative widths or media queries rather than fixed pixel widths.
