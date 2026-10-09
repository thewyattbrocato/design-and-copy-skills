Not for status colors. Your brand is red, and red already means "failed" on a deploy dashboard.

- **Buttons read as danger.** A red "Deploy" button looks like a destructive action, and a red "Failed" badge looks like a brand element.
- **Failures get lost.** If brand red is everywhere, a failed deployment no longer stands out.
- **Status colors drawn from the brand palette** would be tints and shades of the same hue family, so they'd be hard to tell apart at a glance.

Keep the brand red for buttons, links and focus, and give statuses their own conventional hues. Make them feel on-brand through matching saturation and lightness, not shared hues.

| Status | Text/icon | Tint fill | Icon + label |
|---|---|---|---|
| Running | `#1f6fd1` blue | `#e6f0fc` | spinner, "Running" |
| Succeeded | `#1a7f4b` green | `#e3f4ea` | check, "Succeeded" |
| Failed | `#b3261e` deep crimson | `#fbe7e6` | ✕, "Failed" |
| Waiting for approval | `#8a5a00` dark amber | `#fff3d1` | pause or clock, "Awaiting approval" |

- **Failed vs. brand.** The crimson is deeper than `#d93a35`, so the two differ by shade. The ✕ icon and the word "Failed" carry the rest. Don't use `#d93a35` for failed.
- **Amber is dark.** Light amber text on white fails contrast, so the amber status uses dark amber text on a pale tint.
- **Not color alone.** Each status has its own icon shape and label, so they still read in grayscale and for red-green color blindness.
- **Contrast.** By my estimate, each text color is about 5:1 or better against its tint. I can't run a checker here, so verify with a contrast tool before shipping.

If you want the statuses to feel branded, tint your neutrals slightly warm and share corner radius and badge styling. Dark mode needs its own lighter versions of these four, re-measured on the dark surfaces.
