Here's the message, under 120 words:

---

Hey team, we're cleaning up our design tokens. Please stop adding one-off colors and spacing values.

**Naming:** Name tokens by role, not by look or location.
- Good: `color.text.secondary`, `color.surface.raised`, `space.inset.md`
- Avoid: `gray-600`, `homepage-blue`, `15px`

Components use only semantic tokens, never raw values.

**Proposing a change:**
1. Check whether an existing token already fits.
2. If none does, request it with the screen, the value, and why no current token works.
3. Design reviews it. If approved, we add it or merge it into an existing step.

Need a one-off? Mark it as a local exception so we can track it.

---

I wrote the examples generically because I couldn't find your token file in the working directory. Swap in your real token names before posting, and tell me where the tokens live if you want me to check the names against them.
