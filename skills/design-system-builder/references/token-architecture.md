# Token architecture

## Tiers

| Tier | Holds | Example | Who may read it |
|---|---|---|---|
| Raw | Ramps and scales, no meaning | `blue.600`, `size.4` | Semantic tier only |
| Semantic | Purpose | `color.text.secondary`, `space.inset.md`, `radius.control` | Components, pages |
| Component | A knob only one component needs | `button.padding-x` | That component |

Components never read raw values. If a component needs a color no role covers, add a role or accept an exception; do not reach down a tier.

## Naming grammar

`category.role.variant.state`, most general first: `color.text.primary`, `color.surface.raised`, `color.border.subtle`, `color.accent.default`, `color.accent.hover`, `color.danger.default`. Space by use (`space.inset.sm`, `space.stack.md`, `space.section`), not by pixels. Radius by component size (`radius.control`, `radius.container`). Motion by purpose (`duration.fast`, `ease.exit`). Drop adjectives that describe appearance (`light`, `big`, `blue`) from semantic names; they lie after the next theme.

## Formats

```css
:root {
  --blue-600: #1f5fbf;           /* raw */
  --color-accent: var(--blue-600); /* semantic */
}
[data-theme="dark"] { --color-accent: var(--blue-400); }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --color-accent: var(--blue-400); } }
```

```json
{ "color": { "accent": { "default": { "$value": "{blue.600}", "$type": "color" } } } }
```

Keep one token file as the source and export to CSS variables, native platforms and design-file variables. Generated files are not edited by hand.

## Themes

A theme is a second set of semantic assignments over the same names. Check in each theme: body and secondary text on every surface, text on accent fills, focus ring against its neighbors, disabled that is still legible, borders that still separate. Dark themes: layer by lightness, soften large white areas, reduce saturation of big fills, express elevation as lighter surfaces plus a faint border instead of heavier shadows. A brand theme changes the raw ramp or the accent role only; layout, spacing and radius stay shared.

## Cleanup method (a messy token file)

1. Export every distinct value in use with a count and where it appears.
2. Cluster: grays by lightness, spacings by nearest scale step, sizes by role. Pick the survivor of each cluster by use count and neighbor spacing.
3. Write the merge map: old value or name, new token, number of places affected.
4. Rename by role. Keep old names as deprecated aliases for one release with a removal date.
5. Migrate by area, highest use first; add a lint or review rule that rejects raw values in components.
6. Report values that fit no step as layout problems to solve, not as steps to add.
