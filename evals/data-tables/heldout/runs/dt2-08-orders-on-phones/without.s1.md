On a narrow screen (roughly under 640px), I'd turn each table row into a stacked card. There'd be no sideways scrolling and no column headers. Big monitors keep the current table.

**Top of the screen**
- A sticky search box that matches order number, customer name, and tracking number. This is how a rep finds an order mid-call.
- Under it, a row of status chips (All, Processing, Shipped, Delivered, and so on) that can scroll sideways, since a short chip row is a normal swipe pattern.
- Newest orders come first.

**Each card, top to bottom**
1. **Order number** in bold on the left, and the **status** as a colored badge on the right. These are the two things a rep scans for first.
2. **Customer name** on its own line, in slightly larger text, because it's what they're matching against the caller.
3. **Items text**, clamped to two lines with an ellipsis.
4. A single muted line with the secondary facts: `Oct 12 · $84.20 · Ground`. That covers date placed, total, and ship method.
5. **Tracking number** at the bottom in a monospace font, with a copy button. Tapping the number opens the carrier's tracking page. Reps often need to read it out or paste it into a message. If the order hasn't shipped, it shows "Not shipped yet" in gray rather than a blank.

**Details**
- Every field from the table is on the card, so nothing is lost. You may not need a detail view, but if you add one, tapping a card could open the full item list.
- Cards are separated by spacing or a divider, with at least 44px touch targets for the badge, copy button, and tracking link.
- Long lists use "Load more" or infinite scroll, not tiny pagination controls.

**Implementation**
- Switch at a breakpoint of about 640px with a CSS media query.
- You can restyle the existing rows with `display: block` or grid and put each cell's label in a `data-label` attribute. Or render a separate card component on mobile. The second approach is cleaner if the card order differs from the column order, which it does here.

If you tell me the stack (React, plain HTML, and so on), I can write it.
