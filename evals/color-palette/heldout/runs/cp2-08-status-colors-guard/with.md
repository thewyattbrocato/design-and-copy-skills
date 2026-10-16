Not a good idea, and it's riskier for you than for most products.

- **Your brand red is the status color for "failed."** Red already means failed or danger, so a red primary button next to a red "Failed" badge makes "Deploy" and "something broke" look alike. People shouldn't have to wonder whether a red element is an action or an alarm.
- **Brand-derived hues make statuses hard to tell apart.** Tints of one palette sit close together, and people scan status columns quickly. Status colors need to be clearly different from each other, and users expect green to mean success.

**What I'd do:** use conventional status hues and keep the brand red for actions and identity. Make failed visibly different from the button red through form, not hue:

| Status | Badge text | Badge fill | Icon + label |
|---|---|---|---|
| Running | `#1d6fd1` | `#e8f1fc` | spinner, "Running" |
| Succeeded | `#1a7f4b` | `#e6f4ec` | check, "Succeeded" |
| Failed | `#9f1f1b` | `#fdecea` | ✕, "Failed" |
| Waiting for approval | `#8a5a00` | `#fff4d6` | pause or clock, "Waiting for approval" |

- **Failed is a darker red than `#d93a35`.** It only ever appears as a pale tinted badge with an ✕ and a word. Your brand red stays a solid fill on buttons.
- **Each status carries an icon and a label, not just color.** That keeps the set readable for red-green colorblind users and in grayscale.
- **Amber text is the dark `#8a5a00`.** Bright amber text fails contrast on light backgrounds.
- **Contrast is about 5:1 or better for each text color on its own fill.** These are my estimates, not measured, so run them through a checker before shipping.

**Where to keep it on-brand:** use the neutrals and surfaces. Give the grays a faint warm-red tint, and use the brand red for buttons, focus, and the logo. Then the status colors read as a separate layer.

I assumed a light theme. Dark mode needs these remapped to lighter, calmer values and re-measured.
