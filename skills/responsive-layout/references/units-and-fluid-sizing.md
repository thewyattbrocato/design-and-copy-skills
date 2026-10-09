# Units and fluid sizing

## Which unit for what

- **rem**: type sizes and most spacing, widths of components (`16rem`), breakpoints expressed in em or rem. It follows the root size, which follows the user's browser setting.
- **em**: things that should scale with their own text: icon size, button padding, a gap inside an inline group.
- **ch**: the width of the `0` glyph; use it to cap text measure (`65ch`) and sometimes narrow inputs.
- **%, fr, and container units (`cqi`)**: sizes relative to a parent or a container. Prefer them over `vw` for component sizes.
- **px**: hairlines, borders, shadows, and sizes that must stay absolute (a canvas, an export format).
- **vw, vh and the dynamic family (`dvh`, `svh`, `lvh`)**: viewport questions only. `100vw` includes the vertical scrollbar, so it overflows; use `100%`.

Leave the root size alone, or set it to `100%`. Setting it to a pixel value overrides what the user chose. A user who has raised their default text should get a bigger layout, not a clipped one.

## Why not pixels for type

A pixel font size is fixed regardless of the reader's browser setting, so people who need larger text do not get it. In current browsers page zoom still scales pixels, but the text-size setting does not. Keep rem for type so both work.

## Line height and spacing

Use unitless line heights (`1.5` for body text, tighter for large headings), so the value follows each element's own font size. Tie spacing to the type: a section gap in rem grows when text grows. For specific values and a scale, use spacing-and-grouping and typesetting if installed.

## Fluid values with `clamp()`

`clamp(min, preferred, max)`: the preferred value moves with the viewport, held between a floor and a ceiling.

```css
h1 { font-size: clamp(2rem, 1.2rem + 3vw, 3.5rem); }
section { padding-block: clamp(2rem, 1rem + 5vw, 6rem); }
```

Rules:

- Put a rem term inside the preferred value (`1.2rem + 3vw`). A pure `vw` value ignores the reader's text-size setting and may not scale with zoom.
- Pick the floor and the ceiling first, from content, then the slope. Check the result at the narrowest width, at a wide monitor, and at 200% text.
- Use fluid sizes for display type and large section spacing. Body text stays near a fixed rem; fluid body text rarely helps.
- Never let the measure grow with the viewport: cap line length in `ch`.
- Heading sizes from two or three clamp values beat one per breakpoint.

## Container-relative sizing

Inside a component, `cqi` units (1cqi is 1% of the container's inline size) let type and padding follow the container rather than the screen. Set `container-type: inline-size` on the parent. Keep a `clamp()` around them so a tiny or huge container does not give unusable values.

## Pixels that stay

A one-pixel border or divider, a focus ring offset, a shadow blur. A fixed-format export (social graphic, slide, print) uses its pixel or point canvas throughout; there is no reader setting to respect.
