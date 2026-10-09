I couldn't find your token file or any contributing docs in the working directory, so the naming pattern below is a sensible default. Swap in your real convention and fill in the bracketed links and owner.

---

**Design tokens: how we name them and how to propose changes**

Stop adding one-off colors and spacing values. Use existing tokens first.

**Naming:** `category-role-variant`, e.g. `color-text-primary`, `color-surface-danger-subtle`, `space-400`. Name what the value is *for*, not how it looks. No `color-blue-2` in components.

**Need a new one?**
1. Check the token file [link] and confirm nothing fits.
2. Open a PR adding the token, with a usage example.
3. Tag [owner/channel] for review.

Hardcoded hex or px values in components will be bounced in review.

---

That's about 95 words.
