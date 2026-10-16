The setup is mostly sound. Georgia-first serif body for long reading, a system UI sans for chrome, and a mono stack that ends in `monospace` are the right roles. I changed two things.

1. **`font-weight: 650` on headings.** None of these system sans faces ship a 650 cut. Segoe UI has 400, 600 and 700, Roboto has 500 and 700, and Helvetica Neue and Arial have 400 and 700. The browser snaps 650 to whatever is nearest, so headings render at different weights on different machines. Use a weight the stacks actually have: 600.
2. **Form controls.** `textarea` and `select` aren't in your UI-font selector, and browsers don't inherit fonts into form controls by default. A comment box or dropdown would fall back to the browser's default font. I also added `font: inherit` for `button` and `input`. It's a small addition and not strictly needed.

```css
:root {
  --font-body: Georgia, Cambria, 'Times New Roman', serif;
  --font-ui: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-mono: ui-monospace, Menlo, Consolas, 'Courier New', monospace;
}
body { font-family: var(--font-body); font-size: 1.125rem; line-height: 1.6; }
nav, button, label, input, textarea, select, .meta { font-family: var(--font-ui); }
code, pre { font-family: var(--font-mono); font-size: 0.9em; }
h1, h2, h3 { font-family: var(--font-ui); font-weight: 600; letter-spacing: -0.01em; }
```

I left the rest alone: all fonts are system fonts, the fallbacks are real, and Georgia has true bold and italic, so nothing is synthesized.

One thing for you to decide: sans headings over a serif body is a legitimate pairing. For a slow, long-form essay site, though, serif headings (`var(--font-body)` at 600 or 700) would feel more bookish and cohesive. Keep the sans if you want a modern, editorial look. I didn't change it because it's a style choice and not an error.
