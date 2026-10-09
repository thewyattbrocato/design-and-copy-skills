```css
:root {
  --color-text-heading: #14213d;
  --color-text-body: #3a4660;
  --color-bg-page: #fcfbf8;
  --color-bg-card: #ffffff;
  --color-action-primary: #0b6e4f;
  --color-error: #c2410c;
}
```

I estimated these contrast ratios by hand and didn't run a checker:
- Body text on the page background is about 9:1.
- Error on the page background is about 5:1, and on a white card about 5.2:1.
- White text on the primary button is about 6.2:1.

All of them clear the 4.5:1 minimum for body text, and the error color also clears the 3:1 minimum for borders.

I didn't add a token for the button label. White works on it, so use `var(--color-bg-card)` or add something like `--color-text-on-action: #ffffff`.
