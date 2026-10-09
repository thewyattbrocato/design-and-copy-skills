**What's going wrong:** almost every color sits in the same mid-tone, low-saturation olive-khaki band. Nothing is light enough to feel fresh or dark enough to feel crisp, so the whole screen reads as dim. The biggest problem is that the text and links fail contrast. Body text is about 1.5:1 on the background (4.5:1 is the minimum for body text), so it's hard to read, and that difficulty comes across as tired.

Ratios below are my hand calculations, not measured with a tool, so verify them before shipping.

| Pair | Current ratio | Result |
|---|---|---|
| Body `#a39b82` on page `#cfc8b0` | ~1.5:1 | Fails badly |
| Links `#9c8b5e` on page | ~1.9:1 | Fails badly |
| Errors `#b5654a` on page | ~2.4:1 | Fails |
| Secondary button `#7d8a6b` with white text | ~4.2:1 | Fails for normal text |
| Primary button `#8a7f5c` with white text | ~4.8:1 | Passes, but just barely |

**Suggested fix:** keep the olive and rust identity, but add a light ground and darker ink.

- **Page background:** `#f6f1e4`, a warm off-white. Use `#cfc8b0` only for tinted panels, not the whole page.
- **Body text:** `#3b3628`, a warm near-black. About 10:1 on the new background.
- **Primary button:** `#6b5a2e` with white text, about 6.7:1. It keeps the brand hue but has a clear lightness gap.
- **Secondary button:** `#66724f` with white text, about 5.1:1.
- **Links:** `#6b5a2e`, about 6:1 on the new background. Underline them so they don't depend on color alone.
- **Error messages:** `#9a4a32`, about 5.5:1. It's a distinct rust, so it won't read as a brand color. Pair it with an icon and a word, such as "Error:".

**Trade-off:** the darker olive is calmer and more trustworthy, but it is less warm than your current palette. If you want more warmth, add one small saturated accent for the main call to action (such as a honey or apricot), and keep the olive for secondary actions.
