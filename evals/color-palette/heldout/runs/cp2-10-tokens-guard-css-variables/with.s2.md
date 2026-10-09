```css
:root {
  --color-heading: #14213d;
  --color-bg-page: #fcfbf8;
  --color-bg-card: #ffffff;
  --color-text-body: #3a4660;
  --color-button-primary: #0b6e4f;
  --color-error: #c2410c;
}
```

I used one `--color-error` for both error text and borders, since they share a value. If you want to tune them separately later, split it into `--color-error-text` and `--color-error-border`.
