Your palette is already restrained and suits letterpress. Ink on paper is about 11:1, and one warm accent is the right call. The main issues are contrast on a few text colors, and the palette matters less to "premium" than type and spacing.

**Contrast fixes (WCAG AA, 4.5:1 for body text)**

I calculated these from the hex values:

- **Rust on paper: about 4.15:1.** That fails for small link text. Darken it slightly to `#a94127` (about 4.6:1) to keep the same hue. Rust buttons with white text are fine as they are (about 5.4:1).
- **Muted on paper: about 4.2:1.** Captions are the most likely text to fail. Darken it to `#555f62` (about 5:1). It will still read as secondary.
- **Sage on paper: about 2.6:1.** Keep it for rules, dividers, and decorative tags only. If a tag contains text, set the text in ink or muted and use sage for the border or background.

**Other suggestions**

- **Warm up the ink, optionally.** Ink is a cool blue-green gray on a warm cream paper. That mismatch can make the page look a little clinical. Try a warm charcoal like `#2a2623` and compare the two side by side. If you like the current ink, keep it.
- **Add one paper tone.** A slightly lighter cream, such as `#fbf8f2`, for product cards or the price list panel adds depth without introducing a new hue.
- **Typography and space will do more than color.** A refined serif for headings, a clean sans for body, generous margins, and fewer boxes will carry most of the premium feel.
- **Proof the printed price list.** Screen colors won't match ink on stock. Ask your printer for a proof, and consider matching rust and sage to Pantone or checking them in CMYK, since bright reds and muted sages often shift in print.

If you want, I can write the revised palette as CSS variables with the contrast ratios checked.
