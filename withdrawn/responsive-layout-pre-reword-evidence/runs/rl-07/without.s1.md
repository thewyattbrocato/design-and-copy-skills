Your page is almost certainly missing the viewport meta tag, so mobile browsers render it at a virtual desktop width (~980px) and scale it down. Add this inside your `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If it still looks off after that, check that your CSS uses relative widths (`%`, `rem`, `max-width`) or media queries rather than fixed pixel widths.
