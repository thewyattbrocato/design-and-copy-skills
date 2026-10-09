The problem is nested surfaces plus gaps that are too small. Here is what I'd change, in order of impact.

**1. Flatten the nesting. This is the biggest fix.**
- Make the outer panel the only card. Keep its border and drop the shadow, or keep a very soft shadow and drop the border.
- Take the border and shadow off the three inner cards. If they need to read as separate units, give them a faint tinted background with no border and no shadow. Better still, make them plain sections separated by space.
- No element should carry border, shadow and fill together. Pick one or two.

**2. Make the gaps bigger than the padding.**
- The 8px gaps between the inner cards are much smaller than their 24px padding, so the cards blur into one mass. This is the main reason the groups are hard to tell apart.
- Set the gap between groups to 24px, the same as the padding or larger. If the inner cards lose their surfaces, use 32px.

**3. Reduce the padding stack.**
- Right now content sits 48px from the panel edge (24 outer + 24 inner). That is a lot of dead space.
- Keep 24px on the outer panel. If the inner groups have a tint, give them 16px padding. If they have no surface, give them 0.
- The inner content should line up on a single left edge.

**4. Fix the heading spacing.**
- 16px above and 16px below makes a heading float between sections. A heading should sit closer to what it introduces than to what came before it.
- Use 32px above and 12px below. For the first heading in a group, drop the top spacing to 0 and let the container gap do the work.

**5. Let the parent own the spacing.**
- Use `gap` on the flex or grid container instead of `margin-bottom` on each child. That removes doubled space after the last item.

**6. Use a small scale.**
- 4, 8, 12, 16, 24, 32 covers everything above. Snap any one-off values to these.

**Rough CSS**

```css
.panel { padding: 24px; border: 1px solid var(--border); border-radius: 12px; box-shadow: none; display: grid; gap: 32px; }
.panel-group { padding: 0; border: 0; box-shadow: none; }   /* or: background: var(--surface-subtle); padding: 16px; */
.panel-group > h3 { margin: 0 0 12px; }
.panel-group + .panel-group { margin: 0; }                  /* the grid gap owns the spacing */
```

**Optional.** If the three groups need a visible divider and space alone isn't enough, use a 1px hairline in a quiet color with 32px on each side. Don't add boxes back.

**Check after the change.** Squint at the page. You should see one panel containing three clear groups, and each heading should look attached to its content.

I haven't seen your code. If you point me at the component or stylesheet, I can make these edits directly.
