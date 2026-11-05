I couldn't find your token files in this directory, so I don't know your actual naming scheme. The draft below uses a common pattern (`color.surface.primary`, `space.4`). Swap in your real names before posting.

---

Hi team, we're cutting down on one-off colors and spacing values. Please use design tokens, not raw hex or px.

**Naming:** `category.role.variant`, e.g. `color.text.primary`, `color.surface.danger`, `space.4`. Name by purpose, not appearance. Don't use `color.blue200` in components.

**Need a new value?** Check the token file first; a close match usually exists. If not:
1. Open a PR that adds the token to `[tokens file path]`.
2. Tag `[owner/channel]` in the PR.
3. Say what the value is for and why an existing token doesn't fit.

Ad-hoc values in a PR will be sent back.

---

Word count: about 105.
