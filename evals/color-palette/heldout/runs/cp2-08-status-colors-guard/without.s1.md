Mostly no. I'd keep status colors separate from the brand palette.

**Why it backfires**

- **Your brand red reads as "failed."** Red already means error or failure to nearly everyone. If your primary buttons are `#d93a35`, a red "Deploy" button sits next to red "Failed" badges, and the dashboard gives two different messages in the same color. If you pull status colors from the brand palette, "succeeded" and "failed" are likely to end up too close together or the wrong way round.
- **Status colors carry meaning, so they need to be easy to tell apart and recognize at a glance.** Brand palettes are built for identity and harmony, so their colors tend to sit close together. Status colors need to be clearly different from each other.
- **People scan for status quickly.** Someone checking whether a deploy broke production shouldn't have to learn a custom color mapping first. Green, red, amber and blue are conventions people already know.

**What I'd do**

| Status | Color family | Note |
|---|---|---|
| Succeeded | Green | Standard convention |
| Failed | Red | Keep it clearly different from the brand red (see below) |
| Waiting for approval | Amber/yellow | Signals "needs a human" |
| Running | Blue | Pair with a spinner or animation |

- **Make failed red distinct from the brand red.** Either shift it (for example, more toward crimson or a different lightness) or, better, limit the brand red to buttons and chrome and use a status red only in badges and icons. You can also make buttons more clearly "actions" by giving them a solid fill, while status badges use a tinted background with a colored dot or icon.
- **Don't rely on color alone.** About 8% of men have some red-green color blindness, and red and green are exactly your success and failure colors. Give every status an icon (check, X, clock, spinner) and a text label.
- **Check contrast.** Aim for at least 4.5:1 for text, in both light and dark themes.
- **Keep the saturation and tone of the status colors consistent**, and tune them to sit comfortably next to your brand red. That's where the on-brand feel comes from: a coherent palette, not borrowed colors.

If you'd like, I can draft a concrete palette with hex values for light and dark themes and check the contrast ratios.
