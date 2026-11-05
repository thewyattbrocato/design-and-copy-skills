Here's the one-line change. The link now says where it goes, and I didn't touch anything else:

```html
<a href='/checkout/payment' class='cta'>Proceed to payment</a>
```

I only had the pasted snippet, not a file path, so I haven't edited anything on disk. Swap that line in for the existing `Proceed` link in the footer.

The `href` and `class` are unchanged, so styling and routing stay the same. "Proceed to payment" is longer than "Proceed", so check that the `.cta` button doesn't wrap or overflow on narrow screens.
