# Mark production

## Presentation page (HTML or deck)

Show on one page, each on its real ground: primary lockup; solid one-color version on white; reversed version on a dark ground; the symbol alone; the icon at a large size and at the smallest sizes it will meet (the small ones drawn, not scaled down, if detail is lost); one or two real surfaces. Keep the page quiet: the marks are the content. Label versions in a few words; no decorative gradients behind the marks, and no invented proof (customers, ratings, quotes, taglines the user did not give): a visible placeholder or an empty slot.

## Icons and favicons

- Master icon on a square with the mark centered by optical weight, not by bounding box; leave margin so platform masks (rounded squares, circles) do not clip it.
- Small sizes: one bold shape, thick strokes, no hairline, no text smaller than the stroke can hold. A single letter or a simple symbol is stronger than a full lockup. Redraw for 16 and 32 pixels; do not shrink the large file.
- Check the icon on light, dark and a busy photo ground.

## SVG

- Simple geometry with few nodes; merge overlapping paths; round coordinates sensibly.
- A correct `viewBox`, no fixed width and height baked in, so it scales; a transparent background.
- Text converted to outlines for the logo, or the font named in a comment when live text is required; never rely on an unembedded font.
- Flat fills from a short list of named colors; no filters, blurs or gradients in the core mark.
- A one-color version using `currentColor` so it follows the text color; a reversed version for dark grounds.
- An accessible name: `role="img"` with a `<title>` (or alt text where the SVG is an image), and `aria-hidden` when decorative next to visible text.
- File set: full color, one color, reversed, symbol only, icon sizes, in SVG with PNG exports where needed.

## Cleaning a supplied SVG

Report what you changed in one line each (nodes cut, viewBox added, text outlined, gradient flattened, currentColor version added). Do not redraw the design; if its idea is the problem, say so separately.
