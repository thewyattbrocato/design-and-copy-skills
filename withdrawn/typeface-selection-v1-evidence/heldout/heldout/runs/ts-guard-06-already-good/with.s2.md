The stack is sound for a long-form essay site. It has serif for reading, system sans for interface and headings, and mono only for code. Each role has a real fallback chain, and Georgia has a true bold and italic. I changed four things.

```css
:root {
  --font-body: Georgia, Cambria, 'Times New Roman', serif;
  --font-ui: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-mono: ui-monospace, Menlo, Consolas, 'Courier New', monospace;
}
body { font-family: var(--font-body); font-size: 1.125rem; line-height: 1.6; font-synthesis: none; }
nav, button, label, input, textarea, select, figcaption, .meta { font-family: var(--font-ui); }
code, pre { font-family: var(--font-mono); font-size: 0.9em; }
pre code { font-size: inherit; }
h1, h2, h3, h4, h5, h6 { font-family: var(--font-ui); font-weight: 600; letter-spacing: -0.01em; }
```

1. **Nested code shrank twice.** `code, pre` both get `0.9em`, so a `<pre><code>` block rendered at about 0.81em. `pre code { font-size: inherit; }` fixes that.
2. **`h4`–`h6` were missing.** They would have fallen back to the serif body font and looked inconsistent with `h1`–`h3`. They now share the heading rule.
3. **Form controls and captions weren't covered.** `textarea` and `select` don't inherit the page font, so they would have used the browser default. I added them, plus `figcaption`, which is the usual caption element in essays. Drop `figcaption` if you set captions in the serif.
4. **Weight `650` was unreliable.** Only variable system fonts honour it. Segoe UI, Arial and Helvetica snap to 400 or 700, so headings would look different from platform to platform. `600` is more predictable.

I also added `font-synthesis: none` so a missing weight or style can't be faked with fake bold or italic. Georgia and the system sans fonts have real ones, so nothing changes today.

I assumed a Latin-script, screen-only site that uses system fonts only. If the client wants a custom web font for the headings or body, the stack should be revisited. I haven't previewed this in a browser.
