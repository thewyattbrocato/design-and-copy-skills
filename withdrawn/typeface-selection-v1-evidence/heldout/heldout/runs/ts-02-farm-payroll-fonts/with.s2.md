**Recommendation:** use system fonts for the app and for the marketing site's body text. They cost 0 KB, never block rendering, and load instantly on bad connections. The only optional download is one self-hosted heading font on the marketing site.

Assumptions: Latin script (Spanish and Vietnamese accents are fine in system fonts), and a tool used mostly for scanning forms and numbers.

```css
:root {
  /* App + marketing body: Roboto on Android, Segoe UI on old Windows, SF on Apple */
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  /* Only for code/IDs (e.g. employee IDs, export previews) */
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}

html {
  font-family: var(--font-ui);
  font-synthesis: none; /* no faked bold/italic */
}

/* Money, hours and rates must align in columns */
.num, td.amount, .timesheet-hours, .pay {
  font-variant-numeric: tabular-nums;
}

code, .employee-id { font-family: var(--font-mono); }
```

**App:** use `--font-ui` for everything. Make hierarchy with weight (400 body, 500/600 labels, 700 totals) and size, not with extra families. Use tabular figures for every pay or hours column.

**Marketing site (optional heading upgrade):** the site's heading voice is the only place a custom font is worth the bytes. If your designer wants one, use a single open-license serif for headings only, such as Source Serif 4. Keep the body in the system stack.

```css
/* One subsetted Latin WOFF2, self-hosted. Check the file's license (OFL) before shipping. */
@font-face {
  font-family: "Source Serif 4";
  src: url("/fonts/source-serif-4-latin-var.woff2") format("woff2");
  font-weight: 400 700;
  font-display: swap;
}

/* Tuned local fallback so the swap doesn't shift the layout. Measure and adjust these values. */
@font-face {
  font-family: "Heading Fallback";
  src: local("Georgia");
  size-adjust: 100%; /* tune with the real font's metrics */
}

h1, h2, h3 {
  font-family: "Source Serif 4", "Heading Fallback", Georgia, "Times New Roman", serif;
  font-weight: 600;
}
```

```html
<link rel="preload" href="/fonts/source-serif-4-latin-var.woff2" as="font" type="font/woff2" crossorigin>
```

**If the page-weight budget is strict,** drop that block. Set headings in `--font-ui` at weight 700 and the site still looks consistent with the app.

**Checks before shipping:**
- Subset the font to Latin plus the accents you need, and ship WOFF2 only.
- Test with the font blocked and on a throttled connection. On a cheap Android phone the headings should fall back to a serif without the layout jumping.
- Confirm the license terms on the font page yourself. I haven't verified them, and I'm not quoting file sizes. Measure the subsetted file.
