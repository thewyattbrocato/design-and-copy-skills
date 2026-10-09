[...]

Roughly 40 distinct values are doing the work of about 12 decisions. The inconsistency comes from the drift, not from any single bad choice. That's why nobody can point at it.

[...]

2. **Fix the scales on paper.** Pick short scales and a merge map (old → new). A starting proposal:
   - Spacing: 4, 8, 12, 16, 24, 32, 48
   - Radius: 4, 8, 12 (control, container, overlay)
   - Elevation: 2 levels (raised, overlay)
   - Type: 5 roles, such as caption 12, body 14, lead 17, heading 23, display 31
   - Colors: one value per role. Pick the most-used one from the inventory, not an average.
   - Control height: one value, so inputs, selects and buttons align.

[...]

4. **Migrate in blast-radius order.**
   1. Colors, which are mechanical and nearly invisible.
   2. Radius and control heights, where you'll see small, visible alignment changes.
   3. Spacing, which shifts layouts, so do it screen by screen with visual diffs.
   4. Type and shadows last.

[...]

Don't start with a redesign or a component library. The bulk of the problem is value drift, and steps 1–3 remove most of it without changing the intended look.

[...]
