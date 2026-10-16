Your setup is already solid: a system font stack, a comfortable line-height, tabular numerals on number columns, and slightly tightened heading spacing. These are the changes I'd make, in order of impact.

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
  -webkit-text-size-adjust: 100%;
  text-rendering: optimizeLegibility;
  font-kerning: normal;
}

h1, h2, h3 {
  font-family: var(--font-body);
  font-weight: 650;
  line-height: 1.2;
  letter-spacing: -0.01em;
  text-wrap: balance;
}

h1 { font-size: 2rem; }
h2 { font-size: 1.5rem; }
h3 { font-size: 1.25rem; }

p, li { max-width: 70ch; }

table td.num,
table th.num {
  font-variant-numeric: tabular-nums;
  text-align: right;
}

code, kbd, samp, pre {
  font-family: var(--font-mono);
  font-size: 0.92em;
}
```

**What changed and why**

1. **Heading sizes (`h1`–`h3`).** Your headings had weights and spacing but no sizes, so they fall back to browser defaults, which vary. Setting a clear scale keeps them consistent.
2. **Line length (`max-width: 70ch`).** Long lines are hard to read. About 60–75 characters is the sweet spot. If your layout already constrains width, you can drop this.
3. **`text-wrap: balance` on headings.** This avoids a single orphaned word on the last line of a wrapped heading. Older browsers ignore it, so it's harmless.
4. **Number column headers.** `th.num` now matches `td.num`, so the header lines up with its right-aligned numbers.
5. **Mono stack.** I added `"Liberation Mono"`, which covers many Linux systems. I also applied the mono font to `kbd`, `samp`, and `pre`, so they match `code`.
6. **Small rendering tweaks.** `-webkit-text-size-adjust` stops iOS from resizing text unpredictably in landscape. `font-kerning: normal` makes kerning explicit.

**Things I left alone**

- **System fonts.** For a volunteer-run portal, this is the right call. There's nothing to download or host, it loads fast, and it looks native on each device.
- **Weight 650.** It's a valid value, but it only takes effect with variable system fonts such as the system UI font on recent macOS and Windows. Elsewhere it rounds to 700 (bold). That's fine.
- **Body size and line-height.** 17px at 1.55 is comfortable and accessible.

**One caution:** `code` inside `pre` can end up slightly smaller than intended, because `0.92em` applies to both. If you see that, add `pre code { font-size: 1em; }`.

I haven't seen the actual pages, so I couldn't check these changes in context. If you point me at the project files, I can apply them and look for any conflicting styles.
