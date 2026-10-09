I'd go in this order, most visible and lowest risk first.

**1. Fix the page headings (hours of work, biggest visible win)**
- Change `line-height: 1.0` to about 1.2. Headings that wrap need room, and 1.0 makes the two-line case look cramped.
- Add `text-wrap: balance` so a wrapped heading doesn't leave one orphaned word.
- If the size has to scale with the viewport, use `clamp()` with a `rem` floor, for example `clamp(1.5rem, 1.2rem + 1.2vw, 2rem)`. That should also stop most tablet wrapping.

**2. Fix the 11px all-caps labels**
- Easiest fix: switch to sentence case at normal tracking. This is the default for interface labels.
- If the brand wants caps, keep them for short labels of one to three words. Set them at 12px or larger with `letter-spacing: 0.05em` to `0.08em`. Caps at 11px with no tracking is the worst combination.

**3. Collapse eleven sizes into a token scale (the main refactor)**
- Use five or six sizes, one per role, on a ratio of about 1.2. For example:

  | Token | Size | Role |
  |---|---|---|
  | `--text-sm` | 12px | metadata, captions, caps labels |
  | `--text-base` | 14px | body |
  | `--text-md` | 16px | inputs, emphasized text |
  | `--text-lg` | 20px | section heading |
  | `--text-xl` | 24px | page title |
  | `--text-2xl` | 32px | display, fluid |

- Write them in `rem` and don't set the root size in pixels.
- Map each of the eleven existing sizes to the nearest token, then delete the strays.
- Heading levels (`h1` to `h6`) should follow the document outline. Take the visual size from a class or token, and let two levels share a size.

**4. Raise body text from 13px to 14px, with `line-height: 1.5`**
- 14px is the floor for a dense tool. Use unitless line height, and keep any paragraph-like text, such as descriptions and comments, to about 65ch.
- Anything someone must read to act, such as errors, instructions and prices, should be at body size or larger. Don't put it in 12px helper text.

**5. Rework the 12px gray helper text**
- Check its contrast against your accessibility floor first. Light gray at 12px is the most likely thing to fail.
- Show helper text only where it earns its place. It doesn't need to sit under every field. Self-evident fields can drop it, and rarely needed hints can move into a tooltip or placeholder-style hint.
- If a hint is needed to complete the field correctly, set it at body size.

**6. Final pass: numbers**
- Add `font-variant-numeric: tabular-nums` to figures in tables, task counts, timers, budgets and dashboards. Right-align them and use the same number of decimals on every row.

Steps 1 and 2 are small CSS changes you can ship right away. Steps 3 to 5 are best done together as one token migration. Otherwise you'll restyle the same elements twice.

If you point me to the stylesheet or the design tokens, I can inventory the eleven sizes and propose the exact mapping.
