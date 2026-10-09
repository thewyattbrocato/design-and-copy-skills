Here's the message, at about 105 words:

---
**Design tokens: how we name them and change them**

Please stop adding one-off colors and spacing values. Use what exists first.

**Naming:** by role, not appearance or page.
• `color.text.secondary`, `color.surface.raised`, `space.inset.md`
• Not `gray-600` in components, and never `homepage-hero-blue`
• Components read semantic roles; raw values stay in the token file.

**Need something new?**
1. Check whether an existing token fits or can be merged.
2. Still a gap? Open a request in [link] with the screen, the value, and why no token works.
3. It's added once a second screen or team needs it. Until then, keep it local and comment it as an exception.

Questions here in thread.

---

Replace `[link]` with wherever you want requests to go. I didn't name an owner or approver because I don't know who that is on your team. If you add one, say who has the final call.

The example token names are placeholders. Swap in your real ones if they differ.
