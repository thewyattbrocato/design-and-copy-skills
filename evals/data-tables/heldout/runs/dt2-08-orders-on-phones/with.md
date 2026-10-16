On a narrow screen, replace the table with a stack of order cards, one per order, and keep the real table for wide screens. Reps look up one order at a time and don't compare rows, so a card works better than a table here. A frozen first column plus sideways scroll would still leave them hunting.

## What a rep sees on a phone (below roughly 640px)

**At the top:** a search box that stays pinned. It matches order number, customer name and tracking number, because a rep usually has one of those from the caller. Orders are sorted newest first. There is no sort control, since the search does that job.

**Each order is a card with four lines:**

```
#48213                      ● Shipped
Dana Whitfield
2 × Trail jacket (blue, M), wool socks…
Placed Oct 12            Total $184.20
UPS Ground
Tracking 1Z999AA10123456784        [Copy]
```

- **Line 1:** the order number in bold on the left, with the status as a word and a small shape on the right. Color is only a third cue.
- **Line 2:** the customer name, at normal body size.
- **Line 3:** the items text, wrapped and clamped to two lines. Tapping the card shows the full text. It helps a rep confirm "the blue jacket?" with the caller.
- **Line 4:** the placed date on the left and the total on the right. The total is in tabular figures with the same decimals on every card, and the currency appears once in its label.
- **Line 5:** the ship method, then the tracking number. The number sits on one line and is never truncated. It's a long code, so allow it to break rather than scroll sideways. A Copy button (about 44px tall) sits beside it, and it links to the carrier page if you have that.
- **No tracking yet:** show "Tracking — not shipped yet" instead of leaving it blank.

All eight fields stay visible, and each value keeps a small label (Placed, Total, Tracking), so nothing is hidden behind a tap. Text is 14px or larger, and cards are separated by a hairline or space, not boxes inside boxes. That gives about three or four orders per screen.

## What a dispatcher sees

At wider widths nothing changes. They keep the full table.

## Implementation notes

- Don't restyle the `<table>` with `display: block`, because that can strip table semantics in some browsers. Render the cards as a separate list, with a description list (`dl`) inside each card, and show one structure or the other by breakpoint.
- Keep the field order in the cards the same as in the table. Give the wide table a `<caption>`, `th scope`, and visible sort buttons with `aria-sort` on the active column.
- Design the no-results state ("No orders match 'whitfeld'", with a Clear search button), plus loading placeholder cards and an error state with a retry.

I haven't seen your code, so I can sketch the HTML and CSS if you tell me the framework.
