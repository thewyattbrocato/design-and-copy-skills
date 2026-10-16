**Use system fonts for both. That means no font downloads and no licence cost, and the text shows up on the first paint even on a bad connection.** Cheap Android phones render Roboto or Noto, and old Windows laptops render Segoe UI. Both are sturdy at small sizes.

I assumed Latin script (English and Spanish accents are covered by system fonts) and screens only.

```css
:root {
  /* App + marketing body: scanning UI text, forms, tables */
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;

  /* Marketing headlines only: warmer, farm-friendly voice, still zero bytes */
  --font-display: "Iowan Old Style", Charter, "Palatino Linotype", Georgia, serif;

  /* Employee IDs, pay codes, exports */
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}

html { font-family: var(--font-ui); font-synthesis: none; }

/* Hours, wages and totals must line up in columns */
table, .money, .hours, input[type="number"] { font-variant-numeric: tabular-nums; }

/* Marketing site only */
.marketing h1, .marketing h2 { font-family: var(--font-display); font-weight: 700; }

code, .employee-id { font-family: var(--font-mono); }
```

**Roles**
- **App:** `--font-ui` only. Build hierarchy with weight (400, 500/600, 700) and size, not a second family. Use at least 16px for body text and inputs, since workers will use it outdoors on small, low-quality screens.
- **Marketing site:** the same UI stack for body text. Headlines use the serif stack, so the site feels less like software. It renders as Charter or Iowan on Apple devices, Georgia on Windows and Noto Serif on Android. Check that once on a real cheap Android phone, because it will look different on each platform.
- **Mono:** only for IDs and codes, never for headings or buttons.

**Caveats**
- System stacks look slightly different on each device, so the brand will not look identical everywhere. That is the cost of loading nothing.
- If you later want one distinctive face, add a single self-hosted, subset WOFF2 for marketing headlines only, with `font-display: swap`. Pick an open-licence face and confirm its licence terms with the foundry. Leave the app on system fonts.
