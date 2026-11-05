**Use one free family, Source Sans 3, for everything, and self-host it.**

I'm assuming English plus possibly Spanish, a mix of phones and locked-down library PCs where readers can't install fonts, and print made from the same files as the web pages.

**Why one family:** It's open-licensed (SIL OFL), so it costs nothing and you can use it on the web and in print. It has regular, semibold, bold and a true italic, so you can build headings, callouts and emphasis from weight and size alone. Two families would add work and loading time without much benefit for plain guides. Confirm the license on the Google Fonts or Adobe page before you rely on it.

**Roles:**
- **Body:** Regular 400, with true italic for emphasis.
- **Headings and key deadlines:** Semibold 600 or Bold 700, in the same family.
- **Callouts such as "You have 5 days to respond":** Semibold at body size, in a boxed or tinted block. Don't use all caps or color alone.
- **Code or monospace:** Not needed.

**CSS:**
```css
@font-face {
  font-family: "Source Sans 3";
  src: url("/fonts/SourceSans3-Regular.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
}
/* repeat for Italic, Semibold (600), Bold (700) */

body {
  font-family: "Source Sans 3", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
```
The fallbacks are real fonts on your readers' devices. Roboto is the default on Android, and Segoe UI and Arial are on Windows library machines. If the web font fails to load, the page stays readable and looks reasonable. `font-display: swap` means text never goes invisible. Self-host four woff2 files, subset to Latin (add Latin-Extended if you need Spanish accents). Don't load from a third-party CDN, since library networks sometimes block them and it adds a privacy question for tenants.

**Print:** Install the same four fonts on the staff machines that make the handouts and embed them when you export to PDF. That keeps print and web matching and avoids a substituted font on a copier-room computer.

**Starting sizes:**
- **Web body:** 17–18px.
- **Print body:** 11–12pt.
- **Small print or footnotes:** Never below 10pt or 14px. Many of your readers are stressed, reading on small screens, or working in a second language.

**Before you commit:** Put one real paragraph from your eviction guide in it and view it on the oldest Android phone you can borrow, and on a library computer. Check that numbers, dates and dollar amounts are easy to tell apart (1/l/I, 0/O).

**Alternative:** If the guides feel too cold and you want a book-like serif for long reading, **Literata** (free, OFL) is a good body face. Keep Source Sans 3 for headings and callouts. That's the most I'd add, and it makes two families to maintain, so I'd start with one.
