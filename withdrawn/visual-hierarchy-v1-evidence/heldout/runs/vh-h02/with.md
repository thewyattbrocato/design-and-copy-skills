**What's wrong**

The screen has no ranking. Nearly everything is loud, so nothing stands out, and that's why staff don't know where to look.

1. **Everything is bold.** The title, the headings, the helper sentences and every toggle label are all bold. When emphasis covers most of the screen, it stops meaning anything. The toggle labels are the content people actually scan, and they're the same weight as the headings above them.
2. **The levels are too close together.** Section headings are 20px bold and labels are 16px bold. That is a small size step with no weight step, so the headings barely read as headings.
3. **Colour is working against the content.**
   - Bright blue headings take the strongest colour on the page for what is only a label.
   - Red helper text reads as an error or warning. Red should be kept for real problems, such as "SMS is off, so patients won't get reminders." Using it for routine explanations teaches staff to ignore red.
4. **There are two primary buttons.** "Save changes" and "Reset to defaults" are identical blue fills side by side. That is a risky pairing: Reset is destructive and sits next to Save with the same weight. The gray "Cancel" link is the quietest of the three, but Cancel and Reset are close in function.
5. **Borders and shadows are on everything.** Section boxes, toggles, buttons and inputs each have a 1px border and a drop shadow. The marks stack up into visual noise without grouping anything. Space would group the content more cleanly.
6. **The same style is reused for different roles.** Headings, helper text and labels all get "bold plus colour", so the style doesn't tell you what role a piece of text has.

**How I'd fix it**

Decide the ranking first. The screen's job is to let staff check and change how patients and staff get notified, then save. So:

- Primary: the toggle labels, which are the thing being changed, and the Save button.
- Secondary: the section headings.
- Tertiary: the helper text.
- Meta: Reset and Cancel.

Then apply these changes:

1. **Weight.** Make the toggle labels regular weight, and make section headings semibold. Keep bold for the page title only, or drop the title to semibold. Emphasis should end up on a small share of the screen.
2. **Size.** Keep the title at 28px. Take section headings to about 18–20px semibold, with labels at 16px regular. That is a visible step at each level.
3. **Colour.**
   - Make headings neutral dark text.
   - Make helper text regular weight in a muted gray that still passes contrast, about 14px.
   - Use blue only for the primary button and for the toggles' "on" state.
   - Reserve red for real warnings. Where one applies, pair it with an icon or a label so colour isn't the only cue.
4. **Buttons.** Keep one filled blue "Save changes". Make "Reset to defaults" a quieter outline or text button. Put it away from Save, for example on the left edge, and add a confirmation step. Keep "Cancel" as a plain text link next to Save. Align the action row to the same left edge as the content.
5. **Borders and shadows.** Remove all the shadows. Drop the borders around toggles and buttons. Separate the four sections with generous vertical space, or at most a thin divider line between them. If you need any elevation, use one level on a single container.
6. **Structure.** Within each section, put the toggles in one aligned column with the switch at a consistent edge. If Quiet hours has time inputs, indent them under their toggle.

**Check after the changes**

- Squint at the screen: you should see the title, the section headings, and the blue Save button, in that order.
- Convert to grayscale: the order should still hold without colour.
- Count the loud things: there should be one primary button and about a tenth of the text emphasized.

I haven't seen the real screen, only your description, so the specific sizes and greys are starting points to test with staff rather than final values.
