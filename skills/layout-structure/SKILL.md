---
name: layout-structure
description: Use when you design, build, plan or review the overall structure of a page, screen, slide, poster or social graphic - a landing or marketing page, a documentation or article page, a product catalog or listing, a settings or app screen, a magazine-style opening, or one message adapted to several formats. Decides which kind of grid or column system the content needs, the reading measure, how navigation lines up with content, what the first screen must establish, how a long page is paced, and when to break the grid on purpose. Not for CSS mechanics, spacing values, emphasis between elements, multi-chart dashboards, or single components such as a button sheet.
---

# Layout structure

A layout is the answer to four questions: what is the material, how much of it is there, how wide is a line of text, and what happens in a container you did not design. Models usually skip them and reach for a stock template (twelve columns, a centered stack, heading plus three cards, repeated). This skill puts the questions first and lets the structure follow from the answers.

## When to use

- Deciding how a page, app screen, article, catalog, documentation page, landing page, slide, poster, or social card is organized before styling it.
- Reviewing a layout that feels generic, misaligned, monotonous, or hard to read.
- Choosing columns, a sidebar, image spans, or where navigation sits relative to content.
- Adapting one message to several formats or aspect ratios.

## When not to use

- Writing the CSS (flex, grid, breakpoints, container queries): use the responsive-layout skill if installed. This skill decides what structure is needed, not how to code it.
- Padding, gaps, and grouping by proximity: use spacing-and-grouping if installed.
- Which element is loudest, button ranking, emphasis: use visual-hierarchy if installed.
- Exact line length and leading numbers: use typesetting if installed; this skill only says the measure comes first.
- Multi-chart screens and KPI boards: multi-chart dashboard layout, outside this skill.
- Single components (a button sheet, one card, a tooltip) and small edits: do not run the procedure. A simple aligned arrangement is enough.
- Wide data tools and spreadsheet-like grids: the measure cap is for prose. Full width can be correct there (see judgment calls).
- When a neighbor skill named above is not installed, use ordinary judgment for that part.
- Always yield to explicit user instructions, an existing design system, and platform conventions.

## Procedure

Scale it to the task. A full page uses every step; a header fix needs steps 1 and 6 only.

1. **Run the intake.** Answer four things in a sentence each: what the material is (continuous prose, comparable items, separate chunks, bands of different content, or a mix), how much there is and what the worst case looks like (longest title, empty state, one item versus a hundred, translated text), who reads and what they must find first, and whether the format is fixed (slide, poster, print, social card) or reflowing. If the content does not exist yet, write plausible content first; a layout drawn around placeholder boxes fits nothing.
2. **Pick a structure family.** Match the material, not a habit: see the table below, and load the structure reference for worked cases.
3. **Set the measure, then derive columns.** Decide how wide the main text may run, then see how many columns of that width the container supports. Do not start from a count of columns and pour text across them. A twelve-unit lattice is a planning sketch; reading text never spans most of it.
4. **Size unequal columns on purpose.** A main column roughly twice a secondary one is a dependable starting pair. A navigation or filter sidebar often sits around 14 to 20rem. Let the secondary column hold what it needs (a table of contents, notes, captions) and no more.
5. **Place images by need.** Load the images reference when the page has more than a decorative picture.
6. **Line up navigation with content.** Navigation shares an edge with the content column, or is offset from it by a deliberate whole column. A centered bar over left-aligned content reads as a mistake. Local navigation (tabs, an on-this-page list) should look different from global navigation.
7. **Make the first screen answer the basics.** A newcomer should see what the thing is, what they can do with it, and why it suits them, in plain words, with the primary path visible without scrolling. No manifesto.
8. **Pace anything long.** Decide the order of the content first, then the feel of the sequence: alternate open, woven, and full sections, allow one loud section, keep the others calmer, and do not repeat one section template down the page. Load the pacing reference for landing pages and long reads.
9. **Break the grid only for a named job.** Write the job in a phrase before breaking. Everything else stays on the structure.
10. **Check the stacked order.** On a narrow screen the source order is the reading order. The argument and the primary action must survive it.
11. **Fixed formats get their own rules.** For slides, posters, social cards, and print, load the fixed formats reference before choosing sizes.

## Structure families

| Material | Default structure | Notes |
| --- | --- | --- |
| Continuous reading (essay, story, long help article) | One column with a capped measure and generous side margins | Figures may be wider than text. |
| Comparable peers (products, people, listings) | Grid of equal cells that wraps | One image ratio, one content order per cell. |
| Article with figures, captions, notes | Column grid; secondary text takes a narrower column | Captions beside or under their figure. |
| Marketing or landing page | Horizontal bands, each with its own inner structure, sharing one content edge | Pace the bands. |
| Application or documentation | Shell: navigation plus main (plus optional outline), sharing at least one alignment | Content region has its own measure. |
| Wide data or tool surface | Full available width with frozen identifying columns | Prose inside it still gets a measure. |

## Judgment calls

- **Fluid or strict grid.** Default: on screens use fluid structures (a column that caps and centers, cells that wrap, a sidebar that drops below when narrow). Change when the format is fixed (slide, poster, social card, print page); there the units are exact and must add up.
- **Measure cap.** Default: keep prose lines to roughly 45 to 75 characters (about `60` to `70ch` for long reading). Change for code, tables, logs, captions, and data grids, which can run wider or scroll; keep any prose paragraphs inside them capped.
- **Twelve columns.** Default: use it as a sketch to talk about proportions, if at all. Change when a design system already provides a twelve-column layout; then place content on it, but still cap text blocks.
- **Symmetry.** Default: left-aligned, asymmetric structure for reading and exploring. Change for ceremony, authority, and single-focus moments (an invitation, a short hero, a certificate), where a centered block suits. A centered block of left-aligned text is fine; centered paragraphs longer than a couple of lines are not.
- **Margins and gutters.** Default: outer margins at least as large as the gutters, usually larger. On small screens side margins may shrink while the top inset holds. Change when the content must fill the width (a map, a canvas, a data tool).
- **Density.** Default: tools and dashboards denser, reading and marketing airier. Change when the task contradicts it (a dense reference table in a marketing page, an airy onboarding step in an app). The structure should stay legible at either density.
- **Navigation placement.** Default: top bar for few, flat destinations; side navigation for many or nested ones. Change to match the platform or the existing product.
- **Breaking the grid.** Default: stay on the structure. Change for a full-bleed image that is the page, a pull quote hanging into the margin, a single odd item in an obedient set, or an expressive piece where the break is the point. In an expressive piece keep a clear entry point and keep key facts findable. If the same break appears three times, it has become a rule; build it into the structure.
- **Golden ratio.** Default: do not use it as a page, column, or sidebar ratio; derive widths from content and measure. Change only when the user asks for it.
- **Plan for reflow.** Default: assume text can be longer, bigger, or translated, and the container narrower than your mockup. Change only for fixed formats, where you check the worst case instead.

## Common failures

- Article text spanning ten of twelve columns at over 100 characters per line → a capped reading column; wider elements only for figures and code.
- Everything centered, paragraphs and lists included → one flush edge; center only short blocks.
- Heading plus three icon cards, repeated in every section → pick each section's structure from its content (a sequence, a comparison, a single statement, a gallery) and let one section be the loud one.
- Centered navigation bar over a left-aligned page, or a header container wider than the content container → shared edges, or a deliberate whole-column offset.
- Screenshots, diagrams, and receipts cropped into card ratios → give whole images whole spans.
- Every section at the same density → alternate; one loud section, calmer others.
- Collage of overlaps and rotations with the main action buried → entry point first, then breaks with named jobs.
- A social card made by shrinking or cropping the desktop hero → recompose for each ratio.
- A sidebar or column width taken from a ratio instead of content → size it from what it holds.
- A layout that works only with the demo text → test with the longest title, an empty state, and a hundred items.
- Plan for the wide frame only, so stacking on a phone puts the call to action below the fold → check the stacked order.
- A written answer that runs past a length limit the user gave → keep to it; cut material before the limit.

## Quick checks

- Say what the material is, and name the family chosen for it.
- Count characters in a typical body line; it should sit in the measure range unless it is code or data.
- Draw the vertical edges; header, nav, and content should share at least one, and every extra edge needs a reason.
- Run the worst case: longest title, empty state, one item versus a hundred.
- Read the stacked, single-column order top to bottom; the point and the action should survive.
- List the section patterns down a long page; no two neighbors should share a template unless the content is parallel.
- Whole-image content is not cropped; a set of photos shares one ratio.
- Every grid break has a name for its job, or has been removed.
- For a fixed format: do the columns, gutters, and margins add up exactly, and is key text inside the safe area?

## References

- [references/choosing-a-structure.md](references/choosing-a-structure.md): load at the start of a layout. Material-to-family guidance, a worst-case checklist, and worked outlines for an article, catalog, landing page, documentation page, app shell, and settings page.
- [references/images-and-media.md](references/images-and-media.md): load when placing images, galleries, diagrams, captions, or text over a picture.
- [references/pacing-long-pages.md](references/pacing-long-pages.md): load for landing pages, long reads, and any page with more than three or four sections; covers sequencing, density alternation, section patterns beyond card rows, and breaks.
- [references/fixed-formats.md](references/fixed-formats.md): load for slides, social graphics, posters, and print pages: unit arithmetic, margins, safe areas, recomposition across ratios, sheet proportions, and bleed.
