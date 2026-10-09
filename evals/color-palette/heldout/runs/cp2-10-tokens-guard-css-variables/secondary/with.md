```css
:root {
  --color-heading: #14213d;
  --color-page-background: #fcfbf8;
  --color-card-background: #ffffff;
  --color-body-text: #3a4660;
  --color-primary-button: #0b6e4f;
  --color-error: #c2410c;
}
```

The error color is one token because it covers both text and borders. If you want those separately adjustable, split it into `--color-error-text` and `--color-error-border`.
