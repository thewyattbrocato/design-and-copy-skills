I can't see the logo, so this is based on your description. The main issues are contrast and the 32px favicon, and both are likely to be real problems.

**1. Contrast is too low for the text.** I calculated #c9a227 on white at about **2.4:1**. WCAG asks for 4.5:1 for text and 3:1 for graphics. A thin script in a light gold will be hard to read on a sign from across a room, and it will look faded on a cup. Gold reads as premium, but at this value and weight it reads as washed out. Options:
- Darken the gold for the wordmark (around #8a6d1a or #7a5f14 should reach 4.5:1 or close to it), and keep the brighter gold for accents only.
- Or set the wordmark in a deep tea color (dark green-brown or near-black) and use gold for the leaf or a rule.
- If the sign and cups must be gold, make the wordmark heavier. Don't rely on the color to carry it.

**2. Hairlines won't survive small sizes or print.**
- At 32px, hairline strokes disappear or turn into grey noise. The wordmark will not be readable as a favicon at any color.
- On paper cups, very fine strokes often fill in or break up from ink spread, and a gold approximation in CMYK shifts the color further. A common minimum for print is about 0.5 mm for line art, and thicker for knockout or foil.
- Test by printing a proof at real size on the actual cup stock before you commit.

**3. The leaf above the "i" will probably vanish.** At sign and cup scale it may read as a stray speck, and at favicon size it's gone. Consider making the leaf replace the i-dot, which keeps it integrated and gives it more mass.

**4. The favicon needs its own mark, not a shrunk wordmark.** Use a monogram (a "P" or a leaf-i), a simple bold shape, and possibly a solid tile in the brand color behind it. Design it as a separate asset, and test it at 16px and 32px.

**A quick check before you go further:**
- Squint or blur it. Can you still read "Pemberly"?
- Render it in grayscale. Does the contrast hold up?
- Shrink it to 32px. Is the leaf still visible? Are the hairlines still there?

If you can paste the SVG source here as text, I can measure the actual stroke widths and point out exactly which parts will fail, instead of working from your description. Otherwise, tell me the rough stroke width in px at your largest intended size and I can give you specific minimums.
