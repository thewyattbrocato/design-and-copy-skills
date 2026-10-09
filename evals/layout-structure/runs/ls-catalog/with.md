# Kettle & Co. catalog page layout

**Material:** about 200 comparable products, so a wrapping grid of equal cells. Worst cases are a long product name, zero results, and three items selected for comparison.

## Desktop (1280px and up)

- **Header:** full width. Its logo and the filter sidebar share the same left edge.
- **Filter sidebar:** 16rem fixed, sticky, scrolls independently. It holds category, material, price range, and capacity. Each option shows a result count, and options with zero results are disabled.
- **Results region:** takes the remaining width, about 930px at 1280px.
  - **Toolbar:** the result count ("84 products") sits left, active filter chips below it, and the sort dropdown right.
  - **Grid:** 3 columns at 1280px and 4 at 1440px and up, with a 24px gap. 24 products load per page, followed by "Showing 24 of 84" and a Load more button.
- **Compare tray:** hidden until the first selection, then a sticky bar along the bottom of the results region. It has three slots with thumbnails and a Compare button that activates at two items. At three items, the other cells' checkboxes disable with a "Compare is full" tooltip.

## Product cell (same order everywhere)

1. Image in one 1:1 ratio, with a Sale or New badge in the corner
2. Name, clamped to two lines
3. Descriptor line: material · size
4. Price
5. Rating and review count
6. "Compare" checkbox

The whole cell links to the product page. The checkbox is the only exception.

## Phone

- **Order:** header, then a sticky toolbar with Filter and Sort buttons, then the count and chips, the grid, and Load more.
- **Filters:** open as a full-height sheet with a pinned "Show 84 results" button. Sort opens as a small sheet.
- **Grid:** 2 columns, 16px side margins, 12px gap. The cell content and order are unchanged.
- **Compare tray:** a bottom bar with three thumbnail slots and a Compare button. Tapping it opens the comparison as a horizontally scrolling table with the product name column frozen.

## No results

The toolbar and sidebar stay in place. The grid area shows:

- "Nothing matches those filters."
- The active filters as removable chips.
- A primary **Clear all filters** button.
- A suggestion such as "Remove 'Copper' to see 12 products."
- A row of popular categories below.

On a phone this stacks in the same order, centered within the grid area. If the user had items in the compare tray, they stay there.
