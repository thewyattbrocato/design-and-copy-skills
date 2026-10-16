Here's a draft at about 75 words:

```markdown
### Adding a new component?

- [ ] **Needed?** Could Button, Input, Select, Modal, or Tabs be extended with a prop or composed instead?
- [ ] **Two real uses.** Link the two places that need it. One-off UI belongs in the app, not the library.
- [ ] **API.** Prop names match existing components. It forwards `ref`, accepts `className`, and is keyboard and screen-reader accessible.
- [ ] **Docs.** Story or example covers every variant and state.
- [ ] **Tests.** Rendering and interaction are covered.
```

- **Reuse first:** The first two items are the main gate. On a small team, the usual problem is near-duplicate components, not missing ones.
- **Naming the five components:** It gives people something concrete to compare against. Update that list when you add a sixth, or swap it for "existing components" to avoid maintaining it.
- **Checklist items:** I kept to what a reviewer can verify from the diff. Add or drop items to match your conventions, such as design tokens or a changelog entry.
