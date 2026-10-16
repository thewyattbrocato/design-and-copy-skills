Here's the type system as CSS. I had no brand fonts or sizes to work from, so the values are placeholders. Mobile is the default and desktop applies at 768px and up, so the template works mobile-first.

```css
/* Help-center article: type styles */

:root {
  --font-sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  --color-text: #1a1a1a;
  --color-text-muted: #5c5c5c;
  --color-accent: #0b5fff;
  --color-code-bg: #f4f5f7;
}

/* ---------- Mobile (default) ---------- */

.article {
  font-family: var(--font-sans);
  color: var(--color-text);
}

.article h1 {
  font-size: 1.75rem;      /* 28px */
  line-height: 1.2;
  font-weight: 700;
  letter-spacing: -0.01em;
  margin: 0 0 1rem;
}

.article h2 {
  font-size: 1.375rem;     /* 22px */
  line-height: 1.3;
  font-weight: 650;
  margin: 2rem 0 0.75rem;
}

.article h3 {
  font-size: 1.125rem;     /* 18px */
  line-height: 1.4;
  font-weight: 600;
  margin: 1.5rem 0 0.5rem;
}

.article p,
.article li {
  font-size: 1rem;         /* 16px */
  line-height: 1.6;
  font-weight: 400;
  margin: 0 0 1rem;
}

.article code,
.article pre {
  font-family: var(--font-mono);
  font-size: 0.875rem;     /* 14px */
  line-height: 1.5;
}

.article pre {
  background: var(--color-code-bg);
  padding: 0.75rem 1rem;
  border-radius: 6px;
  overflow-x: auto;        /* scroll, don't wrap, on small screens */
  margin: 0 0 1.25rem;
}

.article p code,
.article li code {
  background: var(--color-code-bg);
  padding: 0.125em 0.35em;
  border-radius: 4px;
  font-size: 0.9em;
}

.article figcaption {
  font-size: 0.8125rem;    /* 13px */
  line-height: 1.4;
  color: var(--color-text-muted);
  margin-top: 0.5rem;
}

.article blockquote,
.article .pull-quote {
  font-size: 1.25rem;      /* 20px */
  line-height: 1.4;
  font-weight: 500;
  font-style: italic;
  margin: 1.5rem 0;
  padding-left: 1rem;
  border-left: 3px solid var(--color-accent);
}

/* ---------- Desktop ---------- */

@media (min-width: 768px) {
  .article h1 {
    font-size: 2.5rem;     /* 40px */
    line-height: 1.15;
    margin-bottom: 1.5rem;
  }

  .article h2 {
    font-size: 1.75rem;    /* 28px */
    margin: 2.5rem 0 1rem;
  }

  .article h3 {
    font-size: 1.25rem;    /* 20px */
    margin: 2rem 0 0.75rem;
  }

  .article p,
  .article li {
    font-size: 1.0625rem;  /* 17px */
    line-height: 1.65;
  }

  .article code,
  .article pre {
    font-size: 0.9375rem;  /* 15px */
  }

  .article pre {
    padding: 1rem 1.25rem;
  }

  .article figcaption {
    font-size: 0.875rem;   /* 14px */
  }

  .article blockquote,
  .article .pull-quote {
    font-size: 1.75rem;    /* 28px */
    line-height: 1.35;
    margin: 2.5rem 0;
    padding-left: 1.5rem;
  }
}
```

Notes for the handoff:
- **Placeholders:** Swap in the real font stacks, colors, and accent. I used `rem` throughout so user font-size settings are respected.
- **Selectors:** I assumed an `.article` wrapper and `figcaption` / `blockquote` / `.pull-quote` markup. Adjust these to match the template's actual class names.
- **Breakpoint:** I used a single 768px breakpoint. If the design calls for a tablet step, it's easy to add another.
- **Long code lines:** Code blocks scroll horizontally on mobile instead of wrapping. Change that if you'd rather they wrap.

If you have the design file, send me the real sizes and I'll replace the placeholders.
