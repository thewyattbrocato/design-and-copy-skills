# Grouping devices

Load this when you decide how to show that items belong together: space, a rule, a tint, or a card.

## Order of preference

Try the lightest device first and move down only when it fails.

| Device | Use when | Cost |
| --- | --- | --- |
| Space and alignment | Items can be moved closer or farther apart | Almost none |
| Heading | A group needs a name | One more text style to keep consistent |
| Hairline rule | Many tight items need scan lines, or unlike items must touch | Adds visual noise as lines multiply |
| Tinted region | A cluster must read as one unit and cannot be moved | Competes for attention; needs padding |
| Card (border or shadow, plus padding) | The content is a discrete object | Heavy; repeated cards dominate the page |

When two cues disagree, a shared region or connecting line beats nearness, and nearness beats similarity of look. That is why a box can rescue a cluster you cannot move, and why a box around every group is noise.

## What counts as a real object

A card earns its surface when the whole thing can be treated as one thing:

- it can be opened, selected, dragged, reordered, compared, or deleted as a unit;
- it has its own actions and could move to another page whole;
- it must stand apart from a busy or textured background;
- it represents something in the user's data (a task, a product, a contact, a ticket).

A card does not earn its surface when it only wraps a heading and a paragraph, or when the page would read the same without the box. A section of a settings page, a block of marketing copy, and a list of benefits are groups, not objects.

## Nested surfaces

- Do not put a bordered surface inside another bordered surface. Flatten: keep the outer container and drop the inner borders, or drop the outer one and let the inner items sit on the page.
- If the inner items are true objects, they may be cards on a plain section with no outer card. If the outer is a true object (a panel with its own header and actions), the inner content is grouped by space and subtle rules.
- Use one edge treatment per surface. Pick border or soft shadow or a fill that differs from the ground; two of the three are rarely needed and all three look heavy.
- If cards must share a surface (a board column, a result list), keep the card style quiet and the gaps between cards about as large as their padding.

## Lists

- Short list of rich items (a few lines each): space between items. Cards only if each item is an object.
- Long list of uniform rows (notifications, files, transactions): hairline dividers or subtle alternating shading, or space alone when rows are tall enough. Keep row gaps consistent.
- Dividers should not touch other lines. Inset them to the text edge when the rows have icons or avatars, or run them full width when rows are plain.
- Last row: no divider after it, and no extra bottom space.

## Tinted regions

Make the tint a small step from the ground. Pad the region so the content has about the same inset on all sides. Keep the region count low; three tinted bands on one screen start to read as stripes.

## Repeated sets

Three or six identical boxes with an icon in a circle usually stand in for a plain list or a few columns. Ask what the user will do with each item. If the answer is "read it", use space, a heading and one line per item, and align the items to a shared edge. If the answer is "choose one" or "open one", cards are justified.

## Checks

- Remove the borders in your head; do the groups survive? If yes, the borders were doing nothing.
- Count nested surfaces. Zero is the usual answer.
- Compare surfaces of the same kind; they should share radius, edge, and padding.
