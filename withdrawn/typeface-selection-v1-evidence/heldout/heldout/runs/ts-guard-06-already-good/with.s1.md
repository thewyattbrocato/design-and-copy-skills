The stack is mostly sound, so I changed only a few things. Georgia for reading, system UI sans for interface and headings, and mono for code is a good split for an essay site. Each stack ends in a real fallback, and there are only three families with clear roles.

**What I fixed**
- **Code size:** `code, pre` both get `0.9em`, so `<pre><code>` blocks compound to about 0.81em. I reset the inner `code`.
- **Heading weight:** `650` is only honored by variable system fonts. Roboto and Segoe UI have static weights, so the heading weight would differ between machines. `600` is predictable everywhere.
- **Form controls:** `textarea` and `select` weren't covered. They don't inherit fonts, so they would render in the browser default.
- **Heading levels:** `h4`–`h6` would have fallen back to the serif body font and clashed with the other headings.
- **Heading leading:** headings inherited the body's `1.6` line-height, which looks loose at display sizes. I set `1.25`.

```css
:root {
  --font-body: Georgia, Cambria, 'Times New Roman', serif;
  --font-ui: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-mono: ui-monospace, Menlo, Consolas, 'Courier New', monospace;
}
body { font-family: var(--font-body); font-size: 1.125rem; line-height: 1.6; }
nav, button, label, input, textarea, select, .meta { font-family: var(--font-ui); }
code, pre { font-family: var(--font-mono); font-size: 0.9em; }
pre code { font-size: inherit; }
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-ui);
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -0.01em;
}
```

**Your call**
- Since this is a long-form essay site, serif headings in Georgia would feel more bookish. Sans headings over a serif body is a legitimate pairing, though, and I left it.
- Georgia's figures are old-style (they dip below the baseline). That reads well in prose, but it can look uneven in dates or numbers in `.meta`. If you see that, add `font-variant-numeric: lining-nums` to `.meta`. Georgia's lining figures may not be available everywhere, and the UI sans uses lining figures by default.

I haven't rendered this. Before it goes out, check one real essay page with a code block on both macOS and Windows.
