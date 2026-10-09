Not a good idea, at least for failed. Your brand red is also your button color, so a failed deployment would look like your primary action. Users would have to work out which red is "click me" and which is "something broke". If green, amber, and blue were pulled from the brand palette, they'd also have to be bent away from the hues people already read as success, warning, and in-progress.

I'd keep the brand palette for buttons and chrome, and use conventional status hues in a separate semantic set. The brand red stays on solid fills, and status uses tinted badges (pale fill, dark text, icon). That way the two reds differ in treatment as well as shade.

| Status | Text/icon | Tint fill | Icon + label |
|---|---|---|---|
| Running | `#1d5fd1` | `#e8f0fd` | spinner, "Running" |
| Succeeded | `#1a7f4b` | `#e6f4ec` | check, "Succeeded" |
| Failed | `#b42318` | `#fdeceb` | ✕, "Failed" |
| Waiting for approval | `#8a5300` | `#fdf3dc` | clock or pause, "Awaiting approval" |

- **Failed vs. brand:** `#b42318` is deeper and darker than `#d93a35`. Only brand red is ever a solid fill, and only failed uses the tinted red badge.
- **Contrast:** each text color on its tint should land around 4.5–6:1. These are my estimates and I haven't run a checker, so measure them before shipping. Dark text on pale tints leaves room to adjust within a family.
- **Not color alone:** every status has an icon and a word, so the set still reads in grayscale and for red-green color blindness. Running blue and succeeded green are close in lightness, which is one more reason the icon and label matter.
- **Dark mode:** don't invert these. Use lighter, calmer text colors on darker tints, and re-measure each pair.

If you'd like the brand to show up in the status set, put it in the layout rather than the hues. Rounded badge shapes, the type, and the card styling can all carry it.
