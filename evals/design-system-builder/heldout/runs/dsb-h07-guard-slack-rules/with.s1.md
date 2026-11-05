**Design tokens: how we name them and how to change them**

Please stop adding one-off hex and px values. Use a token.

**Naming:** by role, not by color or page.
`color.text.secondary`, `color.surface.raised`, `space.inset.md`
Never `gray-600` in components or `homepage-hero-blue`.

**Need something that's missing?**
1. Check the existing scale. Is a neighboring value close enough?
2. If not, open a request in [channel/link] with the screen, the role it plays, and the nearest existing token.
3. A new value needs a second real use. Until then, keep it local and comment it as an exception.

Changes replace or merge with an existing value rather than add to it.

It's about 105 words. I left `[channel/link]` as a placeholder because I don't know where your team tracks requests. The example token names are also placeholders, so swap in your real ones.
