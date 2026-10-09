**Why it feels boxed in**

1. **Every section gets the same container.** When everything has a border, nothing stands out. The eye sees a grid of equal rectangles, not a hierarchy, and the borders compete with your content.
2. **Borders add visual noise.** Each card has four edges, and every edge draws attention. Several cards on a page mean a lot of lines to look past.
3. **16px of padding is tight for a container.** The border sits close to the text, so the content looks held in. Padding also doesn't change with the size of the section, so large and small sections get the same squeeze.
4. **The gaps between cards are probably about as small as the padding.** If the gap is 16px or less, the cards blur into one mass of boxes. The space inside a group and the space between groups need to be clearly different.
5. **Boxes mean "this is an object."** A card tells the reader that it's a discrete thing they can open, select or act on. Using it for ordinary sections makes everything look like a separate item and hides the real structure of the page.

**Other ways to show items belong together**

Try these in order and stop at the first one that works.

1. **Space (try this first).** Keep items in a group close together and put roughly twice that distance between groups. For example, use 8px between related items and 32px between sections. Proximity is the strongest grouping signal, and it costs no ink.
2. **Headings and alignment.** A heading that sits closer to the content below it than to the section above it ties the group together. A shared left edge reinforces that.
3. **A hairline rule.** Use a thin, quiet divider when space isn't enough, such as in dense lists or tables. Keep one weight and one color, and leave space on both sides of the line.
4. **A tinted region.** A subtle background fill suits a cluster of controls that has to read as a unit, like a filter panel, a toolbar or a sticky footer. Use the fill instead of a border.
5. **A card, only for real objects.** Use one when the item is something users open, select, drag or compare, or when it must stand apart from a busy background. Give every such object the same single surface.

**Quick fixes for what you have now**

- Remove the borders from ordinary sections and let headings and whitespace do the grouping.
- If you keep a card, use one of border, shadow or fill, not all three. Don't nest cards inside cards.
- Make the gap between groups at least as big as the padding inside them, or bigger.
- Let the parent container set the spacing (for example with CSS `gap`) rather than a `margin-bottom` on every child. That avoids a doubled gap after the last item.
- To check the result, squint at the page. You should see only the groups you intended.

If you share the markup or CSS, I can suggest specific changes.
