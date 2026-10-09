# Contrast levers

Load this when you need to separate levels and are not sure which lever to pull, or when two levels look too alike.

## The levers, roughly strongest to weakest for static ranking

1. **Position and space.** Being first, being alone, or being surrounded by empty room ranks an element before any styling does. Try this first because it costs nothing and cannot clash with a design system.
2. **Size.** Large reads as important at a glance and survives blur. It also costs room, so spend it on one or two elements.
3. **Weight.** Heavier strokes stand out within a line or block of text of the same size. This is the cheapest way to emphasize inside running content.
4. **Value (light against dark).** The element with the biggest light-dark difference from its ground wins. Lowering the value contrast of secondary items is how you push them back.
5. **Color (hue and saturation).** A single saturated accent among quiet neutrals is strong; the same accent repeated ten times is noise. Never rely on color alone for meaning.
6. **Case, style, and texture.** Capitals, italics, underline, and patterns are weak, noisy, or both. Use them for labels and rare cases, not for ranking.

## Combining levers

- Change one lever per step between levels. Title to subtitle: size. Subtitle to body: weight or value. Body to meta: value or size.
- Two levers on one element make it a boss; three make it shout. If a thing already has size and a bold weight, leave its color alone.
- Motion sits outside this ranking: it pulls the eye harder than any static lever. Reserve it for a state change the user must notice, and keep it short.
- Use a lever the same way each time. If bold means "label" in one place and "warning" in another, readers learn neither.
- On a dark ground, value contrast is easy to overdo: light text glows and looks heavier than it is. Drop a weight step and dim secondary levels; the typesetting skill (if installed) has the weight and size defaults.
- Surface area acts as weight. Bold text and solid icons look heavy, so soften an icon's color beside lighter text; strengthen a faint hairline by thickening it, not by darkening it to black.

## Text colors and weights

Three text values (dark for primary, mid for secondary, lighter for tertiary) and two weights (regular to medium for normal, semibold to bold for emphasis) cover most interfaces. Avoid weights below regular on small text; to quiet something, use a lighter value or a smaller size, and keep it above the text contrast floor.

## Starting step sizes

These are starting points, not rules; check them by squinting at the result.

- Size: about 1.25 between neighbors in dense or tool-like views, 1.4 to 1.6 for content pages, 2 or more for a marketing headline against body copy.
- Weight: skip at least one step in the family (regular to semibold, or medium to bold). Adjacent steps like regular to medium rarely register.
- Value: if two text grays do not look different on a mid-quality screen, they are not different. Aim for a clear visible gap, while the quieter one still clears the accessibility contrast floor for text.
- Space: separating a heading from the text above it should take clearly more room than separating it from the text it introduces; exact values are a spacing decision, not a hierarchy one.
