**Recommendation: use one family, Source Sans 3, for everything.** Use regular for body text, semibold or bold for headings, and the true italic for emphasis. It's free and open source, and I believe it's under the SIL Open Font License. Confirm that on its download page before you rely on it. It comes in all the weights you need and has a real italic. Its shapes are sturdy and open, so it holds up on low-resolution screens and on photocopies.

I assumed English text, possibly with some Spanish. Source Sans 3 covers accented Latin letters, but test your actual copy, including `¿`, `¡` and `ñ`. I also assumed the handouts are printed from the same files as the web pages.

**Why one family:** The guides are long and full of headings, checklists and deadlines. One family with strong weight differences keeps the look consistent between web and print. It also means only two to four font files to host, which matters on old phones and slow library connections.

**Web CSS:**

```css
@font-face {
  font-family: "Source Sans 3";
  src: url("/fonts/SourceSans3-Regular.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
}
/* repeat for Italic (400 italic), Semibold (600), Bold (700) */

body {
  font-family: "Source Sans 3", system-ui, "Segoe UI", Roboto, Arial, sans-serif;
  font-synthesis: none;
}
```

- **Self-host the fonts.** Use WOFF2 files, subset to Latin plus accents, and limit them to those four files. This keeps pages fast and makes sure the font actually loads.
- **Fallback:** If the font fails, `system-ui` gives Roboto on Android and Segoe UI on Windows library machines. Both are decent, so the page degrades gracefully. Check it once by blocking the font in your browser.
- **`font-synthesis: none`:** This stops browsers from faking bold or italic. It only works if you load the real italic and bold files.

**Print:** Install the same font on whoever lays out the handouts, and export to PDF with fonts embedded. Don't use a different font for print. A different font would make the web and print versions look like separate publications.

**Starting sizes:** Use about 18px (roughly 12pt in print) for body text, because many of your readers will be on small or worn screens. Don't go below 16px anywhere. Use bold, not light weights, for headings. Avoid the light weights entirely.

**Two things to skip:**
- A decorative or "friendly" display font. It costs legibility and adds nothing.
- Monospace for deadlines or case numbers. Use bold Source Sans 3 instead, with tabular figures if you show dollar amounts in columns.

**If you want a second option:** Atkinson Hyperlegible is also free and designed for low-vision readers. It would suit the web pages well, but its look is more distinctive. Source Sans 3 is the safer match across web and print.

I haven't checked either font's license or glyph coverage myself, so verify both before you publish.
