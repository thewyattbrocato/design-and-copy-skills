The layout is sound: the type scale is clear, the restraint is consistent, and teal means "on" or "primary action" and nothing else. I'd change a few things before handoff, most important first.

**Worth changing**
1. **Say when changes apply.** Switches usually take effect immediately, but this page has a Save button. Specify that nothing applies until Save is clicked. Also specify:
   - Save is disabled until something changes.
   - A clear confirmation appears after saving. With no icons or toasts, a short inline "Saved" next to the button works.
   - What happens if the user navigates away with unsaved changes.
2. **Make "Reset to defaults" safe.** It sits right beside the primary button and can wipe many settings. Either add a confirmation, or make it only reset the form without saving, so Save is still the commit step. Also say which defaults it restores: the saved ones or the factory ones.
3. **Don't rely on colour alone for the switches.** Grey vs teal fails for some colour-blind users. The knob position helps, but check these:
   - The off-state track needs at least 3:1 contrast against white.
   - The on-state needs the same.
   - Consider a visible "On"/"Off" text label, or at least an accessible state name.
4. **Check text contrast.** Grey 14px text is the usual failure point. It needs at least 4.5:1 on white, and the same applies to white text on the teal button. Brand teals are often too light for that.

**Worth specifying**
5. **Content width.** Cap the content column at about 640–720px. On wide screens, a switch far from its label makes the eye lose the row. Make the entire row clickable, or at least give the label and switch a proper association and a 44px touch target.
6. **Focus states.** "Nothing else is teal" leaves keyboard focus undefined. Define a visible focus ring, and use a dark neutral if you want to keep teal exclusive.
7. **Button position.** At the bottom of a long page, Save can fall below the fold. Consider a sticky footer bar (no shadow needed, just a top border) if the page is taller than a typical viewport.
8. **Small screens.** Say that the explanation text wraps beneath the label and the switch stays vertically centred and right-aligned. Also say whether the button and link stack.

**Minor**
- 18px vs 16px is a small step. Semibold carries the hierarchy, which is fine, but the extra section spacing has to do the work, so make sure it's clearly larger than the row spacing.
- If "Weekly summary" needs more than a switch (day, time), the row pattern will need a variant. If it's a single switch, a section with one row looks sparse, so confirm that's intended.
- Decide whether any settings depend on others, such as a section master toggle, and how disabled child rows look.
