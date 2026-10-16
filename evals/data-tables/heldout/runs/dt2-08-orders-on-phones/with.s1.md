**On a phone, stop showing a table. Show one card per order, stacked down the screen, with no sideways scrolling.** Reps are looking up one customer's order, not comparing orders. Eight columns can't fit in 360px, and a frozen first column with sideways scrolling would still hide most of what they need.

**What each order looks like (about 360px wide):**

```
#48213                      [Shipped]
Dana Whitfield
3 items: Oak shelf, brackets, screws
─────────────────────────────────────
Tracking   1Z999AA10123456784
Ship via   Ground
Placed     Oct 12, 2026
Total      $184.50
```

- **Top line:** order number on the left in bold, status on the right as a word (Shipped, Backordered, Cancelled). A small icon or shape can go with it, but color shouldn't be the only cue.
- **Second line:** customer name, in regular body text. Reps usually find the order by the caller's name or order number, so these two lead.
- **Third line:** the items text, wrapped to at most two lines. If it's longer, cut it with an ellipsis and let the rep tap the card to see the full text.
- **Below the divider:** four labeled pairs, in this order: tracking number, ship method, date placed, total. Tracking comes first because "where's my package?" is the most common call. Labels sit on the left and values on the right. The total is right-aligned, in tabular figures, with the currency stated once.
- **Tracking number:** it never wraps. It's a tap-to-copy or tap-to-open-carrier link, and the tap target is about 44px tall. If an order hasn't shipped, show "—", not a blank.
- **Text size:** 14px or larger throughout. Cards are separated by a hairline or some space, not by heavy boxes.

**Finding the right order**
- A search box is pinned at the top: order number, customer name or tracking number. This matters more than anything else on the screen. Without it, reps are just scrolling a long list of cards.
- A sort control sits next to the search box, defaulting to newest first. Quick filter chips for status ("Shipped", "Not shipped") are optional.

**What stays the same**
- Dispatchers keep the full table on wide screens. Switch layouts at about 700px.
- Both layouts use the same data, and the fields are in the same order, so reps and dispatchers see the same thing.

**Build notes**
- Keep the real `<table>` for wide screens. For phones, render a separate list where each order is a description list (label and value pairs), and show one layout or the other with CSS. Restyling table cells into blocks can strip their table semantics in some browsers, and a separate list avoids that.
- Don't use `display: none` to drop columns, because screen-reader users lose that data too.

I haven't seen your code, so I can't say how this fits your components. If you point me to the table component, I can build the phone layout.
