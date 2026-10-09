The muddiness comes from three things: everything sits in the same narrow band of value and saturation, the text doesn't contrast with the background, and the accents don't stand apart from the page.

**1. Everything is the same mid-tone.** Your background, buttons, links, and text all fall between roughly 20% and 58% relative luminance, and all are desaturated olive-khaki. Nothing is light, nothing is dark, and no color has energy, so the screen reads as one tone.

**2. Text and links fail contrast.** These are my hand calculations, so check them with a contrast tool before you commit:

| Pairing | Ratio | Needed (body text) |
|---|---|---|
| Body text `#a39b82` on background `#cfc8b0` | ~1.7:1 | 4.5:1 |
| Highlight/link `#9c8b5e` on background | ~2.0:1 | 4.5:1 |
| Error `#b5654a` on background | ~2.5:1 | 4.5:1 |
| Primary button `#8a7f5c` with white text | ~4:1 | 4.5:1 |

Body text is the biggest problem. At 1.7:1 it is hard to read on a phone in daylight, and for a health product that is a real usability issue, not just a style one. Low contrast also drains warmth, because it makes everything look faded.

**3. Low chroma reads as tired.** Warm and friendly palettes usually pair a light, clean surface with one or two saturated accents. Yours are all grayed, so the app has no sparkle and no clear sense of what to tap.

**A direction that keeps the warmth:**

| Role | Hex | Notes |
|---|---|---|
| Background | `#FBF7EF` | Warm cream, much lighter than now |
| Surface (cards) | `#FFFFFF` | Lifts content off the cream |
| Body text | `#2E2A24` | Warm charcoal, ~13:1 on cream |
| Primary button | `#1E6B66` | Deep teal, white text ~6:1 |
| Links | `#1E6B66` | Same teal, ~6:1 on cream |
| Secondary | `#E3EDE6` fill, teal text | Soft sage tint, doesn't compete with primary |
| Highlight accent | `#E07A5F` | Coral for illustrations, badges, decoration. Keep it off body text |
| Error | `#B3261E` | A true red so it doesn't blend with the warm palette, ~6:1 on cream |

The teal and coral are a classic pairing for pet and care brands: calm, trustworthy, and friendly. Keep the olive family only as a light tint if you want to carry some of the original feel forward.

Two things to check before launch: test the palette in a bright outdoor light on a phone, and run every text and button combination through a WCAG checker, since the hex values above are my estimates.
