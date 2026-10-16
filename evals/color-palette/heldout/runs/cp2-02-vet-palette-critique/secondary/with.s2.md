**What's wrong:** the palette is all one value and one chroma. Every color sits in the same dull, desaturated middle band, so nothing has a clear lightness gap from its neighbors. Primary and secondary buttons are nearly the same olive-brown, and the body text is lighter than the page background's shadows, so it looks washed out. Low saturation reads as tired, and mid-tone text on a mid-tone beige reads as muddy.

**Measured contrast on your current pairs** (WCAG 2.x, calculated by hand, so treat as estimates until a checker confirms them):

| Pair | Ratio | Need |
|---|---|---|
| Body `#a39b82` on page `#cfc8b0` | 1.8:1 | 4.5:1 |
| Link `#9c8b5e` on page | 2.1:1 | 4.5:1 |
| Error `#b5654a` on page | 2.7:1 | 4.5:1 |
| White on primary `#8a7f5c` | 4.0:1 | 4.5:1 |
| White on secondary `#7d8a6b` | 3.7:1 | 4.5:1 |

Every text pair fails. The body text fails badly.

**Proposed palette** (keeps the warm cream and sage feel, adds lightness separation and one clear lead):

| Role | Hex | Why | Ratio |
|---|---|---|---|
| Page background | `#f8f3e8` | Lighter warm cream, so the page breathes | — |
| Card / input surface | `#fffdf8` | Lifts content off the page | — |
| Body text | `#3a3128` | Warm charcoal, reads as friendly rather than gray | 11.5:1 on page |
| Muted text (captions, helper) | `#6b5f52` | Clearly secondary, still legible | 5.7:1 on page |
| Primary button, links | `#2a6f61` | Deep teal, the one lead; calm and trustworthy for health | White on it 5.4:1; on page 4.9:1 |
| Secondary button | `#e4ebe0` fill, `#24443b` text | Sage tint, quieter than primary | 8.8:1 |
| Error | `#b03a2e` | Warm red, distinct from the teal lead | 5.4:1 on page |
| Highlight (badges, illustrations only, not text) | `#e9a23b` | Sunny accent, kept small | Not for text |

Rules for using it: error messages also get an icon and a word, not color alone. Hover on primary should be a step darker (around `#22594d`), not a tint change.

**Trade-offs:**
- Moving the lead from olive to teal is the biggest change. If the olive is a brand decision, keep its hue and just push it to `#5f6b3e` for primary (white text ratio about 6:1) and lift the page and text as above. That keeps the identity and still fixes the contrast.
- I computed these ratios by hand, so run them through a contrast checker before shipping.
