I can't see the logo, so this is based only on your description. From that, the main risk is that the mark is too light and too fine to survive the smaller uses.

**The big issues**

1. **The gold is too light on white.** `#c9a227` on white is about 2.4:1 contrast. Hairlines in that color will look washed out on a sign or a cup, especially in daylight. Thin strokes make it worse, because antialiasing lightens them further.

2. **The hairlines won't survive 32px.** At favicon size, hairline strokes either disappear or blur into a gold smudge. The leaf above the "i" will probably be a few pixels of noise. Your favicon needs its own design; a scaled-down version of the wordmark won't work.

3. **Print will be hard.** Hairlines on paper cups depend on the printer's minimum line weight and registration. Gold is also hard to match in CMYK, and on kraft or colored cups it can vanish. If you can use a foil or spot color, it will look better, but the hairlines still need to be thicker than what you describe.

**What I'd do**

- **Darken the gold for the primary mark.** Something around `#8C6D1A` gives roughly 4.9:1 on white and still reads as gold. Keep the brighter `#c9a227` for accents or on dark backgrounds, where it has better contrast.
- **Thicken the strokes.** Aim for a stroke weight that still reads at roughly 1/8" on a cup. If you want to keep the delicate feel, use a slightly heavier cut for production and keep the hairline version for large applications like the sign.
- **Make a simplified favicon mark.** Drop the leaf and the thinnest strokes. A monogram ("P" or a "PT" ligature) in a heavier weight, or a leaf alone, will be more legible at 16–32px.
- **Test at real sizes.** View the logo at 16, 32, and 64px, on a cup mockup, and on the actual sign material if you can. Check it on a dark background too, since many shop signs and cup sleeves use dark colors.
- **Supply a vector.** An SVG for the sign shop and printer will avoid rasterization problems.

**What would help me give more specific feedback**

- The script style (formal copperplate, brush, monoline?) and how the letters connect.
- Whether the leaf sits on the i's dot or floats above it.
- The exact width of the hairlines in points or pixels.

If you can paste the SVG source or describe the letters' spacing and proportions, I can be more specific about where the weight should change.
