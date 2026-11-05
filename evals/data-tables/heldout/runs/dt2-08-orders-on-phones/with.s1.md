On a phone, show each order as a stacked card instead of a table row. Dispatchers keep the table on big monitors.

Reps look up one order at a time while a customer is on the line. That isn't a comparison task, so sideways scrolling is the wrong fix. Eight columns can't fit in 360px without making numbers wrap or the text tiny.

**What a rep sees for each order (about 5 lines):**

```
#10482                          ● Shipped
Maria Alvarez
2× desk lamp, 1× shade set
Placed Oct 27 · Total $184.20
Tracking 1Z999AA10123456784  [Copy]
Ground (UPS)
```

- **Top line:** the order number in bold on the left, and the status as a word on the right, with a small shape and color as extra cues. Never use a colored dot alone.
- **Customer:** on its own line, at body size. This is usually what the rep is matching against the caller.
- **Items:** the short text, allowed to wrap to two lines. It is the one column that wraps.
- **Date and total:** one line, labeled "Placed" and "Total". The currency is stated once, and the date includes the year if it isn't this year.
- **Tracking:** labeled, on one line, and never wrapped or cut off. Add a copy button of about 44px, because reps will paste it to the customer or the carrier site.
- **Ship method:** a quiet line below tracking.
- **Missing tracking:** show "Tracking —  Not shipped yet". Don't leave it blank.

All eight fields stay visible, so nothing is hidden behind a tap. Every value keeps its label, and the order matches the desktop columns.

**Finding the order (this matters more than the card layout):**
- Put a sticky search box at the top. It should match order number, customer name, and tracking number, since callers give any of the three.
- Add a status filter next to it, and sort newest first by default.
- When nothing matches, show "No orders match 'xyz'" with a Clear button.

**Build notes:**
- Switch at roughly 720px. Below that, render a separate list of cards, each a description list. Above it, render the real `<table>`. This avoids the screen-reader problems of restyling table cells into blocks.
- Keep the same data and the same order in both views.
- Keep the card text at 14px or larger.

I can sketch the HTML and CSS for both views if you share the current component.
