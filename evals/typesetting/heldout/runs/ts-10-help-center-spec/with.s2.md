```css
/* Help-center article: type styles
   Desktop is the default. Mobile overrides below 40rem (640px). */

.article {
  --text-h1: 2.5rem;       /* 40px */
  --text-h2: 1.875rem;     /* 30px */
  --text-h3: 1.375rem;     /* 22px */
  --text-body: 1.0625rem;  /* 17px */
  --text-quote: 1.5rem;    /* 24px */
  --text-small: 0.875rem;  /* 14px: captions, code */

  font-size: var(--text-body);
  line-height: 1.5;
  font-synthesis: none;
}

.article h1,
.article h2,
.article h3 {
  text-wrap: balance;
  font-weight: 700;
}

.article h1 {
  font-size: var(--text-h1);
  line-height: 1.15;
  letter-spacing: -0.015em;
  margin: 0 0 1rem;
}

.article h2 {
  font-size: var(--text-h2);
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin: 2.5rem 0 0.75rem;
}

.article h3 {
  font-size: var(--text-h3);
  line-height: 1.3;
  margin: 2rem 0 0.5rem;
}

.article p {
  font-size: var(--text-body);
  line-height: 1.5;
  max-width: 65ch;
  margin: 0 0 1rem;
  text-wrap: pretty;
}

/* Code snippet (block) and inline code */
.article pre,
.article code {
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: 0.9375rem;    /* 15px */
  line-height: 1.5;
}

.article pre {
  margin: 1.5rem 0;
  padding: 1rem 1.25rem;
  overflow-x: auto;
  white-space: pre;        /* keep unwrapped; scroll instead */
  tab-size: 2;
}

.article :not(pre) > code {
  font-size: 0.9em;
}

/* Image caption */
.article figcaption {
  font-size: var(--text-small);
  line-height: 1.4;
  margin-top: 0.5rem;
  max-width: 65ch;
}

/* Pull quote */
.article blockquote,
.article .pull-quote {
  font-size: var(--text-quote);
  line-height: 1.35;
  font-weight: 500;
  max-width: 40ch;
  margin: 2.5rem 0;
  text-wrap: balance;
}

/* Mobile */
@media (max-width: 40rem) {
  .article {
    --text-h1: 1.875rem;   /* 30px */
    --text-h2: 1.5rem;     /* 24px */
    --text-h3: 1.25rem;    /* 20px */
    --text-body: 1rem;     /* 16px */
    --text-quote: 1.25rem; /* 20px */
    --text-small: 0.875rem;
  }

  .article h1 { line-height: 1.2; margin-bottom: 0.75rem; }
  .article h2 { margin: 2rem 0 0.5rem; }
  .article h3 { margin: 1.5rem 0 0.5rem; }

  .article pre,
  .article code { font-size: 0.875rem; } /* 14px */

  .article pre {
    padding: 0.875rem 1rem;
    margin: 1.25rem 0;
  }

  .article blockquote,
  .article .pull-quote {
    line-height: 1.4;
    margin: 2rem 0;
  }
}
```

- **Assumptions:** I scoped everything under `.article` and used element selectors, so swap in your template's real class names. I also left out typefaces and colors, so the developers will need to add those.
- **Scale:** The sizes follow roughly a 1.25 ratio on desktop. The code snippet and caption are the small sizes. Space above each heading is about double the space below it.
