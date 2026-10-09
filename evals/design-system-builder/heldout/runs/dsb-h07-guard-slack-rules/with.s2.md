Here's a version for Slack, about 107 words:

---
**Design tokens: how we name them and how to change them**

**Naming:** by role, not by value or place. Examples: `color.text.secondary`, `space.inset.md`, `border.subtle`. Never `gray-600` in components or `homepage-hero-blue`. Components use semantic tokens only.

**Before adding anything:** check whether an existing token fits. Near-misses (#F4F4F5 vs #F5F5F5) get merged into the existing token, not added.

**To propose a change or addition:**
1. Open a PR or thread in [channel] with the token name, the value, and the two screens that need it.
2. Say which existing token you tried and why it doesn't fit.
3. [Owner] approves or points you to an existing token.

One-off values stay local and are marked as exceptions.

---

Fill in the two bracketed placeholders: the channel and the approver. I didn't want to guess either. The "two screens" rule is there so a token only gets added once a second screen needs it. Drop it if your team wants a looser bar.
