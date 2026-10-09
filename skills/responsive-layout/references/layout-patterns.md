# Layout patterns

Find the problem you have, then take the short recipe under it. Recipes are starting points, and the class names are placeholders for your own. Verify browser support for newer features against current compatibility tables before relying on them.

## Content that must wrap or stack

**A column that spaces itself.** The parent owns the space between children.

```css
.column { display: grid; gap: var(--column-gap, 1rem); }
.column > .new-section { margin-block-start: 1.5rem; }
```

Use `gap` for even spacing and one extra rule on the child that starts a new section. Failure: margins on every child collide, double, or leave a stray gap at the end of a card. If the column sits inside a padded box, give the box the same padding as the column's gap so it looks even; a full-bleed child (an image) takes a negative inline margin equal to that padding, or the padding moves onto its siblings.

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
.all-or-none { --breaks-at: 40rem; display: flex; flex-wrap: wrap; gap: 1rem; }
.all-or-none > * { flex: 1 1 calc((var(--breaks-at) - 100%) * 999); }
```

Below the threshold the basis is a huge positive number, so each item fills its row; above it the basis is negative and ignored. To stack once there are too many items (five or more here), add a rule on the container:

```css
.all-or-none:has(> :nth-child(5)) > * { flex-basis: 100%; }
```

A container query is the simpler choice when the team knows it.

## Text that must stay readable

**A capped reading width.**

```css
.article { padding-inline: 1rem; }
.article > :is(p, ul, ol, h1, h2, h3) { max-inline-size: 65ch; margin-inline: auto; }
```

Cap the text elements, not the page wrapper. Failure: a capped wrapper also narrows figures, tables and grids. Let code and data run wider.

## Two regions side by side

**A side area with a preferred width, and a main area that takes the rest.** They drop to one column when the main area would get too narrow.

```css
.with-aside { display: flex; flex-wrap: wrap; gap: 1.5rem; }
.with-aside > .aside { flex: 1 1 16rem; }
.with-aside > .content { flex: 999 1 0; min-inline-size: 50%; }
```

The content wraps below the aside once it cannot keep half the row. Tune the percentage (where it wraps) and the aside's basis from the real content. Failure: the aside stretching across a full row after wrapping; cap it with `max-inline-size` if that matters. A grid alternative: one `minmax(0, 1fr)` column by default and a two-column template inside a container query.

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
