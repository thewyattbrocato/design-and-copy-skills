**Diagnosis.** This is a browsing and comparison page, and the structure works against that. Shoppers on a category page are narrowing 1,800 SKUs and comparing peers. Almost everything above the first product, and everything inside each card, is spent on something else.

## What's wrong

1. **The banner takes the first screen.** A 180px full-width banner plus the header leaves little or no product above the fold on a laptop. The delivery paragraph is sitewide reassurance, not category content. It pushes the products down on every category page.

2. **The filter sidebar is a second page.** Fourteen groups, all expanded, run to about four screens. Three things go wrong:
   - The groups that matter (type, size, material, finish, price) are buried among rarely used ones.
   - The sidebar is longer than the visible grid, so the two columns scroll out of step and the left column ends up mostly blank.
   - On a phone it's worse. The stacked sidebar sits above the grid, so shoppers scroll four screens of filters before they see a single product.

3. **Six across on 1440 makes the cards too small for the job.** Each cell is roughly 190–200px wide. Hardware is compared on detail (thread, length, pack size, finish), and the small square photo shows none of it.

4. **The cards hold name and price and nothing else.** For fixings, near-identical products differ in exactly the attributes you've left out: pack quantity, size or spec, stock and delivery status, and unit price. Shoppers can't compare from the grid, so they open product pages and bounce back. That drives both the lower conversion and the pogo-sticking.

5. **24 per page with plain pagination is too few across 1,800 SKUs.** That's 75 pages. At six across it's only four rows, so the shopper hits the pager almost immediately. There is also no sort control, no result count and no active-filter summary. You can't tell what you've applied or how many products are left.

6. **The phone layout has no mobile structure.** The content order is banner, filters, grid. The primary task is last.

## What I'd change

**Top of page**
- Cut the banner to a compact header: breadcrumb, category name, result count. Move the delivery promise to a one-line strip in the site header or under the sort bar.
- Add a row above the grid with sort on one side, the active filters as removable chips, and the count.
- If you have subcategories (say Screws → Wood, Machine, Self-tapping), show them as one row of links. They narrow the range faster than any filter.

**Filter rail**
- Keep a fixed-width rail of about 16–18rem on the left.
- Open only the 4–5 groups that apply to the category, and collapse the other nine.
- Order the groups by use, with size, type and material first.
- Add a "show more" inside long groups, with counts per option.
- Let the rail scroll or stick independently so it never outlasts the grid.
- Show the filters that change by category only where they apply, since a drill-bit size filter has no place on a hinge page.

**Grid**
- Use 3–4 columns on desktop, set by a minimum cell width of about 260–280px and letting the count follow, rather than fixing it at six.
- Use a 4:3 or square image ratio, the same in every cell.
- Give each card a fixed content order:
  1. Image.
  2. Name, with room for two lines.
  3. One line of key spec (size, material, pack of N).
  4. Price, with unit price if you sell in packs.
  5. Stock and delivery state.
  6. Quick add, if the product has no required options.
- Raise the page size to 48 or more, or use "Load more" with a visible count ("Showing 48 of 612"). If you keep pagination, repeat it above the grid.

**Phone**
- Order the page as header and count, then a sticky "Filter and sort" bar, then the grid.
- Open the filters as a full-screen sheet with an "Apply (N results)" button.
- Use 2 columns, with the spec line cut to one line and the quick add dropped.

## Worst cases to test
- The longest product name, such as "M8 × 120mm zinc-plated hex head coach bolt, pack of 50".
- A filter combination that returns zero results, which needs a message and a "clear filters" action.
- A category with 6 products, where the rail would be mostly empty.
- A category with 600 products.

If you can share analytics, I'd check the filter-open rate by group, the scroll depth on the sidebar, and the product-page bounce back to the category page. That would tell you which of the 14 groups earn their place, and it would confirm whether the thin cards are what's costing you conversions.
