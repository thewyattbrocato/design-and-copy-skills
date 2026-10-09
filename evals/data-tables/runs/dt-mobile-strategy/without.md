**Use a card list.** Support staff look up one order at a time, so each order should read as a single self-contained unit.

- **Card header:** order number, status, and total. Those are what staff scan for first.
- **Card body:** customer and placed-on date.
- **Expandable detail:** items, subtotal, tax, and shipping. Show them on tap, or as a small label/value list.
- **Search and filter:** put a search box on order number or customer at the top, since lookup is the main task.

Horizontal scroll fails here because the order number is pinned to the left. Staff would lose it while reading the totals on the right. Hiding columns fails because support will need the hidden ones, especially tax and shipping, when answering billing questions.

Keep the full table on desktop and switch to cards below roughly 640px. Render both from the same data so they can't drift apart.
