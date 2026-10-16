**Recommendation:** use the system font stack in the app, which costs 0 KB. On the marketing site, use the same stack for body text and one self-hosted web font for headings only. Both are free.

## App (Android phones and old laptops)

```css
:root {
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Roboto Mono", monospace;
}

body {
  font-family: var(--font-ui);
}

/* Hours, pay rates and totals: digits line up in columns */
.num, td.num, input[type="number"] {
  font-variant-numeric: tabular-nums;
}
```

- **Cost:** nothing to download, no flash of unstyled text, and no layout shift.
- **Look:** cheap Android phones get Roboto and old Windows laptops get Segoe UI. Both are built for legibility on low-quality screens.
- **Numbers:** `tabular-nums` matters for a payroll app, because hours and dollar columns need to align.

## Marketing site

Use Inter Bold for headings only, self-hosted as a Latin-only WOFF2 subset (about 15–25 KB). Keep body text on the system stack.

```css
@font-face {
  font-family: "Inter Heading";
  src: url("/fonts/inter-bold-latin.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

/* Metric-matched fallback so headings don't jump when the font loads */
@font-face {
  font-family: "Inter Fallback";
  src: local("Arial");
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}

:root {
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-heading: "Inter Heading", "Inter Fallback", var(--font-body);
}

body { font-family: var(--font-body); }
h1, h2, h3 { font-family: var(--font-heading); font-weight: 700; }
```

Preload it in `<head>`, and only the heading font:

```html
<link rel="preload" href="/fonts/inter-bold-latin.woff2" as="font" type="font/woff2" crossorigin>
```

## Getting the file

Inter is licensed under the SIL OFL, so it's free for commercial use. Download it from [rsms.me/inter](https://rsms.me/inter) or GitHub, then subset it:

```sh
pip install fonttools brotli
pyftsubset Inter-Bold.ttf \
  --unicodes="U+0020-007E,U+00A0-00FF,U+2013,U+2014,U+2018,U+2019,U+201C,U+201D,U+2022,U+2026,U+20AC" \
  --flavor=woff2 --layout-features='kern,liga,tnum' \
  --output-file=inter-bold-latin.woff2
```

## Things to avoid

- **Google Fonts CDN:** it adds a DNS lookup, a TLS handshake and a CSS round trip before the font file even starts. On a bad rural connection that is the worst case.
- **Full variable fonts or many weights:** each extra weight is another request.
- **Icon fonts:** use inline SVG instead.
- **Web fonts inside the app:** the app is where reliability matters most, and the system stack already looks fine there.

The fallback metrics (`size-adjust` and the overrides) are approximate. Check them against your actual subset, or generate exact values with a tool like Fontaine or Capsize.

If the designer wants more personality for the marketing site, swap in a different single-weight heading font and keep the same pattern. Budget about 20 KB for it.
