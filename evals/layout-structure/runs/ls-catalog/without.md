# Kettle & Co. Catalog Page Layout

## Desktop (≥1024px, content max-width 1280px, centered)

**Regions, top to bottom:**
1. **Header** (full width, 72px): logo, search, cart.
2. **Title bar** (full width): "Cookware" heading, result count ("200 products"), and the sort dropdown aligned right.
3. **Main body**, two columns:
   - **Filter sidebar**, 260px fixed, sticky. Collapsible groups: Category, Price range, Material, Brand, Color, In stock. An "Active filters" chip row and "Clear all" sit at its top.
   - **Product grid**, the remaining ~960px, four columns with 24px gutters. Show 24 items per page, with numbered pagination below.
4. **Compare tray**: a bar fixed to the bottom, hidden until an item is selected. It holds three slots (filled thumbnails or empty placeholders) and a "Compare" button, which is disabled until two items are chosen.

## Phone (<640px)

- **Header**: 56px, with logo, search icon, and cart.
- **Toolbar**, sticky under the header: two equal-width buttons, "Filter" (with an active-count badge) and "Sort". Both open bottom sheets. The filter sheet has an "Apply (N results)" button.
- **Grid**: two columns, full width, 12px gutters. A "Load more" button replaces pagination.
- **Compare tray**: a compact bar showing "2 of 3 selected" and a Compare button. A fourth selection is blocked with a short message.

## Product cell (same order on both)

1. Image, square, with a sale or new badge at the top-left corner and a compare checkbox at the top-right.
2. Product name, limited to two lines.
3. Material or size, one short line.
4. Star rating and review count.
5. Price, with the original price struck through if the item is on sale.
6. "Add to cart" button. On desktop it is full width and visible on hover and focus. On phone it is always visible.

## No results

The grid area shows an illustration and the heading "No products match your filters." Below it are the active filter chips, each removable, and a primary "Clear all filters" button. Beneath those sit a few suggestions, such as widening the price range, plus a row of popular categories. The result count reads "0 products", and the sort control is disabled. On phone, the same content fills the space below the toolbar.
