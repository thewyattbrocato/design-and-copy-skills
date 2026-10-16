On a narrow screen, drop the table and show each order as a stacked card. Add a search box at the top, because a rep on a call is looking for one order, not browsing.

**Top of the screen**
- A sticky search field that matches order number, customer name, and tracking number. It stays pinned while the list scrolls.
- Below it, a row of status chips (All, Processing, Shipped, Delivered, Problem) that scroll horizontally. Horizontal scroll is fine for a small chip row, though not for the data itself.

**Each order card, top to bottom**
1. **Line 1:** the order number in bold on the left and the status badge on the right. The badge uses color and a word, never color alone.
2. **Line 2:** the customer name, at a slightly larger size, since that's usually what the rep is matching against the caller.
3. **Line 3:** the date placed and the total, e.g. "Oct 9 · $84.20". This is secondary text in a muted color.
4. **Line 4:** the ship method and the tracking number. The tracking number is a tappable link to the carrier's page, with a small copy icon beside it. If there's no tracking yet, it reads "Not shipped yet" in muted text, not a blank space.
5. **Line 5:** the items text, cut to one line with an ellipsis. It's the least useful field for identifying an order, so it gets the least space.

Each card is one full-width block of about 5 short lines. Cards are separated by spacing and a thin border, with no horizontal scrolling at any point.

**Tapping a card**
It expands in place, or opens a detail screen, showing the full items text and all fields as label/value pairs. A rep who needs the whole order gets it there, and the list stays scannable.

**Sorting and ordering**
- Newest first by default, with no column headers to tap.
- If sorting matters, put one "Sort: Newest ▾" dropdown next to the search box.

**Why this design**
- Customer, status, and tracking number are what a rep reads out to a caller, so they're visible without tapping.
- Order number is the identifier the customer is most likely to give, so it leads each card.
- Total, date, and ship method are for confirming details, so they sit in the middle at lower emphasis.
- Items is long and variable, so it's truncated.

**Implementation**
- Use a CSS breakpoint around 640px. Above it, keep the table exactly as dispatchers have it. Below it, render the card layout.
- Both layouts can use the same data and component logic. Only the markup and CSS differ.
- Make tap targets at least 44px tall, and keep body text at 16px or larger so it's readable without zooming.

**Two things to check with your reps**
- Do they search by phone number or email? If so, add those to the search.
- Do they need to act on an order (resend a confirmation, flag an issue), or only look? If they act, the detail view needs buttons. If they only look, keep it read-only.
