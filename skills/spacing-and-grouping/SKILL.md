---
name: spacing-and-grouping
description: Use when you design, build, restyle or review any interface or page where several items sit near each other - a settings screen, a form, a card grid, a feature section, a list, a toolbar, a dashboard panel or an article page - and whenever you set or fix whitespace: padding, gaps, margins, density, spacing scales, and whether items are grouped by space, a rule, a tinted region, or a card. Also for interfaces that look cramped, uniformly padded, or boxed-in. Not for choosing emphasis, palettes, page grids, CSS layout mechanics, or expressive posters.
---

# Spacing and grouping

Space is how a layout says what belongs together. Left to defaults, models pad everything the same, box every block, nest cards, and scatter one-off numbers; this skill replaces that with a map of relationships, a small scale, and the lightest grouping device that works.

## When to use

- Building or restyling any interface or page where several items sit near each other: forms, settings, lists, cards, toolbars, dialogs, dashboards, article pages.
- Fixing a design that looks cramped, sparse, flat, or boxed-in, or where related things do not look related.
- Choosing between space, a divider, a tinted region, and a card.
- Cleaning up CSS full of ad-hoc margins and paddings, or defining a spacing scale.
- Setting a compact or comfortable density.

## When not to use

- Which element wins attention and how big the steps between levels are: use visual-hierarchy if installed.
- Page structure, column systems, reading measure: use layout-structure if installed. CSS layout primitives and overflow: use responsive-layout if installed.
- Token tiers and naming for a whole system: use design-system-builder if installed. Whether a card is one big link: detailed component accessibility work, outside this skill.
- When a neighbor skill named above is not installed, use ordinary judgment for that part.
- Posters, covers, and other expressive compositions, where tension and scale contrast matter more than even rhythm. Use space deliberately there; do not apply product-UI padding rules.
- A one-line tweak ("add some room under this heading") needs only the matching check, not the procedure.
- Always yield to explicit user instructions, an existing spacing system or token set, and platform conventions. Fix relationships inside the values the system gives you.

## Procedure

Scale this to the task. A single component gets steps 1, 2, 4 and 8; a full page gets all of them.

1. **Map relationships before picking numbers.** List which items form a unit, which units are siblings, and which must be pushed apart. A label belongs to its field, a field to its section, a section to the page. Write the map down, even as a few lines, then choose values.
2. **Make within clearly smaller than between.** Space inside a group is about half of the space between groups, or less. A heading sits closer to what it introduces than to what precedes it, roughly one part above to one part below at the least, more often two to one.
3. **Use a small scale.** Five to eight steps cover most products. Build them from a base unit or from the body line height (see the scale reference). Every gap and padding comes from the scale; no 13s, 22s, or 37s.
4. **Step outward.** Space grows with the size of what it separates: letters, words, lines, paragraphs, groups, sections, page margins. A gap between columns stays smaller than the outer margin around them.
5. **Group with the lightest device that works.** Try space first. Add a hairline rule when space alone cannot separate (dense lists, unlike items that must sit close). Add a tinted region when a cluster must read as one unit and cannot be moved. Use a card only for a discrete object. See the grouping reference.
6. **Match density to the task.** Daily expert tools can be compact; reading and marketing pages can be generous. Compress the steps, not the ratio between within and between.
7. **Pad by size and content.** Padding grows with the element. Text inside a surface gets about equal padding on its sides. Buttons get horizontal padding of roughly one and a half to two times the vertical. See the component reference.
8. **Let the parent own the gap.** Space between siblings comes from the container (a `gap`, or a rule on the sibling that follows), not from a bottom margin on every child. This removes the doubled gap after the last item and inside padding.
9. **Leave room to touch.** Interactive targets of about 44 px or more where fingers are used, with roughly 8 px or more between neighbors. Dense pointer-only tools may go smaller on purpose (see the density reference).
10. **Check consistency and holes.** The same relationship gets the same space everywhere. Content inside a surface lines up on one inner edge. Empty regions are fine when chosen; a stray gap inside a group splits it.

## Judgment calls

- **Cards.** Default: no card; use space, headings, and alignment. Change when the item is a discrete object the user can open, select, drag, compare, or act on as a whole, or when it must stand apart from a busy background. Then give every such object one consistent surface.
- **Rules versus space.** Default: space. Change when rows are many and tightly packed, when a table needs scan lines, or when two unlike things must touch. A rule between items needs space on both sides of it; use one rule weight and a quiet color.
- **Tinted regions.** Default: skip them. Change when a cluster of controls must read as one unit and the items cannot be moved closer (a toolbar, a filter panel, a sticky footer).
- **Density.** Default: moderate, set by the task. Change toward compact for tools used all day by experts where rows per screen is the point, toward generous for reading, onboarding, and marketing. Keep the within/between ratio either way. Offer a density setting only in data-heavy tools.
- **The scale base.** Default: a 4 px base with named steps, or steps tied to the body line height when text dominates. Change when the project has its own system; use it.
- **Baseline grids.** Default: relate steps to the line height where it is easy, and do not force a strict baseline grid onto interface layouts. Change for print-like or fixed-format work where shared baselines are the goal.
- **Section spacing on small screens.** Default: shrink page margins and section gaps as the screen narrows, for example with `clamp()`. Keep within/between ratios and keep card or row gaps readable. Change nothing about the relationships.
- **Large empty areas.** Default: let them stand when they frame one thing on purpose. Change when a region looks abandoned or a hole sits inside a group; tighten the group or fill it with its real content.

## Common failures

- One padding and gap value everywhere in a layout with several distinct groups, so nothing groups → make within smaller than between. A small block with a single level of relationships that already reads clearly is fine as is; say so briefly.
- Heading with equal space above and below, so it floats between sections → more above, less below.
- Every section wrapped in a bordered, shadowed box → remove the boxes; use headings and space. Keep boxes for objects.
- A card containing cards, each with border, shadow, and padding → flatten to one surface or none.
- Border, shadow, and background fill on the same element → keep one, at most two.
- Six identical cards with icon circles for a feature list → a simple list or columns; keep cards only if each is an object.
- Buttons padded 4 px by 8 px → horizontal padding about twice vertical, comfortable height.
- `margin-bottom` on every child, so the last one doubles the gap → parent-owned gap.
- Values like 5, 14, 27 px scattered across the CSS → snap each to a scale step.
- Field far from its label, list items spaced like sections → tighten within, widen between.
- Gaps between cards smaller than the card padding, so cards blur into one mass → gap at least as large as the padding, or separate with a surface.
- Rows of tappable items with no gap → add space between the targets.
- Compact mode made by shrinking everything equally, so groups merge → shrink steps, keep the ratio.
- A written answer that runs past a length limit the user gave → keep to it; cut material before the limit.

## Quick checks

- Squint or blur: you should see the groups you intended, no more and no fewer.
- Each heading is visibly closer to its content than to the thing above it.
- List every distinct gap and padding value; all should be scale steps.
- Pick any two elements with the same relationship; their spacing should match.
- No surface sits inside another surface without a reason; no element has border, shadow and fill together.
- The last child in every container adds no extra space.
- Targets that fingers hit have room around them.
- Narrow the view: do groups still read as groups?

## References

- [references/spacing-scale.md](references/spacing-scale.md): load when choosing or auditing values, building a scale from a base unit or the line height, naming steps, or writing custom properties.
- [references/grouping-devices.md](references/grouping-devices.md): load when deciding between space, rules, tints, and cards, handling nested surfaces, or dividing lists.
- [references/component-spacing.md](references/component-spacing.md): load when padding buttons, inputs, lists, tables, cards, bars, and dialogs, or setting touch spacing.
- [references/density.md](references/density.md): load for dense tools, compact and comfortable modes, or any request to fit more rows on screen.
