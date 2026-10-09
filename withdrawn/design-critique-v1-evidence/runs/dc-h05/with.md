**The card has no hierarchy.** Every row is 15px Helvetica in the same navy (#0b3d91), so nothing tells you where to look first. Squint at it and you see a block of blue text with nothing standing out.

**Why it feels off**

1. **Bold is the only differentiator, and it's applied to the wrong things (major).** The first three rows are bold: operator, times, route. The prices and the seat warning are regular weight, and the prices are what you decide on. The operator name gets the same weight as the departure time, and the times get the same weight as the route.
2. **The Select button doesn't read as a button (major).** It's a `<span>` with a 1px outline, no fill, and the same color and size as the text. It looks like a tag or a label. It's the one action on the card, and it has the least visual weight of anything on it. It's also not a real `<button>` or link, so there's no keyboard focus or semantics. That's a separate problem from the look.
3. **The key facts are buried (major).** The departure and arrival times are the core information, but they're set at body size. The prices are crammed into one line separated by hyphens ("Foot passenger $18 - Bicycle $6 - Car $64"), so you have to parse them instead of scanning. The hyphens also stand in for the en dash in "09:40 – 11:05" and for the word "to".
4. **The seat warning is invisible (minor).** "Only 4 seats left at this price" is plain navy body text. Its message is urgent, but it looks like a footnote. Worth checking that the claim is true. If it is, it should be visible. If it isn't, it shouldn't be there at all.
5. **Spacing is uniform (minor).** The rows have no margin between them except the 10px above the button. Nothing is grouped, so the operator, the trip, the prices and the action all run together as one stack. The card also has a gray border on a pale blue background, which makes it look flat and a bit generic.

**Contrast is not the problem.** I estimate #0b3d91 on #f4f9ff at roughly 9.5:1, well above WCAG AA. The text is easy to read, but it has no variation to guide the eye.

**What works**
- The single-hue navy on pale blue is coherent and suits a ferry brand.
- The content is the right set: times, route, fares, availability and one action.
- The 340px width and 16px padding are sensible.

**Limit:** this is static markup. I haven't seen how it looks with real content lengths or how it behaves in a list of cards.
