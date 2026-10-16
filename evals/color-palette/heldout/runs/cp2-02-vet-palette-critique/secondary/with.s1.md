**What's going wrong**

Your palette is almost all one hue family (olive and khaki) at similar mid-lightness, on a mid-value greige background. Nothing has enough contrast to stand out, so the whole screen looks dull. The specific problems, by impact:

1. **Body text is nearly invisible.** `#a39b82` on `#cfc8b0` is about 1.7:1. Body text needs 4.5:1. This is the biggest reason the app feels tired.
2. **The background is too dark and too gray for a warm, friendly feel.** At mid-value it dulls everything placed on it, and there's no clean lighter ground for the content to sit on.
3. **Primary, secondary, and link blend together.** All three are desaturated olive at similar lightness, so they don't read as different jobs.
4. **Links fail.** `#9c8b5e` on the background is about 2:1.
5. **Error reads as brown.** `#b5654a` is rust-brown on greige at about 2.5:1, so it doesn't signal alarm.
6. **Buttons are borderline.** White text on the primary is about 4:1 and on the secondary about 3.7:1. Both fall short of 4.5:1 for normal-size labels.

**A warmer, friendlier fix**

| Role | Hex | Why | Est. contrast |
|---|---|---|---|
| Page background | `#fbf6ef` | Warm off-white; a clean ground that lets color stand out | — |
| Body text | `#3b3128` | Warm dark brown instead of gray; reads softly | ~11.7:1 on background |
| Primary buttons | `#1f6f6a` (deep teal) | Calm and trustworthy for healthcare; white label | ~5.9:1 with white text |
| Secondary buttons | Fill `#e3efec`, text `#1f6f6a` | Quieter tint with the same teal, so it stays in the family | Teal text on tint, roughly 5.5:1 |
| Highlight / links | `#a8462a` (terracotta) | The warm accent, so links feel friendly; keeps the palette from going cold | ~5.4:1 on background |
| Error | `#b42318` (clear red) | Reads as an alarm, not brand; add an icon and words too | ~6.1:1 on background |

Why this direction: teal carries the trust that a vet product needs, and terracotta supplies the warmth. The cream ground keeps the whole thing from feeling clinical. Teal and terracotta are different hues at different lightness, so primary and link no longer blur together.

**Caveats**

- I couldn't run a contrast checker in this session, so the ratios above are hand-calculated estimates. Verify them with a tool such as WebAIM's contrast checker before you ship.
- I assumed white text on the primary button. Check hover, pressed, and disabled states too.
