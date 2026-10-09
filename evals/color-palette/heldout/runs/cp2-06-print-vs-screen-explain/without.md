It's partly a cop-out. Print can't match a screen exactly, but "brownish" suggests something fixable.

**What's true**
- Screens emit light and print only reflects it, so a screen orange will always look a bit more luminous than ink on paper.
- Print uses CMYK, which has a smaller gamut than the RGB on screens. Saturated oranges, greens and blues are where the gap shows most.

**Why it's still not a good excuse**
- #ff6a1a is a fairly vivid orange, but a decent CMYK version exists. It's roughly 0C / 65–70M / 95–100Y / 0K. On coated stock it should look clearly orange, not brown.
- Brown usually means black or cyan crept into the mix. That tends to happen when:
  - an RGB file gets auto-converted with the wrong profile
  - the paper is uncoated, which soaks up ink and mutes color
  - the color was built with extra K or C

**What to do**
1. **Ask the printer three things:** what paper stock the proof was on, what color profile they used, and what CMYK values your orange came out as. If it has any cyan or black in it, that's your brown.
2. **Supply the color explicitly.** Give them a CMYK build with 0 cyan and 0 black, like the one above, instead of letting them convert the RGB file. Have your designer set it up in CMYK from the start.
3. **Consider a Pantone (spot) ink** for the brand orange. It's a pre-mixed ink, so it's the most consistent option, and it costs more. Match it against a physical swatch book, not on screen.
4. **Check the stock.** If the menu is on uncoated paper, expect duller color. Coated or a silk finish will be much punchier.
5. **Ask for a physical proof** of the revised file before the full run. A PDF or screen proof won't show you how the color really prints.
6. **Set expectations.** Even when it's done right, the print will be a little less glowing than the website. You're aiming for the same orange that reads as warm and bright, not a pixel-exact match.

If you send me the printer's specs (stock, profile, the CMYK values they used), I can help work out where the brown is coming from.
