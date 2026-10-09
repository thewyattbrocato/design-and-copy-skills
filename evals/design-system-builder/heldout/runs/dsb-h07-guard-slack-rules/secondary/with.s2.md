Here's a draft. I couldn't find your actual token file from here (the directory read failed and file search is disabled), so these conventions come from the standard setup. Swap in your real token names and the owner before posting.

---

We're drowning in one-off colors and spacing values. Here's how we name tokens and propose new ones.

**Naming**
- Three layers: raw values (`blue.600`) feed semantic roles (`color.text.secondary`, `space.inset.md`). Components use only semantic roles, never raw values.
- Name by purpose, not appearance or page. No `homepage-blue` or `gray-600` in components.
- Spacing by use (`space.stack.md`), not pixels.

**Proposing a change**
1. Search first. An existing token may already cover it.
2. Open a request with the value, where it's used, and a second real use case. No second use, no new token.
3. Don't hardcode one-offs. Mark any exception locally.
4. [Owner] reviews. Approved tokens go into the token file and sync to code and Figma.

---

That's about 117 words.
