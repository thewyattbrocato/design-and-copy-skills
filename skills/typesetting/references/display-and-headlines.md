# Display and headlines

Load this when a headline, hero line, slide title or pull quote is set large (about 40px and up) and its breaks, spacing or finish are in play. Body text keeps the ranges in SKILL.md. Values are starting points: judge by eye on the real words at the real width. A headline already broken at its phrases, inside the display leading range, needs no change.

## Breaks

- **Break by phrase.** Default: break where the sense pauses, not where the lines come out even. `text-wrap: balance` evens line lengths but can still split a phrase ("Doors open at / seven, rain or shine"). Keep phrases whole with `nowrap` spans or non-breaking spaces; never end a line on a one- or two-letter word. Change when the column cannot hold the longest phrase: cut words or lower the size before splitting it.
- **No hyphens.** `hyphens: manual` on headlines even when the body hyphenates.

## Spacing

- **Leading.** Default: inside the display range in SKILL.md, a notch tighter for a line set entirely in capitals, which has no descenders to clear. The floor is collision: no descender touching the ascender or accent below. Open up for long lines or a large x-height.
- **Word gaps.** Default: close them slightly at display size, where the face's gaps scale up and look loose (`word-spacing: -0.05em` is a first try). This is partly taste, so compare both and keep the default if the face already looks even. Stop while words still separate clearly.
- **Pairs.** After uniform tightening, look once for pairs that still gap or touch (A, V, T, Y, W beside lowercase). Fix only those with a span margin or in the design tool; do not loosen the whole line for one pair.

## Shape

- **No synthetic stretch.** Do not squeeze or widen display type to fill a space (`transform: scaleX()`, uneven SVG scaling, `font-stretch` on a face with no width axis). A few percent is invisible; past that, stroke thickness goes uneven. Use a narrower cut, a real width axis, or change the size.
- **Reversed.** Light display type on a dark field or photo reads smaller and thinner than the same line dark on light. If it looks weak beside that version, add a step of weight or size, and put a scrim behind a busy photo.
- **Hung punctuation.** A big opening quote mark pushes the first letter in and breaks the left edge. Let the mark hang in the margin. `hanging-punctuation: first` is Safari-only, so it is an extra: elsewhere use a negative `text-indent` about the width of the mark (start near `-0.4em`) on that quote only (room needed in the margin). Nothing may depend on it.

## Checks

- Every break falls between phrases; no hyphens; no line ends on a small word.
- No descender touches the line below; words still separate; no pair is touching.
- Nothing is stretched; reversed headlines look as strong as their dark-on-light version.
