**Verdict:** The printer is partly right, but "just how print works" is too glib. The shift is real, and it's fixable.

#ff6a1a is a very saturated screen orange. Four-color process printing (CMYK) can't reproduce colors that bright, so the printer's software maps it to the nearest color the inks can make, which usually looks duller and browner. That's the gamut limit they're describing. But the amount of shift depends on how the file was set up and what paper you chose, so some of it is controllable.

**What to do, roughly in order of impact:**

1. **Use a spot color for the orange.** Ask whether they can print a Pantone spot ink. Pantone 021 C is a common bright orange that's much closer to #ff6a1a than CMYK can get, though it's worth checking swatches in a Pantone book to confirm. Spot inks may add a setup cost or an extra ink pass, so ask for a quote.

2. **Check the paper.** Uncoated stock soaks up ink and dulls color noticeably. A coated or silk stock keeps the orange more vivid. Ask the printer to show the same orange on the paper you're considering, not just on a proof.

3. **Ask for a soft proof or a drawdown before you approve.** Request a physical press proof or a drawdown on the actual stock. Your monitor can't show you the print result accurately.

4. **Make sure the file is color-managed.** Ask the printer which CMYK profile they use (commonly GRACoL or US Web Coated SWOP, depending on their press and paper). Don't let anything auto-convert RGB to CMYK with a default setting. If you're converting yourself, use Illustrator or Photoshop's soft proof with their profile to preview the shift.

5. **Pick a print-safe orange.** If spot ink is off the table, choose a CMYK orange that's in gamut and use it for the menu. Keep #ff6a1a for the web. Having a separate print value is normal, and it's better than accepting an unpredictable brown.

**Questions to ask the printer:** Which CMYK profile do you use? Can you print a spot Pantone for the orange, and what does it cost? Can I see a drawdown on the paper I'm choosing?
