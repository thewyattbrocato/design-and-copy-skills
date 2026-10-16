Your setup is already solid: a system font stack (fast, no downloads), a comfortable line height, and tabular numbers in tables. I'd make a few small changes.

```css
:root {
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}

body {
  font-family: var(--font-body);
  font-size: 1.0625rem;
  line-height: 1.55;
  font-weight: 400;
}

h1, h2, h3 {
  font-weight: 700;
  line-height: 1.2;
  text-wrap: balance;
}
h1, h2 { letter-spacing: -0.01em; }

table th.num,
table td.num { font-variant-numeric: tabular-nums; text-align: right; }

code, pre { font-family: var(--font-mono); }
code { font-size: 0.92em; }
pre code { font-size: inherit; }
```

**What changed and why**

- **Weight 650 → 700.** Weights between the standard steps (400, 500, 600, 700) only work with variable fonts. System fonts usually don't have them, so each browser rounds 650 to a different weight. 700 looks the same everywhere. Use 600 if you want something lighter.
- **Removed `font-family` from the headings.** They inherit it from `body`, so repeating it did nothing.
- **Letter-spacing only on h1 and h2.** Tightening helps large text, but at h3 size it just makes the letters crowd.
- **`text-wrap: balance` on headings.** This stops a single word from sitting alone on the last line of a wrapped heading. Older browsers ignore it, which is harmless.
- **Header cells now get tabular numbers and right alignment too.** A column header like "Dues" then lines up with the numbers under it. This assumes you add `class="num"` to those `<th>` elements.
- **Added `pre` and `Liberation Mono`.** Code blocks now use the mono font, and Linux users get a decent mono font. `pre code { font-size: inherit }` stops the 0.92em shrink from applying twice inside code blocks.

I left the 17px body size and 1.55 line height alone, since both are good for reading. Custom web fonts would add loading time and upkeep, and a volunteer-run site probably doesn't need them.

I haven't seen your actual pages, so check a table and a code block in the browser after you paste this in.
