```css
/* Help-center article type styles
   Assumes a light ground and a system font stack. Swap --font-body and
   --font-mono for the brand faces if they differ. */

.article {
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  /* Desktop */
  --fs-h1: 2.25rem;
  --fs-h2: 1.5rem;
  --fs-h3: 1.25rem;
  --fs-body: 1.0625rem;
  --fs-small: 0.875rem;   /* code, captions */
  --fs-quote: 1.5rem;

  font-family: var(--font-body);
  font-size: var(--fs-body);
  line-height: 1.55;
  font-synthesis: none;
}

@media (max-width: 600px) {
  .article {
    --fs-h1: 1.75rem;
    --fs-h2: 1.375rem;
    --fs-h3: 1.125rem;
    --fs-body: 1rem;
    --fs-quote: 1.25rem;
    /* --fs-small stays 0.875rem */
  }
}

.article h1,
.article h2,
.article h3 {
  max-width: 30ch;
  text-wrap: balance;
}

.article h1 {
  font-size: var(--fs-h1);
  line-height: 1.15;
  font-weight: 700;
  letter-spacing: -0.015em;
  margin: 0 0 1rem;
}

.article h2 {
  font-size: var(--fs-h2);
  line-height: 1.25;
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

.article p,
.article li {
  max-width: 65ch;
  text-wrap: pretty;
}

.article p {
  margin: 0 0 1rem;
}

/* Code snippet */
.article code,
.article pre {
  font-family: var(--font-mono);
  font-size: var(--fs-small);
  line-height: 1.5;
}

.article pre {
  max-width: 100%;
  margin: 1.5rem 0;
  padding: 1rem;
  overflow-x: auto;   /* keep code unwrapped; scroll instead */
  white-space: pre;
  tab-size: 2;
}

/* Image caption */
.article figcaption {
  max-width: 65ch;
  margin-top: 0.5rem;
  font-size: var(--fs-small);
  line-height: 1.4;
}

/* Pull quote: one step up from body, differs by size and style only */
.article blockquote {
  max-width: 40ch;
  margin: 2rem 0;
  font-size: var(--fs-quote);
  line-height: 1.35;
  font-style: italic;   /* needs a real italic face in the brand font */
  text-wrap: balance;
}
```

Notes:
- The desktop sizes are 36, 24, 20, 17, 24 (quote) and 14px. On mobile, h1 drops to 28px and body to 16px. That makes five distinct sizes, and the pull quote shares the h2 size.
- The pull quote uses italic, so the brand font needs a real italic face. If it doesn't have one, switch to a heavier weight or add a left rule, because `font-synthesis: none` stops the browser from faking italics. I didn't set any colors, since the template didn't specify them.
