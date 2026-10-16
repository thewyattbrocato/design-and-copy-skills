**Short answer:** use the system font stack for the app, and the same stack plus one small self-hosted heading font for the marketing site. Everything here is free (system fonts, or OFL-licensed).

## App: system fonts only (0 bytes)

Your users are on cheap Android phones (Roboto) and old office laptops (Segoe UI or Arial). Those fonts are already installed, so they render instantly with no layout shift, even offline.

```css
:root {
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Consolas, "Roboto Mono", monospace;
}

body {
  font-family: var(--font-ui);
}

/* Hours, wages, and totals line up in columns */
table, .num, input[type="number"] {
  font-variant-numeric: tabular-nums;
}
```

`tabular-nums` matters most for a payroll app. Without it, columns of hours and pay can look ragged in some system fonts.

## Marketing site: system body, one web font for headings

Body text stays on the system stack. Add a single font for headings and the logo for some personality. I'd pick **Bitter**, a sturdy slab serif under the SIL OFL that suits a farm audience. The alternative is **Source Serif 4**. Load only one weight or one variable file, Latin only.

```css
@font-face {
  font-family: "Bitter";
  src: url("/fonts/bitter-latin-var.woff2") format("woff2");
  font-weight: 600 800;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+2000-206F, U+20AC, U+2122;
}

:root {
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-heading: "Bitter", Georgia, "Times New Roman", serif;
}

body { font-family: var(--font-ui); }
h1, h2, h3 { font-family: var(--font-heading); font-weight: 700; }
```

```html
<link rel="preload" href="/fonts/bitter-latin-var.woff2" as="font" type="font/woff2" crossorigin>
```

## Setup notes

- **Self-host, don't use the Google Fonts CDN.** It costs an extra DNS and TLS round trip on a bad connection.
- **Subset to Latin and convert to woff2.** The full font files are much larger than you need:
  ```sh
  pip install fonttools brotli
  pyftsubset Bitter[wght].ttf --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122" \
    --flavor=woff2 --layout-features='kern,liga,lnum' --output-file=bitter-latin-var.woff2
  ```
  Check the output size. A Latin-only variable subset should land in the tens of KB. If it's bigger than you want, drop to a single static weight (700).
- **Keep `font-display: swap`.** Text shows immediately in the fallback and swaps when the font arrives, so a slow connection never gives you blank headings.
- **Add Spanish accents if needed.** The `U+0000-00FF` range already covers á, é, ñ and similar. If you serve other languages, check the glyph coverage before subsetting.

If the designer wants the page lighter still, drop Bitter and use the system stack with heavier weights for headings. That gives you zero font requests, and it would still look fine.
