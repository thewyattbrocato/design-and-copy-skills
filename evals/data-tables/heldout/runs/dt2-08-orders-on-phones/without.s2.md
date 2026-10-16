On a phone, I'd replace the table with a stack of cards, one per order, and nothing would scroll sideways. Above roughly 640px wide, dispatchers keep the table as it is.

**Each card, top to bottom**

1. **Order number** in bold on the left and a **colored status badge** (Shipped, Delayed, and so on) on the right. A rep should be able to read a card's state at a glance.
2. **Customer name** on its own line, in a large font. This is usually what the rep is matching against the caller.
3. **Items text**, cut off at two lines with an ellipsis. Tapping the card opens the full text.
4. **A small gray line** with ship method and date placed, such as `UPS Ground · Placed Oct 12`. The **total** sits right-aligned on the same line.
5. **Tracking number** on its own line, in a monospace font. Tapping it opens the carrier's tracking page, and a small copy icon beside it copies the number. If there isn't one yet, it reads "No tracking yet" in gray, so a rep can tell it's missing and not that the screen failed to load.

**Above the cards**

- A **search box pinned to the top** that matches order number, customer name, and tracking number. Reps start from whatever the caller reads out, so this matters more than anything else on the phone.
- Below it, a row of **status filter chips** (All, Processing, Shipped, Delayed, Delivered). It scrolls sideways if it overflows, which is fine for a chip row.

**Why these choices**

- The fields reps need on a call (order number, customer, status, tracking) get the most visual weight.
- Date and ship method are secondary. Total is useful for confirming an order with a caller but rarely what they search by.
- Showing every field on every card keeps the phone view complete. Reps never have to wonder whether a column got dropped.

**Left out on purpose**

- Hiding columns behind an expand toggle. It would save space, but reps would have to tap on every order, and tracking is the thing they need most.
- Column sorting on the phone. Search and filter chips cover how reps look things up, and sort controls would take up screen space.

If you tell me the framework (React, plain CSS, and so on), I can write it. For this layout the table and cards can share the same data, with CSS or a breakpoint hook deciding which one renders.
