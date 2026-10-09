## Why it happens

Contrast depends on the lightness difference between text and background, not on how "bright" the text color looks. The tan banner is darker than white, so every text color loses some contrast on it. I computed WCAG contrast ratios by hand from your hex values:

| Text | on white | on tan #e9dcc3 |
|---|---|---|
| Red #d92d20 | ~4.8:1 (passes AA) | ~3.6:1 (fails 4.5:1) |
| Green #12b76a | ~2.6:1 (fails) | ~1.9:1 (fails badly) |

- **Red:** it only just clears AA on white. The tan is darker, and it's also a warm hue close to red. That removes the hue contrast that helped on white, which is why it looks muddy.
- **Green:** #12b76a is a mid-lightness color, and the tan's lightness is high but not far above it. Their luminance is close, so the text nearly disappears. It's also borderline on white. It looks fine there mostly because it's bold or large, or because an icon carries the meaning.

## What to do

1. **Darken the text colors until they clear 4.5:1 on the darkest surface they appear on (the tan).** Then they pass on white too. Approximate values from my calculation, which you should check with a contrast tool:
   - Error: `#b42318` (~4.9:1 on tan, ~6.6:1 on white)
   - Success: `#05603a` (~5.7:1 on tan, ~7.7:1 on white)

   The original brighter colors can stay for fills, borders and icons, where the bar is 3:1.

2. **Make them semantic tokens, not raw hex values.** For example, `--text-error` and `--text-success` hold the dark shades, while `--fill-error` and `--fill-success` hold the bright ones. If the banner ever needs a different shade, you can override the token per surface instead of fighting it in components.

3. **Don't rely on color alone.** Add an icon (✕ or ✓) and clear wording. Red and green are also the pair most likely to be confused in color-vision deficiencies, and the icon helps when contrast is marginal.

4. **Consider changing the banner.** If you'd rather keep the brighter text colors, a lighter, more neutral banner background (closer to white) would raise contrast for all of them. Even then, the green would need darkening to pass on white.

I haven't looked at Plumbline's code, since only the colors came up. If you point me to the stylesheet or token file, I can make the change.
