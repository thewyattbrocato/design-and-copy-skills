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

I kept your values as they are. I calculated contrast by hand, so treat these ratios as estimates:

- **Body text on page background:** about 9:1.
- **Headings on page background:** above 14:1.
- **White text on the primary button:** about 6.2:1.
- **Error on card or page background:** about 5:1. That passes for text and for borders.

`--color-error` covers both error text and error borders, since you gave them one color.
