I'd go with **cards**, built as a responsive list. Here's why.

**Why cards fit this data**
- Each shift is a small bundle of 4 fields, and people scan for "which one fits me?" That means date first, then role and location, then whether there's room. A card lets you give each of those a clear place.
- 14 items is short enough that you don't need pagination or dense scanning, so you don't need a table's compactness.
- On a phone, a card is a natural tap target. If you add a "Sign up" button, it has an obvious home.

**Why not the others**
- **Table:** Four columns can technically squeeze onto a phone, but location and role strings wrap awkwardly, and you end up with horizontal scrolling or tiny text. Collapsing a table into stacked rows on mobile is basically building cards anyway, just with more CSS work.
- **Simple list:** Works, but with four attributes per row it's hard to give hierarchy without effectively making a card. It's a fine fallback if you want minimal markup.

**How I'd build it**
- Use a single `<ul>` of `<li>` cards, so it stays semantic and accessible.
- Single column on phones, and a 2–3 column grid on wider screens (`grid-template-columns: repeat(auto-fill, minmax(260px, 1fr))`).
- Card hierarchy: **date** as the heading (the primary sort key), **role** as the next line, **location** as secondary text, and **spots left** as a badge.
- Make the spots badge say more than a number: "3 spots left", with a distinct "Full" or "Only 1 left" state. Don't rely on color alone.
- Sort by date, and if dates repeat, consider grouping under date headers.

**When I'd change my mind**
- If users need to compare or sort/filter across many shifts (say 50+), or this is an admin view, use a table.
- If it's a quick, read-only listing with no actions, a plain list is less work and perfectly fine.

If you tell me the stack (plain HTML, React, etc.), I can sketch the markup and CSS.
