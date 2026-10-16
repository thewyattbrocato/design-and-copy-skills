**Why it feels boxed in**

1. **Borders everywhere create visual noise.** Every card edge is a line the eye has to process. With many cards, the page becomes a grid of competing rectangles, and nothing stands out as more important.
2. **Uniform containers flatten hierarchy.** If every section gets the same border and padding, everything looks equally weighted. Nesting (a card inside a card, or a bordered table or input inside a bordered card) makes it worse.
3. **16px padding is tight for a container.** Content sits close to a hard edge, so it feels cramped. Bordered boxes usually need more inner padding (20–32px) than the same content would need without a border.
4. **Borders separate when you want to group.** A border says "this is a distinct thing, walled off from the rest." If the sections are related parts of one page, the walls work against that.
5. **Gaps between cards are often too small** relative to the padding inside. If the space between cards is about the same as the space inside them, the grouping reads poorly.

**Other ways to show items belong together**

- **Proximity (whitespace).** This is the strongest cue. Put related items close together and separate groups with noticeably more space. A common pattern is 8–12px between items in a group and 32–48px between groups.
- **Headings and typographic hierarchy.** A clear section title with a muted subtitle often does the work a box was doing.
- **Subtle background tint.** A faint fill (e.g. `#f7f7f8`) with no border and a small radius groups items softly. Use it for the one or two areas that need emphasis, not for every section.
- **Soft elevation.** A very light shadow (`0 1px 2px rgba(0,0,0,.06)`) instead of a border feels lighter. Don't combine shadow and border.
- **Dividers.** A single hairline between rows or sections, or a divider list inside one container, groups items without enclosing each one.
- **Alignment.** A shared left edge, consistent column widths, and a consistent grid imply relationships without any drawn lines.
- **A left accent rule.** A 2–3px colored line on the left suits callouts and quotes.
- **Shared color or icon treatment.** Items with the same accent color or icon style read as a set.

**A practical approach**

1. Remove all the borders and see how the page reads with only spacing and headings.
2. Add structure back only where grouping is still unclear, starting with whitespace, then dividers, then a tint.
3. Keep full cards for things that are actually self-contained objects, like a product, a pricing plan, or a draggable item.
4. If you keep cards, increase the padding, soften the border color (e.g. a light gray rather than a mid-gray), and make the gap between cards larger than the padding inside them.

If you share the markup or a screenshot, I can suggest specific CSS changes.
