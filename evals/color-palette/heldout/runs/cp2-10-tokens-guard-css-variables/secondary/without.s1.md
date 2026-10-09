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

The error color is one variable because it's used for both text and borders. If you later need them to differ, split it into `--color-error-text` and `--color-error-border`.
