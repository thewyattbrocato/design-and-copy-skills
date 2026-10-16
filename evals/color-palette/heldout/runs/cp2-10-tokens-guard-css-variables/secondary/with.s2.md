```css
:root {
  --color-heading: #14213d;          /* page headings */
  --color-page-background: #fcfbf8;
  --color-card-background: #ffffff;
  --color-text-body: #3a4660;
  --color-button-primary: #0b6e4f;
  --color-error: #c2410c;            /* error text and borders */
}
```

The error text and borders share one color, so they share one property. If you expect them to diverge later, split it into `--color-error-text` and `--color-error-border`.
