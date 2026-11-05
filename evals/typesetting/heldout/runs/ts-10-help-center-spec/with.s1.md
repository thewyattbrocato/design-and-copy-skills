```css
/* Help-center article: type styles
   Scale ratio ~1.25 on desktop. Sizes are in rem so they follow the user's browser setting. */

:root {
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;

  /* Desktop sizes */
  --fs-h1: 2.5rem;       /* 40px */
  --fs-h2: 1.875rem;     /* 30px */
  --fs-h3: 1.375rem;     /* 22px */
  --fs-body: 1.0625rem;  /* 17px */
  --fs-quote: 1.5rem;    /* 24px */
  --fs-small: 0.875rem;  /* 14px: caption */
  --fs-code: 0.9375rem;  /* 15px */
}

/* Mobile sizes */
@media (max-width: 40em) {
  :root {
    --fs-h1: 1.875rem;   /* 30px */
    --fs-h2: 1.5rem;     /* 24px */
    --fs-h3: 1.25rem;    /* 20px */
    --fs-body: 1rem;     /* 16px */
    --fs-quote: 1.25rem; /* 20px */
    --fs-small: 0.875rem;/* 14px */
    --fs-code: 0.875rem; /* 14px */
  }
}

.article {
  font-family: var(--font-body);
  font-size: var(--fs-body);
  line-height: 1.55;
  font-synthesis: none;
  text-align: left;
}

/* Headings: tight leading, about twice as much space above as below */
.article h1,
.article h2,
.article h3 {
  text-wrap: balance;
}

.article h1 {
  font-size: var(--fs-h1);
  line-height: 1.15;
  font-weight: 700;
  letter-spacing: -0.015em;
  margin: 0 0 0.75rem;
}

.article h2 {
  font-size: var(--fs-h2);
  line-height: 1.2;
  font-weight: 650;
  letter-spacing: -0.01em;
  margin: 2.5rem 0 0.75rem;
}

.article h3 {
  font-size: var(--fs-h3);
  line-height: 1.3;
  font-weight: 600;
  margin: 2rem 0 0.5rem;
}

/* Body text: capped measure, gap between paragraphs, no indent */
.article p {
  max-width: 65ch;
  margin: 0 0 1em;
  text-wrap: pretty;
}

/* Code: monospace, unwrapped, scrolls instead of breaking */
.article pre,
.article code {
  font-family: var(--font-mono);
  font-size: var(--fs-code);
  font-variant-ligatures: none;
}

.article pre {
  line-height: 1.5;
  tab-size: 2;
  white-space: pre;
  overflow-x: auto;
  margin: 1.5rem 0;
  padding: 1rem 1.25rem;
}

/* Inline code inside a block keeps the block's style */
.article pre code {
  font-size: inherit;
}

/* Image caption: one step down, muted by value rather than opacity */
.article figcaption {
  font-size: var(--fs-small);
  line-height: 1.4;
  color: #5a5f66;
  margin-top: 0.5rem;
}

/* Pull quote: one size step up, medium weight, no faux italic */
.article blockquote {
  font-size: var(--fs-quote);
  line-height: 1.35;
  font-weight: 500;
  max-width: 32ch;
  margin: 2rem 0;
  padding-left: 1.25rem;
  border-left: 3px solid currentColor;
  text-wrap: balance;
}
```

- I assumed the markup is `.article` containing `h1`–`h3`, `p`, `pre > code`, `figcaption` and `blockquote`. Rename the selectors to match your template.
- I used a system font stack and a light background. If the brand font is licensed, put it first in `--font-body` and keep the system stack as the fallback. The caption color `#5a5f66` is a placeholder to swap for your palette.
