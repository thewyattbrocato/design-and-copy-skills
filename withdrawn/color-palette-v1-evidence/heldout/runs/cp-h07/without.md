# Harbor Light donation page: color plan

**Strategy:** A warm cream and deep-navy base carries the trust. One saturated amber-orange is reserved for the donate action and used almost nowhere else. Everything else stays quiet so the donate buttons are the loudest thing on the page.

## Palette

| Role | Hex |
|---|---|
| Page background (cream) | `#FBF6EE` |
| Alt section background (warm sand) | `#F3E9DA` |
| Card/surface | `#FFFFFF` |
| Primary text (deep navy-ink) | `#1F2A37` |
| Secondary text | `#5B6573` |
| Brand / trust (harbor navy) | `#1E3A5F` |
| **Donate accent (lantern amber)** | `#E8731A` |
| Donate hover/pressed | `#C85E0D` |
| Text on donate button | `#FFFFFF`, or `#1F2A37` if you need a stronger contrast ratio (see note) |
| Progress fill (golden) | `#F2A93B` |
| Progress track | `#E6DCCB` |
| Footer background | `#16202C` |
| Footer text / links | `#D9DEE5` / `#F2A93B` |
| Borders/dividers | `#E2D8C6` |
| Focus ring | `#1E3A5F` (2px, offset 2px) |

## Section by section

**1. Top bar.** The background is `#FBF6EE` with a 1px bottom border of `#E2D8C6`. The logo wordmark is in navy `#1E3A5F`. The "Give" button is solid `#E8731A` with white text. It's the first appearance of the accent, so the donate color is learned immediately. Hover is `#C85E0D`.

**2. Hero.** Put the shelter photo under a warm-tinted overlay, a gradient from `rgba(22,32,44,0.65)` at the bottom to transparent at the top. The overlay keeps the headline legible and adds a lamplit mood. The headline "Keep the lights on through winter" is `#FFFFFF`. If you want emphasis, set "lights" in `#F2A93B`, which suggests a glow without adding a new hue. Don't put a second orange button here. The amount selector right below it is the action.

**3. Amounts + Donate now.** This is the focal block. Place it on a white card (`#FFFFFF`) with a soft shadow, on the cream background.
- Unselected amount chips: white fill, 1.5px border `#1E3A5F`, text `#1E3A5F`.
- Selected chip: fill `#1E3A5F`, text `#FFFFFF`. Using navy for selection keeps orange exclusive to the final action.
- Pre-select $60 so the button is never in an empty state.
- "Donate now": full-width, solid `#E8731A`, text `#FFFFFF`, bold. Hover `#C85E0D`. It's the largest and most saturated element on the page.

**4. Impact stories.** The section background is warm sand `#F3E9DA`. Cards are `#FFFFFF` with a `#E2D8C6` border. The dollar figure in each story ("$25 provides…") is bold navy `#1E3A5F`. Body text is `#1F2A37`, and captions or names are `#5B6573`. There are no orange buttons here. If you add a "Give $25" link, make it a navy underlined text link.

**5. Progress bar.** The section is back on cream `#FBF6EE`. The track is `#E6DCCB` and the fill is `#F2A93B`, at 68.7% width (41,200 / 60,000). The fill is a warmer gold, distinct from the button orange, so it reads as progress and not as a clickable control. The label "$41,200 raised of $60,000" is `#1F2A37` with the raised amount in bold navy. Add a small "$18,800 to go" in `#5B6573`. Finish with one more `#E8731A` "Donate now" button below the bar, because the progress bar is a natural moment of motivation.

**6. Footer.** The background is `#16202C`, a navy-black that's softer than pure black. Body text is `#D9DEE5`, headings `#FFFFFF`, and links `#F2A93B` with an underline on hover. The tax-deductibility note ("Harbor Light is a 501(c)(3)… EIN …") goes in `#B4BCC8` at a slightly smaller size, with a 1px divider of `#2C3A4A` above it. Keep the text readable, since this note matters for trust.

## Why this works

- **Warm:** The cream and sand backgrounds, the amber accent, and the gold progress fill give a lamplight feel, which fits a winter shelter.
- **Trustworthy:** Navy for text, headings, and selection states signals stability. The footer carries it through, and plain white cards keep things clean.
- **Unmistakable donate action:** Orange `#E8731A` appears only on the Give button, Donate now, and the repeat Donate now button. Nothing else on the page uses it. The accent is the one warm-saturated color against cool navy and neutral cream, so the eye goes to it.

## Contrast notes

- Navy `#1E3A5F` on cream `#FBF6EE` is about 10:1, which is well above AA.
- Body text `#1F2A37` on cream is about 13:1.
- **White on `#E8731A` is about 3.2:1.** That passes AA only for large or bold text (18px+ bold, or 24px+). Keep button labels large and bold, or darken the button fill to `#C85E0D` (about 4.5:1 with white) if you want to be safe at smaller sizes. Navy `#1F2A37` text on `#E8731A` is about 5:1 and also works if you prefer it.
- `#F2A93B` on the dark footer `#16202C` is about 8:1, so links are fine there. Don't use `#F2A93B` as text on cream (about 2:1). It's for fills only.
- Don't rely on color alone for the progress bar. The numeric label already covers this.

If you'd like, I can turn this into CSS custom properties or a quick HTML mockup so you can see it.
