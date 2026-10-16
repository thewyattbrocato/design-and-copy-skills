Your setup is already sound. It uses system fonts, which load instantly, need no licensing, and look native on every device. The body size and line height are good for reading. I'd only make a few small changes.

```css
:root {
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", "Cascadia Mono", Menlo, Consolas, "Liberation Mono", monospace;
}

html { -webkit-text-size-adjust: 100%; }

body {
  font-family: var(--font-body);
  font-size: 1.0625rem;
  line-height: 1.55;
  font-weight: 400;
}

h1, h2, h3 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.01em;
  text-wrap: balance;
}
h1 { font-size: 2rem; }
h2 { font-size: 1.5rem; }
h3 { font-size: 1.25rem; }

p, li { max-width: 70ch; }

table th.num,
table td.num { font-variant-numeric: tabular-nums; text-align: right; }

code, kbd, pre { font-family: var(--font-mono); font-size: 0.92em; }
```

**What changed and why**

- **Heading weight 650 → 700.** 650 only works with variable fonts. Most system fonts (Segoe UI, Arial, Helvetica) only have regular and bold, so browsers round 650 to one or the other, and the result differs between devices. 700 gives the same look everywhere.
- **Heading sizes.** You didn't set any, so headings use browser defaults, which can be too close to body size or too large. The sizes above give a clear hierarchy. Adjust them to taste.
- **`text-wrap: balance`.** Stops headings from leaving a single word alone on the last line. Browsers that don't support it ignore it.
- **Mono stack.** Added Cascadia Mono (newer Windows) and Liberation Mono (Linux) as fallbacks. I also applied the font to `kbd` and `pre`, which otherwise use the browser's default monospace.
- **`th.num`.** Without it, a right-aligned number column has a left-aligned header sitting over it.
- **`max-width: 70ch` on text.** Keeps lines readable on wide screens. Skip it if your layout already limits the width.
- **`-webkit-text-size-adjust`.** Keeps iOS from resizing text unpredictably when a phone is rotated.

I left `tabular-nums`, the 1.55 line height, the 17px body size and the slight negative heading letter-spacing alone, since they're already well chosen.

This was pasted text rather than a file, so I haven't changed any files. If you tell me where the stylesheet is, I can apply the changes there.
