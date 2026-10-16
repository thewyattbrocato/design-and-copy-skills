On a phone, I'd replace the table with a stacked list of order cards, one per order, with a search box pinned above it. Dispatchers keep the full table on big screens. Your reps look up one customer's order at a time and read it across, so sideways scrolling is the wrong fix. Stacking suits that job, and nothing needs to scroll horizontally.

**What a rep sees, top to bottom**

1. **Search field, pinned at the top.** It's labeled "Search order #, customer, or tracking #". Most calls start with a name or an order number, so a rep should type that and not scroll. The list sits below it, newest orders first.
2. **One card per order, about four lines, full width.**
   - **Line 1:** the order number in bold on the left, and the status as a word on the right ("Shipped", "Delayed", "Processing"), with a small icon and color as extra cues. Never color alone.
   - **Line 2:** the customer name.
   - **Line 3:** the items text, cut to one line with an ellipsis. Tapping the card shows the full text.
   - **Line 4:** "Placed Oct 12 · $84.20". The date and total are on one line, and the total uses tabular figures. The currency goes in the label, not repeated.
   - **Line 5:** the ship method and tracking number, such as "UPS Ground · 1Z999AA10123456784". The tracking number is a tappable link to the carrier page, with a copy button next to it, because reps will paste it to the customer. If the order hasn't shipped, this line shows "— Not shipped yet", not a blank.
3. **Every value keeps its label.** The date and total can share a line, but each is tagged ("Placed", "Total"). The same eight fields appear in the same order as in the desktop table.

Tapping a card opens a detail view with the full item list. The cards can stay short because everything is still reachable.

**Why this and not the alternatives**
- **Horizontal scroll with a frozen order-number column** is the right call for comparing many numeric columns. Your reps don't compare. They find one order and read the answer, so scrolling would keep the problem you have now.
- **Hiding columns** would drop tracking number or ship method, and those are what a customer on the phone usually asks about.

**Build notes**
- Render the stacked list as its own structure at narrow widths, with each card holding a description list. Show the real `<table>` (caption, `th scope`) at wide widths and swap between them with a breakpoint. This is safer for screen readers than restyling table cells into blocks.
- Make the tap targets, meaning the card, the tracking link and the copy button, at least 44px tall.
- Use 14px text or larger. Keep order numbers, dates and tracking numbers on a single line.
- Keep the search term and scroll position when a rep opens a detail view and goes back.
- Design the empty states too. "No orders match 'Smith'" should have a clear-search button, and the list should show placeholder cards while it loads.

If you share the component or markup, I can sketch the CSS and breakpoint swap.
