```css
:root {
  --color-heading: #14213d;        /* page headings */
  --color-page-background: #fcfbf8;
  --color-card-background: #ffffff;
  --color-body-text: #3a4660;
  --color-primary-button: #0b6e4f;
  --color-error: #c2410c;          /* error text and borders */
}
```

Since error text and borders share one color, I gave them a single `--color-error` property. If you want them to diverge later, split it into `--color-error-text` and `--color-error-border`.
