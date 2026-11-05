On a phone, show each order as a two-line row with the five fields a rep needs to recognize it, and put the rest behind a tap. Nothing scrolls sideways.

**What a rep sees in the collapsed row (about 360px wide)**

- **Line 1:** the order number in bold on the left, and the status as a word with a small icon on the right (for example "Shipped" or "Processing"). Color is only a third cue.
- **Line 2:** the customer name, which wraps if it's long, and the date placed, such as "Oct 24".
- Rows are at least 48px tall with 14px or larger text, and a hairline between them.
- A search box stays pinned above the list. It matches order number, customer, and tracking number. When a customer calls, typing a name or order number is faster than scrolling, so this is the biggest fix.
- Orders are newest first.

**What they see after tapping a row**

The row expands in place and shows the other four fields as label and value pairs:

- **Items:** the full text, wrapping as needed.
- **Ship method**
- **Total:** right-aligned with tabular figures, and the currency named in the label.
- **Tracking number:** on its own line with a "Copy" button and a link to the carrier's page. If there's no tracking number yet, it shows "— Not shipped yet", never a blank.

Several rows can be open at once. Opening one doesn't collapse the others, so a rep can compare a customer's two orders. Open rows stay open if the data refreshes.

**Why this split**

This is a lookup task: the rep scans for the right order, then reads one or two details from it.

- Order number, customer, date, and status identify the order and answer "where is it?" at a glance.
- Items, ship method, total, and tracking are details you read after you've found it.
- Tracking is probably what reps want most often. If so, swap it with date placed so it's visible without a tap. Your call counts here, since I'm guessing at their call patterns.

**What I'd avoid**

- Shrinking the table until text wraps.
- Stacking all eight fields on every row. That's about eight lines per order, so you'd see two orders per screen.
- Truncating the customer name or order number.

**Implementation notes**

- Keep the real `<table>` markup and restyle it below roughly 640px. Dispatchers on big monitors keep the full table unchanged.
- Make the expand control a real button with `aria-expanded`, so it works with keyboard and screen readers.

I can build this as a CSS and markup change if you point me at the order screen's code. This directory doesn't have it.
