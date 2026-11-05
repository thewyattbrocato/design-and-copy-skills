**Short version:** the page spends its prime space on things that don't help someone choose a product, and it squeezes the thing they came to compare. People on a category page are comparing peers and narrowing them down. The layout should push them to the products fast and give each product enough information to judge.

## What's wrong

1. **The banner pushes the products down.** 180px of dark band plus a paragraph of delivery copy sits above everything. On a 1440×800 viewport, the sidebar and grid both start low. The delivery promise is useful, but it's the same on every category, so it's not what the category page is for. A shopper arriving from search or an ad needs to see products first.

2. **The sidebar is a wall.** 14 groups, all expanded, about four screens tall. The top few groups are visible, and the rest is scroll-past clutter. Most of these groups will be used rarely. Hardware filters like thread size, material, or head type only matter in specific categories, and applying them is the real task. A long sidebar also leaves the grid sitting beside empty space once the sidebar scrolls out of view, or makes the sidebar fight the grid for attention.

3. **The cards are too thin for fixings.** A small square photo, a name, and a price don't let someone tell an M6 × 40 zinc bolt from an M6 × 50 stainless one. For this product type, the differentiators (size, material, pack quantity, stock or delivery) are the content. With nothing else on the card, people must open each product, and that's a likely source of lost conversions.

4. **Six across at 1440 makes the cards tiny and the grid hard to scan.** With a sidebar taking roughly 260px, six cells leave about 170–180px each. Photos are small, names will wrap or truncate, and there's no room to add useful card content. You've traded information per item for items per row.

5. **24 per page with numbered pagination is hard work at 1,800 SKUs.** Categories will run to many pages. Pagination is fine, but 24 is low, and there's no sort control or result count, so people can't orient themselves or re-order.

6. **Mobile stacks the sidebar above the grid.** On a phone, a four-screen filter list means the first product is several screens down, or never reached. This is almost certainly your worst-performing breakpoint, and probably much of the conversion drop.

7. **There's no sort, result count, or active-filter row.** Nothing tells people how many products they're looking at, what's applied, or how to clear it. Also unplanned: the zero-results state after stacking filters.

## What I'd change

**Top of page**
- Cut the banner to a compact heading row: category name, result count, and a one-line description. Move the delivery promise to a slim strip or the site header, so it's seen without costing 180px.
- Under it, one toolbar row: sort, active-filter chips with "clear all", and a view toggle if you want one.
- Optional: if the category has obvious sub-categories (say, Screws → Wood / Machine / Self-tapping), show them as a single row of links above the grid. That's often a faster filter than any sidebar group.

**Filters**
- Keep a left rail, about 16–18rem, sticky, scrolling independently of the page.
- Open only the 3–4 groups that matter for that category (usually type, size, material, price or availability), and collapse the rest. Order groups by use, not alphabetically. Drive this from category data, since "thread pitch" is irrelevant under adhesives.
- Show counts per option, and cap long option lists with a "show more" link or a search box inside the group (size lists get long fast).
- Put the selected options in the chips row so people don't have to reopen groups to see what's on.

**Grid and cards**
- Go to 4 across at 1440 with the rail, and let it wrap by minimum card width (roughly 220–240px) rather than fixed column counts. That gives 3 on a laptop, 2 on a tablet.
- Keep one image ratio and one content order in every card. Add what distinguishes fixings: key spec line (size, material, finish), pack quantity or price per unit, stock or delivery status, and an add-to-basket or quantity control if people often reorder. The longest product name should wrap cleanly in two or three lines without breaking the card heights.
- Consider a list view toggle for trade buyers, who compare specs more than photos. It's the same data in a full-width row with more columns.

**Pagination**
- Raise the page size to 48 (or use "Load more" with a visible count, e.g. "Showing 48 of 312"), keep the toolbar's sort and count at the top, and repeat pagination at the bottom. Check that back-navigation from a product returns people to the same page, scroll position, and filters, because that's a common leak.

**Phone**
- Products first. Put one "Filter & sort" button in a sticky bar; it opens a full-screen sheet with the groups collapsed, and an "Apply (N results)" button at the bottom.
- 2 columns for cards, with a shortened spec line. Chips for active filters appear under the sticky bar.
- Banner shrinks to the title and result count. The delivery copy goes to a single line.

**Empty and worst cases to plan for**
- Zero results: say which filter removed everything and offer a one-click remove.
- One result and 300 results should both look intentional.
- Longest product name, translated or enlarged text, and a filter option list of 60 sizes.

## If you can only do three things

1. Shrink the banner so products start in the first screen.
2. Collapse the filters to a few relevant groups, and on phones move them behind a button.
3. Add spec, pack size, and stock to each card, and drop to 4 across so there's room for them.

I'd also check your analytics before and after: scroll depth on mobile, filter usage per group, and whether product-page entry rate dropped (suggesting cards don't give enough to click) or whether clicks held up but add-to-basket fell (suggesting the problem is on the product page, not the listing). That tells you which of these to do first.
