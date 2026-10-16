```css
/* Help-center article: type styles
   Desktop is the default. Mobile overrides apply at 40rem (640px) and below. */

:root {
  --font-text: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-code: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}

.article {
  font-family: var(--font-text);
  font-size: 1.0625rem;      /* 17px body */
  line-height: 1.55;
  font-synthesis: none;
}

/* Headings */
.article h1,
.article h2,
.article h3 {
  font-weight: 700;
  text-wrap: balance;
  max-width: 30ch;
}

.article h1 {
  font-size: 2.5rem;         /* 40px */
  line-height: 1.15;
  letter-spacing: -0.015em;
  margin: 0 0 1rem;
}

.article h2 {
  font-size: 1.75rem;        /* 28px */
  line-height: 1.25;
  margin: 3rem 0 0.75rem;
}

.article h3 {
  font-size: 1.3125rem;      /* 21px */
  line-height: 1.3;
  margin: 2rem 0 0.5rem;
}

/* Body */
.article p,
.article li {
  max-width: 65ch;
  text-wrap: pretty;
}

.article p {
  margin: 0 0 1em;
}

/* Code snippet (monospace, unwrapped, scrolls sideways) */
.article pre,
.article code {
  font-family: var(--font-code);
  font-size: 0.9375rem;      /* 15px */
  line-height: 1.5;
}

.article pre {
  margin: 1.5rem 0;
  padding: 1rem 1.25rem;
  overflow-x: auto;
  white-space: pre;
}

/* Image caption */
.article figcaption {
  font-size: 0.875rem;       /* 14px */
  line-height: 1.4;
  margin-top: 0.5rem;
  max-width: 65ch;
}

/* Pull quote: differs from body by size only */
.article blockquote {
  font-size: 1.5rem;         /* 24px */
  line-height: 1.35;
  max-width: 40ch;
  margin: 2.5rem 0;
  text-wrap: balance;
}

/* Mobile */
@media (max-width: 40rem) {
  .article {
    font-size: 1rem;         /* 16px body */
    line-height: 1.5;
  }

  .article h1 {
    font-size: 1.875rem;     /* 30px */
    line-height: 1.2;
    margin-bottom: 0.75rem;
  }

  .article h2 {
    font-size: 1.5rem;       /* 24px */
    margin-top: 2.5rem;
    margin-bottom: 0.625rem;
  }

  .article h3 {
    font-size: 1.1875rem;    /* 19px */
    margin-top: 1.75rem;
    margin-bottom: 0.5rem;
  }

  .article pre,
  .article code {
    font-size: 0.875rem;     /* 14px */
  }

  .article pre {
    padding: 0.875rem 1rem;
  }

  .article figcaption {
    font-size: 0.8125rem;    /* 13px */
  }

  .article blockquote {
    font-size: 1.25rem;      /* 20px */
    line-height: 1.4;
    margin: 2rem 0;
  }
}
```

- **Assumptions:** I used a system font stack because no typeface was specified. I also used the selectors `.article`, `figcaption` and `blockquote`, so rename them to match the template's markup.
- **Spacing:** The space above each heading is about four times the space below it. That keeps headings tied to the text they introduce. Pull-quote margins are the only other generous spacing.
