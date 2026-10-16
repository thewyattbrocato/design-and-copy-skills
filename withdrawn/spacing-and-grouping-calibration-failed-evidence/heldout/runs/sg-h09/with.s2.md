**Ship B.**

**A** has the same 16px between every element. Title, level, blurb, and button all sit at equal distances, so nothing reads as a group. The title and level are one unit ("Spanish Basics, Beginner"), but A spaces them as if they were unrelated.

**B** spaces by relationship:
- **Title → level (4px):** these two read as one header unit.
- **Level → blurb (12px):** a medium step into the description.
- **Blurb → button (24px):** a clear break before the action, so the button stands apart as the next step.
- **Padding (20px):** a little more breathing room around the whole tile, and larger than any internal gap except the last, which is how it should be.

B's gaps get bigger as the things they separate get less related (4, 12, 24), and the within-group space is much smaller than the between-group space.

**Small tweaks to B:**
- **Snap to a scale.** If you use a 4px base, all of B's values (4, 12, 20, 24) already fit it.
- **Let the parent own the gaps.** Use `display: flex; flex-direction: column;` on `.tile` with the margins moved onto a few `gap` or wrapper rules. Otherwise the last element's bottom margin can add extra space at the bottom of the tile. Here the button is last and has no margin, so B is fine as written.
- **Check the tile gap.** In the grid, keep the space between tiles at least as large as the 20px padding, so neighboring tiles don't blur together.
