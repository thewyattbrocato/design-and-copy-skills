---
name: responsive-layout
description: Use whenever CSS layout has to hold up on any screen, container or setting, including when someone says the page breaks on phones, overflows, scrolls sideways, clips, looks cramped when zoomed or stretched too wide, or asks to make it responsive, fluid, mobile-friendly or modern, in any language and at any length: stacks, sidebars, wrapping grids, card rows, heroes, media frames, overlays and modals, scroll strips, app shells, units, clamp, container queries versus media queries, long-text overflow, zoom, right-to-left, safe areas; not for choosing page structure (layout-structure), spacing values (spacing-and-grouping), dialog focus and other detailed component accessibility semantics or type scales (typesetting).
---

# Responsive layout

Write CSS that adapts to the space it is given, not to a list of devices. State the tolerances (the narrowest an item may get, the longest a line may run, the gap) and let the browser work out the rest. The model's default habits come from older tutorials; the fixes are small and current.

## Do not produce

- Media queries at device widths (480, 768, 1024) to re-lay out a component that lives in containers of many sizes.
- A grid minimum a fixed pixel size larger than a small screen, such as `minmax(300px, 1fr)` with no cap.
- Pixel font sizes, or a root size set in pixels, that ignore the reader's settings.
- `height: 100vh` on a region that holds content, or absolute-plus-transform centering of content that can grow.
- `margin-bottom` on every child instead of a gap owned by the parent.
- `z-index: 9999` or any escalating number.
- `width: 100vw` inside a page that has a vertical scrollbar.
- Flex or grid children with no escape for long strings (URLs, compound words).
- Blocked zoom (`user-scalable=no`, `maximum-scale=1`).
- Physical `left`/`right` spacing in a layout that may be read right to left.
- Responsive machinery on a fixed-size export or a one-element page.

## When to use

- Writing, reviewing, fixing or modernizing CSS (or utility classes) for layout: page shells, sidebars, card grids, toolbars, heroes, modals, galleries, scrollers, forms in columns.
- Complaints that something overflows, clips, scrolls sideways, is too wide on a monitor, too cramped on a phone, or breaks when text is long, large or translated.
- Choosing units, `clamp()` sizes, container versus media queries, or where a breakpoint belongs.
- Any page or component build, as a last pass on the layout CSS it produced.

The request can be one line and never say "responsive" ("it looks broken on my phone"). A short request is not a small one.

## When not to use

- Deciding what structure a page needs (columns, hierarchy of regions, what is on the first screen): use layout-structure if installed. This skill codes the structure once chosen.
- Gap and padding values, grouping by proximity: use spacing-and-grouping if installed. This skill only says who owns the gap.
- Dialog semantics, focus handling, keyboard use: detailed component accessibility work, outside this skill.
- Type scale numbers and line spacing: use typesetting if installed.
- Layout tokens and their naming: use design-system-builder if installed.
- A fixed-size export (social graphic, slide, poster, print page): pixel sizes are correct. Fit the frame exactly and skip adaptive machinery.
- A trivial page (one centered message and a link): a centered flex or grid container and a readable measure is the whole job.
- Layout that already holds up. If it survives the checks below, say so and change nothing, or only what fails. Do not rewrite working CSS to show effort.
- When a neighbor named above is not installed, use ordinary judgment for that part.

A user's stack, framework, design system or stated constraint wins (a Tailwind project gets utilities, a project that must support an old browser gets that browser's fallbacks). Express the same decisions in what they use.

## Inputs

Only what changes the CSS: the code or markup to fix (if any), the narrowest width and the browsers or frameworks that matter, whether the layout is fixed-format, and any reading direction beyond left to right.

- Large build in an interactive session: ask once, each item with a default ("no minimum given: 320 CSS pixels; evergreen browsers; plain CSS; left to right").
- Anything else, or no answer: deliver on the defaults and list at most three assumptions after the work.
- Never reply with only questions.

## Deliver

- Put the requested output first: code for a build, the fixed code for a fix, a verdict for a question. No preamble, no restating the brief, no tour of CSS history.
- Give exactly the number of options asked for. Honor any stated length: drop the lowest-value point instead of shrinking every point.
- For a review, list problems by impact, each with the replacement code. Name what already works and leave it alone.
- Verify instead of asserting: count the breakpoints you kept and say why each stayed, list the units you changed, and give widths you reasoned about (320 CSS pixels, a narrow container, a wide one).

## Procedure

Small fixes start at step 6. For a large build, write steps 1 to 4 as a short plan (regions, patterns, queries), then write one representative region in full before the rest, and continue unless the user redirects.

1. **Constraints from content.** For each region, note the longest line allowed, the gap, the smallest comfortable width of a repeated item, and the worst content (long title, long URL, zero items, a hundred items).
2. **Global axioms.** Border-box sizing; rem for type and most spacing, `ch` for text measure, em for things that scale with the text beside them, pixels only for hairlines; images capped at their container; the root size left at the user's default. See [units and fluid sizing](references/units-and-fluid-sizing.md).
3. **One pattern per region.** Match each region to the problem it has in [layout patterns](references/layout-patterns.md): content that must wrap or stack (self-spacing column, wrapping items, fitted cards, all-or-none row), a readable text width, side-by-side regions, something that must keep a shape or size (media ratio, screen-filling region), overlays, deliberate sideways scrolling.
4. **Choose the query, if any.** First try a pattern that needs none. Then a container query for components, a media query only for viewport or device questions. See [queries and breakpoints](references/queries-and-breakpoints.md).
5. **Fluid sizes with bounds.** `clamp()` with a rem floor and ceiling for display type and big section spacing; never let the measure grow with the viewport.
6. **Guard overflow.** `min-inline-size: 0` on flex and grid children that hold long content, `overflow-wrap: anywhere` for long strings, scrolling only inside a labeled region and only in one direction. See [overflow, zoom and direction](references/overflow-zoom-and-direction.md).
7. **Overlays and stacking.** Size from the viewport, scroll inside, use a small named stacking scale or the top layer.
8. **Direction and edges.** Logical properties; safe-area insets for edge-to-edge layouts; scroll margin under sticky headers.
9. **Run the checks** at the end of this file.

## Judgment calls

**Container or media query.** Default: a container query for any component that appears in places of different widths (cards, tables of contents, toolbars); a media query for questions about the whole viewport or device (primary navigation pattern, hover and pointer, print, reduced motion, color scheme). Change when the component is the whole page, or the browser support you must meet lacks container queries: then use a media query with a comment saying why.

**Breakpoints.** Default: as few as possible, found by resizing until the content breaks, written in em or rem so they follow the reader's text size. Change when a team or system already names its breakpoints: use those.

**Intrinsic pattern or query.** Default: use the pattern when the change is "wrap or don't". Change to a query when the change is a different arrangement (a table becoming a list, a label moving inside a control).

**Switching row.** Default: peers sit in one row or all stack, switching together, and stack automatically when there are too many to fit. Change when the items are really unequal in importance: use a sidebar split or a grid.

**Grid minimum.** Default: the smallest comfortable item width, capped by the container (`min(16rem, 100%)`). Change to auto-fit when empty tracks should collapse and auto-fill when a lone item should stay card-sized, then look at one item and at three.

**Text measure.** Default: cap paragraphs and headings at roughly 60 to 70ch and leave wrappers and grids free. Change for code, tables and data tools, where full width is right.

**Fixed versus fluid size.** Default: relative units and `min-block-size`. Change to a fixed size for hairlines, icon boxes that must stay square, canvases, and export formats.

**Screen-height regions.** Default: `min-block-size` in dynamic viewport units with a plain `vh` line before it as a fallback. Change to a plain flow when the region holds only a short message.

**Horizontal scrolling.** Default: avoid. Allow it inside a deliberate strip or a wide table wrapper that is labeled, keyboard-reachable and shows a scrollbar. Change never to two directions at once.

**Utility classes or frameworks.** Default: say the technique in the user's tools. Change to plain CSS when no stack is stated.

## Common failures

- Component layout flipped by media queries at 768 and 1024 → a wrapping pattern or a container query.
- `minmax(300px, 1fr)` overflowing a phone → `minmax(min(16rem, 100%), 1fr)`.
- `max-width: 800px` on the page and pixel type → a `ch` cap on text elements and rem type.
- `height: 100vh` hero clipping its button → `min-block-size` with `100vh` then `100dvh`, and centering that can grow.
- Absolute plus `translate(-50%, -50%)` content spilling out → flex or grid centering.
- `margin-bottom` on every child → a parent `gap`, or one rule between siblings.
- `z-index: 9999` → a named scale, `isolation: isolate` on components, or the dialog or popover top layer.
- A long URL pushing a flex item out of its card → `min-inline-size: 0` and `overflow-wrap: anywhere`.
- `width: 100vw` causing sideways scroll → `inline-size: 100%` or the container's own width.
- `margin-left` and `padding-right` everywhere → logical properties.
- A modal with a fixed width and tall content → `inline-size: min(40rem, 100% - 2rem)`, a `max-block-size`, internal scroll.
- Nested scrollers fighting each other → one scroll owner per region, `overscroll-behavior: contain` on inner ones.
- A rewrite of CSS that already adapts → say it holds up, change only the failing line.
- Answers that pad with theory past the requested length → code and verdict first, cut the rest.

## Quick checks

- At 320 CSS pixels wide there is no sideways page scroll and nothing is clipped.
- At 200% text size and with larger default text, nothing overlaps or hides.
- Paste a very long URL and a long compound word into every flex or grid child.
- A component placed in a narrow and a wide container both look right.
- Each remaining media query asks about the viewport or device, and each has a reason.
- No fixed height holds text; no `100vw` without a reason.
- Direction flipped to right to left reads correctly.
- No stacking number above a small named scale; overlays scroll inside themselves.
- Working CSS was kept and said so; the answer has exactly the number of options asked for and is within any stated length.

## References

- [references/layout-patterns.md](references/layout-patterns.md): load when building or repairing regions; each pattern with a short recipe, when to use it and how it fails.
- [references/units-and-fluid-sizing.md](references/units-and-fluid-sizing.md): load when setting font, spacing or container sizes, or writing `clamp()`.
- [references/queries-and-breakpoints.md](references/queries-and-breakpoints.md): load when a layout needs a query, a breakpoint, or a preference or capability check.
- [references/overflow-zoom-and-direction.md](references/overflow-zoom-and-direction.md): load when hardening: long strings, scroll regions, zoom and reflow, right to left, safe areas, sticky headers, stacking.
