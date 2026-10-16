**Use one family: Atkinson Hyperlegible Next, for headings, body and labels.** Use bold for hierarchy and its true italic for emphasis.

Atkinson Hyperlegible was designed for low vision, so letters like I/l/1 and O/0 are easy to tell apart. That matters for case numbers, dates and dollar amounts. I believe it's free under the SIL Open Font License, with several weights and real italics. Confirm the license on the Braille Institute or Google Fonts page before you embed it. It's sturdy at small sizes on weak screens and low-quality printers, and a second family would add nothing for guides like these.

**If you'd rather have a serif for long reading,** pair it with a serif body: Source Serif 4 (also open) for body text, with Atkinson for headings, callouts and tables. Keep it to those two.

**Web CSS:**

```css
:root {
  --font: "Atkinson Hyperlegible Next", system-ui, "Segoe UI", Roboto, Verdana, sans-serif;
}
body { font-family: var(--font); font-size: 1.125rem; line-height: 1.6; }
```

- **Fallbacks:** Roboto is on Android and Segoe UI is on Windows. Verdana is the closest widely installed look-alike if neither is there.
- **Hosting:** Self-host WOFF2 files, with only the regular, italic, bold and bold italic. Don't load them from a CDN, because library networks sometimes block those.
- **Loading:** Use `font-display: swap`, so text shows right away in the fallback and never goes invisible.
- **Old phones:** Test on one real older Android phone and on a library computer. Make sure the page still reads well in the fallback face.

**Print:**
- Embed the same font in your PDFs, so handouts match the web version.
- Use at least 11 pt for body text. Go to 12 pt if your readers skew older.
- Don't use faux bold or italic. If a weight is missing, load the real file.

**Don't use:**
- Thin or light weights for body text.
- Decorative or script faces.
- Monospace for headings.
- A third family.

I assumed English text, or Spanish and other Latin-script languages. If you publish in Arabic, Chinese, Vietnamese or another script, tell me. Those need a different plan, because this font won't cover them.
