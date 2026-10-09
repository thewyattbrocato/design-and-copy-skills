The palette is already good, so I wouldn't change the five colors. It's restrained, warm and coherent, and the single rust accent suits letterpress. Most of what reads as premium will come from how you use the colors.

**Contrast (my calculations from the hex values)**
- Ink on Paper is about 12:1, which is excellent.
- Rust on Paper is about 4.8:1, so it passes for links and buttons. For button text, use Paper or white on Rust. White gives about 5.4:1.
- Muted on Paper is about 4.9:1. It passes, but it's close to the limit, so don't use it below about 14px or on any darker surface.
- Sage on Paper is about 3:1. That's fine for decorative rules. It fails for text, so any tag with Sage text needs a darker shade (around `#4f6657`) or a Sage-tinted background with Ink text.

**What I'd add**
1. **A second paper tone for surfaces.** Something like `#ede6d6` for cards, the price list's alternating rows and footers. A page with only one flat background looks less finished than one with a subtle step.
2. **A hairline color.** Use Ink at about 15% opacity (or `#d9d1bf`) for dividers and borders. Thin warm lines look more refined than Sage or Muted rules at full strength.
3. **A deeper Rust for hover and pressed states**, around `#9a3a21`. Don't introduce a second accent. Keeping to one is what makes it feel deliberate.
4. **Avoid pure black and pure white.** Your Ink and Paper already do this well, so keep it consistent in shadows, photo borders and PDFs.

**Where the premium feel comes from**
- Use Rust sparingly: links, the primary button and maybe one detail per page. If it shows up everywhere, it stops feeling special.
- Use generous whitespace, a serif for headings with a clean sans for body text, and tight, consistent spacing.
- Use real photography of the printed pieces, with the debossed texture visible, on your Paper tone.

**For the printed price list**
- Screen hex values won't match on press. Choose Pantone or CMYK equivalents and proof them on your actual stock. Your Paper color is really the stock itself, so you may want to print only Ink and Rust on it.
- Sage at 3:1 is too faint for small print text, so use it for rules only.

I can turn this into CSS variables (including the tints and states) or check the pairings against your real page if you'd like.
