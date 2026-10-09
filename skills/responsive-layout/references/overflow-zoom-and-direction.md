# Overflow, zoom, direction, and stacking

## Long strings

Flex and grid children default to a minimum size of their content, so one long unbreakable string widens the whole row. Give them room to shrink and a way to break.

```css
.row > * { min-inline-size: 0; }
.text, td, .card { overflow-wrap: anywhere; }
```

- `min-inline-size: 0` (or `min-width: 0`) on the child that holds the long content. In grid, `minmax(0, 1fr)` does the same for a track.
- `overflow-wrap: anywhere` breaks at any point and, unlike `break-word`, lets the break count toward the element's minimum size, which is what a flex or grid child needs.
- `hyphens: auto` needs a correct `lang` attribute; use it for prose, not for URLs, code or names.
- For one line that must stay on one line, use `text-overflow: ellipsis` with `overflow: hidden; white-space: nowrap;` and expose the full text another way (a title or an expanded view). Do not truncate content the user must read.

## Wide tables and code

Wrap the wide element in a labeled scroll region (`role="region"`, `aria-label`, `tabindex="0"`) with `overflow-x: auto`. Keep header cells readable. For tables that are mainly readable on a phone, a stacked arrangement may be better; see data-tables if installed.

## One scroll owner per region

Pages with side panels, drawers and overlays often end up with nested scrollers. Make one element the scroll owner for each region. Use `overscroll-behavior: contain` on inner scrollers, `min-block-size: 0` on a flex child that must scroll inside a column, and `scrollbar-gutter: stable` where appearing scrollbars make content jump. Do not create sideways page scroll to hide an overflow; find the cause (usually `100vw`, a fixed width, or an image without `max-inline-size`).

## Zoom and reflow

- Content remains usable at 320 CSS pixels wide with no scrolling in two directions; that is what 400% zoom does to a 1280-pixel window. Exceptions are real two-dimensional content: maps, data tables, diagrams, code.
- Text can be resized to 200% without loss. Use rem for type, and avoid fixed heights on text containers.
- Do not block zoom. Never set `user-scalable=no` or `maximum-scale=1` in the viewport meta tag.
- Text-spacing overrides (line height 1.5 times the font size, paragraph spacing twice the font size, letter spacing 0.12 em, word spacing 0.16 em) should not clip or overlap. That fails for fixed-height boxes and `overflow: hidden` on text.
- Keep fixed or sticky headers from eating the screen at high zoom: let them scroll away or shrink at small viewport heights.
- External standards change; check the version in force.

## Direction and writing mode

Use logical properties so the same layout reads correctly right to left and in vertical writing modes:

- `margin-inline`, `padding-block`, `inset-inline-start`, `border-inline-end`, `inline-size`, `block-size`, `text-align: start`.
- Flex and grid follow direction automatically when the markup has `dir`; avoid hard-coding `row-reverse` just to place things.
- Physical properties are fine for things that do not flip: a square icon's width and height, a shadow offset (decide per case), a flipped arrow icon (mirror icons that show direction, such as back and forward, not the ones that are objects).
- Set `lang` and `dir` on the document or the element holding mixed content; use `dir="auto"` for user-generated text.

## Safe areas and viewport edges

For edge-to-edge layouts on devices with notches and gesture bars, set `viewport-fit=cover` and pad with `env(safe-area-inset-bottom)` and its siblings, with a fallback: `padding-block-end: max(1rem, env(safe-area-inset-bottom));`. Fixed bottom bars are the usual casualty. Use dynamic viewport units for full-height regions as in the screen-height pattern.

## Sticky headers and anchors

A sticky or fixed header hides the target of an in-page link. Add `scroll-margin-block-start` to targets (or `scroll-padding-block-start` on the scroll container) equal to the header's height. Test by following an in-page link, and by keyboard focus moving under the header.

## Stacking order

- Most components need no `z-index`. Use DOM order and positioned elements first.
- Create stacking contexts on purpose with `isolation: isolate` on a component, so its inner values cannot compete with the rest of the page.
- Keep a short named scale in custom properties (base, sticky, dropdown, overlay, toast) with a few steps apart. No `9999`.
- A modal `dialog` opened with `showModal()` and elements in the popover top layer render above everything with no `z-index`.
- A `z-index` with no effect usually means the element is not positioned, or sits inside another stacking context (a `transform`, `opacity` below one, `filter`, or `will-change` creates one).
