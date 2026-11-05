Going only on your description, the page is built around the wrong job. Shoppers on a hardware category page are narrowing 1,800 near-identical items down to the right one, and the layout does little to help with that. Everything below is a hypothesis. I haven't seen the page or your analytics.

## What's wrong

1. **The banner uses prime space on a message that isn't category-specific.**
   - 180px of dark band plus a paragraph pushes the first product row toward or below the fold on a laptop.
   - The delivery promise is the same on every page, so it's reassurance. It isn't the category's content.

2. **The filter sidebar outweighs the products.**
   - 14 groups, all expanded, about four screens long: the rail is bigger than the thing it filters.
   - The groups that matter most for fixings (type, size, material or finish, stock) sit among rarely used ones like brand and rating, so nothing says which ones to use first.

3. **Cards carry too little information.**
   - Hardware is the case where name and price aren't enough. "M6 hex bolt" at six sizes, two materials and several pack quantities looks identical in a grid of small squares.
   - At 6 across, minus the sidebar, each card is roughly 170px wide. The photos are too small to tell parts apart, so shoppers have to open each product to compare.

4. **The grid has no toolbar.** There's no result count, sort control, or visible active filters. Once someone filters, they can't see what's applied or remove it.

5. **24 per page is too few for this catalog.** At 6 across that's only four rows, so shoppers hit pagination constantly. It also forces a page load for every few items.

6. **On mobile the filters come before the products.** Stacking the sidebar above the grid means about four screens of filters before the first product. The stacked source order puts the secondary content first.

## What I'd change

**Header**
- Cut it to a slim title row of roughly 56–72px. It holds breadcrumb, category name and result count, not a hero.
- Move the delivery promise into one line, either a thin strip under the site header or a note beside the title. Don't give it a paragraph per page.
- On top-level categories, show subcategories as a row of links or tiles, since that's the fastest way to narrow hardware.

**Filter rail**
- Fix the width at about 16–18rem and make it sticky, with its own scroll.
- Open only the 4–5 groups that do the most work for that category, such as type, size or dimension, material or finish, and availability. Collapse the rest, and show a count next to each collapsed group when something inside it is active.
- Long option lists (sizes, brands) get a short visible list, "show more", and a search box in the group.
- Check your filter usage data to decide which groups open by default.

**Grid**
- Set a minimum cell width of about 220–240px and let the column count follow. That gives 3–4 across next to the rail at 1440.
- Use one image ratio for every card. Product shots on white are whole-image content, so show them with `contain` and no cropping.
- Use one content order in every card: image, name (allow 2–3 lines), a key-spec line (size, material, pack quantity), price (per-unit price if you have it), then a stock or delivery cue. Reserve room for the longest product name.
- Add a toolbar above the grid with the result count, sort control, and removable chips for active filters.

**Paging**
- Show 48 per page. It divides evenly into 2, 3, 4 and 6 columns, so the last row never sits half empty.
- Add a "Showing 48 of 312" line with a "load more" button or numbered pages. If you load more in place, keep the URL in sync so the back button returns to the same spot.
- Design the zero-result state: tell shoppers which filter caused it and give a one-click way to clear it.

**Phone**
- Order the page as slim header, a sticky "Filter & sort" bar, then products. The filters open in a full-screen sheet, with the groups collapsed and an "Show 37 results" button at the bottom.
- Use a 2-column grid and keep the same card content order, with the spec line shortened if it has to be.

## Order of work
1. Mobile filter sheet and the banner cut. These are the biggest structural fixes and the cheapest.
2. The toolbar and filter chips, then the rail's default-open groups.
3. Card content and grid density, then page size.

To confirm this is the cause, check scroll depth to the first product, filter usage by group, and the mobile versus desktop conversion gap before and after launch.
