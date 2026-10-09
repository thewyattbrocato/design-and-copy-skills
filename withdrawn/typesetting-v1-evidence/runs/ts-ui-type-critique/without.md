I'd go in this order: fix the outright bugs, then set the scale, then migrate to it, then lock it in.

## 1. Fix the heading line-height (hours of work)
- Line-height 1.0 is a bug. It clips descenders and makes wrapped lines collide.
- Set headings to about 1.2–1.3 (1.1–1.2 for very large display sizes) and body text to 1.5.
- Add `text-wrap: balance` to headings so a wrap on tablets doesn't leave an orphaned word.
- Use fluid sizing, e.g. `clamp(1.5rem, 1.2rem + 1.5vw, 2rem)`, so headings shrink on tablets instead of wrapping. Shorten the longest titles too, since some wrapping is unavoidable.

## 2. Fix contrast and legibility of the small text (a day or so)
- Check the gray helper text against WCAG AA, which needs 4.5:1 for small text. Light gray at 12px usually fails. Darken it to roughly `#595959` or darker on white.
- Make the 11px all-caps labels either sentence case at 12–13px with medium weight, or keep caps at 12px with about 0.04–0.08em letterspacing. All-caps with no tracking is the worst combination for readability. I'd prefer sentence case, since it also scans better in a dense PM interface.

## 3. Define a type scale (about a day of design work)
Collapse eleven sizes into 6–7 tokens, for example:

| Token | Size | Use |
|---|---|---|
| `text-xs` | 12px | Helper text, captions, badges |
| `text-sm` | 14px | Labels, secondary UI, table cells |
| `text-base` | 16px | Body text |
| `text-lg` | 18px | Emphasized body, card titles |
| `text-xl` | 22px | Section headings (h3) |
| `text-2xl` | 28px | Page sections (h2) |
| `text-3xl` | 36px | Page titles (h1), fluid |

Define them in rem as CSS variables or theme tokens, each with a paired line-height and weight. Map every existing size to its nearest token. The mapping will show you which of the eleven are accidents.

## 4. Raise the body size (once the tokens exist)
- 13px is small for sustained reading. Move body text to 14px at minimum, and 16px if the layout can absorb it.
- If the app is dense (tables, boards), a reasonable split is 14px for dense UI and 16px for long-form content like descriptions and comments.
- Do this through the token, not by editing individual styles. Then check for overflow in tables, kanban cards, and nav.
- Helper text under every field is also a layout problem. Show it only where it adds information, and otherwise use placeholder-free, self-explanatory labels. A smaller number of helper lines will look much cleaner.

## 5. Enforce it
- Add a lint rule (stylelint or an ESLint rule for Tailwind) to ban raw `font-size` values outside the tokens.
- Document the scale with usage examples.
- Run a visual regression pass on tablet widths (768 and 1024) before shipping.

## Why this order
Steps 1 and 2 are small, low-risk, and fix the problems users notice today. Step 3 has to come before step 4, because changing body size without a scale just creates a twelfth size. Step 5 stops the sprawl from coming back.

If you can point me at the codebase, I can inventory the eleven sizes and propose the exact mapping.
