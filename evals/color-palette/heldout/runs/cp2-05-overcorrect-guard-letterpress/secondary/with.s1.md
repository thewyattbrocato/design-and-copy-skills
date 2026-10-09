**Short answer:** the palette is already close to what your friend means. Warm paper, deep ink, one rust accent, and grays in the same family as the ink all read as restrained and deliberate. The changes below are about making the roles hold up on the page and in print, not about the hues.

**Changes, by impact**

1. **Sage text fails contrast.** Sage on Paper is about 3.0:1, below the 4.5:1 needed for small text. If tags are Sage-filled or Sage-lettered, change the tag text to Ink (about 13:1) or Muted (about 4.9:1). Keep Sage for rules, borders, and ornaments, which don't need text contrast. If a tag must be Sage, use a Sage hairline outline around Ink text.
2. **Print values are not these hex codes.** Screen hex doesn't translate directly to ink. Ask your printer for a proof, or for a close match to Rust and Ink on your actual stock. If you letterpress, the ink-on-cream result will differ from the screen anyway. Don't print Paper as a flood fill; let the stock itself be the paper.
3. **Sage rules may disappear in print.** Light tints break up on press, especially at hairline weights. Set Sage rules heavier than a hairline and check a printed proof before you commit.
4. **Rust links and buttons are at the floor.** Rust on Paper is about 4.8:1, and the paper-colored label on a Rust button is the same. Both pass for body-size text, but with no margin. Keep the Rust text as is, underline links so they don't rely on hue alone, and if you add a hover state, darken Rust and measure it. Don't lighten it.
5. **Muted is passing but close.** Muted on Paper is about 4.9:1. Don't lighten it for a softer look. If you put Muted text on a darker card or tint, re-measure, since the ratio drops.

**Pair check** (hand-calculated from sRGB luminance, so treat these as estimates until you run a checker)

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | ~13.0:1 | Pass, body text |
| Muted on Paper | ~4.9:1 | Pass, body text |
| Rust on Paper | ~4.8:1 | Pass, body text, little margin |
| Paper on Rust (button label) | ~4.8:1 | Pass, body text |
| Sage on Paper | ~3.0:1 | Fails for text; decorative use only |

**Premium-feel notes**

- Don't add colors. The palette already has one accent and a clear hierarchy, and more hues would undo that.
- Most of the premium read will come from the paper stock, the type, and the amount of white space, not from the hues.

I haven't changed any files. If you share the stylesheet or the price list layout, I can apply the Sage-tag fix and check the actual surfaces the text sits on.
