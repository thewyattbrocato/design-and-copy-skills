Partly a cop-out. The printer is right that the screen color can't be reproduced exactly, but "brownish" suggests something fixable.

**What's true**
- Your website orange is RGB light, emitted by a backlit screen. Print is ink reflecting light off paper, so it can't be as luminous. Some dulling is unavoidable.
- #ff6a1a is also outside what standard CMYK inks can hit exactly. The nearest CMYK match is a little less vivid.

**Why it's a cop-out**
- A well-converted CMYK orange should look like a slightly softer orange. It shouldn't look brown. Brown usually means one of these:
  - The file was converted with the wrong color profile, or by a naive conversion.
  - Black (K) ink got mixed into the orange, which darkens it.
  - The paper is uncoated. Uncoated stock soaks up ink and dulls colors a lot, and if your menu is on it, that's likely a big part of this.
  - Your design file was still RGB and the printer's software converted it without a soft proof.

**What to do**
1. **Ask the printer what happened.** Ask which paper stock they used, what the CMYK breakdown of the orange is, and what color profile they converted with. A good printer can answer this quickly.
2. **Try a CMYK mix with no black.** Something around C0 M70 Y100 K0 is a typical starting point for a vivid orange. Treat those numbers as a starting point, not a spec.
3. **Consider a spot color.** Ask them to print the orange as a Pantone ink instead of building it from CMYK. It costs more, since it's an extra ink or plate, but it's the most reliable way to get a bright, consistent orange. Pick the swatch from a physical Pantone book, not on your screen.
4. **Consider coated or silk stock.** It keeps colors much brighter than uncoated. If you want the uncoated look, accept a softer orange or use the spot color.
5. **Get a physical proof before the full run.** Ask for a press proof or a printed swatch of the orange on the actual paper. Don't approve it from a PDF or a screen.
6. **Set expectations for the brand.** You could define a separate print orange, tuned by eye on paper, as a companion to the web orange. Most brands do this.

If you send me the printer's specs (stock, file format, and any CMYK values they gave you), I can help figure out which of these is the likely cause.
