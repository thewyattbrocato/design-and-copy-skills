**What's wrong**

The page gives every piece of information the same weight, so the one that matters most has nothing to separate it.

1. **The alert is the quietest thing on the card.** An out-of-range state changes one 28px number from one orange to a slightly darker orange, plus an 11px grey word. On a dark monitor or from across a room, that's almost invisible. Room 5 at 61% looked like every other card. The alert is a subtle color shift with no shape, position, or size change, so it fails the grayscale and squint tests.
2. **Everything is the same size and weight.** Eight identical cards, and within each card four identical 28px bold numbers. Days to harvest (a slow planning number) competes with humidity (an urgent one). With no ranking, the eye has no starting point, which is why it reads as flat.
3. **It shows state but not duration or target.** "61%" tells you nothing without the target band, and nothing about how long it has been wrong. Room 5 was off for six hours, and the page couldn't show that.

**What to change first**

Make out-of-range state a structural signal, not a color tint. For each card that's out of range:

- Give the card a visible border weight or a tinted header band (one cue, applied the same way every time).
- Replace the 11px "alert" with a readable line such as **"Humidity 61% · target 85–90% · 6h"**, at a size close to the labels.
- Add a status marker (a filled dot or triangle) so it survives in grayscale.

Then move alerted rooms to the top of the grid, or add a single summary line above it: "1 room out of range: Room 5, humidity, 6h." Sorting by problem severity is the fastest way to make the page answer "what needs attention right now" in a few seconds.

**Secondary changes, after that**

- Demote "days to harvest" to a smaller or lighter-value number so the live environmental readings lead.
- Show the target range on every metric so "in range" is visible on normal cards too, not only inferred from the absence of orange.

**Assumptions:** I'm working from your description, not the code. I'd also check whether 61% counts as out of range for your target band. If your band is 85–90%, the page should have caught it, which suggests the alert threshold may also be wrong. That's worth confirming before you redesign.
