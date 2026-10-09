I'd pair a serif for headings with the system sans for body text.

**Headings: Georgia, with a serif fallback**
```css
--font-heading: Georgia, "Times New Roman", serif;
```
Georgia ships on Mac, Windows and iOS. A serif reads as established and trustworthy, which suits law firms, and it's the quickest way to make the marketing site feel less generic. Android doesn't ship Georgia, so it falls through to the generic `serif` (Noto Serif). That's acceptable, but check it on a real Android device.

**Body and UI: the system UI stack**
```css
--font-body: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
```
This resolves to SF Pro on Apple devices, Segoe UI on Windows and Roboto on Android. It's crisp and familiar, and it's built for small sizes. The pairing works because the two faces differ clearly in structure, so the contrast looks deliberate.

**Where to use the serif**
- **Marketing site:** use it for h1 through h3, pull quotes and big numbers in hero sections.
- **Product UI:** use it sparingly, if at all. Page titles are fine. Georgia's default old-style (lowercase-height) numerals look wrong and misalign in invoices, ledgers and tables. Keep all money and data in the sans with `font-variant-numeric: tabular-nums`.

**An alternative**
If you want something less ubiquitous than Georgia, use a Charter-style stack: `Charter, "Bitstream Charter", "Sitka Text", Cambria, serif`. It's more distinctive, but it's a different typeface on each platform, so your design will look slightly different from one to the next. Georgia is the safer choice while you're limited to system fonts.

When legal clears web fonts, you only need to swap the two variables. A good upgrade would be a serif like Source Serif or Newsreader for headings, with Inter or the system stack for body.

I can draft the CSS variables and a type scale if you point me at the codebase.
