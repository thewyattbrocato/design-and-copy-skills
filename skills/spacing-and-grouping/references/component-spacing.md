# Component spacing

Load this when you pad specific components or set gaps inside them.

## Principles

- **Padding grows with the element.** A tag gets less than a button, a button less than a card, a card less than a dialog.
- **Text on a surface gets equal side padding.** Vertical padding may be smaller than horizontal for short single-line elements, but never so small that the text touches the edge visually.
- **A box pads; its parent spaces.** The component's own padding is set on the component. The space between that component and its neighbors is set by the container that holds them.
- **A wrapping group's row gap equals its column gap**, and the group's padding matches that gap if it has a surface.
- **Inside a surface, content shares one inner edge.** Headings, text, fields and buttons start at the same left inset.

## Parent-owned gaps

Prefer a container rule over a margin on each child:

```css
.flow  { display: flex; flex-direction: column; gap: var(--space-4); }
.tags  { display: flex; gap: var(--space-2); flex-wrap: wrap; }
```

If you cannot use `gap`, space from the previous sibling and skip the first:

```css
.flow > * + * { margin-top: var(--space-4); }
```

Avoid `margin-bottom` on every child. The last child pushes an extra gap into the container's padding, and a component that is moved elsewhere carries its old margin along. Use a local override only when one item truly needs more room, and make it a scale step.

## Buttons

- Horizontal padding about 1.5 to 2 times vertical. A button with 8 px by 16 px or 10 px by 20 px reads as a button; 4 px by 8 px reads as a cramped link.
- Total height at least about 40 px for pointer use, 44 px or more for touch.
- Icon-plus-label buttons: gap of 6 to 8 px between them; less padding on the icon side if it looks optically heavier.
- Button groups: gap of 8 to 12 px; the destructive or secondary button does not touch the primary.
- Pair actions at the end of a form or dialog with a clear gap from the last field, usually the "between groups" step.

## Inputs and labels

- Label to field: tight (4 to 8 px). Field to next label: wider (16 to 24 px). The gap between the field and its help or error text matches the label gap.
- Input padding: about 10 to 12 px vertical, 12 to 14 px horizontal, so that the text does not hug the border.
- Group related fields (first name and last name, street and city) closer than unrelated ones.

## Lists and rows

- Row padding in lists follows the density mode: roomier when comfortable, tighter when compact, with the ratio between within and between kept. Table rows follow the data-tables skill (if installed).
- Leading icon or avatar to text: 12 px or so. Trailing action to edge: same inset as the leading side.
- A row with an action button needs a gap between the text block and the button so the two do not merge.

## Tables

- Cell padding and row height for tables belong to the data-tables skill (if installed); otherwise choose them from the density steps and keep horizontal padding larger than vertical.
- Right-aligned numbers need room on their right so they do not touch the next column's text.
- The header row gets slightly more space or a rule below it, not a box around it.

## Cards

- One padding step on all sides. Title to body: small step. Body to actions: medium step.
- Gap between cards equal to or larger than the padding, unless the cards share one surface.
- A card's media bleeds to the card's edge or sits inside the padding, never half and half.

## Navigation bars and toolbars

- Item gap in the same family as the padding of an item (items 8 to 12 px apart, padding 8 to 16 px).
- Group related items closer than the gap between groups (logo, primary links, utilities).
- Bar height from the line height plus two vertical padding steps; keep it consistent across breakpoints.

## Dialogs and popovers

- Padding at the larger end of card padding (20 to 32 px).
- Title to body: small to medium step. Body to the button row: medium to large step.
- Buttons align to one edge, usually the end edge, with the primary closest to it or per platform convention.

## Touch spacing

- Targets about 44 px or larger on touch screens (or an equivalent hit area that exceeds the visible mark).
- At least about 8 px between neighboring targets, more for destructive actions.
- Adjacent small icon buttons are the usual offender; either enlarge the hit area or add a gap.
- Dense pointer-only tools can use smaller targets, with the gap kept so that near-misses do not trigger the wrong control.
