I haven't seen the file, so this is feedback on the concept as you've described it. The main problem is that the design is built for the sign, and the cups and favicon will work against it.

**What's working**
- A script wordmark suits a small tea shop. It feels personal and a bit old-fashioned, in a good way.
- The leaf above the "i" is a nice idea. It replaces the dot with something that says "tea" without a cliché teacup icon.
- Gold on white reads as refined, and the name "Pemberly" fits that tone.

**Concerns, roughly in order of severity**

1. **Gold #c9a227 on white has low contrast.** It comes out around 2.4:1, well under the 3:1 minimum for graphics and 4.5:1 for text. Thin strokes make it worse, because the line is so fine that anti-aliasing blends it into the white. At a distance on a sign, or on a cup in someone's hand, it will look pale and washed out.

2. **Hairline strokes won't survive the real uses.**
   - **Cups:** flexographic printing and ink spread on curved paper will fill in or break up hairlines.
   - **Sign:** hairlines vanish at viewing distance, especially in daylight.
   - **Favicon:** at 32px (and 16px in a tab), hairline script becomes a blur.

3. **The tiny leaf will disappear.** At small sizes it will read as a smudge or just a dot, and that dot may make the "i" look like a plain "i" again. At 32px it's gone.

4. **A full script wordmark can't work as a favicon.** "Pemberly Tea" won't be legible in 32px. This is normal, and the fix is to design a separate small mark rather than shrink the logo.

5. **Script legibility.** Check that "Pemberly" doesn't read oddly, since the "mb" and "rl" pairs are easy to muddle in thin script. Also check that the "P" and "T" capitals are clear.

**What I'd do**
- **Add weight.** Keep the elegant feel, but make the thinnest strokes noticeably heavier. A good test is to print it at about 1 inch wide and see if every stroke still holds.
- **Deepen the gold for small and print uses.** Something like #a67c00 or #9a7b1c keeps the warmth with much better contrast. Keep the lighter gold only for large, high-quality applications like the sign, ideally on a dark background, where gold looks best.
- **Consider a dark backing.** Gold on deep green, navy, or charcoal is far more legible than on white, and it feels more premium. A cup in dark green with the gold wordmark would look great.
- **Make a simplified favicon and small-size mark.** Use a "P" monogram, or the leaf alone, in a solid shape with no hairlines. A filled leaf in a rounded square would hold up at 32px.
- **Make the leaf bolder, and test it.** Make it a solid shape, not an outline, and scale it up slightly so it stays visible when small.
- **Prepare a one-color version.** Cups and signs often need a single flat color, plus a version in black or white for stamps, receipts, and bags. Gold gradients or metallic effects won't print reliably.

**Quick tests before you finalize**
1. Shrink it to 32px and 16px and see what's left.
2. Print it in grayscale at about 1 inch wide.
3. View it from across a room, or squint at it.
4. Mock it on a real cup and on the sign background.

If you can describe the letterforms, or export a PNG and tell me what you see at small sizes, I can give more specific advice. The concept is good. The execution just needs to be sturdier to survive real-world use.
