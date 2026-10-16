**Not for these four. Use the brand red for buttons and identity, and give statuses their own conventional hues.**

Your brand is red, and red already means "failed" on a deployment dashboard. If statuses come from the brand palette, a red "Create deployment" button sits next to red "Failed" badges and users can't tell an action from an error. The other three statuses would also need hues that read as running, succeeded and waiting, and a brand palette rarely has those. People expect blue or teal for running, green for success and amber for waiting. Following that convention means nobody has to learn your colors.

You can still make the set feel on-brand without borrowing hues. Give the greens, blues and ambers the same saturation and the same slightly warm neutrals as your red. Use tinted pill badges, not solid fills. Solid red then always means "click this", never "something broke".

| Status | Text/icon on tint | Tint background | Icon + label |
|---|---|---|---|
| Running | `#1458a8` | `#e8f1fc` | spinner or progress arc, "Running" |
| Succeeded | `#17663a` | `#e6f4ec` | check in circle, "Succeeded" |
| Failed | `#a3201c` | `#fdeceb` | ✕ in circle, "Failed" |
| Waiting for approval | `#8a5a00` | `#fdf3dc` | pause or clock, "Awaiting approval" |

- **Contrast:** Each text color on its tint is about 5.5 to 7 to 1, so it clears the 4.5 to 1 body-text floor. Those figures are my estimates, because I haven't run a contrast checker. Please verify them before shipping.
- **Failed vs. brand red:** The failed red is a deeper, darker shade than `#d93a35`. It always appears as dark text on a pale tint, with an ✕ icon and the word "Failed". It never appears as a solid fill or as a button.
- **Not by color alone:** Green and red come out at similar lightness, and they are the pair most likely to be confused in red-green color blindness. The icon and label carry the meaning, so the badges stay readable in grayscale.

I assumed a light UI. For a dark theme, the status colors need to be remapped and re-measured, not inverted.
