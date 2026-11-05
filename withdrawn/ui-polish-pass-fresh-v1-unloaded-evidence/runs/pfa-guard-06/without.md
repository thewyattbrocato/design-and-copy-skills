I've changed only the "Proceed" link's text, so it now says where it goes. The `href` and `class` are unchanged.

```html
<a href='/checkout/payment' class='cta'>Proceed to payment</a>
```

Nothing else in the file was touched. This was pasted inline rather than a file in the working directory, so there was nothing for me to edit on disk. Swap that line into your file.

The longer text could wrap in a narrow footer on mobile, so check how `.cta` looks there.
