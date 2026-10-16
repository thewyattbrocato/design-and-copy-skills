```css
:root {
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  /* Desktop scale, ratio about 1.25 */
  --fs-h1: 2.5rem;       /* 40px */
  --fs-h2: 1.75rem;      /* 28px */
  --fs-h3: 1.25rem;      /* 20px */
  --fs-body: 1.125rem;   /* 18px */
  --fs-quote: 1.5rem;    /* 24px */
  --fs-code: 0.9375rem;  /* 15px */
  --fs-caption: 0.875rem;/* 14px */
}

@media (max-width: 640px) {
  :root {
    --fs-h1: 1.75rem;    /* 28px */
    --fs-h2: 1.375rem;   /* 22px */
    --fs-h3: 1.125rem;   /* 18px */
    --fs-body: 1rem;     /* 16px */
    --fs-quote: 1.25rem; /* 20px */
    --fs-code: 0.875rem; /* 14px */
    --fs-caption: 0.875rem;
  }
}

body {
  font-family: var(--font-body);
  font-size: var(--fs-body);
  line-height: 1.55;
  font-synthesis: none;
}

h1, h2, h3 {
  font-weight: 700;
  text-wrap: balance;
}

h1 {
  font-size: var(--fs-h1);
  line-height: 1.15;
  letter-spacing: -0.01em;
  margin: 0 0 1.5rem;
}

h2 {
  font-size: var(--fs-h2);
  line-height: 1.25;
  margin: 2.5rem 0 1.25rem;
}

h3 {
  font-size: var(--fs-h3);
  line-height: 1.3;
  margin: 2rem 0 0.75rem;
}

p, li {
  max-width: 65ch;
  text-wrap: pretty;
}

p {
  margin: 0 0 1em;
}

code, pre {
  font-family: var(--font-mono);
  font-size: var(--fs-code);
}

pre {
  line-height: 1.5;
  margin: 1.5rem 0;
  overflow-x: auto;
  white-space: pre;
}

figcaption {
  font-size: var(--fs-caption);
  line-height: 1.4;
  margin-top: 0.5rem;
  max-width: 65ch;
}

blockquote {
  font-size: var(--fs-quote);
  line-height: 1.35;
  font-weight: 500;
  max-width: 40ch;
  margin: 2rem 0;
  padding-left: 1.25rem;
  text-wrap: balance;
}
```

- I used element selectors (`blockquote`, `figcaption`, `pre`) since I haven't seen the template's markup. Swap in the developers' class names as needed.
- I left color out because no palette was given. Make sure the caption's color still has enough contrast, since it's the smallest text.
