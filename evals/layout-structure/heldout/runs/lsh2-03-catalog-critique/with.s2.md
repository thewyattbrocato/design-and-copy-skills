# What's wrong with the structure

This is a catalog page: people compare many similar items and narrow them down. Most of your problems come from the layout working against that.

## Problems

1. **The banner pushes the products off the first screen.** 180px of banner plus the site header leaves little room for products on a laptop. The delivery paragraph is also reading material sitting in a place where shoppers want to browse. They've already chosen a category, so it tells them nothing new.

2. **14 filter groups, all expanded, make a four-screen sidebar.** Shoppers have to scroll past filters to reach anything, and the grid is only visible next to the first few groups. Fixings are filtered by a few things that matter a lot (type, size, material, finish, pack quantity, stock) and many that matter rarely. Treating all 14 as equal buries the useful ones.

3. **Six across with small square photos is too dense for this product type.** At 1440 with a sidebar, each card is roughly 190px wide. For hardware, the decision depends on specifics like size, pack quantity, material and stock. Those are what shoppers compare, and a photo of a bolt tells them very little. Name and price alone force a click into each product page to find out whether it's the right one. I expect this is the biggest conversion cost.

4. **24 per page with plain pagination is the wrong size for 1,800 SKUs.** 24 is four rows at six across, so it's a very short page, and filtering is hard work when you can't compare many items. A fixings shopper often checks several near-identical products. Every page change loses their place.

5. **On mobile the sidebar is stacked above the grid.** A phone shopper has to scroll through all 14 filter groups before seeing a single product. This is probably your worst page on mobile. Mobile is likely a large share of traffic, so the damage is large.

6. **There is no sort control, no result count, and no active-filter summary.** You didn't list them, so I'm assuming they're missing. Check this, because if they are, shoppers can't see what's applied or how many results remain.

## What I'd change

**Top of page**
- Cut the banner to a slim header strip of about 60–80px: category name, result count, and sort. Move the delivery promise to a single line near the header or to a site-wide strip. It can also go below the grid.
- Put sort and result count above the grid, aligned with the grid's left edge.
- Add a row of removable chips for active filters.

**Filters**
- Keep the sidebar at about 15–18rem, sized to the filter labels.
- Open only the 3–4 most-used groups by default. Collapse the rest, ordered by how often people use them.
- Long option lists (size, thread) get a scroll area or a "show more" link, with counts beside each option.
- Make the sidebar sticky with its own scroll so it stays reachable while the grid scrolls.
- Check your analytics to see which filters get used, and let that decide the order and the defaults.

**Grid**
- Go to 3–4 across at 1440 with the sidebar, so each card is about 250–300px wide.
- Add the specs shoppers use to compare: size or spec line, pack quantity, stock or delivery status, and price per unit where packs differ.
- Keep one photo ratio across the whole grid, and keep the same order of content in every card.
- Put a quick-add or quantity control on the card, since hardware is often bought in multiples and re-bought.
- Consider a list view toggle. For fixings, a compact list or table with spec columns is often what trade buyers want.

**Pagination**
- Raise the page size to about 48, or use "Load more" with a count ("Showing 48 of 312"). Keep the URL in sync so Back returns to the same place.
- Avoid infinite scroll, because it strands the footer and loses position.

**Mobile**
- Hide the filters behind a **Filter** button, opening a full-screen or bottom sheet with a "Show 214 results" apply button. Put **Filter** and **Sort** in a sticky bar.
- Show products two across, with fewer spec lines per card, and have the first screen show products rather than controls.
- Keep the active-filter chips visible above the grid.

## Priority order

If you can only do some of it, I'd start with these, since they have the best chance of recovering conversions:

1. Mobile filters behind a button.
2. Richer cards (specs, stock, pack size) at 3–4 across.
3. Collapse the filter groups and slim the banner.
4. Raise the page size.

Since this went live last week, compare device split and filter usage before and after the change. If the drop is mostly on mobile, item 1 explains most of it.
