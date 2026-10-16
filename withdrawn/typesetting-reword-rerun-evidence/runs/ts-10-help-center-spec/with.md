```css
/* Help-center article: type styles
   Sizes are in rem so they follow the user's browser setting.
   Roles: h1 / h2 / h3 and pull quote / body / code / caption. */

:root {
  --font-text: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-code: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;

  /* Desktop */
  --size-h1: 2.5rem;
  --size-h2: 1.75rem;
  --size-h3: 1.375rem;      /* shared with pull quote */
  --size-body: 1.125rem;
  --size-code: 0.9375rem;
  --size-caption: 0.875rem;
}

/* Mobile */
@media (max-width: 40rem) {
  :root {
    --size-h1: 1.875rem;
    --size-h2: 1.5rem;
    --size-h3: 1.25rem;
    --size-body: 1rem;
    --size-code: 0.875rem;
    --size-caption: 0.8125rem;
  }
}

.article {
  font-family: var(--font-text);
  font-size: var(--size-body);
  line-height: 1.6;
  font-synthesis: none;
  hyphens: manual;
}

/* Headings: about twice the space above as below */
.article h1,
.article h2,
.article h3 {
  font-weight: 650;
  text-wrap: balance;
}

.article h1 {
  font-size: var(--size-h1);
  line-height: 1.15;
  letter-spacing: -0.015em;
  margin: 0 0 1rem;
}

.article h2 {
  font-size: var(--size-h2);
  line-height: 1.25;
  letter-spacing: -0.01em;
  margin: 2.5rem 0 0.75rem;
}

.article h3 {
  font-size: var(--size-h3);
  line-height: 1.3;
  margin: 2rem 0 0.5rem;
}

/* Body: measure capped on the text, not the wrapper */
.article p,
.article li {
  max-width: 65ch;
  text-wrap: pretty;
}

.article p {
  margin: 0 0 1em;
}

/* Code snippet */
.article code,
.article pre {
  font-family: var(--font-code);
  font-size: var(--size-code);
  line-height: 1.5;
}

.article pre {
  margin: 1.5rem 0;
  padding: 1rem 1.25rem;
  overflow-x: auto;
  white-space: pre;      /* keep code unwrapped; scroll instead */
  tab-size: 2;
}

/* Image caption */
.article figcaption {
  font-size: var(--size-caption);
  line-height: 1.4;
  margin-top: 0.5rem;
  max-width: 65ch;
}

/* Pull quote: same size as h3, set apart by style and space */
.article blockquote {
  font-size: var(--size-h3);
  line-height: 1.4;
  font-style: italic;
  font-weight: 500;
  max-width: 40ch;
  margin: 2.5rem 0;
  padding-left: 1.25rem;
  text-wrap: balance;
}

.article blockquote p {
  margin: 0;
}
```

Notes:
- I assumed a system font stack and left colors to the template. Swap `--font-text` for the brand face when you have it.
- Desktop and mobile share the same six roles. Only the values change, in the one `@media` block. H3 and the pull quote share a size, so the pull quote stands out through italic, indent and space.
