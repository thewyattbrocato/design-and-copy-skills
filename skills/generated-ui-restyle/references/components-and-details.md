# Components and details

Load in the parts-and-fill pass. These are the small parts where a generated screen gives itself away at a glance, and where a restyle most often stops halfway: the resting state fixed, hover and focus left in the old style.

## Icons in place of emoji

- **Default:** one icon family for the whole interface, the one the project already ships if it has one, drawn at the size it is shown. Labels after the icons share one starting edge, so give the icons a common slot. Soften icon color to balance the label beside it, as visual-hierarchy does for icon sets; a different color per item is cause 4.
- **No icon** when the word is enough and the picture would only repeat it before every item. Icons earn their place by speeding recognition (visual-hierarchy), and a column of pictures in front of a column of words rarely does.
- **Change when** emoji are the content: reactions, a person's own message, a category system the users chose. Keep them there and nowhere else.
- **Status** is a word, optionally with a small shape in a status color; never a picture or a color alone (color-palette: meaning never lives in hue alone).

## Counts, badges and tags

- **Default:** a count is meta, the lowest level of the order: plain numerals with tabular digits, quieter than the label it belongs to. A filled shape only for a count that asks for action (items waiting for this person), and then one style for that one kind.
- A badge stays only when it names a state the person must notice now, in one word, in one style everywhere. Promotional tags on menu items go.
- A static tag must not look like the button beside it (spacing-and-grouping lists this lookalike).

## Corner radii

- **A short radius scale** (design-system-builder fixes scales, radii included, in advance). Default: a small step for parts inside other parts, a middle step for controls and rows, a larger step for containers. A full pill only for things that are pills by nature, such as tags, toggles and filter chips.
- **Nested corners share a center.** When a rounded shape sits inside another with padding between, subtract the padding from the outer radius to get the inner one, so the two curves stay parallel. An inner corner rounder than its container looks pinched. When the padding is larger than the outer radius, give the inner shape its own step from the scale.
- **Change when** the decision notes call for square or very soft forms (a print-like editorial page, a toy-like app); then the one choice applies everywhere.

## Figures and charts

- A single key figure follows chart-design: the number with its comparison, not a chart. Anything added only to fill a tile is cause 1.
- Inside each chart, chart-design's rules decide the form, the colors and the axis. Bars styled as glowing capsules, or a different hue for every bar of one series, are causes 1 and 4; fix them with those rules.
- Arranging several charts and tiles into a dashboard is outside these skills; use ordinary judgment and keep every figure the original showed.

## The product's mark

- Keep the product name and any real logo exactly.
- A placeholder mark from a generator is brand-identity's job. Until there is a real one, the name set in the interface face stands in; say so in a note instead of inventing a symbol.

## Pictures

- **Show the product.** Default for a landing page or a hero: an HTML and CSS rendering of the product doing what the headline says, in the restyled palette, with names and figures that match the copy around it. Crop to the part that carries the point rather than shrinking a whole app until nothing in it can be read.
- **A real picture** the person supplies goes with its subject facing the text and the text on a calm area, checked for contrast at the worst point behind it (layout-structure on eyeline, visual-hierarchy on text over images).
- **When a picture is needed and none exists,** leave a placeholder sized to the slot, with a visible caption saying what belongs there and that it must be supplied. Never draw a fake photograph, a fake client logo or a screenshot of something the product does not do.
- Decorative art without a subject goes, and nothing new takes its place unless the notes name a job for it.

## States

Restyle every state, not only the resting one: hover, pressed, selected, focus, disabled, error, empty, loading. A focus ring still in the old glowing accent, or a selected row still on a gradient, keeps the generated look alive. Missing states are ui-polish-pass's job; add only what the restyle broke or what the person asked for.
