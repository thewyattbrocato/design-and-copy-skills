**Use extra space and headings only.** Don't use cards or horizontal lines.

**Why:**
- **Size.** 12 fields in three sections is a small form with one level of grouping. Space and a clear heading are enough to show the groups.
- **Cards are for objects.** A card suits something users open, select, drag, or act on as a whole. Form sections aren't objects. Wrapping each one adds borders and padding that compete with the inputs, and it gets worse if any section has a nested panel.
- **Rules need dense content.** Lines help in long, tightly packed lists or tables. Here, a rule between sections only repeats what the space already says.

**How to set it up:**
- **Space inside a section** (label to field, field to field): one step, for example 16 px between fields and 4–8 px from label to input.
- **Space between sections:** about twice that or more, for example 40 px. The gap between sections should be clearly larger than the gap between fields. If it isn't, the groups blur together.
- **Headings:** put roughly 2:1 more space above a heading than below it. The heading then sits closer to its own fields than to the section above.
- **Spacing owner:** let the form container set the gaps (`gap` on a flex or grid layout) instead of adding `margin-bottom` to every child. This avoids a doubled gap after the last item.
- **Scale:** use values from one small scale (for example 4/8/16/24/40), with no one-off numbers.
- **Preferences toggles:** keep them tight with each other, because they're three related items. Give each row a comfortable touch height, at least 44 px on touch devices.
- **Address fields:** you can pair short fields on one row (city/state/zip). That's a within-group choice and doesn't need any extra divider.

**When to change this:**
- **Hairline rule:** add one only if the form grows long enough that people lose their place while scrolling. Use one quiet weight, with space on both sides.
- **Card:** use one only if the sections become separately savable or collapsible, or the form sits on a busy background. At that point each section is an object.

**Quick check:** squint at the page or blur it. You should see exactly three groups. If two sections merge, increase the between-section gap before adding any lines or boxes.
