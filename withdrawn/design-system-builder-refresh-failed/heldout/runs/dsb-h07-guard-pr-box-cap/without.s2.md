Here's a version at about 85 words. It's six lines, so it should fit without scrolling.

```markdown
### Adding a new component?
_Skip this box if not._

- [ ] I checked Button, Input, Select, Modal and Tabs. None can cover this with a new prop or variant.
- [ ] It's needed in 2+ places (or a second use is planned).
- [ ] It follows existing conventions: props API, naming, design tokens.
- [ ] It works with keyboard and screen reader.
- [ ] It's exported from the index and has a usage example.

**Why a new component?** <!-- one or two sentences -->
```

I chose these items for a small team:

- **The first checkbox** is the most important. It stops near-duplicates of the five existing components.
- **The "2+ places" rule** keeps one-off UI out of the shared library.
- **The "Why" prompt** gives the reviewer the context to push back quickly.

If you have a Storybook or tests requirement, swap it in for the last checkbox. I'd drop the accessibility line before the first three if you need to cut words.
