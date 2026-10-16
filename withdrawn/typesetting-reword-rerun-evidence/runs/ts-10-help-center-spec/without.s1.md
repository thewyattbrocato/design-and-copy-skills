Here's the CSS. I didn't have a type spec or brand tokens, so the font families, sizes and colors are my own defaults. Swap in the real values from the design file before handoff.

```css
/* Help-center article template: type styles
   Mobile-first; desktop overrides at 768px and up. */

:root {
  --font-sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  --color-text: #1a1a1a;
  --color-text-muted: #5c5c5c;
  --color-accent: #0b5fff;
  --color-code-bg: #f4f5f7;

  /* Mobile type scale */
  --h1-size: 1.75rem;    /* 28px */
  --h1-line: 1.2;
  --h2-size: 1.375rem;   /* 22px */
  --h2-line: 1.3;
  --h3-size: 1.125rem;   /* 18px */
  --h3-line: 1.35;
  --body-size: 1rem;     /* 16px */
  --body-line: 1.6;
  --code-size: 0.875rem; /* 14px */
  --code-line: 1.5;
  --caption-size: 0.8125rem; /* 13px */
  --caption-line: 1.4;
  --quote-size: 1.25rem; /* 20px */
  --quote-line: 1.4;
}

@media (min-width: 768px) {
  :root {
    --h1-size: 2.5rem;     /* 40px */
    --h1-line: 1.15;
    --h2-size: 1.75rem;    /* 28px */
    --h2-line: 1.25;
    --h3-size: 1.25rem;    /* 20px */
    --h3-line: 1.3;
    --body-size: 1.0625rem; /* 17px */
    --body-line: 1.65;
    --code-size: 0.9375rem; /* 15px */
    --code-line: 1.55;
    --caption-size: 0.875rem; /* 14px */
    --caption-line: 1.4;
    --quote-size: 1.75rem; /* 28px */
    --quote-line: 1.35;
  }
}

/* Body text */
.article,
.article p {
  font-family: var(--font-sans);
  font-size: var(--body-size);
  line-height: var(--body-line);
  font-weight: 400;
  color: var(--color-text);
}

.article p {
  margin: 0 0 1em;
}

/* Headings */
.article h1 {
  font-family: var(--font-sans);
  font-size: var(--h1-size);
  line-height: var(--h1-line);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 0.75em;
}

.article h2 {
  font-family: var(--font-sans);
  font-size: var(--h2-size);
  line-height: var(--h2-line);
  font-weight: 700;
  letter-spacing: -0.01em;
  margin: 1.75em 0 0.5em;
}

.article h3 {
  font-family: var(--font-sans);
  font-size: var(--h3-size);
  line-height: var(--h3-line);
  font-weight: 600;
  margin: 1.5em 0 0.5em;
}

/* Code snippet */
.article code,
.article pre {
  font-family: var(--font-mono);
  font-size: var(--code-size);
  line-height: var(--code-line);
}

.article pre {
  background: var(--color-code-bg);
  border-radius: 6px;
  padding: 1em;
  margin: 0 0 1.25em;
  overflow-x: auto;
  tab-size: 2;
}

.article :not(pre) > code {
  background: var(--color-code-bg);
  border-radius: 4px;
  padding: 0.15em 0.35em;
}

/* Image caption */
.article figcaption {
  font-family: var(--font-sans);
  font-size: var(--caption-size);
  line-height: var(--caption-line);
  font-weight: 400;
  color: var(--color-text-muted);
  margin-top: 0.5em;
}

/* Pull quote */
.article blockquote,
.article .pull-quote {
  font-family: var(--font-sans);
  font-size: var(--quote-size);
  line-height: var(--quote-line);
  font-weight: 500;
  letter-spacing: -0.01em;
  color: var(--color-text);
  margin: 1.5em 0;
  padding-left: 1em;
  border-left: 4px solid var(--color-accent);
}
```

**Notes for the developers**
- Everything is scoped under `.article`, so rename it to match the template's wrapper class.
- The sizes are tokens in `:root`. Desktop only redefines the variables, so the element rules stay the same.
- Sizes are in `rem`, so they respect users' browser font settings.
- The pull quote targets both `blockquote` and `.pull-quote`. Keep whichever matches the markup.

If you have the type spec from design, send it and I'll replace my defaults with the real values. I can also save this as a `.css` file if you want one.
