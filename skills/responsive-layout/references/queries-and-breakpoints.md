# Queries and breakpoints

## Try no query first

Wrapping rows, auto grids, sidebar splits and switching rows adapt without any query. A query is for the cases they cannot express: a different arrangement rather than a different count per row.

## Container query or media query

Ask what the component is responding to.

- The space the component itself gets (a card in a sidebar versus a main column; a toolbar in a panel): **container query**.
- The viewport or the device (how main navigation works, whether pointer is coarse, print, motion, color scheme): **media query**.

```css
.card-wrap { container-type: inline-size; container-name: card; }
@container card (inline-size >= 28rem) {
  .card { display: grid; grid-template-columns: 8rem 1fr; gap: 1rem; }
}
```

Points to remember:

- The queried element must be an ancestor with `container-type`; a component cannot query its own box.
- `container-type: inline-size` applies size containment on the inline axis: the container no longer sizes itself from its content's width. Give it a width from layout (a grid track, a parent) and do not put it on an inline element or on something that must shrink-wrap.
- Name containers when they are nested so a query hits the intended one.
- Container query units (`cqi`) are available inside the queried subtree.
- Check current browser support before relying on it. If support is required that it lacks, fall back to the intrinsic pattern and note the decision.

## Where media queries still belong

- Primary navigation: a top bar versus a bottom tab bar or a drawer is an ergonomic choice about the device, not the component's box.
- `(hover: hover) and (pointer: fine)` to add hover-only effects; `(pointer: coarse)` for larger touch targets.
- `(prefers-reduced-motion: reduce)` to calm or remove motion; `(prefers-color-scheme: dark)` for theme defaults; `(prefers-contrast: more)`; `print`.
- Orientation or aspect ratio when the layout really depends on it.
- App-shell level splits: side panel versus overlay for the whole page.

Do not use a media query to adapt a component to a column it happens to be in.

## Choosing breakpoints from content

1. Build the narrowest layout first and make it work.
2. Widen the window slowly. Where the lines run too long, items get too far apart, or something looks lost, a break belongs there.
3. Record the width with the reason ("the sidebar fits beside the list at about this width").
4. Merge breakpoints that sit close together. Most pages need only a few; many components need none.
5. Write them in `em` or `rem` (media queries use the browser's default size in `em`, so they also respond to the reader's text-size setting), and prefer range syntax (`@media (width >= 48em)`) if the target browsers support it.

Never name breakpoints after devices; devices change and content does not care what they are called. Where a design system defines breakpoints, use them.

## Test between the breakpoints

Layouts fail between widths, not at them. Drag the window slowly through the whole range, test a component in its narrowest and widest container, and test at larger text sizes. An in-between width that breaks means a missing pattern or a wrong query, not a missing device.

## Mobile-first or desktop-first

Default: write the base styles for the narrowest case and add wider rules with `min-width` queries or `>=` ranges, so small screens load less and override less. Change when an existing codebase is desktop-first: stay consistent and change only what is broken.
