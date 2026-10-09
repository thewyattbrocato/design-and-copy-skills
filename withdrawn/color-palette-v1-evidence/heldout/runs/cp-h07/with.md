**Concept:** a warm paper-cream page with a deep harbor-navy for text and the footer. Orange is reserved for the donate action and appears nowhere else. No logo or brand color was given, so I chose these. Cream and navy do most of the work, and a quiet teal handles supporting details.

| Role | Hex | Where it's used |
|---|---|---|
| Page cream | `#FBF5EC` | Page background, top bar, story section |
| Warm band | `#F3E8D8` | Background band behind the donation panel |
| Surface white | `#FFFFFF` | Donation panel, amount chips, story cards |
| Harbor navy | `#17323F` | Headlines, body text, logo, footer background, selected amount chip |
| Secondary text | `#3F525C` | Story body copy, captions, progress labels |
| **Action orange** | `#C2410C` | "Give" in the top bar and "Donate now" only. Hover is `#9A3412`. |
| Harbor teal | `#2A6F76` | Story icons and eyebrow labels, progress bar fill |
| Control border | `#7A8A91` | Unselected amount chips |
| Track / card edge | `#E6D9C6` | Progress track, story card borders |
| Footer text | `#E8E0D3` primary, `#B9C4C9` secondary | Contact details; tax-deductibility note |
| Footer accent | `#F2A33A` | Footer links and focus ring on navy |
| Hero text and scrim | `#FFF8EE` text over `rgba(23,50,63,0.72)` | Headline over the shelter photo |

**Section by section**
- **Top bar:** Cream background with a navy logo. The orange "Give" button is the only saturated color there.
- **Hero:** The photo has a navy scrim, heaviest on the headline side. The headline "Keep the lights on through winter" is cream. The scrim ties the photo to the footer and keeps the text readable on bright snow or sky.
- **Amounts and Donate now:** The white panel sits on the warm band. The chips ($25, $60, $120) have gray-blue borders. The selected chip fills navy with white text and a check icon, so selection doesn't compete with orange. "Donate now" is a full-width orange button with white text, and it is the only large saturated block on the page.
- **Impact stories:** White cards on cream, with teal icons and eyebrows. Story text is navy and secondary gray. Nothing orange appears here, so the eye returns to the button.
- **Progress bar:** A teal fill on a sand track, with the text "$41,200 raised of $60,000 · 69%" beside it. The numbers carry the meaning, not the color.
- **Footer:** Navy ground, cream text, and amber links. This closes the page with the same navy as the headlines.

**Contrast (computed with the WCAG formula, on the actual surface)**

| Pair | Ratio |
|---|---|
| Navy on cream | 12.4:1 |
| White on orange `#C2410C` | 5.2:1 |
| Orange button vs cream page | 4.8:1 (above the 3:1 boundary floor) |
| Secondary text on white / cream | 8.2 / 7.5:1 |
| Teal on white / cream | 5.8 / 5.3:1 |
| Chip border vs white / cream | 3.6 / 3.3:1 |
| Teal fill vs sand track | 4.2:1 |
| Footer primary / secondary text on navy | 10.2 / 7.5:1 |
| Amber on navy | 6.4:1 |
| Cream headline over the scrim, worst case (pure-white photo pixel) | 5.2:1 |

**Why the donate action is unmistakable**
- Orange is the only warm saturated color, and it appears only on actions. A visitor learns that orange means "give."
- Orange against cream and navy is a strong warm-versus-cool contrast, and it passes contrast without a border.
- In grayscale, the orange button (`#C2410C`) is still the darkest mid-tone block on a light page. The selected chip is the only other dark block, and it has a check icon.

**Assumptions**
1. There is no existing logo or brand color. If there is one, I'd keep it and rebuild the navy and orange around it.
2. The scrim values assume a photo of average brightness. Check the real image at its brightest spot under the headline.
3. These are screen values only, with no dark theme and no print match.
