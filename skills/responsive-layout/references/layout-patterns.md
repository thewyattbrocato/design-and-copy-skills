# Layout patterns

Find the problem you have, then take the short recipe under it. Recipes are starting points, and the class names are placeholders for your own. Verify browser support for newer features against current compatibility tables before relying on them.

## Content that must wrap or stack

**A column with even spacing.** The parent owns the space between children.

```css
.column { display: grid; gap: 1rem; }
```

Failure: margins on every child collide, double, or leave a stray gap at the end of a card.

**Items that wrap like words.** Tags, buttons, toolbars.

```css
.chips { display: flex; flex-wrap: wrap; align-items: center; gap: .5rem; }
```

Space with `gap`, never margins on the items. Failure: a nowrap row that overflows, or a wrapped last item that looks orphaned (accept it, or add `flex: 1 1 auto` so items share the row).

**Cards that fit the space they are given.** The column count follows the container, with no query.

```css
.cards {
  --track: minmax(min(16rem, 100%), 1fr);
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, var(--track));
}
```

The inner `min()` stops the minimum from exceeding the container, so nothing overflows on a narrow screen or in a narrow sidebar. Check a single card (does it stretch across the row? `auto-fill` keeps cards card-sized) and the empty state. Failure: a bare `minmax(300px, 1fr)`, or a class that fixes the column count.

**Peers that go from a row to a stack all at once.** Three items never become two and one.

```css
.group { container-type: inline-size; }
.peers { display: grid; gap: 1rem; }
@container (inline-size >= 40rem) {
  .peers { grid-auto-flow: column; grid-auto-columns: 1fr; }
}
```

Below the container width the peers stack; at or above it they share one row. Choose the threshold from the widest expected count of items and the narrowest comfortable item.

## Text that must stay readable

**A capped reading width.**

```css
.article { padding-inline: 1rem; }
.article > :is(p, ul, ol, h1, h2, h3) { max-inline-size: 65ch; margin-inline: auto; }
```

Cap the text elements, not the page wrapper. Failure: a capped wrapper also narrows figures, tables and grids. Let code and data run wider.

## Two regions side by side

**A side area with a fixed width, and a main area that takes the rest.** One column until the container is wide enough for both.

```css
.region { container-type: inline-size; }
.split { display: grid; gap: 1.5rem; }
@container (inline-size >= 45rem) {
  .split { grid-template-columns: 16rem minmax(0, 1fr); }
}
```

Set the threshold from the aside's width plus the narrowest comfortable main area. `minmax(0, 1fr)` lets long content in the main area shrink instead of pushing the split wider. Failure: a split keyed to the viewport inside a component that lives in a narrow panel.

## Something that must keep a shape or size

**Media that holds its ratio.**

```css
img, video { max-inline-size: 100%; block-size: auto; }
.thumb { inline-size: 100%; aspect-ratio: 16 / 9; object-fit: cover; object-position: 50% 30%; }
```

The ratio sits on the image itself, so no wrapper is needed. Default to the natural ratio. Use a fixed ratio when a set must line up (a card grid), and move `object-position` to the subject's focal point. Never stretch. Do not crop images that must be seen whole (diagrams, screenshots, charts, receipts); use `object-fit: contain` or let them take their own ratio. Add `width` and `height` attributes, or an `aspect-ratio`, to reserve space so the page does not jump while images load.

**A region that fills the screen.**

```css
.stage { min-block-size: 100vh; min-block-size: 100dvh; display: grid; place-content: center; }
```

The first line is the fallback for browsers that skip the second. `min-block-size` lets content grow past the screen; dynamic viewport units follow the browser bars that appear and disappear on phones. Failure: a fixed `height: 100vh` that clips content, or a hero centered by absolute position and a transform. Use `svh` when the region must never be taller than the smallest visible screen.

## Layers and overlays

```css
.popup { inline-size: min(40rem, 100% - 2rem); max-block-size: calc(100dvh - 2rem);
  margin: auto; overflow: auto; overscroll-behavior: contain; }
```

Size from the viewport, not a fixed width, and scroll inside the overlay rather than the page behind it. A `dialog` opened with `showModal()`, or an element in the popover top layer, sits above everything with no `z-index`. Focus and keyboard behavior belong to detailed component accessibility work, outside this skill. Failure: a fixed `width: 600px`, content taller than the screen with no scroll, or `z-index` escalation.

## Scrolling sideways on purpose

A row of cards, or a wide table.

```css
.rail { display: flex; gap: 1rem; padding-block-end: .5rem; overflow-x: auto;
  overscroll-behavior-x: contain; scroll-snap-type: x proximity; }
.rail > * { flex: 0 0 min(18rem, 85%); scroll-snap-align: start; }
```

Label the region (`role="region"` with an `aria-label`, and `tabindex="0"` so keyboard users can scroll it), keep the scrollbar visible, and let the next item peek so the row looks scrollable. Failure: a strip that hides content with no cue, or scrolling in two directions.
