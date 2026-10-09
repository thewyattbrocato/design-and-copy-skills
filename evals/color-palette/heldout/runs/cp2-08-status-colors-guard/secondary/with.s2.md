I wouldn't pull the status colors from the brand palette. Brand palettes are built for identity, so they usually lack the semantic set you need, and brand red collides with failure.

- **Red means both brand and failure.** Your primary buttons will look like error alerts, and a failed deploy won't stand out from the page chrome.
- **Brand colors are often ambiguous as statuses.** A brand palette may have no clear green, blue, or amber, and similar hues make "running" and "waiting" hard to tell apart.
- **Color alone fails some users.** Red/green is the classic problem for color-blind users, so each status also needs a shape and a label.

I'd use a separate, semantic status set and keep brand red for actions:

| Status | Hue | Cue beyond color |
|---|---|---|
| Succeeded | Green | Check icon, "Succeeded" |
| Failed | Red, distinct from brand (deeper or more orange) | X icon, "Failed" |
| Running | Blue | Animated spinner, "Running" |
| Waiting for approval | Amber | Pause or clock icon, "Waiting" |

The failed red is the one to test. Put a primary button and a failed badge side by side. If they read as the same kind of thing, shift the failed hue further from #d93a35 or make the button less alarming.

Exact hex values need contrast checks for text on your light and dark backgrounds, which I haven't done here. I can build and check the full set, including dark mode, with the color-palette skill if you want.
