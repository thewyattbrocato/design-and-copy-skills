**The page is organized around what you want to say, not around what a shopper does there.** A shopper on a hardware category page is comparing near-identical items (e.g. M6 vs M8, zinc vs stainless, pack of 50 vs 100) and narrowing 1,800 SKUs down. Almost every structural choice works against that.

## What's wrong

**1. The banner spends the first screen on the wrong thing.**
- At 180px plus the site header, products start roughly 300px down. On a 768–900px laptop screen, that's a third of the view before any product shows.
- A paragraph about delivery isn't what the category page is for. The shopper already knows what category they clicked.

**2. The sidebar is a wall of 14 expanded groups, about 4 screens long.**
- Most people never reach groups 6–14. The groups that matter most for fixings (type, size, material, finish) are mixed in with rarely used ones.
- It makes the page feel like a form to fill in, not a catalogue.
- Because it's a left rail, the filter column is also visible beside the grid at the same time. The user can't see what their filter choices are doing. There's no sign of active filters or a result count.

**3. Six across at 1440 with small square photos and only name + price is too thin to compare.**
- Each cell is about 200px wide. That is cramped for a product name like "A2 Stainless Steel Countersunk Pozi Wood Screw 4.0 x 40mm".
- Fixings look almost identical in small photos, so the photo does little work. The things that tell products apart (size, material, pack quantity, price per unit, stock/delivery) are missing.
- Without those, people open many product pages to compare, or give up.

**4. 24 per page with pagination, on 1,800 SKUs, makes browsing slow.**
- With 6 across it's only 4 rows. That's a very short page for the effort of clicking through.
- Page-by-page navigation breaks comparison, because the item you wanted to compare against is now on another page.

**5. On mobile, the sidebar stacked above the grid is the worst failure.**
- The shopper has to scroll through four screens of filters before seeing a single product. That alone could explain much of the drop if mobile is a big share of your traffic.
- Check this first in your analytics.

**6. Missing from the structure entirely**: sort, result count, active-filter chips, a way to clear filters, and a zero-results state.

## What I'd change

**Top of page**
- Reduce the banner to a compact header: category name, result count, and maybe a one-line delivery note. Roughly 60–80px, not 180px plus a paragraph.
- If the delivery promise matters, put it in a slim strip in the site header or under the grid controls. Don't make it the headline of every category.
- Add subcategory links as a row of chips or tiles above the grid (e.g. Screws → Wood / Machine / Self-tapping). For a hardware catalogue this is often a better first filter than anything in the sidebar.

**Filters**
- Keep the left rail on desktop, at a fixed 15–18rem width. Do not make it wider.
- Order the groups by how much they narrow: type, size/dimension, material, finish, pack size, brand, then the rest.
- Open only the top 3–4 groups by default. Collapse the rest. Cap long lists (e.g. show 6 options, then "show more"), and give size groups a search box or range control.
- Make the rail sticky with its own scroll so it stays beside the grid.
- Add a bar above the grid with: result count, sort, and active-filter chips with a "clear all" control. This ties the rail to the grid.
- On a phone, collapse the rail behind a single **Filter** button (with a count of active filters), opening as a full-screen sheet with an "Show 143 results" button at the bottom. The grid comes first, with a sticky Sort / Filter bar.

**Grid**
- Drop to 4 across at 1440 (or 3 at narrower desktop widths), and let the count follow a minimum cell width, e.g. around 240px, rather than a fixed number. At 2 across on phones.
- Keep one image ratio and one content order in every cell. A 1:1 or 4:3 frame is fine, but bigger.
- Add to each card what distinguishes the product: key spec line (size, material, finish), pack quantity and price per unit, and stock/delivery status. Allow two lines for the name and plan for the longest title.
- Consider a compact list view toggle for trade buyers who compare specs. They often prefer rows with columns over cards.

**Paging**
- Raise page size to 48 or more, or use "load more" with a visible count ("Showing 48 of 312"). Keep URLs reflecting filters and page so back-button and sharing work.
- Put the paging control at the bottom, and keep filters and sort preserved when the user pages.

**Worst-case states to plan before styling**
- Zero results: say which filter caused it and offer to remove it.
- One result.
- A long product name.
- 1,800 items with no filters: this is where subcategory tiles do the work.

## How I'd prioritize

1. Fix mobile filters (button + sheet). Probably the largest effect, and cheapest.
2. Add spec/pack/stock lines to the cards, and cut to 4 across.
3. Collapse filters and reorder them; add the active-filter bar, sort, and count.
4. Shrink the banner and add subcategory navigation.
5. Raise page size or switch to load-more.

One caveat: I'm working from your description, not data. Check device split and where users exit (filter use, scroll depth, product-page click-through) before deciding the order. If most of your traffic is trade customers on desktop, steps 2 and 3 matter more than 1.
