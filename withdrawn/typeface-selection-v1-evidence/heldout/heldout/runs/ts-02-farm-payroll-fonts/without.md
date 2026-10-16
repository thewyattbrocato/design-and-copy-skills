# Recommendation

- **App:** use the system font stack and ship no font files. That's 0 bytes and no flash of invisible text. Roboto on Android and Segoe UI on old Windows laptops are both readable at small sizes, and they support tabular numerals, which matter for hours and pay.
- **Marketing site:** use the same system stack for body text. Add one self-hosted heading face, **Bitter** (SIL OFL, free for commercial use), at a single weight (700), subset to Latin. This gives the site some farm-friendly personality for roughly 10–20 KB. Treat that size as an estimate and check the file you actually produce.

Don't load fonts from the Google Fonts CDN. It adds a DNS lookup and TLS handshake, which hurts on bad rural connections. Self-host the file instead.

## App CSS

```css
:root {
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

body {
  font-family: var(--font-ui);
}

/* Hours, pay rates, totals: aligned columns */
.num, td, th, input[type="number"] {
  font-variant-numeric: tabular-nums;
}
```

## Marketing site CSS

```css
@font-face {
  font-family: "Bitter";
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url("/fonts/bitter-700-latin.woff2") format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2013-2014, U+2018-201D, U+2022, U+2026, U+20AC;
}

:root {
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-head: "Bitter", Georgia, "Times New Roman", serif;
}

body { font-family: var(--font-ui); }
h1, h2, h3 { font-family: var(--font-head); font-weight: 700; }
```

Preload it so the headings don't wait on the CSS:

```html
<link rel="preload" href="/fonts/bitter-700-latin.woff2" as="font" type="font/woff2" crossorigin>
```

## Making the font file

Download Bitter from Google Fonts (the download is OFL-licensed). Then subset it and convert it to woff2:

```sh
pip install fonttools brotli
pyftsubset Bitter-Bold.ttf \
  --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+2013-2014,U+2018-201D,U+2022,U+2026,U+20AC" \
  --flavor=woff2 --layout-features='kern,liga,lnum' \
  --output-file=bitter-700-latin.woff2
```

If you need Spanish or other accented text, `U+0000-00FF` already covers it. If you expect workers' names outside Latin-1, widen the range.

Two other points:

- `font-display: swap` means headings show in Georgia first and then swap. That's the right trade-off on slow connections.
- If you'd rather ship nothing on the marketing site either, drop the `@font-face` and set `--font-head: Georgia, serif`. It will still look deliberate.
