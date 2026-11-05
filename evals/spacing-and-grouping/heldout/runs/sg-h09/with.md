**Use extra space and headings. Don't use cards or horizontal lines.**

Twelve controls in three sections is a small form with one level of grouping. Space and headings can show that grouping on their own.

- **Cards:** Cards are for discrete objects that a user opens, selects, or compares. These sections are just parts of one form. Boxing each one adds borders and padding, and it can make the page feel like three separate forms.
- **Horizontal lines:** Lines help when many rows are packed tightly, or when unlike things have to sit close together. Here you have room, so a rule would only repeat what the space already says.
- **Space and headings:** A clear difference between the gaps does the grouping. Make the space within a section about half the space between sections.

**Suggested values** (on a 4px scale, so adjust to your own tokens):
- Between a label and its field: 4–8px.
- Between fields in a section: 16px.
- Between sections: 32–40px.
- Between a heading and its first field: 12–16px. A heading should sit visibly closer to its content than to the section above it, so put roughly twice as much space above it as below it.
- Set the gaps on the container (`gap`) rather than as a bottom margin on each child. That avoids a doubled gap after the last item.

**Two small additions:**
- The Preferences toggles are a different kind of control. Give them a row layout with the label on the left and the switch on the right, with tighter spacing between toggles than between the text fields above.
- If the Address fields (such as city, state, and zip) can share a row, pair them. That makes the section look shorter and more compact.

**When to change this:**
- If the sections become long, or users have to jump between them, add a hairline rule or a card per section.
- If a section is a separate object, such as a saved address you can edit or delete as a unit, use a card for it.
- If your design system already sets a pattern for form sections, follow that and apply the within-versus-between spacing ratio inside it.

**Check:** Squint at the form. You should see exactly three clusters. If two of them blur together, increase the between-section gap rather than adding a border.
