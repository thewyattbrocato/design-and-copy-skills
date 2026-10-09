## What's wrong

The core problem: **everything is shouting, so nothing is heard.** Hierarchy works by contrast, and this screen has almost none.

1. **Flat typographic hierarchy.** Title is 28px, headings 20px, and helper text and every toggle label are all bold 16px. Bold on body text means bold carries no information. Staff can't tell a label from a description from an instruction.
2. **Color is misused.** Bright blue headings compete with the blue buttons, so blue no longer means "clickable." Red helper text reads as an error or warning on every section, so people either stress or learn to ignore it, including the times it matters.
3. **Helper text is in the wrong voice.** Red, bold, and a full sentence per section. It's the loudest thing under each heading, yet it's secondary information.
4. **Borders and shadows on everything.** With every element boxed and lifted, there's no foreground or background. Containers, toggles, and buttons all look equally "raised," so the eye has no entry point.
5. **Buttons don't express priority.** "Save changes" and "Reset to defaults" are identical filled blue. One is the primary action. The other is destructive-ish and should be hard to hit by accident. Placed side by side, a mis-click resets the user's work.
6. **Cancel is the weakest element, but it's the escape hatch.** Gray link with low contrast may also fail accessibility contrast.
7. **No grouping signal.** Four sections of 3-5 toggles each, with no spacing or structure distinguishing "section" from "item," makes the page a long undifferentiated list.

## How I'd fix it

**Establish one focal point per level:**

- **Page title:** keep 28px bold, neutral dark text (not colored).
- **Section headings:** 18-20px, semibold, dark neutral (or a single muted accent). Not bright blue.
- **Toggle labels:** 16px, **regular weight**, dark neutral. This is the content staff scan, so it should be the most legible, not the heaviest.
- **Helper text:** 14px, regular, muted gray (about #5F6B7A or darker, to keep ≥4.5:1 contrast). Place it under the heading or under the relevant toggle.
- **Reserve red** for real errors and warnings only. If one helper truly is a warning (e.g., "Turning off voice calls means no urgent cancellation alerts"), show it inline, only when it applies, with an icon.

**Quiet the chrome:**

- Remove borders and shadows from toggles and text. Use **whitespace** (e.g., 32-40px between sections, 12-16px between toggles) and perhaps a single hairline divider between sections.
- If you want containers, use one level: a subtle card per section with a light border *or* a shadow, not both.

**Make actions tell the truth:**

- **Save changes:** the only filled, accent-colored button. Place it at the right (or left, matching your product's convention).
- **Reset to defaults:** secondary. Use an outlined or text button, and ideally put it away from Save (e.g., on the opposite side), with a confirm step if it discards changes.
- **Cancel:** a text button with adequate contrast, adjacent to Save.
- Consider a sticky footer so actions are always visible on a long page.

**Color system:** one accent color (blue) used only for interactive things: toggles in the on state, the primary button, links. Everything else is neutral.

**Optional improvements for a clinic context:**

- Put a short summary at the top of each section ("Email: 3 of 4 on") or a section-level master toggle, so staff don't have to read every toggle.
- Group critical alerts (e.g., appointment cancellations) first within each section.
- Disable Save until something changes, and show an "Unsaved changes" indicator.

## Resulting reading order

Title → section headings (by size and spacing) → toggle labels (by clarity) → one blue Save button. Helper text recedes until needed, and red appears only when something genuinely needs attention.

A quick way to validate: squint at the screen, or blur it. You should be able to identify the title, the four sections, and the Save button. If you can't, the hierarchy still isn't strong enough.
