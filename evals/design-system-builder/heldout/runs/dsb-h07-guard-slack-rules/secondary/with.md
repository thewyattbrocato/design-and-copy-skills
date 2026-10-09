Here's the message. I didn't find any existing token files in the working directory, so the names below are generic examples from the skill's conventions. Swap in your real token names before posting.

---

Hey team, we're drifting: one-off colors and spacing values keep creeping in. Here's how we name and change tokens.

**Naming**
- Colors by role, not look: `color.text.secondary`, `color.surface.raised`, `color.danger.default`. Never `gray-600` or `blue` in components.
- Spacing by use: `space.inset.sm`, `space.stack.md`. Not `12px`.
- Components read semantic tokens only.

**Proposing a change**
1. Check the token list first. Most needs already exist.
2. If nothing fits, open a request with the use case, where it appears, and a screenshot.
3. Add a new value only if it's clearly different from its neighbors; otherwise we merge into an existing one.
4. Post it in [channel] for review; [owner] signs off.

One-off values need an exception note in the PR, not a silent merge.

---

Word count: about 115, under your 120 cap. Fill in `[channel]` and `[owner]` before posting.
