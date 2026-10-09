# Images and media

Load this when a layout includes photographs, screenshots, diagrams, galleries, or text over a picture. First decide what the image is for. The treatment follows.

## Two kinds of image

- **Whole-image content:** a diagram, screenshot, chart, artwork, scan, receipt, product on a plain background. Every edge carries information. Do not crop it into a card ratio. Give it the span it needs to be read, and let its height follow its width.
- **A window onto something:** most photography, mood images, backgrounds. The frame can crop. Choose one aspect ratio for a set so rows line up, and set the focal point so the subject survives the crop.

If you cannot tell which, ask what would be lost if the outer fifth were cut off.

## Spans

- Match image width to column edges: one column, two, the full text width, or the full container. A width that lines up with nothing looks accidental.
- A figure may be wider than the text around it, but if it is wider, make it clearly wider, not a few pixels.
- A small figure inside a reading column sits flush to the text edge, not centered with ragged gaps on both sides.
- On narrow screens, images normally go to full column width. A diagram that cannot be read at that size needs a tap-to-enlarge or a horizontal scroll, not shrinking.

## Aspect frames and focal points

- Pick the frame by the set: 4:3 or 3:2 for general photography, 1:1 for avatars and tiles, 16:9 for wide scenes, 4:5 or 3:4 for portraits.
- With CSS frames, `aspect-ratio` plus `object-fit: cover` and an `object-position` aimed at the subject.
- When images arrive from users, assume faces and products are not centered; offer a focal-point control or choose `contain` for non-photo content.
- Do not mix ratios in a grid unless the mix is the point.

## Captions

- A caption sits with its image: under it, or beside it in a narrow column, at the same edge as the image.
- Keep captions short, in a smaller or quieter style, and left-aligned even in a centered layout.
- Credits and notes can sit on the trailing edge of the caption line.

## Galleries

- Equal cells that wrap are the default; plan the count at each width instead of fixing a number of columns.
- Allow one image to span more (a lead image across two columns) only if it has a reason; do not stagger sizes randomly.
- For a large set, add a way to see each image whole.

## Text over images

- Put text only over a quiet area of the picture, or on a solid or scrimmed patch behind the text.
- Check contrast against the lightest and darkest parts the text can land on, not just the average.
- Keep the image from competing with the headline; if the image is the main thing, make the text secondary and small.
- If the image can change (user content, a rotating hero), do not rely on a fixed quiet area; add the scrim.

## Quick checks

- Is any whole-image content cropped?
- Does a set of photos share one ratio and a deliberate focal point?
- Does every caption sit with its image?
- Does any text sit on a busy area without a scrim?
- Do image widths line up with column edges?
