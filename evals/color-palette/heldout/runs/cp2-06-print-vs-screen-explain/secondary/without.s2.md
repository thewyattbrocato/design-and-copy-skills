It's partly true, but "just how print works" is a dodge. Your printer is right that the color can't be reproduced exactly, but a good printer should have a way to get much closer.

**Why it happened:** #ff6a1a is an RGB color made for screens, which can emit light at full intensity. Print uses inks on paper, which can only absorb and reflect light. Standard four-color printing (CMYK) can't reach many bright, saturated oranges, so the printer's software maps your orange to the nearest color the inks can make. That nearest match is duller and browner. Uncoated paper, which soaks up ink, makes this worse.

**What to do:**

1. **Ask for a Pantone spot color.** A spot ink is a premixed color, so it can hit oranges that CMYK can't. Ask the printer to match #ff6a1a to the nearest Pantone orange, and to show you the swatch in a physical Pantone book or a printed chip before you approve. This is the most reliable fix, and it usually costs a bit more, since it adds an ink.

2. **If you stay with CMYK, soft-proof first.** Ask the printer for their ICC profile (for example, a GRACoL or SWOP profile for their press). In Illustrator or Photoshop, set that profile, turn on the out-of-gamut warning, and adjust the orange until it looks as vivid as you want while staying printable. Then send the CMYK values to the printer, not the hex code.

3. **Change the paper if you can.** A coated or semi-gloss stock keeps color saturation much better than uncoated or kraft-style paper. If the menu needs a rustic feel, consider using the orange only for a small accent (a logo bar or heading) and leaving the rest of the menu on the paper's natural finish.

4. **Don't judge color on your monitor.** Your screen won't match print, so always check a physical proof under daylight-balanced light, side by side with your website.

**What to tell the printer:** "I need the orange to match my brand. Please give me the nearest Pantone match to #ff6a1a, or a CMYK build with an ICC soft-proof, and show me a physical swatch on the paper I'm using." A printer who can't offer either option is the one who's giving you the cop-out.
