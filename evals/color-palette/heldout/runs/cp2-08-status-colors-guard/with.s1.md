Not a good idea, and your brand color is the reason.

**Why it's risky**
- **Red already means two things.** Your main buttons are red, and "failed" is red too. If the status colors come from the brand palette, a user can't tell "this is the action I can take" from "this broke". Pulling the other statuses from the brand palette would also blur their meaning, because green, amber and blue only read as success, waiting and in-progress by convention.
- **People scan these colors without reading.** On a deploy dashboard, a green or red that doesn't match what people expect costs attention at the moment it matters most.

**What I'd do**
- Use conventional status hues for the four statuses.
- Keep the brand red for buttons, links and focus states only.
- Make "failed" a deeper, slightly cooler red than the brand red. Show it as an icon plus the word "Failed" in a pale pill, not as a solid filled button.
- Carry meaning with an icon and a label as well as color, so status still reads in grayscale and for red-green colorblind users.

| Status | Text/icon | Pill background | Icon |
|---|---|---|---|
| Running | `#1a62c7` | `#e6effb` | spinner |
| Succeeded | `#1a7f4b` | `#e5f4ec` | check |
| Failed | `#b42327` | `#fdeceb` | X |
| Waiting for approval | `#8a5a00` | `#fff3d6` | clock |

I couldn't run a contrast checker here, so these ratios are estimates. By hand, each text-on-pill pair should land around 5:1 or better, which clears the 4.5:1 floor for small text. Check them in your tooling before shipping. Your brand red with white text works out to about 4.6:1, so the buttons pass but with little room to spare.

**Keeping it on-brand**
Tint your neutrals (page background, cards, borders) slightly toward the brand red's hue. That gives the dashboard a branded feel without touching the status colors.

I assumed a light theme. A dark theme needs the status colors remapped and re-measured, and I can do that next if you want.
