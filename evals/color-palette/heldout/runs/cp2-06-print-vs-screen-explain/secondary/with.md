It's partly true, but "just how print works" skips over real fixes.

**Why it happened:** Your website color is RGB, which is made of light. Print uses CMYK inks on paper, which can't reproduce every screen color. Vivid, highly saturated oranges like #ff6a1a sit near the edge of what CMYK can produce, so the printer has to map them to the nearest reachable color, and that often comes out duller and browner. Uncoated paper makes it worse because the paper absorbs ink and softens the color. So the printer is right about the physics. But they should have flagged this before the proof, and it's fixable.

**What to do:**

1. **Ask for a spot color (Pantone/PMS).** This is the most reliable way to match a brand color in print. The printer mixes a dedicated ink for the orange instead of building it from CMYK. It usually adds a small cost, since it can add a plate or ink run. Ask them to find the closest PMS match to #ff6a1a and show you a printed swatch next to your screen color. I can't confirm the exact match number from here, so let them or a Pantone library pick it.

2. **If you stay with CMYK, ask for a brighter, in-gamut orange.** Have the printer or designer soft-proof the orange using the printer's ICC profile (often a U.S. Web Coated SWOP or their own profile) and nudge the color until it looks right. A slightly different hex will often print better than the exact one.

3. **Check the paper.** A coated stock (gloss or silk) makes oranges noticeably more vivid than uncoated or kraft stock. If the menu is on a rustic uncoated paper, expect a softer orange and plan the color around that.

4. **Ask for a press proof or a contract proof.** A printed proof from the press, or a calibrated contract proof, is more reliable than a desktop printer. Check it under daylight-balanced light, since color looks different under warm restaurant lighting too.

5. **Set a brand standard.** Once you've picked the approach, record the spot color or the CMYK values in your brand guide so future menus, signs, and boxes match.

If you tell me the paper stock and whether the menu is 4-color or can take a spot ink, I can suggest a specific approach and a CMYK starting point to ask the printer to test.
