```css
:root {
  --color-text-heading: #14213d;
  --color-text-body: #3a4660;
  --color-text-error: #c2410c;

  --color-bg-page: #fcfbf8;
  --color-bg-card: #ffffff;
  --color-bg-button-primary: #0b6e4f;

  --color-border-error: #c2410c;
}
```

I split error into a text token and a border token that share one value. That way you can change either one later without touching the other.

I did the contrast checks by hand, so treat the ratios as estimates:
- Body text on the page background is about 9:1.
- Error on the page background is about 5:1, and on the card about 5.2:1.
- White text on the primary button is about 6.2:1.

You didn't give a button label color, so I left it out. White is the one to use.
