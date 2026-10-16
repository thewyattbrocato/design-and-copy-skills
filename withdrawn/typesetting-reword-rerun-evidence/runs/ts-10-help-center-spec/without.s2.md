I didn't have a design spec, so the font families, sizes and colors below are placeholders. Swap in your brand values, which are all in the custom properties at the top. Desktop is the default, and one breakpoint overrides it for mobile.

```css
/* Help-center article: type styles */

:root {
  /* Families (placeholders: replace with brand fonts) */
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-serif: Georgia, "Times New Roman", serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  /* Colors */
  --text: #1a1a1a;
  --text-muted: #5c5c5c;
  --code-bg: #f4f5f7;
  --accent: #2563eb;

  /* Desktop scale */
  --h1-size: 2.5rem;      /* 40px */
  --h1-line: 1.2;
  --h2-size: 1.875rem;    /* 30px */
  --h2-line: 1.25;
  --h3-size: 1.375rem;    /* 22px */
  --h3-line: 1.3;
  --body-size: 1.0625rem; /* 17px */
  --body-line: 1.65;
  --code-size: 0.9375rem; /* 15px */
  --code-line: 1.55;
  --caption-size: 0.875rem; /* 14px */
  --caption-line: 1.45;
  --quote-size: 1.5rem;   /* 24px */
  --quote-line: 1.4;
}

/* Mobile overrides */
@media (max-width: 768px) {
  :root {
    --h1-size: 1.875rem;    /* 30px */
    --h1-line: 1.25;
    --h2-size: 1.5rem;      /* 24px */
    --h2-line: 1.3;
    --h3-size: 1.1875rem;   /* 19px */
    --h3-line: 1.35;
    --body-size: 1rem;      /* 16px, avoids iOS zoom and stays readable */
    --body-line: 1.6;
    --code-size: 0.875rem;  /* 14px */
    --code-line: 1.5;
    --caption-size: 0.8125rem; /* 13px */
    --caption-line: 1.4;
    --quote-size: 1.25rem;  /* 20px */
    --quote-line: 1.4;
  }
}

/* Base */
.article {
  font-family: var(--font-sans);
  font-size: var(--body-size);
  line-height: var(--body-line);
  color: var(--text);
}

/* Headings */
.article h1 {
  font-size: var(--h1-size);
  line-height: var(--h1-line);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 1.5rem;
}

.article h2 {
  font-size: var(--h2-size);
  line-height: var(--h2-line);
  font-weight: 700;
  letter-spacing: -0.01em;
  margin: 2.5rem 0 1rem;
}

.article h3 {
  font-size: var(--h3-size);
  line-height: var(--h3-line);
  font-weight: 600;
  margin: 2rem 0 0.75rem;
}

/* Body text */
.article p {
  font-size: var(--body-size);
  line-height: var(--body-line);
  font-weight: 400;
  margin: 0 0 1.25rem;
}

/* Code: inline and block */
.article code,
.article pre {
  font-family: var(--font-mono);
  font-size: var(--code-size);
  line-height: var(--code-line);
}

.article code {
  background: var(--code-bg);
  padding: 0.15em 0.4em;
  border-radius: 4px;
}

.article pre {
  background: var(--code-bg);
  padding: 1rem 1.25rem;
  border-radius: 6px;
  margin: 0 0 1.5rem;
  overflow-x: auto;      /* scroll rather than wrap, important on mobile */
  tab-size: 2;
}

.article pre code {
  background: none;
  padding: 0;
}

/* Image caption */
.article figcaption {
  font-size: var(--caption-size);
  line-height: var(--caption-line);
  color: var(--text-muted);
  margin-top: 0.5rem;
}

/* Pull quote */
.article blockquote.pull-quote {
  font-family: var(--font-serif);
  font-size: var(--quote-size);
  line-height: var(--quote-line);
  font-style: italic;
  font-weight: 400;
  color: var(--text);
  border-left: 4px solid var(--accent);
  padding: 0.25rem 0 0.25rem 1.5rem;
  margin: 2rem 0;
}

@media (max-width: 768px) {
  .article blockquote.pull-quote {
    padding-left: 1rem;
    margin: 1.5rem 0;
  }
}
```

Before you hand it off, check these:
- **Selectors:** I assumed the template wraps content in `.article` and marks the pull quote as `blockquote.pull-quote`. Match these to the developers' markup.
- **Breakpoint:** 768px is a common default. Use your own if you have one.
- **Units:** Everything is in `rem`, so sizes follow the user's browser font setting. The pixel values in the comments assume a 16px root.
- **Spacing:** I included margins because they affect how the type reads. Drop them if layout spacing lives elsewhere.

If you share the brand fonts and the type scale from the design file, I can replace the placeholders with the real values.
