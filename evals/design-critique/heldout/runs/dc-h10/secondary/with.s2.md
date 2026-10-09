Based on your description, the main problem is the gold on white. The hairlines and the tiny leaf will struggle on all three uses.

**1. The gold has too little contrast on white (the biggest issue)**
`#c9a227` on white is about **2.4:1**. WCAG asks for 4.5:1 for text and 3:1 for graphics, so this fails both. Thin strokes make it worse, because they carry less ink and look even paler. On a sign it will wash out in daylight, and on a cup it will look faded.

- Darken the gold for light backgrounds. `#8a6d1a` is about **4.9:1** on white and still reads as gold.
- Keep `#c9a227` for dark backgrounds. Gold on deep green, espresso brown, or charcoal is where that brightness works, and it looks rich there.

**2. The hairlines won't survive the cup or the favicon**
- **Paper cups:** Hairlines can fill in with ink spread or break up in print. Aim for a minimum stroke of roughly 0.5–0.75 pt for print, and test at actual size. If the cups are gold foil or metallic ink, very fine lines are the first thing to fail.
- **32px favicon:** A script wordmark cannot be read at that size, and the leaf will disappear. Make a separate icon instead: a monogram ("P" or "PT"), or the leaf alone, with strokes thick enough to hold at 16–32px. Test it at 16px too, since browser tabs are often that small.

**3. The leaf above the "i" is the weakest detail**
A tiny leaf is the first thing to disappear at small sizes or in print. Make it larger (roughly the cap height of the x-height area), or drop it from the small-format versions entirely. Keeping the leaf in the favicon monogram is an option.

**4. The shop sign**
The sign works if it is big and gold-on-dark, or if it's a darker gold and the strokes are not hairline. At a distance, a sign with hairline script on white will read as blank. Check the sign at the distance people will see it, from across the street, not at arm's length.

**What I'd do, in order:**
1. Pick a deep gold for light backgrounds and keep the bright gold for dark ones.
2. Thicken the strokes for print and the sign, so the minimum stroke is about 0.5 pt.
3. Make a simplified monogram for the favicon and small uses.

I'm working from your description, so I can't see the letterforms, spacing, or how the leaf sits. If you can paste the SVG source, or tell me the typeface name and stroke width, I can give more specific notes. If you can get a PNG at small and large sizes later, I can also check how it holds up.
