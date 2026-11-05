Here's the message (about 110 words):

---

**Design tokens: naming and changes**

**Naming:** by role, not value or place. `color.text.secondary`, `space.inset.md`, `radius.sm`. Never `gray-600` in components or `homepage-hero-blue`. Components use semantic tokens only.

**Before adding anything:** pick the nearest existing token. No one-off colors or spacing.

**To propose a change:**
1. Post in [channel/link] with: where it's needed, which token you tried, why it falls short.
2. Needed by a second screen or team? It's a candidate. Otherwise keep it local and label it an exception.
3. [Owner] approves, or merges it into an existing token.
4. Approved changes land in the shared token file, so design and code update together.

Removals are announced first, with a migration.

---

Fill in the two bracketed placeholders: the channel or form for requests, and who approves. I used example token names, so swap in your real ones if they differ.
