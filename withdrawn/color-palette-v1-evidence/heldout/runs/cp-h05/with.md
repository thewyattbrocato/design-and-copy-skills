I'd leave the colors as they are. The palette already holds up, and changing it just to show effort would risk the look members like.

I measured each text pair on the surface it sits on, using the WCAG contrast formula. The usual floor is about 4.5:1 for body text and 3:1 for large text.

| Pair | Ratio |
|---|---|
| Body text `#2f2a24` on page `#faf6ee` | 13.2:1 |
| Body text on callout `#efe5cf` | 11.3:1 |
| Headings `#3b5a3a` on page | 7.2:1 |
| Button text `#faf6ee` on `#3b5a3a` | 7.2:1 |
| Links `#2f6b3b` on page | 5.9:1 |
| Links on white card | 6.4:1 |
| Links on callout | 5.1:1 |
| Sale tag, white on `#b5472a` | 5.4:1 |
| Footer text `#d9d0bd` on `#2f2a24` | 9.3:1 |
| `.meta` `#6e6556` on page | 5.3:1 |
| `.meta` on white card | 5.7:1 |
| `.meta` on callout | 4.6:1 |

**Why it works**
- **Roles:** The warm cream base, the green lead and the single rust accent each have a clear job. The rust is used only for sales, so it stands out.
- **Neutrals:** The grays and browns all lean warm, so they sit well with the green.
- **Links:** They are underlined, so they don't depend on color alone.
- **Sale tag:** The rust reads as "sale" through its label and position, and it is clearly separate from the green.

**One thing to watch**
- `.meta` on the callout is the thinnest margin at 4.6:1. It passes, but only just. It's fine if meta text is normal size and rarely sits in a callout. If you put small gray text there often, darken `.meta` a step within the same brown.

**Assumptions**
- I checked screen colors only, in light mode.
- Some email apps auto-invert colors in dark mode, which can wash out the cream and green. If members read on phones in dark mode, send yourself a test to check.
