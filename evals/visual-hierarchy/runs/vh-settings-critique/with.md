**Diagnosis:** the page's job is to let people review settings and save changes. Right now nothing is ranked. Squint at it and you'd see a stack of equal boxes and three equal blue buttons, with no focal point and no obvious next step.

## Fixes in priority order

1. **Use one primary button.** Three solid blue buttons mean three bosses, so the eye has no entry point.
   - Keep Save as the only solid blue button.
   - Make Reset a quiet outline or text button.
   - Move Export away from Save and Reset, for example to the page header or its relevant section, in outline or text style. It isn't part of the save/discard decision.
   - Reset throws away edits, so keep it visually quieter than Save and don't put it right next to it.

2. **Make section titles clearly different from body text.** 15px over 14px is a ratio of about 1.07, which reads as a mistake rather than a choice.
   - Add a weight jump (regular to semibold) first.
   - Then add a modest size bump, aiming for at least 1.25× body.
   - Use one style for all section titles.

3. **Give rows a internal hierarchy.** With every row at the same weight, label, value and control all read as one level.
   - Make setting labels medium or semibold.
   - Keep values and descriptions regular.
   - Rank the order of the sections too, with the most-used settings first and rarely touched ones lower.

4. **Remove most of the borders.** Boxes around every group give everything equal weight and add visual noise.
   - Separate groups with whitespace and the stronger section titles from fix 2.
   - Use a hairline divider between rows only if you need one.
   - Keep a box for something that earns it, such as a danger zone (delete account) or a sticky footer bar.

5. **Darken the helper text.** Light gray at 12px probably fails contrast, and it is the one place the design fades text to lower its rank.
   - The size step down to 12px already ranks it.
   - Use a mid-dark gray that clears the accessibility contrast floor, and keep it at 12–13px.

## What the page should look like after these fixes
- **Grayscale and squint:** the section titles form a clear scaffold, labels sit one step below them, and Save is the only heavy mark.
- **Emphasis budget:** the page would have about one solid-filled element, a handful of semibold labels, and no boxes competing with them.

Fixes 1 and 2 give most of the improvement. Fixes 3–5 refine it. I can write the CSS for these changes if you share the stylesheet or component.
