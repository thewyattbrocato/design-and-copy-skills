# Navigation, search, and lists you act on

Load when structuring navigation, adding search or filters, or letting people select, bulk edit, reorder or drag.

## Navigation

- Count the places. One main view with two or three panes, or two navigation areas plus content, is plenty. Many peer destinations, deep trees and drawers that hide primary functions make people hunt.
- Three to five visible primary destinations on a phone (a tab bar), a sidebar for larger or many-object tools, a top bar when there are few and the entry point must be clear. Drawers are for secondary destinations only, and their button carries a text label.
- Always show where you are: highlighted item, title, breadcrumbs for deep content. Landmarks stay in the same place.
- Prefer flat groups plus search over three-level hierarchies. Label by the person's words and outcomes ("Newest first", not "Descending").
- Back, Esc and closing a detail panel return to the same scroll position, filters and selection. Every view has a link that reopens it.
- For dense work tools add a command palette and shortcuts; show the shortcut next to the slow route so the slow route teaches it. Dangerous commands get no one-key shortcut.
- Show details beside the list (side panel) rather than a new page when people compare or triage.
- Pages and apps differ: content sites live on bookmarkable pages and findability; work apps behave more like a single workspace with few full reloads.

## Search, filter, sort

- On focus, before typing: recent and frequent searches. While typing: suggestions grouped by kind, tolerant of typos.
- Index what people remember (names, content, activity, dates), not only the title.
- Show active filters as removable chips and the result count; facets show counts so a choice never leads to zero.
- Zero results: say which filters caused it and offer one tap to relax them, plus a nearby suggestion.
- On phones, one "Refine" surface holding sort and filter together; update live when it is fast and keeps focus and scroll; use one Apply when results reload or the query is slow. Keep sort and filter across navigation and sessions; saved views for repeated sets.
- Infinite scroll suits feeds where old items fade. Use paging or a load-more with a position marker when people must compare, reach the end, use the footer or return to a place.

## Selecting and bulk actions

- Selection model: click selects one and replaces; a modifier (or a checkbox) adds; a range modifier extends. When the list scrolls or acts in bulk, show checkboxes, since they say "many" and survive scrolling. Selected rows differ by more than color.
- When something is selected, a bar appears with the count ("3 selected"), the actions, and a clear control. It names exactly what will change. Selection persists across refresh and paging, or says it does not ("12 on this page, select all 240").
- Bulk actions follow the recovery rules: do, then Undo; the toast says what happened to how many.
- Keep row actions visible or revealed on hover and on focus, in one place; never hover-only.
- Edit in place when the change is small and the context matters; one add row always present at the end of an editable list.
- Do not scroll text sideways. Wrap, or truncate with the full text on focus and hover and in the detail view.
- Table appearance, alignment and sorting display belong to `data-tables` if installed.

## Reorder and drag

- A visible handle, a lifted state, an insertion line, a highlighted drop target. Ignore a few pixels of drift before a drag starts, and auto-scroll near an edge after a short delay (starting values: about 3 px, about half a second).
- Escape cancels. Dropping in the wrong place is undoable.
- Give each drag a keyboard route (select, move up or down, or a "Move to" menu) and a touch route; announce the move to screen readers.
- Remember a manual order; make clear when a sort is overriding it.
