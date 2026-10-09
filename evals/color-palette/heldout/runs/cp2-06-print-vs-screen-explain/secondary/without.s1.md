It's partly true, but "just how print works" is a cop-out. Your printer is right that the problem exists, but there are concrete ways to fix it.

**Why it happens:** Your screen mixes light (RGB), and print mixes inks (CMYK). CMYK can't reach some bright, saturated colors, and #ff6a1a is one of them. When a color is out of range, the conversion pulls it toward the nearest reproducible color, which is often a duller orange-brown. Uncoated paper makes this worse because it soaks up ink and mutes colors. Your screen can't show you this gap, so the website orange looked fine.

**What to do:**

1. **Use a spot color for the orange.** Ask the printer for a Pantone spot ink in the orange family, such as PMS 021 C or 1655 C. Spot inks are mixed ready-made and print far more vivid than a CMYK build. Ask them to show you the swatch on the same paper stock before you commit. This is usually the biggest improvement, and the cost is one extra ink, which many printers charge a modest surcharge for. If the menu is already one or two colors, this may cost little.

2. **If you stay in CMYK, choose the build deliberately.** Ask the printer for their ICC profile (commonly U.S. Web Coated SWOP or GRACoL, depending on the press). In Illustrator, InDesign, or Photoshop, turn on Proof Colors and the gamut warning, then convert your orange to CMYK with that profile. The warning shows where the color is out of range. Pick the brightest CMYK value that looks right, often something in the range of C0 M65–75 Y95–100 K0, and test a few on a press proof rather than trusting one number.

3. **Ask for coated stock.** A gloss or silk coated paper holds brighter color than uncoated. If the menu is on uncoated stock for texture, that may be the source of the dullness, so ask whether a coated stock with a matte finish would work.

4. **Get a proper proof.** An inkjet at the office is not a color proof. Ask for a press proof or a color-matched proof (Epson or similar, calibrated to the press profile), and check it under daylight-balanced light, since warm indoor light also shifts orange.

5. **Check the file.** Make sure the orange and any images are CMYK in the file you sent, not RGB that the printer converted automatically with a default profile.

If you tell me which design app you use and whether the menu is one color or full-color, I can help you pick specific values or write the email to the printer.
