The layout already holds up. The order is clear: title, then section headings, then setting names, then explanations. Your restraint (no cards, shadows or icons, and teal only for state and the one action) is working, so I'd leave it alone. These are the things I'd change or confirm before handoff, in order of impact:

1. **Cap the content width.** The switch sits at the far right of each row, so on a wide screen the eye has to travel a long way from the setting name to its switch. This is the biggest risk with your layout. Constrain the content column to roughly 640–720px and left-align it. The Save button still shares the left edge.

2. **Settle when changes take effect.** Switches normally apply instantly, but this page has a Save button. Tell the developer that nothing applies until Save is pressed. Also say what happens if someone leaves with unsaved changes. If the page is long, make the Save row sticky at the bottom, or the primary action may sit below the fold.

3. **Make "Reset to defaults" look clickable without making it loud.** Teal is reserved, so use the body text color with an underline, or a medium weight. Leave a clear gap between it and Save so it isn't clicked by accident. Because it discards the user's settings, it should ask for confirmation or offer an undo.

4. **Don't let color be the only on/off cue.** The grey off-state track must still reach about 3:1 contrast against white. The knob position (left or right) should carry the state too, and the switch needs an accessible label tied to the setting name. The 14px grey explanations must also stay at 4.5:1 or better. Pale grey is the usual way this kind of page fails.

5. **Check the step from section heading to setting name (18px semibold to 16px regular).** The size step is small, but the weight difference carries it, so it's fine. Don't lower the heading weight. Put noticeably more space above each heading than between the heading and its first row, so the heading clearly belongs to its list.

**Notes:**
- If most switches are on, the page will show a lot of teal. The solid Save button should still win because it's the only large filled shape. Check this in a screenshot with every switch on.
- I only had your description, not a mockup. If the Weekly summary needs a day or time picker, that control isn't covered here.
