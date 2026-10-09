# Visual hierarchy critique

The page is flat. Almost everything has the same size, weight, color and container treatment, so nothing tells the eye where to start or what matters most.

## Fixes in priority order

**1. Differentiate the footer buttons (highest impact).**
Three solid blue buttons make Save, Reset and Export equally prominent, and the one action that matters competes with a destructive one.
- Keep **Save** as the only solid primary button.
- Make **Export** a secondary button (outline or ghost).
- Make **Reset** a tertiary text button. If it discards changes, use a neutral or red text style and add a confirm step.
- Put Save at the end of the row, with Reset and Export visually separated from it.

**2. Make section titles actually read as titles.**
At 15px against 14px body text, the 1px difference is barely perceptible. Titles only look like titles because of position.
- Use weight, not just size: 16–18px at 600 weight for section titles, 14px at 400 for body.
- Add more space above a section than below its title, so the title groups with its content.

**3. Add weight variation within rows.**
When every row has the same weight, labels and values merge and the eye has nothing to scan.
- Make setting labels medium weight (500) and values or descriptions regular, or the reverse, but be consistent.
- Make high-stakes or frequently changed settings more prominent than rarely touched ones.

**4. Remove the per-group borders.**
A bordered box around every group adds visual noise and makes all groups look equally important. The lines compete with the content, and nested boxes make the page heavier.
- Replace most boxes with whitespace and a thin divider between sections.
- Keep a container only where it has meaning, such as a danger zone or a highlighted card.
- This also reclaims horizontal padding and makes the page easier to scan.

**5. Fix the helper text contrast.**
Light gray at 12px is likely to fail WCAG AA (4.5:1 for small text) and is hard to read.
- Darken it to a mid-gray that reaches at least 4.5:1 against the background, such as `#6b7280` on white (about 4.8:1).
- Consider 13px. Helper text should be quieter than body text through color, not through being hard to read.
- Place it directly under its label with tight spacing so the association is clear.

**6. Establish a clear type and spacing scale.**
Once the changes above are in, check that the scale is coherent. For example: 18/600 for page title, 16/600 for section titles, 14/500 for labels, 14/400 for body, 13/400 for helper text. Use consistent vertical rhythm (for example 8px multiples), with larger gaps between sections than between rows.

## Expected result
The eye should land on the page title, then section titles, then the labels and controls, and finally the single Save button. Helper text should be readable but secondary.

If you share the actual markup or a screenshot, I can turn these into specific CSS changes.
