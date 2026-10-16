## What's wrong

**1. On mobile, shoppers see no products for several screens.** Stacking 14 expanded filter groups above the grid is probably your biggest conversion problem. After the banner, a phone user scrolls through about four screens of checkboxes before the first product. Most will leave or use the search box instead.

**2. Desktop has the same problem, to a lesser degree.** The banner (180px) plus the site header means products start around 300px down, so the first row is barely above the fold. The delivery paragraph is also the lowest-value content on the page for someone who is browsing. It's a trust message, so it doesn't need a hero.

**3. The filter sidebar has no hierarchy.** Fourteen groups at equal weight means the useful ones (type, size, material or finish, pack quantity, in stock) are buried among rarely used ones. Expanded by default, it pushes the filters people need out of view. It also only works well if the sidebar scrolls with the user, which a four-screen sidebar makes awkward.

**4. The cards are too small and carry too little.** With a sidebar of about 260px, six columns leaves each card roughly 170px wide. A square photo that size can't show a thread, head type or finish. Hardware SKUs also look alike. "Hex bolt M8" at £4.20 could be a box of 10 or a box of 200, zinc or stainless, and in stock or not. A name and a price can't answer those questions, so people have to click into each product to compare. There's also no add-to-cart or quantity control, which hurts repeat trade buyers most.

**5. 24 per page is too few for 1,800 SKUs.** At six across that's four rows per page, and about 75 pages across the catalogue. People who are comparing hit the pagination quickly.

**6. Things you didn't mention that I'd check for.** Is there a sort control, a result count, and removable chips showing the active filters? Do category pages lead with subcategory links? For a catalogue this size, "Bolts → Hex / Carriage / Coach" navigation often matters more than filters.

## What I'd change

**Header:** Reduce the banner to a compact title row of about 60–80px with the category name and result count. Move the delivery promise to a one-line strip under the site header, or into the product cards. Put subcategory links or chips right under the title.

**Filters, desktop:**
- Keep the sidebar at about 240px and sticky, scrolling independently.
- Expand only the top 4–5 groups, ordered by actual usage. The rest are collapsed or behind "Show more filters".
- Show an active-filter chip row above the grid.

**Filters, mobile:**
- Remove the stacked sidebar. Put a sticky "Filter & Sort" bar above the grid, with the grid starting immediately below it.
- The bar opens a full-screen drawer with the groups collapsed. The apply button should read "Show 142 results" so people see the effect.
- The grid should be 2 columns.

**Grid and cards:**
- Use 4 columns at 1440 (5 at most). That gives roughly 250px cards and photos large enough to read.
- Add to each card:
  - A one-line key spec, such as size, material or finish.
  - Pack size and price per unit.
  - A stock or delivery badge.
  - A quantity field and Add button, or at least a quick-add.
- Keep the layout consistent. Give names a fixed two-line height so rows don't jump.

**Pagination:**
- Show 36 or 48 per page (a multiple of your column count), or use "Load more" with a page counter.
- Keep filter and page state in the URL, and restore scroll position when someone returns from a product page.
- Add a visible sort control: price, best-selling, in stock first.

## Priority order

1. The mobile filter drawer and grid-first order.
2. Richer cards (spec, pack size, stock, add to cart).
3. Shrinking the banner.
4. Filter ordering and default-collapsed groups.
5. Per-page count and pagination.

I'm working from your description, not your analytics. To confirm the diagnosis, split the conversion drop by device. If mobile fell much more than desktop, item 1 is the main cause. Also check filter usage by group and scroll depth on category pages. The filter usage data tells you which five groups to keep open.
