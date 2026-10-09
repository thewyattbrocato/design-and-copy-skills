**I'd keep the status colors separate from the brand palette.** Brand colors are chosen for identity, not for meaning, so they usually don't give you four clearly different states.

The biggest problem is the red. If "failed" uses #d93a35, it's the same color as your primary buttons. Users will associate that red with "click this" as much as with "something broke," and a red CTA next to a red failed badge makes both harder to read.

Status colors need to do three things:

- **Be distinct from each other.** Failed and succeeded are the most important pair to separate. Red and green is the classic colorblind trap, so don't rely on hue alone.
- **Be distinct from the brand.** Primary actions and status signals should not share a color.
- **Hold up on the dashboard background,** in light and dark mode.

Here's a starting point to validate:

| Status | Hue | Example (light bg) |
|---|---|---|
| Succeeded | Green | `#1a7f37` |
| Failed | Deep red or crimson, darker than brand | `#b42318` |
| Running | Blue | `#1d5fd1` |
| Waiting for approval | Amber | `#b45309` |

Some practical rules:

- **Never use color alone.** Pair each status with an icon and a text label (✓, ✕, spinner, ⏸). This also covers colorblind users.
- **Use semantic tokens** like `status-failed` and `brand-primary`, mapped to hex values in one place. That lets the brand change without touching the status meanings.
- **Check contrast.** Text should be at least 4.5:1 against its background, and the status icons at least 3:1. The hex values above are starting points I haven't measured yet.
- **Define dark-mode variants** separately. The same hex values often won't work on a dark background.

If you want, I can run these through the color-palette skill to check contrast and colorblind separation, and propose a dark-mode set.
