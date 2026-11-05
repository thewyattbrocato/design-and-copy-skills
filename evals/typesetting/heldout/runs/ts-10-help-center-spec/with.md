```css
/* Help-center article: type styles
   Sizes are in rem so they follow the user's browser setting.
   Colors are left to the theme. */

:root {
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  /* Desktop scale (ratio ≈ 1.25) */
  --fs-h1: 2.5rem;
  --fs-h2: 1.75rem;
  --fs-h3: 1.25rem;
  --fs-body: 1.125rem;
  --fs-quote: 1.5rem;
  --fs-small: 0.875rem; /* caption and code */
}

@media (max-width: 40em) {
  :root {
    --fs-h1: 1.875rem;
    --fs-h2: 1.5rem;
    --fs-h3: 1.125rem;
    --fs-body: 1rem;
    --fs-quote: 1.25rem;
    --fs-small: 0.875rem;
  }
}

.article {
  font-family: var(--font-body);
  font-size: var(--fs-body);
  line-height: 1.6;
  font-synthesis: none;
}

/* Body text */
.article p,
.article li {
  max-width: 65ch;
  text-wrap: pretty;
}
.article p {
  margin: 0 0 1em;
}

/* Headings: about twice the space above as below */
.article h1,
.article h2,
.article h3 {
  text-wrap: balance;
  max-width: 30ch;
}
.article h1 {
  font-size: var(--fs-h1);
  line-height: 1.15;
  font-weight: 700;
  letter-spacing: -0.015em;
  margin: 0 0 0.6em;
}
.article h2 {
  font-size: var(--fs-h2);
  line-height: 1.2;
  font-weight: 650;
  letter-spacing: -0.01em;
  margin: 2em 0 0.75em;
}
.article h3 {
  font-size: var(--fs-h3);
  line-height: 1.3;
  font-weight: 600;
  margin: 1.75em 0 0.5em;
}

/* Code snippet: monospace, never wrapped, scrolls sideways */
.article pre,
.article code {
  font-family: var(--font-mono);
  font-size: var(--fs-small);
}
.article pre {
  line-height: 1.6;
  margin: 1.5em 0;
  padding: 1em 1.25em;
  overflow-x: auto;
  white-space: pre;
  tab-size: 2;
}
.article :not(pre) > code {
  font-size: 0.9em; /* inline code sits level with the body x-height */
}

/* Image caption: one step down, tight leading, close to its image */
.article figcaption {
  font-size: var(--fs-small);
  line-height: 1.4;
  max-width: 65ch;
  margin-top: 0.5em;
}

/* Pull quote: larger and lighter in tone, not a different face */
.article blockquote.pullquote {
  font-size: var(--fs-quote);
  line-height: 1.35;
  font-weight: 500;
  max-width: 28ch;
  margin: 2em 0;
  padding-left: 1em;
  text-wrap: balance;
}
.article blockquote.pullquote p {
  margin: 0;
  max-width: none;
}
```

Notes:
- **Curly quotes:** use “ ” in the pull quote's HTML. The CSS doesn't add them.
- **Italics and caption color:** I used no italics, because they need a real italic face (`font-synthesis: none` blocks fake ones). For the caption, make the color a lighter gray than body text but keep it readable. Don't use opacity.
