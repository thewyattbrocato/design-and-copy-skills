```css
/* Help-center article: type styles
   Sizes are in rem so they follow the user's browser setting.
   Desktop values are the default. Mobile overrides are at the bottom. */

.article {
  --fs-h1: 2.5rem;       /* 40px */
  --fs-h2: 1.75rem;      /* 28px */
  --fs-h3: 1.25rem;      /* 20px */
  --fs-body: 1.0625rem;  /* 17px */
  --fs-quote: 1.5rem;    /* 24px */
  --fs-code: 0.9375rem;  /* 15px */
  --fs-caption: 0.875rem;/* 14px */

  font-size: var(--fs-body);
  line-height: 1.55;
  font-synthesis: none;
}

/* Prose elements get the measure cap, not the page wrapper */
.article p,
.article ul,
.article ol,
.article h1,
.article h2,
.article h3 {
  max-width: 65ch;
}

.article h1,
.article h2,
.article h3 {
  text-wrap: balance;
  font-weight: 650;
}

.article h1 {
  font-size: var(--fs-h1);
  line-height: 1.15;
  letter-spacing: -0.015em;
  margin: 0 0 0.6em;
}

/* Space above is about double the space below */
.article h2 {
  font-size: var(--fs-h2);
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin: 2.25em 0 0.75em;
}

.article h3 {
  font-size: var(--fs-h3);
  line-height: 1.3;
  margin: 1.75em 0 0.5em;
}

.article p {
  font-size: var(--fs-body);
  line-height: 1.55;
  margin: 0 0 1em;
  text-wrap: pretty;
}

.article code,
.article pre {
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: var(--fs-code);
  line-height: 1.5;
}

/* Inline code sits slightly smaller than the text around it */
.article :not(pre) > code {
  font-size: 0.9em;
}

.article pre {
  margin: 1.5em 0;
  padding: 1em 1.25em;
  overflow-x: auto;   /* code stays unwrapped and scrolls */
  white-space: pre;
  tab-size: 2;
}

.article figcaption {
  font-size: var(--fs-caption);
  line-height: 1.4;
  margin-top: 0.5em;
  max-width: 65ch;
}

/* Pull quote differs from body by size and style only */
.article blockquote {
  font-size: var(--fs-quote);
  line-height: 1.35;
  font-style: italic;
  font-weight: 500;
  letter-spacing: -0.005em;
  max-width: 28em;
  margin: 2em 0;
  padding-left: 1.25rem;
  text-wrap: balance;
}

/* Mobile */
@media (max-width: 40rem) {
  .article {
    --fs-h1: 1.875rem;     /* 30px */
    --fs-h2: 1.5rem;       /* 24px */
    --fs-h3: 1.1875rem;    /* 19px */
    --fs-body: 1rem;       /* 16px */
    --fs-quote: 1.25rem;   /* 20px */
    --fs-code: 0.875rem;   /* 14px */
    --fs-caption: 0.8125rem; /* 13px */
  }

  .article h1 { line-height: 1.2; }
  .article h2 { margin-top: 2em; }
  .article h3 { margin-top: 1.5em; }

  .article p { line-height: 1.6; }

  .article blockquote {
    padding-left: 1rem;
    margin: 1.5em 0;
  }
}
```

I assumed the template wraps everything in `.article` and uses `figcaption` and `blockquote` for the caption and pull quote. Swap in your real class names if they differ.

I left font family and color out. The mobile sizes sit at about 75–80% of desktop for headings and 94% for body.
