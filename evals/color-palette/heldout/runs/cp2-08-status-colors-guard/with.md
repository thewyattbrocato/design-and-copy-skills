Not for all four. Deriving the status colors from the brand palette will cost you on the dashboard.

- **Your brand red and "failed" would collide.** The primary buttons are #d93a35. A red "failed" badge next to a red "Deploy" button makes the main action look like an error, or the error look like an action.
- **People already read these colors a certain way.** Green means succeeded, red means failed, amber means waiting, blue means in progress. Off-brand hues make people stop and decode them, which is the wrong cost on a screen that people scan during an incident.
- **Keep the brand in the chrome.** Use it for buttons, links and the logo. Let the status colors be a separate semantic set.

Here's a set that keeps "failed" visibly different from the brand red. Contrast figures are my estimates, not computed.

| Status | Pill fill | Text/icon | Pair ratio | Icon + label |
|---|---|---|---|---|
| Running | #e3eefc | #1d4fa3 | ~7:1 | spinner, "Running" |
| Succeeded | #e0f3e8 | #17663f | ~6.5:1 | check, "Succeeded" |
| Failed | #fbe3e8 | #a31d3c | ~6.5:1 | ✕, "Failed" |
| Waiting for approval | #fdf0d0 | #7a4e00 | ~6:1 | pause or clock, "Awaiting approval" |

- **Failed is a crimson, not the brand red.** #a31d3c leans cooler and darker than #d93a35. It sits on a pale pink tint, so it doesn't look like a button. The icon and the word carry the meaning, so the hue difference only has to be enough, not large.
- **Use pale tint pills with dark text.** This keeps every pair readable and keeps the dashboard calm. Reserve solid saturated fills for the single row or banner that needs attention, such as a failed production deploy.
- **Amber needs dark text.** White on amber fails contrast, so the waiting state uses brown text on a cream tint.
- **Never rely on hue alone.** Every state has an icon and a label, so it still reads in grayscale and for red-green color blindness.
- **If you want it to feel on-brand,** tint your neutrals slightly warm to match the red, and use the same corner radius and type on the pills as on the buttons. That ties the statuses to the brand without borrowing its hues.

If you add a dark theme, don't reuse these values. Use the same hues with dark tinted fills and lighter text, and re-measure each pair.
