**Ship B.**

**Relationships in the tile:** the title and level label form one unit (the heading block). The blurb is the body. The Start button is the action, and it should sit apart from the content above it.

**A:** Every gap is 16px, so nothing groups. The title, level, blurb and button all read as equally related, and the tile looks like four stacked items. The padding is also the same size as the gaps, so the edges don't read as a boundary.

**B:** The gaps follow the relationships.
- **Title to level (4px):** these read as one heading unit.
- **Level to blurb (12px):** a step out, so the heading block is distinct from the description.
- **Blurb to button (24px):** the biggest gap, so the action is separate from the content.
- **Padding (20px):** larger than the inner gaps, so the content sits clearly inside the tile.

The gaps step outward (4, 12, 24), with each gap sized to what it separates.

**Small fixes to B before shipping:**
- **Snap to a scale.** 4, 12, 20 and 24 all sit on a 4px base, so this is fine. Just keep to those steps elsewhere.
- **Let the parent own the gaps.** Use `display: flex; flex-direction: column` on `.tile` with per-child spacing. Margins on the last child can otherwise add extra space at the bottom. The simplest change is to drop `margin-bottom` from `.start` (it already has none) and make sure the blurb's 24px is the only space above the button.
- **Check the tap target.** 40px is fine for pointer use. If this is used on mobile, go to 44px or more.

If you have several tiles in a grid, keep the gap between tiles at least as large as the 20px padding so they don't blur together.
