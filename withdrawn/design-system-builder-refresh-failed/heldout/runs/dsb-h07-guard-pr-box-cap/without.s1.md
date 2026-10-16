**Adding a new component?**

Before you open this PR:

- [ ] Check it can't be built by composing or extending Button, Input, Select, Modal, or Tabs.
- [ ] Link the issue or design where the team agreed we need it.
- [ ] Follow the existing pattern: typed props, forwarded `ref`, keyboard and screen-reader support.
- [ ] Add a story and tests covering each variant and state.
- [ ] Export it from the library index.

Not sure it belongs? Open a draft PR or ask in the team channel first.

That's about 80 words and roughly 8 lines, so it should fit on one screen. Wrap it in an HTML comment (`<!-- -->`) if you'd rather it not show up in the PR body once submitted.

I haven't seen your repo, so adjust the checklist to match your conventions. For example, change "forwarded `ref`" if you don't use that pattern, or name your actual story and test tools.
