Here's a box of about 80 words. It's a checklist, so it stays short and reviewers can scan it.

```markdown
### Adding a new component? (delete if not)

- [ ] Checked Button, Input, Select, Modal and Tabs. None can cover this with a new prop or by composing them.
- [ ] Needed in 2+ real places (link them), not speculative
- [ ] Uses design tokens, with no hard-coded colors or spacing
- [ ] Covers hover, focus, disabled, error and loading states
- [ ] Works by keyboard and with a screen reader
- [ ] Has a story or docs page showing props and an example
- [ ] Exported from the library index
```

- **Reuse check first:** it's the check that most keeps a small library from sprawling.
- **"2+ real places":** this stops one-off components from landing in the shared library.
- **Delete-if-not line:** PRs that don't add a component can drop the box, so it doesn't turn into noise.

If you add more items, the box will stop fitting without scrolling. I'd cut the exports line first, since a lint rule or CI check can catch it.
