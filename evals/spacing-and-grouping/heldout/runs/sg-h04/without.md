# Why it feels boxed in

Each bordered card adds a closed shape, and the eye reads every closed shape as a separate object. A few things make it worse:

- **Borders get equal weight everywhere.** When every section has the same outline, nothing is primary. The page becomes a grid of rectangles that compete with the content.
- **Nesting multiplies lines.** Inputs, tables, and buttons inside a card carry their own borders. The result is boxes inside boxes.
- **16px is tight.** The padding is the same as the typical gap between cards, so inside and outside spacing look alike. Grouping depends on inside spacing being clearly smaller than outside spacing.
- **Containment is the heaviest grouping signal.** Using it for every relationship leaves you nothing to emphasize with.

# Other ways to show items belong together

These are roughly ordered from lightest to heaviest.

1. **Proximity.** Put related items close together and separate groups with noticeably more space. For example, use 8px between items in a group and 32–48px between groups. This often does the job on its own.
2. **Alignment.** A shared left edge or a consistent column grid links items without any line.
3. **Headings and typography.** A section title with a small-caps label or a weight change defines a group. Body text and secondary text can differ in size or color.
4. **Whitespace as a gutter.** A wide margin between columns works like a divider.
5. **Subtle background tint.** A faint fill (for example, 2–4% darker than the page) with no border groups items softly. Use it for a few key areas, not every section.
6. **Hairline dividers.** A 1px low-contrast rule between sections, or between rows in a list, separates without enclosing. Leaving off the outer border opens up the layout.
7. **Shadows or elevation.** A soft shadow can replace a border where you want a card, though it's still a container.
8. **Accent edges.** A colored left rule or top border marks a group without enclosing it.
9. **Shared visual treatment.** Use the same icon style, color, or tag for items in a category.

# Practical recipe

- Drop borders on most sections and rely on spacing plus headings.
- Reserve cards, whether bordered or tinted, for things that are truly discrete and interactive. Examples are items in a grid, a modal, or something the user can click or drag.
- If you keep cards, raise the padding to 24px or more. Use a lighter border color, or swap the border for a faint background. Keep gaps between cards larger than the padding inside them.
- Avoid nesting containers. Inside a card, use dividers or spacing instead of more boxes.

If you share the page or its CSS, I can suggest specific changes.
