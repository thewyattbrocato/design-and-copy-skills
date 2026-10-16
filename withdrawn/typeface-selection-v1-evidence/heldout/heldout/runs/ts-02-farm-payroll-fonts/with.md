**Recommendation: system fonts for the app, and one self-hosted open-licence font for the marketing headlines only.**

Assumptions: Latin script only, English first. Seasonal workers may need other languages later, and that would change the pick.

The app runs on cheap Android phones and old office laptops over bad connections. For a tool like that, the system font is the right choice, not a fallback. It costs 0 KB, never flashes or shifts, and is already tuned for each device's screen. Roboto on Android and Segoe UI on Windows are both sturdy and easy to read at small sizes.

**App (0 KB of fonts)**
```css
:root {
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}
body { font-family: var(--font-ui); font-synthesis: none; }

/* Money, hours and totals: figures must line up in columns */
.num, td.amount, td.hours { font-variant-numeric: tabular-nums; }

/* Only for IDs, codes and export previews, never headings or buttons */
code, .mono { font-family: var(--font-mono); }
```
Use weights 400, 500/600 and 700 for hierarchy. Don't use a light weight on cheap, low-density screens. `tabular-nums` matters for a payroll tool, because it keeps pay and hours aligned.

**Marketing site (one small file, headlines only)**

Use **Source Serif 4** for headlines. It is a warm, sturdy serif that suits farms and trust without looking like a gimmick. Set body text in the same system UI stack as the app, so the site and product feel like one thing and the page stays light. The only licence I can point you to is the SIL Open Font License, which Google Fonts lists for it. Confirm that on the font's page before you ship.

```css
@font-face {
  font-family: "Source Serif 4";
  src: url("/fonts/source-serif-4-latin-semibold.woff2") format("woff2");
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}

/* Fallback tuned so the swap doesn't shift the layout.
   Take the override values from a metrics tool such as Fontaine or Capsize. */
@font-face {
  font-family: "Source Serif Fallback";
  src: local("Georgia");
  /* size-adjust / ascent-override / descent-override / line-gap-override */
}

:root {
  --font-display: "Source Serif 4", "Source Serif Fallback", Charter, "Iowan Old Style", Georgia, serif;
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

body { font-family: var(--font-ui); font-synthesis: none; }
h1, h2 { font-family: var(--font-display); font-weight: 600; }
```
```html
<link rel="preload" href="/fonts/source-serif-4-latin-semibold.woff2" as="font" type="font/woff2" crossorigin>
```

- **Self-host it.** Download the font, subset it to Latin and save it as WOFF2 with a tool like `pyftsubset` or glyphhanger. Don't load it from a third-party CDN. That's an extra connection on a slow link, and Google Fonts is also a privacy concern in some regions.
- **One weight, one file.** I haven't measured the size. A Latin-subset WOFF2 for a single weight is typically small, but check the real file against your budget. If it's too big, drop the web font and use the `Charter, "Iowan Old Style", Georgia` stack for headlines. That's free.
- **Never block text.** `font-display: swap` keeps headlines visible while the font loads, and Georgia is a decent stand-in.

**Test before shipping:** load the site on a throttled connection with the font blocked, on a real low-end Android phone, and on an old Windows laptop. Check that the fallback headlines and the money columns still look right.

If you'd rather ship zero font files on the marketing site too, use the Charter/Georgia stack for headlines. You'd lose a little consistency across platforms and keep every byte.
