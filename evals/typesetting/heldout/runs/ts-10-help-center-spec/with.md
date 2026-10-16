```css
/* Help-center article type styles.
   Sizes are rem so they follow the user's browser setting.
   Swap --font-body / --font-mono for the brand faces. */

:root {
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  /* Desktop scale (ratio ≈ 1.25) */
  --text-h1: 2.25rem;
  --text-h2: 1.75rem;
  --text-h3: 1.375rem;
  --text-quote: 1.375rem;
  --text-body: 1.125rem;
  --text-code: 0.9375rem;
  --text-caption: 0.875rem;
}

/* Mobile scale */
@media (max-width: 40rem) {
  :root {
    --text-h1: 1.75rem;
    --text-h2: 1.5rem;
    --text-h3: 1.25rem;
    --text-quote: 1.25rem;
    --text-body: 1rem;
    --text-code: 0.875rem;
    --text-caption: 0.875rem;
  }
}

.article {
  font-family: var(--font-body);
  font-size: var(--text-body);
  line-height: 1.55;
  font-synthesis: none;
}

/* Headings: tighter leading, about twice as much space above as below */
.article h1 {
  font-size: var(--text-h1);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.01em;
  margin: 0 0 0.75em;
  text-wrap: balance;
}

.article h2 {
  font-size: var(--text-h2);
  font-weight: 700;
  line-height: 1.2;
  margin: 2em 0 0.75em;
  text-wrap: balance;
}

.article h3 {
  font-size: var(--text-h3);
  font-weight: 600;
  line-height: 1.25;
  margin: 1.75em 0 0.5em;
  text-wrap: balance;
}

/* Body: gap between paragraphs, no indent */
.article p,
.article li {
  max-width: 65ch;
  text-wrap: pretty;
}

.article p {
  margin: 0 0 1em;
}

/* Code snippet: not prose, so it keeps its own width and doesn't wrap */
.article pre,
.article code {
  font-family: var(--font-mono);
  font-size: var(--text-code);
  line-height: 1.5;
}

.article pre {
  margin: 1.5em 0;
  padding: 1rem;
  overflow-x: auto;
  white-space: pre;
  tab-size: 2;
}

/* Image caption: one step down from body, tighter leading */
.article figcaption {
  max-width: 65ch;
  margin-top: 0.5em;
  font-size: var(--text-caption);
  line-height: 1.4;
}

/* Pull quote: set off by size alone (no italic, no extra indent) */
.article blockquote {
  max-width: 40ch;
  margin: 2em 0;
  font-size: var(--text-quote);
  font-weight: 500;
  line-height: 1.35;
  text-wrap: balance;
}
```

Two assumptions:
- I used a system font stack as a placeholder, so swap in the brand faces through the two `--font-*` variables.
- I guessed at the selectors (`.article`, `figcaption`, `blockquote`, `pre`), so rename them to match the template's markup.
