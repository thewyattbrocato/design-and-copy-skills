**Why it feels boxed in**

- **Borders everywhere create visual noise.** Every card edge is a line competing for attention, so nothing is the focal point. The eye has to parse the boundaries before reading the content.
- **Uniform containers flatten hierarchy.** If every section gets the same border and padding, a minor note and a primary section look equally important.
- **Padding is trapped inside the box.** 16px inside a card, plus the gap between cards, makes the whitespace feel fragmented instead of flowing. Containers also mean nesting (card in card in page), which multiplies edges.
- **Borders say "separate," not "related."** A bordered box is a strong, closed shape. You use it for things that are truly distinct objects, so using it for everything over-segments the page.

**Other ways to show grouping (roughly from lightest to heaviest)**

1. **Proximity.** Put related items close together and separate groups with larger gaps. For example, 8px between items in a group and 32–48px between groups. This is the strongest grouping cue and costs nothing.
2. **Whitespace plus headings.** A clear section heading with generous space above it and tighter space below it ties the heading to its content.
3. **Alignment.** A shared left edge or consistent column makes items read as a set.
4. **Subtle background tint.** A faint fill (e.g. a 2–4% gray) groups without drawing an outline. It's softer than a border and works well for a few key areas.
5. **Dividers instead of boxes.** A single hairline between sections, or between rows in a list, groups by separation rather than enclosure.
6. **Shadow or elevation.** Use sparingly, only for things that are interactive or float above the page (menus, modals, draggable cards).
7. **A left accent bar or color.** A thin colored rule or a small label chip can mark membership without enclosing anything.
8. **Typography.** Size, weight, and color differences (a muted label, a bold title) create groups and hierarchy without any shapes.

**Practical approach**

- Start with no containers. Use spacing and headings, and add a container only where the grouping is still unclear.
- Reserve bordered cards for items that are actual discrete objects (a product, a record, something clickable or draggable).
- If you keep cards, drop the border and use a light background tint, or keep a border and remove the padding-heavy look by increasing the gap between cards.
- Avoid nesting containers. If a card holds a bordered table or another card, remove one of the layers.
- Vary emphasis: make one or two sections prominent and let the rest sit quietly on the page background.

If you share your markup or a screenshot, I can suggest specific CSS changes.
