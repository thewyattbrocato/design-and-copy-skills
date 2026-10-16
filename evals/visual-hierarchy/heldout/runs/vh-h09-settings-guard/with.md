The layout already works, so I wouldn't redesign anything. The order reads clearly: title, then section headings, then row names, then explanations. Teal is reserved for controls and the one primary action, and the page has no decoration. Here are the few things I'd change or specify, most important first.

1. **Set a max content width.** The brief doesn't give one. If rows stretch across a wide screen, the switch ends up far from its label, and the eye loses the row. Cap the content at about 640–720px, with the switch at the right edge of that column. The left-aligned Save button then lines up with the content, as you intend.

2. **Check that the Save button is visible.** It's the only primary action, but it sits at the bottom of three sections. On a short screen it could be below the fold, and people may toggle switches and leave without saving. Either make the footer sticky, or make sure the full page fits on common laptop heights. Also say whether switches apply instantly or only on Save. I'd keep Save, disabled until something changes.

3. **Handle "Reset to defaults" with care.** As a plain link beside the primary button, it has the right weight. But it's the one control that can wipe settings, so ask the developer to add a confirmation or an undo.

4. **Give the developer the contrast requirements.** You say "grey" in three places, and they are where this design usually fails.
   - The 14px description text needs at least 4.5:1 against white.
   - The off-state switch track needs at least 3:1 against white. A pale grey track makes the off state look disabled.
   - White text on the teal button needs at least 4.5:1. If the brand teal is light, use a darker shade for the button.

5. **Optional: widen the step between the section heading and the row name.** 18px semibold over 16px regular is a small size step, and the weight difference is doing most of the work. That's fine. But if the sections blur together in testing, put more space above each heading than below it, or make the heading 20px.

Leave these alone: the thin dividers between rows, the extra space between sections, the single teal button, and the absence of icons and cards.

I assumed the switch's position (knob left or right) shows on versus off, so the state doesn't depend on teal versus grey alone. If it doesn't, add that.
