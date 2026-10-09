A twelve-column grid is a useful default, not a universal rule. It fails when:

- **Content doesn't divide evenly.** Twelve splits cleanly into 2, 3, 4, and 6. Five equal cards, or a 7/5 split, produce awkward gutters or leftover space.
- **The layout is simple.** A single-column article, a form, or a login page gets no benefit. The grid adds markup and class noise.
- **The design is irregular.** Editorial or asymmetric layouts often work better with CSS Grid areas, `auto-fit`/`minmax`, or custom tracks.
- **Small screens.** Twelve columns on mobile usually collapse to one or two, so the extra granularity is unused. Every breakpoint needs its own column spans, which adds maintenance.
- **Components are reused in different contexts.** Container queries or intrinsic sizing adapt to the space available, not to the viewport grid.
- **It's treated as the goal.** Consistent spacing, alignment, and a clear hierarchy matter more than the column count.

I'd suggest a shared grid for page-level layouts, with flexibility to opt out where it doesn't fit.
