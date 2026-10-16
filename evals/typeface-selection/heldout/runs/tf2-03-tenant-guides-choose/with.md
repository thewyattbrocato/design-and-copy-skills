**Use one family, Source Sans 3, for everything: body, headings and labels.** It's free (open SIL license, but confirm on the download page) and installs on your design computer for print. It has a true italic and a full weight range, so regular, semibold and bold give you the hierarchy without a second typeface. The letters are open and sturdy, so it stays readable on small, low-resolution screens and on photocopied handouts. Its figures also line up, which helps with rent amounts, dates and deadlines.

I'm assuming English plus possibly Spanish. Source Sans covers Latin-extended, Vietnamese, Greek and Cyrillic, but check it against any other languages you translate into.

**Web CSS**

```css
body {
  font-family: "Source Sans 3", "Segoe UI", Roboto, Arial, sans-serif;
  font-size: 1.125rem;   /* 18px; don't go below 16px */
  line-height: 1.55;
}
h1, h2, h3 { font-weight: 700; }
.amount, td { font-variant-numeric: tabular-nums; }
```

- **Self-host the font.** Put WOFF2 files on your own site and don't rely on Google Fonts. Library computers are often locked down or filtered, and self-hosting also avoids sending readers' data to a third party.
- **Keep it to about four files:** regular, italic, semibold and bold. Use `font-display: swap` so text never goes invisible.
- **Check the fallback.** If the font doesn't load, readers get Segoe UI on library Windows PCs and Roboto on Android. Both are fine, so the guide stays readable and nothing falls back to Times.

**Print**
- Use the same family at 11–12 pt for body text. Use bold or semibold for headings, not all caps, and keep italics short.
- Install the same font files in whatever you lay out in, and embed the fonts when you export the PDF.

**Things to avoid**
- Don't use thin or light weights for body text. They wash out on old screens and photocopies.
- Don't use script or decorative faces, or a second sans that's nearly the same.
- Don't fake bold or italic. Use the real styles in the family.

**Alternative:** If many of your readers have low vision, Atkinson Hyperlegible is a free option. The Braille Institute designed it so that look-alike characters like I, l, 1, O and 0 are easy to tell apart. It's slightly less refined at 15–30 page lengths, but it's a defensible choice for your audience.

To test either one before committing, print a page of a real guide on your office printer and photocopy it. Also load it on the oldest Android phone you can borrow.
