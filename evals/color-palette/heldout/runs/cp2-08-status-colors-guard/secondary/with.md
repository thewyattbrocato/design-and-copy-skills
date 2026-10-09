**Not a good idea, at least not for the status colors.** Brand palettes are built to express identity, and status colors have to carry meaning fast. Three problems:

1. **Your brand red is already the failure color.** Red means "error" to most people. If `failed` uses the brand red and your primary buttons use it too, a red "Retry" button sits next to a red "Failed" badge and the two compete. Users will read the button as a warning.
2. **Brand colors are often similar in hue and lightness.** Brand palettes commonly include several reds, oranges, or purples that look nearly identical as small dots or badges. Running, waiting, and failed need to be clearly distinct at a glance.
3. **Status colors need to be tuned for the job.** They have to pass contrast on the dashboard background, work for color-blind users, and match each other in lightness. Brand colors aren't chosen for any of that.

**What I'd do instead:**

- **Keep the brand red for actions and identity only** (buttons, links, logo, focus accents).
- **Use a separate, semantic status set**, one hue per state:

| Status | Hue | Example starting point |
|---|---|---|
| Running | Blue | `#2f6fdb` |
| Succeeded | Green | `#1e8a4c` |
| Failed | Deep red or crimson | `#b42318` |
| Waiting for approval | Amber | `#b54708` (text) / `#f79009` (fills) |

- **Never rely on color alone.** Pair each status with an icon and a text label (spinner for running, check for succeeded, ✕ for failed, clock or hand for waiting). This matters for color-blind users and for anyone scanning quickly.
- **Make the failed red visibly different from the brand red** (darker, or shifted toward crimson), and keep it away from primary buttons, or make the primary button a different color if you want them to coexist.

These hex values are starting points, not validated. I haven't checked contrast against your actual backgrounds or the color-blind simulations. If you want, I can run them through the color-palette skill to check contrast and separation in light and dark modes.
