Here's the full updated file. I kept the `#num` and `#room` IDs, and your update script doesn't need any changes. A `MutationObserver` watches those two elements and plays a short "new call" animation whenever their text changes.

[...]

What changed, and why:

[...]

- **Look:** There's a soft gradient background, a rounded "now serving" panel with depth, and a faint glow on the number. The upcoming cards fade in one after another when the page loads.
- **Alive:** A pulsing green dot sits next to "NOW SERVING". A clock shows in the corner, which also makes it obvious the screen hasn't frozen.
- **New call:** The number and room pop in and a light sweep crosses the panel. That catches people's eye when the call changes. It plays only on a change, so nothing is moving constantly while people read.
- **Readability:** I didn't use any cycling or scrolling text, and the contrast is the same or slightly higher than before. Numbers use tabular figures so digits don't shift width. Animations switch off if the TV or browser has "reduce motion" enabled.

[...]
