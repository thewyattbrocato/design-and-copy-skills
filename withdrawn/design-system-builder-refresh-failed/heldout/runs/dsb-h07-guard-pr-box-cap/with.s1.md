Here's a draft at about 85 words:

```markdown
### Adding a new component?
<!-- Delete this section if your PR doesn't add one. -->

We already have Button, Input, Select, Modal and Tabs. Before adding another, check that:

- [ ] An existing component or a new variant/prop can't do the job
- [ ] It's needed in 2+ places, or clearly about to be
- [ ] It uses design tokens, with no hardcoded colors or spacing
- [ ] It's keyboard accessible, with visible focus and correct ARIA
- [ ] It has a story/example and tests
- [ ] Prop names match existing ones (`variant`, `size`, `disabled`)
```

- **Checklist format:** reviewers can see at a glance what was considered, and it's quick to fill in.
- **First two items:** these keep the library from growing by accident, which matters most on a small team.
- **HTML comment:** it lets PRs that don't add a component skip the section.
- **Last item:** swap the example prop names for your real conventions.

I can shorten it further or add a line linking to a contributing doc if you have one.
