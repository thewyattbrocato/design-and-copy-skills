The page puts a lot of weight above the products, hides the product detail shoppers compare on, and treats phones as an afterthought. Here are the problems, then what I'd change.

## What's wrong

1. **The banner pushes the products down.** At 180px, most of the first screen goes to a dark band with a delivery paragraph. A category page exists to get people to products. Delivery messaging is the same on every category, so it doesn't belong in a banner that repeats all over the site.

2. **The sidebar is a wall.** Fourteen filter groups, all expanded, make a column about four screens long. Nobody scrolls it to find "Thread size". The filters that matter (usually 3–5, such as type, size, material, and finish) sit among ones that rarely matter. The product grid beside it is much shorter than the sidebar, so the sidebar sets the page rhythm.

3. **The cards can't support a purchase decision.** Hardware and fixings are bought on specifications: M6 or M8, length, head type, pack size, stainless or zinc. A small square photo, a name, and a price give none of that. Many of your 1,800 SKUs will look near-identical in photos. Shoppers have to open each product page to compare, which hurts conversion.

4. **Six across on 1440px makes the cards small.** After the sidebar, each card is about 150–170px wide. The photo is too small to show a thread or head type, and the product names will truncate or wrap unevenly. Density here works against comparison.

5. **24 per page with pagination at the bottom is slow for 1,800 SKUs.** Narrowing the range is the main task, and paging through 75 pages is a poor way to do it. Pagination also sits beyond the long sidebar and grid, so people hit it with no sense of where they are.

6. **The phone layout is broken.** Stacking the sidebar above the grid puts four screens of filters between the banner and the first product. Source order is reading order on a phone, and here the products come last.

7. **Nothing helps people start.** There are no subcategory shortcuts, no result count, no sort control, and no applied-filter chips. These are the structural parts of a listing page.

## What I'd change

**Top of page**
- Cut the banner to a compact header: breadcrumb, category name, result count, and one line of intro. Move the delivery promise into a slim strip in the global header or a line under the sort bar.
- Add subcategory links when the category has children. For example, under "Screws" show Wood, Machine, Self-tapping, and so on. This is often the fastest route to the right product set.
- Put a **toolbar** above the grid with sort, result count, and a grid/list toggle. A list view suits spec-driven buying.

**Filters**
- Keep the left sidebar on desktop, but make it about 16–18rem wide and sticky, so it scrolls independently.
- Show only the top 4–5 groups expanded, chosen by category (for fixings: type, size/length, material, finish, pack size). Collapse the other nine by default.
- Show applied filters as removable chips above the grid, with a "clear all" link.
- Give long groups, such as size, a short list with "show more", and a search box if they run past about 8 values.

**Cards and grid**
- Go to **4 across at 1440px** (3 on tablet, 2 on phone). This gives a larger photo and room for text.
- Add to each card the 2–3 specs that distinguish SKUs in that category (size, material, pack quantity), plus stock or delivery status and a unit price where packs differ. Keep one image ratio and one content order on every card.
- Consider a quick-add or quantity control on the card. People buying fixings often know exactly what they need.

**Paging**
- Raise the page size to 48 (or use "load more" with a count, such as "Showing 48 of 312"). Keep a paged fallback for crawlability and for people who want to jump.
- Repeat the pager or load-more control at the bottom only. The toolbar already carries the count and sort.

**Phone**
- Replace the stacked sidebar with a **"Filter" button** in a sticky bar next to "Sort". It opens a full-height sheet with the groups collapsed and a "Show 126 results" button at the bottom.
- Make the order on the phone: compact header, subcategory chips, filter/sort bar, products. The first product should be visible without scrolling.
- Keep applied-filter chips in a horizontally scrolling row under the bar.

## Order of work
If you can only do a few things first, do these three: collapse the filters, add specs to the cards, and fix the phone filter pattern. They hit the most shoppers fastest. I'd also check your analytics for how many category-page visits come from mobile. If it's most of them, the phone fix may be the biggest cause of the drop.

I can sketch the desktop and phone layouts as wireframes, or write a spec for which specs and filters to show per category, if that would help.
