Here's a draft (about 90 words). I didn't have your token files or existing naming scheme, so I assumed a `category-role-variant` pattern. Swap in your real names and fill in the bracketed placeholders.

---

**Design tokens: how we name them, how to add one**

Stop adding one-off colors and spacing. Use tokens only.

**Naming:** `category-role-variant`, e.g. `color-text-primary`, `color-bg-danger`, `space-4`. Name by purpose, not appearance: `color-text-muted`, not `color-gray-500`.

**Proposing a change:**
1. Check the token list first. Most needs are already covered.
2. If nothing fits, open a PR adding the token to [file], with a one-line description of the use case.
3. Tag [@owner] for review.
4. Don't hardcode values in components while you wait.

---

If you share the token file or your current naming, I can make the examples match what your team already uses.
