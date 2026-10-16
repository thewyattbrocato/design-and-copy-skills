The layout mostly holds, so I wouldn't redesign it. The order is clear: title, then section headings, then setting names, then explanations, with one filled button as the only action. Dropping icons, shadows and cards suits a page that's just a list of toggles. Here are the changes I'd make, most important first.

1. **Cap the content width.**
   - **Problem:** You didn't mention a max width. On a wide screen the switch sits far from its setting name, and the eye loses the row.
   - **Fix:** Cap the content column at roughly 640–720px, with the switch at its right edge. The title, headings, rows and Save button then share one left edge.

2. **Make sure Save is visible.**
   - **Problem:** It sits at the bottom, so on a long page it can be below the fold. Users may flip switches and never see it.
   - **Fix:** Keep it where it is but make it sticky at the bottom of the viewport, or confirm with the developer that it's always reachable. If switches save instantly instead, drop the button.

3. **Keep Save the clear primary when many switches are on.**
   - **Problem:** Teal is used for both on-switches and Save. With a dozen switches on, teal covers more area than the one button.
   - **Fix:** This is fine as long as Save stays the largest, solid teal shape on the page. Don't let switches grow beyond the standard size. I wouldn't add a second color.

4. **Check the weakest step: 18px semibold heading over 16px regular row names.**
   - **Problem:** The size gap is small. The semibold weight and the generous space above each section carry the separation.
   - **Fix:** This works only if that section spacing stays clearly larger than the row spacing. If the developer tightens spacing, bump headings to 20px.

5. **Add a second cue for the switch states.**
   - **Problem:** Teal versus grey is a color-only difference.
   - **Fix:** The knob position (left or right) already provides a second cue, so keep it. Make sure the grey off-track is dark enough to be visible against white (at least 3:1 contrast), and that the grey 14px explanations clear 4.5:1. Light greys are the usual failure here.

The rest should stay as is:
- The thin row dividers.
- The text-only "Reset to defaults" link as the tertiary action.
- The one-line grey page description.
- The white background.

If "Reset to defaults" turns out to be hard to spot as clickable, underline it on hover rather than making it teal.
