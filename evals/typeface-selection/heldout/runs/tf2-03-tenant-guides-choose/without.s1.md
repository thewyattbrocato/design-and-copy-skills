**My recommendation is Atkinson Hyperlegible Next for headings and Source Serif 4 for body text in print, with system fonts as the web fallback.** Both are free under the SIL Open Font License, so you can use, embed, and self-host them commercially at no cost.

**Print handouts**
- **Headings, callouts, tables, forms:** Atkinson Hyperlegible Next. The Braille Institute designed it so similar letters (I/l/1, O/0, b/d) are easy to tell apart. That helps readers with low vision, tired eyes, or cheap printer output.
- **Body text:** Source Serif 4, or Literata if you want something a bit sturdier. If you'd rather use one family, set the body in Atkinson too. It holds up fine at 15 to 30 pages.
- **Settings:** 11 to 12 pt body, 1.4 to 1.5 line spacing, and regular and bold weights only. Embed the fonts when you export the PDF.

**Web pages**
Your readers may be on old Android phones and locked-down library PCs. Those machines may have few fonts, slow connections, or blocked external requests, so I'd do this:
- Self-host WOFF2 files instead of loading from the Google Fonts CDN. That avoids a third-party request, which can be slow or blocked.
- Use only two or three weights (regular, bold, maybe one italic). Subset to Latin plus accented characters if you publish in Spanish.
- Use `font-display: swap` so text shows immediately in the fallback font.
- Make the fallback stack safe: `"Atkinson Hyperlegible Next", system-ui, Roboto, Arial, sans-serif`. Old Android falls back to Roboto and library Windows machines to Arial. Both are legible, so nothing breaks if the custom font fails to load.
- Set body text to at least 18 px with 1.5 line height. Keep line length to about 65 characters, and use real bold instead of light weights.

**Things to avoid**
- Thin or light weights, condensed faces, and decorative display fonts. They degrade on low-resolution screens and photocopies.
- Long passages in italics or all caps.
- Paid fonts. They're not worth it here, and web licensing adds complexity.

**Two checks before you commit**
1. Make sure the font covers every language you publish in. Atkinson Next covers Latin-script languages well, but check any others.
2. Load a sample guide on an actual old Android phone and a library computer, and print one page on your cheapest printer. That test matters more than any recommendation, mine included.

If it would help, I can draft a CSS snippet with the font stack, sizes, and `@font-face` rules.
