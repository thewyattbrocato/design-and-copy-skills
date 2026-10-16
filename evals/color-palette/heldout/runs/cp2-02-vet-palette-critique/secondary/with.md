## Why it looks muddy

The problem is value, not hue. All six colors sit in the same middle lightness band, and the page and text are nearly the same brightness.

I computed these from the WCAG sRGB formula by hand:

| Pair | Ratio | Needs |
|---|---|---|
| Body text `#a39b82` on background `#cfc8b0` | **1.8:1** | 4.5:1 |
| Links `#9c8b5e` on background | **2.2:1** | 4.5:1 |
| Error `#b5654a` on background | **2.8:1** | 4.5:1 |
| Error on white | 4.3:1 | 4.5:1 |
| White on primary `#8a7f5c` | 4.0:1 | 4.5:1 (passes 3:1 for large text only) |
| White on secondary `#7d8a6b` | 3.7:1 | 4.5:1 |

- **Body text is the main culprit.** At 1.8:1 it nearly disappears into the background, so the whole page reads as washed out.
- **Nothing has a clear top or bottom.** There is no dark ink, no light surface, and no real lightness step between them. Everything lands in the same tan-olive mid-tones.
- **The background is a dull greige.** Its yellow cast with low saturation reads as dirty rather than warm. Warm light usually comes from a cream or off-white ground.
- **The hues are close cousins.** Four of the six are olive, khaki, or tan, so the palette has little hue contrast to lean on either.

## Suggested fix

Keep the earthy olive identity, but move the values apart and warm up the ground.

| Role | Value | Why |
|---|---|---|
| Page background | `#faf6ee` (cream) | Light, warm ground that lets everything else breathe |
| Card / surface | `#fffdf8` | Small lightness step above the page |
| Body text | `#2e2a22` (warm near-black) | About 13:1 on cream (estimate) |
| Primary button | `#4f5a2f` (deep olive), white label | About 7.4:1 with white (estimate) |
| Secondary button | Outline `#4f5a2f` on cream, or `#e4e9d6` fill with `#2f3a1f` text | About 6.8:1 for the outline version (estimate) |
| Links | `#4f5a2f`, underlined | About 6.8:1 on cream (estimate); keeps links distinct from body text |
| Highlight (decorative) | `#e8a24a` (apricot) | Friendly warmth for badges and illustrations, never for text on cream |
| Error | `#a8432a` (brick) | About 5.5:1 on cream (estimate); reads as a different role from the brand olive |

Two notes:
- The apricot highlight is the one place the palette gets some lift and warmth. Use it sparingly, and pair it with dark ink text if it sits behind words.
- The error color now differs from the brand by shade and deep red-brown rather than sitting close to the old tan. Still pair errors with an icon or a word so meaning does not rest on hue alone.

I could not run code here, so the ratios for the new colors are hand estimates. Run them through a contrast checker before shipping. Also check the button labels against the actual font size, since 4.5:1 applies to normal text.
