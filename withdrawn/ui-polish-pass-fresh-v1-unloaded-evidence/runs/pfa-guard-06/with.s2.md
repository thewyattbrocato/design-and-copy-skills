Here's the change. Only the text of the footer `Proceed` link is different:

```html
<a href='/checkout/payment' class='cta'>Proceed to payment</a>
```

The `href` and `class` are unchanged, and so is everything else in the file. I didn't edit anything on disk because you pasted the HTML rather than naming a file. Swap that one line into your copy.

The link goes to `/checkout/payment`, so "Proceed to payment" tells people where it leads. If the button has a width limit, check that the longer label still fits.
