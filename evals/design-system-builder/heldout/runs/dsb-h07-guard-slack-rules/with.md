Here's the message:

---
**Design tokens: naming and changes**

**Naming:** by role, not by value or location. Components use semantic tokens only, like `color.text.secondary`, `color.surface.raised` and `space.inset.md`. Never raw values (`gray-600`, `#3a3a3a`, `16px`) or page-based names (`homepage-hero-blue`).

**Need something new?**
1. Check the existing scale. The nearest token is usually right.
2. Still a gap? Post in #[channel] with where it's used, the closest existing token, and why that one won't work.
3. We add it once a second screen or team needs it. Until then, keep it local and comment it as an exception.
4. To modify or remove one, open a PR to [tokens file] with a changelog note.

Please, no new one-off values in PRs.

---

It's about 105 words. I filled the bracketed spots with placeholders, because I don't know your channel or tokens file. I also assumed a web product, and the examples are illustrative, so swap in your real token names. I made up the "second screen or team" rule for adding tokens, so change it if your threshold differs.
