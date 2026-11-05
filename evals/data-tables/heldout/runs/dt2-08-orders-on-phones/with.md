**Recommendation: on a phone, show each order as a stacked card. Don't scroll the table sideways, and don't try to shrink it.**

Reps look up one customer's order at a time. They don't compare orders side by side. Eight columns can't fit in about 360px without scrolling, and scrolling is what's losing them the order now. A stacked list fits that job better than a scroll region or a squeezed table.

## What a rep sees on a phone

Each order is one block, about 4 lines tall, in this order:

```
#10482                    Shipped
Maria Alvarez

3 × Oak shelf, 1 × brackets…
Ground · Placed Oct 24, 2026

Total  $412.50
Tracking  1Z999AA10123456784  [Copy]
```

- **Top line:** the order number on the left, in bold, and the status on the right as a word, such as "Shipped" or "Delayed". Color can back the word up, but the word carries the meaning.
- **Second line:** the customer name. A rep usually has the name or the order number from the caller, so these two come first. They are the two things they search by.
- **Items:** one line of the short text, cut off with an ellipsis if it's long. Tapping the card opens the full text.
- **Ship method and date placed:** one quiet line. They matter, but rarely.
- **Total:** labeled, and right-aligned with the same decimals on every card.
- **Tracking number:** labeled, on one line, never wrapped, with a Copy button. Reps will want to read it to the customer or paste it into a carrier site. The button should be about 44px tall so it's easy to hit.
- **Missing values:** if there's no tracking number yet, show "— Not yet shipped" rather than a blank. That way the rep can tell "not shipped" from "the page didn't load."

Every value keeps its label, and the cards appear in the same order as the table rows.

## Add search above the list

Scrolling a list of cards isn't a good way to find one order. Put a sticky search box above the list that matches order number, customer name, and tracking number. Under it, add a few filter chips for status, such as Delayed and Shipped. This will help the rep more than any layout choice.

## Why not the other options

- **Sideways scroll with a frozen first column:** this suits comparison tables. Here it hides tracking number and status, the two fields reps need most, off-screen to the right.
- **Priority columns only:** this would work as a fallback. With 8 columns and nearly all of them useful on a call, though, you'd be hiding too much.
- **Shrinking the table:** the numbers and tracking IDs would wrap or become unreadable.

## Implementation notes

- **Keep the real `<table>` for wide screens.** Render a separate list for narrow screens, with each order as an item that has a label/value `<dl>`. Switch between them at about 640px. This avoids the screen-reader problems you get when you restyle table cells into blocks.
- **Show only one at a time.** Hide the other with `display: none` so the same data isn't read twice.
- **Keep text at 14px or larger.** Use 16px for the order number and total.
- **Dispatchers' view doesn't change.**

I can sketch the HTML and CSS for the card layout if you'd like. If you point me at your order screen's code, I can build it directly.
