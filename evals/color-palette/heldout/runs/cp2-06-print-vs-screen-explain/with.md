The printer is partly right, but "just how print works" doesn't excuse a dull, brownish result. That part is fixable.

**What's true**
- **Your screen is too bright for ink.** #ff6a1a is an RGB color made of light. A monitor can show a very saturated, glowing orange. Standard CMYK ink on paper can't reach it, because ink only absorbs light and can't add any.
- **The conversion is automatic and lossy.** If the file went to the printer as RGB, or the printer converted it, the orange gets pulled into the nearest CMYK color. That is usually a flatter, slightly muddy orange. Uncoated paper makes it worse because it soaks up ink and dulls the color further.

**What's not an excuse**
- **Orange is one of the easier colors to approximate in CMYK.** A good orange is roughly 0% cyan, 65–70% magenta, 90–100% yellow, 0% black. Brown means something else went wrong, such as extra cyan or black in the mix, a bad automatic conversion, or an uncoated stock that wasn't accounted for.
- **A professional printer should have told you** that the color would shift, and shown you a way to control it, before you got a proof.

**What I'd do**
1. **Ask the printer which of two things went wrong.** Was the file RGB and converted automatically? And what exact CMYK values and paper stock were used on the proof?
2. **Convert the orange yourself and set it explicitly in the file.** Start near C0 M68 Y100 K0 as a *starting point*. I haven't seen your proof, so don't treat those numbers as the answer. Make sure there is no cyan or black in the orange.
3. **Ask for a new proof,** not a screenshot or PDF on your screen, and compare it with your own eyes.
4. **Try a coated or silk stock** if the menu is on uncoated paper. It makes oranges look noticeably brighter.
5. **For the exact match, use a spot ink.** Choose the nearest Pantone orange from a physical swatch book (the Pantone Formula Guide). A spot ink is mixed to a specific color rather than built from CMYK dots, so it can look brighter than a CMYK mix. It costs extra, but for one brand color on a bakery menu it's often worth it.
6. **Judge the color on a physical sample,** in the light where the menu will be read. Don't judge it against your phone or laptop.

**A caveat for expectations:** even a good fix won't look as glowing as the website. Print orange will be a little less neon than the screen version. The goal is a warm, appetizing orange that is clearly your brand's, not an identical match.

If you can tell me the paper stock and what file format you sent, I can narrow down which of these is the real cause.
