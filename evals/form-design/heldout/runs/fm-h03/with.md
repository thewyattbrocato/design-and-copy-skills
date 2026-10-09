I'd go with the third proposal, with one tweak: use a stepper for travelers and radio cards for room type.

**Room type: radio cards (or plain radios).**
- Three options is well inside the 2–7 range where people compare choices, so they should all be visible. A select hides them behind a click.
- Room types differ in price and what they include. Put that in each card, for example "Deluxe: king bed, city view, +$40/night". Cards can carry that detail and a bare dropdown can't.
- Make the whole card the click target. Give the group a visible label, "Room type".
- Preselect Standard only if most people keep it. Otherwise leave it unselected and make them choose.
- If you have no price or feature detail to show, plain radios are just as good. The cards are only worth it when there's something to compare.

**Number of travelers: stepper with a typed field beside it.**
- The values are 1–8, which is a quantity. A stepper is quick for small changes, and you can reach any value in at most seven taps.
- Set the minimum to 1 and the maximum to 8. Disable the − and + buttons at those limits.
- Keep a typed numeric field next to the buttons. It should have a visible label, 16px or larger text and a numeric keypad.
- Give the buttons targets of about 44px. Give them accessible names such as "Decrease travelers".
- If someone types 9, say "Enter a number from 1 to 8" at the field, and don't clear their input.
- Eight radios in a row is clunky, especially on a phone. Radios also imply the options are things to compare, and the numbers aren't.

**Why I'd reject the other two:**
- **Select for both:** this hides options that are few enough to show. A select also can't hold the price and feature detail that makes room type a real decision.
- **Radios for both:** this works for room type but is clumsy for 1–8.

**Caveats:**
- If your design system already has a select, radio or stepper component, use it and don't build new ones.
- If some rooms can't sleep 8 people, tie the two fields together. For example, show a clear message when the traveler count exceeds what a room type holds. Ask travelers first, because it affects eligibility and price.
