**Diagnosis:** every color is a mid-lightness, low-saturation yellow-olive, so nothing stands out from anything else. The problem isn't any one color. It's that they're all the same kind of color. I couldn't run code here, so the ratios below are hand-calculated estimates.

| Pair | Estimated contrast | Problem |
|---|---|---|
| Body text #a39b82 on background #cfc8b0 | about 1.7:1 | Needs 4.5:1. This is the biggest cause of the tired look, because the copy is barely readable. |
| Primary button #8a7f5c on background | about 2.4:1 | The main call to action barely separates from the page. |
| Secondary #7d8a6b vs primary #8a7f5c | about 1.1:1 | The two buttons look the same. |
| Links #9c8b5e on background | about 2.0:1 | Links are nearly invisible. They're also close to the body text (about 1.2:1), so they don't read as links. |
| Error #b5654a on background | about 2.6:1 | It's the only color with a different hue, but it's the same lightness as the rest, so it doesn't alarm. |

The background is also a darkish khaki, so the whole screen reads as dim. Warm and friendly usually means a light, creamy ground with dark text and a clearly saturated accent.

**Fix:** keep the warm olive and sage character, but spread the colors across lightness. Each button, link and error colour gets a clear lightness gap from the page.

| Role | New value | Estimated contrast / note |
|---|---|---|
| Page background | #f7f2e4 (warm cream) | Light ground |
| Body text | #2f2a1e (warm dark brown) | about 12.8:1 on background |
| Primary button | #3f6b4a fill, white text | about 5.5:1 against background, about 6.2:1 for text on the button |
| Secondary button | #e6ebd6 fill, 2px #3f6b4a border, #2f4a35 text | Reads as a clearly lighter, outlined button next to the solid primary |
| Highlight / links | #8f5a12 (deep amber), underlined | about 5.2:1 on background |
| Error | #b3261e | about 5.8:1 on background |

- **Errors:** amber links and the red error are close in lightness, so give errors an icon and the words "Error" or similar. Don't rely on color alone.
- **Hue shift:** I moved the primary from olive to a leafy green, since that carries "friendly" better. If the olive is part of your brand, use #5f6b2e instead (about 5.4:1 with white text, by my estimate). It keeps the hue and still passes.
