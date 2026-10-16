Here's a box that comes to about 70 words:

```markdown
### Adding a new component?
Skip this section if not.

- [ ] Button, Input, Select, Modal, and Tabs can't do the job, even with a new prop or variant
- [ ] Needed in at least two places, or a second use is planned
- [ ] Uses existing design tokens, with no hardcoded colors or spacing
- [ ] Keyboard accessible, with visible focus and correct ARIA roles
- [ ] Typed props, exported from the index, story added
- [ ] Disabled, loading, and error states handled where relevant
```

I chose these items for a few reasons:

- **The first two items guard against duplication.** For a small team with five components, the most likely mistake is building a near-copy of one of them. The list names them so people check.
- **The next two cover what reviewers otherwise catch by hand.** Those are token use and accessibility.
- **The last two cover what's often missed.** That means exports, stories and non-default states.
- **Checkboxes keep it short.** They're quick to scan and tick, so the box stays small enough to fit on screen.

If your library has a different convention, such as a docs page instead of a story or a required test file, swap it in for the fifth item.
