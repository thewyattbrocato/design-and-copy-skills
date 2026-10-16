```css
:root {
  --color-heading: #14213d;
  --color-bg-page: #fcfbf8;
  --color-bg-card: #ffffff;
  --color-text: #3a4660;
  --color-button-primary: #0b6e4f;
  --color-error: #c2410c;
}
```

I kept your hex values as given. I estimated these contrast ratios by hand and didn't run a checker:

- Body text on the page background is about 9:1.
- Headings on the page background are about 15:1.
- Error on the page background or a white card is about 5:1.
- White text on the primary button is about 6:1.

All of these clear the 4.5:1 WCAG AA minimum for body text.

I used one `--color-error` for both text and borders, since they share a value. If you later want a different shade for borders or backgrounds, split it into `--color-error-border` and so on.
