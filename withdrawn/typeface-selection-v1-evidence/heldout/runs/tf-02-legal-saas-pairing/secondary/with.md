**Go with a serif for marketing headings and the system sans for body text.** Iowan Old Style on Mac and iOS gives the marketing site a warm, editorial voice, and the sans keeps it sober and legible. That suits a product that handles client money and trust accounts.

- **Marketing headings:** a serif display stack. It is the change that will stop the site from looking bland.
- **Marketing body and product UI:** the system UI sans, with tabular figures for amounts and counts. It is the default, but the figures matter for billing screens.
- **Product UI headings:** keep the sans. Use the serif only on printed or document-like surfaces, such as invoice previews, so the app stays calm in transactional screens.

```css
--font-display: "Iowan Old Style", Charter, "Palatino Linotype", Palatino, Georgia, serif;
--font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;

.amount, td.num { font-variant-numeric: tabular-nums; }
body { font-synthesis: none; }
```

Notes:

- **Platform differences:** Mac and iOS get Iowan Old Style. Windows has no Iowan, so headings fall to Palatino Linotype, which looks different. Android may fall through to a generic serif. Check the headings on Windows and Android before you ship.
- **Not rendered:** I checked this from the stack rules and the font names, not by rendering it. The font inventory per platform is from memory, so confirm it on your target OS versions.
- **Assumptions:** screen-only, Latin-script, no web fonts. Licensing is moot because everything is installed system fonts.
