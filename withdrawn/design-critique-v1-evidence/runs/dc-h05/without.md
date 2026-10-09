The card has no visual hierarchy. Every line is 15px in the same blue, so nothing tells your eye where to start.

- **Three bold lines look identical.** The operator, the times and the route all have the same size, weight and color. The times (the most decision-relevant part) read the same as the company name. The route is arguably the headline, yet it's third.
- **Pricing is a flat run of text.** "Foot passenger $18 - Bicycle $6 - Car $64" is a lighter weight, but the prices don't stand out from their labels. You have to read the line to compare options, and the hyphens as separators make it denser.
- **The urgency line doesn't signal urgency.** "Only 4 seats left at this price" is styled like a footnote. It's also ambiguous. It's unclear which of the three prices it refers to.
- **"Select" doesn't look like a button.** It's a `span` with a thin outline, the same color as the text and the same size. It reads as a tag or label more than the card's main action. It's also not a `button` or `a`, so it has no keyboard or screen-reader affordance.
- **It's all one color.** Blue text, a blue border and a pale blue background leave no accent. Nothing is emphasized, and the action isn't differentiated.
- **Small details add to the unfinished feel.** The font is `Helvetica` with no fallback. Spacing is uneven: only the button row gets a margin, so the lines are packed together while the button floats off by itself. The trip duration (1h 25m) is left for the reader to work out.

The common thread is that the card presents data without ranking it. Size, weight, color and spacing should say what matters first (route and times), what's secondary (operator) and what's the action (Select). Here they all say the same thing.
