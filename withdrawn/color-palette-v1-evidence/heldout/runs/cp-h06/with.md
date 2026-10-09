**Why it happens**

Contrast depends on the surface the text sits on, not on the text color alone. The tan banner is much darker than the white form, and its hue is close to red's. I computed the WCAG contrast ratios by hand:

| Text | on white form | on tan #e9dcc3 | 4.5:1 target |
|---|---|---|---|
| Red #d92d20 | 4.8:1 | 3.6:1 | fails on tan |
| Green #12b76a | 2.6:1 | 1.9:1 | fails on both |

- **Red:** The banner's luminance is about 0.72, against 1.0 for white, so the same red loses about a quarter of its contrast. Red is also a warm hue sitting on a warm yellow-orange ground. With less lightness difference and no cool-versus-warm difference to help, the edge goes soft and the red looks muddy.
- **Green:** #12b76a is a mid-light green with a luminance of about 0.35, close to the tan's 0.72. At 1.9:1 there is almost no lightness edge, so the text nearly disappears. It also only reaches 2.6:1 on white. It looked acceptable there only because white is the easiest ground.

**What to do**

Use darker text colors from the same hue families, so the same value works on both surfaces:

| Role | Value | on white | on tan |
|---|---|---|---|
| Error text | `#b42318` | 6.6:1 | 4.9:1 |
| Success text | `#05603a` | 7.7:1 | 5.7:1 |

These ratios are hand-computed, so run them through your contrast checker before shipping.

- **Keep the bright colors for non-text uses.** Use `#d92d20` and `#12b76a` for fills, borders or large icons only where the ground allows it. On the tan banner, neither reaches the 3:1 icon minimum (the green reaches 1.9:1).
- **Don't rely on hue alone.** Pair each message with an icon and a word ("Error:", "Saved"). Red and green are also the pair that red-green color-blind users confuse.
- **Optional:** If you'd rather keep the brighter text colors, lighten the banner to a pale tint such as `#f7f0e1` and re-measure. The text pairs may still fall short of 4.5:1, especially the green. Darkening the text is the safer fix.

Assumptions: I took 4.5:1 as the target for message text, and I haven't seen the Plumbline code or the banner's other states, such as hover or dismiss.
