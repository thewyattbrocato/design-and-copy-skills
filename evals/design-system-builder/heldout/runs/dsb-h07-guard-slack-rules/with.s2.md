Here's the message, about 100 words:

---

**Design tokens: naming and changes**

**Naming:** `category.role.variant`. Name for purpose, never for color or page.
• `color.text.secondary`, `color.surface.raised`
• `space.inset.md`, `radius.sm`

Not `gray-600` or `homepage-blue`. Components use these role tokens, not raw values.

**Need something new?** Please don't hardcode a one-off. Instead:
1. Check the existing scale. Can the nearest token work?
2. If not, post in [#channel] with what you need, where it's used (it needs a second real use), and the closest token and why it doesn't fit.
3. [Owner] approves, merges, or says no. Approved changes land in the token file and changelog.

Removing a token? Propose its replacement first.

---

Before you post it:
- Fill in `[#channel]` and `[Owner]`.
- I assumed the `category.role.variant` convention and the "second real use" rule. Swap in your team's actual convention and rules if they differ.
