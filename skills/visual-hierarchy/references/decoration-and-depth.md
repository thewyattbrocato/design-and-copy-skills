# Decoration and depth

Load this when a design uses shadows, gradients, glass or blur, illustration, icon sets, or text over images, or when it looks overworked.

## The job test

For each line, box, shadow, gradient, blob, icon, or picture, ask what it does. Acceptable answers:

- **Organize:** it groups items, separates sections, or leads the eye along a path.
- **Emphasize:** it makes the primary thing stand out.
- **Identify:** it carries the brand, product, or mood the user asked for, or it shows what something is (a recognizable icon, a screenshot, a real photograph).

If the honest answer is "it looks premium" or "it fills space", remove it and look again. Often space does the same work better than a box or a rule.

## Boxes and lines

- Try removing a border and giving the group more room around it. Keep the border if the group is interactive, needs a hard boundary (an input), or the space is not available.
- One rule weight per purpose. A hairline for table rows and a heavier line for a section break is fine; five weights is noise.
- A card around every item is a decoration habit. Use cards for items that are independent, interactive, or movable.

## Depth

- Use one light direction across the view. Shadows fall the same way and have the same softness for the same elevation.
- Decorative elevation stays minimal: a card that floats only to look premium has no job. Functional layers are different: a menu, popover, dialog and dragged item sit at different distances, so give each a step from one short fixed scale (a few levels), with softer, larger shadows as the layer rises.
- Soft, low-contrast shadows. A hard dark shadow draws the eye to the container, not the content.
- Value does the depth work: a slightly lighter surface above a darker ground reads as raised, with no shadow at all.
- Gradients, glass blur, glow, and shadow stacked on one surface compete with each other and with the content. Choose at most one of them as the way depth is shown.

## Illustration and imagery

- Illustration is a supporting actor unless the view is about the picture. If it outshouts the headline, reduce its size, saturation, or value contrast, or move it to the quieter side.
- Prefer a real depiction (a product shot, a CSS mockup, a real photo) over generic decorative art that could belong to any product.
- Decorative blobs, abstract waves, and floating shapes need to answer the job test. Most do not.

## Text on images

- Put text on a region of the image that is quiet and has even value, or lay a scrim or solid panel behind it.
- Check the contrast at the worst point of the image behind the text, not the average. Measure it against the accessibility contrast floor for text.
- Place the image so its focal area does not collide with the headline.

## Icon sets

- One family per interface: the same stroke weight, the same corner style, the same grid, and the same level of detail. A single outlier looks like a bug.
- Icons are for recognition. Use one when it is a well-known symbol, or where it speeds scanning. A generic icon in a colored circle above every feature heading adds weight without information; drop it or make it real. The shape itself is not the failure: a small icon that must fill a large area looks chunky when scaled up, so a tinted shape around it is fine when it earns the space. Balance an icon's weight against nearby text by softening its color.
- Pair unfamiliar icons with a text label.
- Size icons to the text they sit with, and align them optically (see the alignment reference).
