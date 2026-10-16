Your layout puts the browsing tools and the products below a lot of content that doesn't help someone find a product. Here are the structural problems, most damaging first, and what I'd change.

## What's wrong

**1. Products start below the fold.**
A 180px banner plus site header, with a paragraph of delivery copy in it, means the first product row sits low or off-screen on many laptops. On a category page, the products are the page. The delivery promise is useful reassurance, but it doesn't belong in the most valuable space on the page.

**2. The sidebar is too long to use.**
14 expanded groups is about four screens of filters. Shoppers will never see most of them, and the ones they need (size, material, finish) may be buried. It also makes the sidebar far taller than the grid beside it, which looks broken and pushes the footer down.

**3. Mobile is likely where the biggest loss is.**
Stacking the sidebar above the grid means a phone user scrolls through four screens of filters before seeing a single product. Many will leave before they get there. This is probably your worst-performing view.

**4. The cards don't carry enough information for hardware.**
Hardware buyers choose on specs: size, thread, material, pack quantity, finish. A small square photo, a name and a price can't answer "is this the M8 × 40 or the M8 × 60?" Many of your 1,800 SKUs probably look near-identical in photos. 6 across at 1440 makes the photos small and leaves no room to add detail. The cards also don't say whether an item is in stock or how it's sold (pack of 50 vs. single), which are common purchase blockers.

**5. 24 per page with classic pagination is too few for 1,800 SKUs.**
Hardware shoppers compare many near-identical items. At 24 per page, a category can run to many pages, and each page click is a chance to drop off. Pagination also loses the shopper's place when they go to a product and come back.

**6. There's no sorting, result count or active-filter display.**
You didn't mention these, so I'm assuming they're missing. If they are, add them. Shoppers need to see "142 products", the filters they've applied, and a way to clear them.

## What I'd change

**Header area**
- Cut the banner to a slim title row: category name, result count, sort control. About 60–80px.
- Move the delivery promise to a one-line strip (e.g. "Free next-day delivery over £X") in the site header or just under it. Keep the full paragraph for the cart and product pages, where it supports a purchase decision.

**Filters (desktop)**
- Keep the left sidebar, but make it a sticky, independently scrolling column.
- Expand only the 3–5 groups that matter most for that category (Brand, Size, Material, Price, perhaps Availability). Collapse the rest. Order them by how often shoppers use them, which you can get from analytics.
- Show counts next to each option, and long lists with a "show more" link and a search box where needed.
- Show active filters as removable chips above the grid, with a "clear all" link.
- Consider making the set of filters category-specific. A screws page doesn't need the filters that apply to hinges.

**Filters (mobile)**
- Replace the stacked sidebar with a "Filter & sort" button, ideally sticky at the top as the user scrolls. It opens a full-screen drawer with the groups collapsed, and an "Show 142 results" button at the bottom to apply them.
- Products should be visible immediately under the title row.

**Grid and cards**
- Go to 4 across at 1440 (3 on tablet, 2 on phone). Larger photos help, and the extra width lets the card hold more.
- Add to each card: key spec line (e.g. "M8 × 40mm, A2 stainless, pack of 50"), stock status, and a price that says what it's for (per pack or per unit). A quick "add to basket" with a quantity field is worth testing, since hardware buyers often reorder.
- Where products are variants of one item (same screw, different lengths), consider grouping them into one card with a size selector, or offer a compact list view. That could cut the visible SKU count a lot.
- A grid/list toggle suits trade customers who scan specs.

**Pagination**
- Raise the page size to 48 (or 36 for 4-across so rows fill evenly).
- Use a "Load more" button with the count ("Showing 48 of 312") rather than infinite scroll, which makes the footer unreachable. Make sure the browser back button returns the shopper to the same position and filters, and keep the URL updated with the filter state.

## Order I'd do it in
1. Shrink the banner and fix mobile filtering. These are the biggest wins and the least work.
2. Collapse the filter groups by default and add active-filter chips.
3. Rework the cards and column count.
4. Change the pagination.

Since you launched last week, compare mobile and desktop conversion, and check scroll depth and filter usage if you have them. That will tell you whether mobile or the cards are costing you more, and which filter groups to keep open. If you can share the previous layout's numbers, I can help work out which of these changes is most likely to matter.
