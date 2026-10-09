The muddiness comes from three problems: everything sits in the same dull mid-tone band, the text is too faint to read, and the page background is dingy.

**1. Everything is the same value and the same hue.** Five of the six colors are low-chroma khaki, olive, or tan, all at roughly 40–50% lightness. Nothing is clearly light or dark, so the eye has no anchor. Only the terracotta error color is saturated, which makes it the one thing with energy, and it clashes with the olive.

**2. The text is too faint to read.** Body text `#a39b82` on background `#cfc8b0` is about 1.7:1 contrast (WCAG asks for 4.5:1 for body text). Your eye reads that as washed out, and it's probably the biggest reason the whole thing feels tired.

**3. The background is the wrong starting point.** `#cfc8b0` is a darkened tan, not a warm cream. Because it's the largest area on screen, it makes everything on top of it look dirty.

Approximate contrast of your current pairs on the page background:

| Pair | Contrast | Problem |
|---|---|---|
| Body text on background | ~1.7:1 | Unreadable |
| Primary button vs. background | ~2.3:1 | Button edge barely visible |
| Links vs. background | ~2:1 | Indistinguishable from body text |
| Error text vs. background | ~2.5:1 | Fails |

Primary and secondary buttons are both olive-khaki at similar lightness, so they also don't read as different.

**A direction that stays warm and friendly:**

- **Background:** a clean cream, such as `#FBF7F0`. Use white for cards.
- **Body text:** a warm near-black ink, such as `#2E2A24` (about 13:1 on the cream).
- **Primary button:** a deep teal, such as `#1E6B66` (about 6:1 with white text). It's calm and trustworthy, and it's a different hue from everything else. Avoid coral or terracotta here, since those would compete with your error color.
- **Links:** the same teal, underlined, so they're clearly tappable.
- **Secondary button:** a soft sage tint, such as `#E3ECE6` background with deep green text. Keep your sage `#7d8a6b` for illustrations, dividers, and tints rather than text.
- **Error:** keep `#b5654a` for icons and borders, but use a deeper red-brown such as `#A4482F` for error text so it passes on cream.

These are my estimates, not measured values, so run the final pairs through a contrast checker before you ship. If you send me your stylesheet or theme file, I can apply the changes and check the contrast ratios in the code.
