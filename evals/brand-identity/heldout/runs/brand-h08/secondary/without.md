**Partly true.** Thread has physical limits, but those limits are a reason to make a different version of the logo for embroidery, not a reason the result had to look like this. A good designer would have flagged the problem before sign-off.

## Why this happens

**Embroidery:** The logo is converted into stitches, and a thread is roughly 0.3 to 0.5 mm wide. Several things blur fine detail:
- Lines thinner than about 1 mm can't hold their shape, so adjacent stitches merge.
- Small text is the worst case. Letters need enough height and stroke weight to read. Rough guidance for a polo is a tagline no smaller than about 6 mm tall, with strokes at least 1 mm thick. Confirm exact minimums with your embroiderer.
- Fabric stretches and puckers under the needle, which closes up small gaps between shapes or colors.

**The 32px favicon:** At that size, any detail thinner than a pixel gets averaged with its background. Thin strokes or low-contrast colors turn into gray. Browser tabs also show the icon on different backgrounds (light and dark mode), which makes this worse.

Both problems come from the same cause: the logo was designed for a large, high-resolution screen and reused everywhere else.

## What to do

1. **Make a simplified mark for small sizes.** Use a bold silhouette, or a monogram or initials, with 2 to 3 high-contrast colors and no fine lines or text. Export favicon.ico (16, 32, 48 px), a 180 px apple-touch-icon, and an SVG favicon if you want. Check each one at actual size in Chrome and Safari, in light and dark mode.

2. **Make an embroidery version of the full logo.**
   - Drop the tagline, or make it large enough to read.
   - Thicken all lines to at least about 1 mm.
   - Limit to 3 to 5 thread colors, with no gradients, halftones, or photo-style shading.
   - Leave clear space between shapes so they don't merge.

3. **Ask the embroiderer for a sew-out or digitizing proof before the next run.** A test stitch on a scrap of the actual polo fabric shows problems before you order a full batch. Ask them what minimum sizes they recommend.

4. **Send the designer a clear brief.** Something like: "Deliver a favicon set, plus an embroidery-ready logo with no tagline under X mm, minimum line weight of Y mm, and at most Z colors." For a single small accounting firm, this is usually a short, inexpensive job, not a big project.

If you want, I can draft that brief for your designer, or write out the favicon size checklist.
