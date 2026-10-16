**Ship B.**

The main reason is spacing hierarchy. A uses 16px between every element. That makes the title, level, blurb and button all look equally related, so the tile reads as a flat stack. B groups them:

- **Title and level:** the 4px gap under `h3` ties the title to the level line, which is the relationship you want. "Spanish – Beginner" reads as one unit.
- **Level and blurb:** 12px separates the metadata from the description without cutting them apart.
- **Blurb and button:** the 24px gap sets the call to action apart. The button gets its own space and is easier to find when scanning a grid of tiles.
- **Padding:** 20px gives the tile a bit more breathing room than A's 16px.

Two things to check before you ship:

1. **The 4px title gap** depends on your `h3` line-height. If it's tight (around 1.1), 4px may look cramped. Bump it to 6–8px if so.
2. **Uneven blurb lengths** can make buttons sit at different heights across a row. This applies to both versions. If the tiles are in a grid, make the tile a flex column and give `.start` `margin-top: auto` so the buttons line up.

Everything is on a 4px grid in both versions, and the button height is the same, so nothing else separates them. B wins on grouping.
