The page makes shoppers work to see products, and then gives them too little information on each product to decide. I'd fix it in this order.

## 1. Too much before the first product
- **The 180px banner with a paragraph is the wrong content in the most valuable space.** On a typical laptop viewport, the header plus banner leaves little room for products above the fold. The delivery promise belongs sitewide, in a slim strip under the header or in the header itself. Category pages need a compact H1, a result count, and breadcrumbs. Put any category copy below the grid.
- **Add subcategory navigation if the category is broad.** With 1,800 SKUs, "Fasteners" or "Fixings" shouldn't dump straight into a grid. Show a row of subcategory links (Bolts, Screws, Anchors) above or at the top of the sidebar.

## 2. The sidebar
- **Fourteen expanded groups is a wall.** Four screens of filters mean the filters scroll away from the results they control.
  - Expand only the 3–5 that matter most for that category, and collapse the rest.
  - Make the sidebar sticky with its own scroll.
  - Cap long lists (such as brand) at 5–6 options with "show more".
  - Show counts per option and hide options that would return zero results.
- **Choose filters per category, not globally.** Fixings are bought by spec. Thread size, length, material, head type, and finish matter for screws and bolts, and they're meaningless for other categories. The top filters should differ by category.
- **Add applied-filter chips above the grid.** Each chip needs a remove "x" and there should be a "Clear all". Right now there's no visible state once someone has filtered.
- **Add a sort control and a results count** at the top of the grid. Neither is in your description, and both are standard.

## 3. The grid and cards
- **Six across is too dense once the sidebar takes its share.** At 1440 wide, with a roughly 260px sidebar, each card is about 180px wide. That's too small to judge a product photo or read a name. Go to 4 across at 1440, 3 at around 1100, and 2 on phones.
- **Name and price isn't enough for hardware.** Many of your products look nearly identical (an M6×30 bolt next to an M6×40). Each card should add:
  - a key spec line (size, material, pack quantity)
  - price with its unit basis ("£4.20 / pack of 50", or per unit)
  - a stock or delivery indicator
  - a rating, if you have reviews
  - an add-to-cart button with a quantity field. Trade and repeat buyers will buy straight from the listing if you let them.
- **Consider a list/table view toggle.** Buyers who know what they need often compare specs and pack sizes faster in rows than in cards.

## 4. Pagination
- **24 per page at 6 across is only 4 rows,** which is about 75 pages at full catalogue size. Show 48 per page, or use a "Load more" button with a "Showing 48 of 612" count. Make sure back-navigation restores the scroll position and loaded state. I'd avoid true infinite scroll because it breaks back-button behaviour and hides the footer.
- Also show the page controls at the top, or make them sticky.

## 5. Mobile
This is probably your worst problem. Stacking the sidebar above the grid means a phone user scrolls through about four screens of filters before seeing a single product.
- Hide filters behind a sticky **Filter & Sort** bar.
- The button opens a full-screen drawer or bottom sheet with the collapsible groups, a live "Show 212 results" button, and a "Clear all".
- Show applied chips in a horizontal scroll row under the bar.
- Use a 2-column grid, and collapse the banner to a one-line title.

## What to do first
I can't tell from here which of these is costing you the most, so check your analytics before building everything. Compare conversion by device, scroll depth to the first product, and how often filters are used and abandoned. My guess is that mobile filter stacking and the card information gap account for most of the drop, and the banner and sidebar length are close behind. If I'm right, the fastest wins are:
1. the mobile filter drawer
2. a slimmer banner
3. collapsed filter groups
4. richer, larger cards

I can sketch a wireframe or write out the card and filter spec per category if that would help.
