Three things are wrong, and they compound.

**1. Everything shares one hue and one lightness.**
Every color except the error red sits around 45° on the hue wheel (khaki/olive). All of them are also low-saturation and mid-lightness. Nothing is light, dark, or vivid enough to stand out, so the page reads as a single beige-brown smear. That's the muddy look you're seeing.

**2. Contrast is too low for text and for controls.**
These are my approximate WCAG ratios:

| Pair | Ratio | Target |
|---|---|---|
| Body text `#a39b82` on background `#cfc8b0` | ~1.7:1 | 4.5:1 |
| Links `#9c8b5e` on background | ~2:1 | 4.5:1 |
| Primary button `#8a7f5c` vs. background | ~2.4:1 | 3:1 |
| White label on primary button | ~4:1 | 4.5:1 |
| Error `#b5654a` on background | ~2.5:1 | 4.5:1 |

Body text at 1.7:1 is the biggest problem. It looks faded and tired, and many people won't be able to read it. For a health app, that's an accessibility and trust issue.

**3. The roles aren't distinguishable.**
- The primary and secondary buttons have nearly the same lightness and saturation, so users can't tell which action matters.
- Links (`#9c8b5e`) are almost the same color as body text (`#a39b82`), so they don't read as clickable.
- The error color is the only one with a different hue, but it's as dim as everything else.

**How to fix it**
Keep the warmth, but add real lightness contrast and one or two distinct accent hues. Here's a starting point. These are my estimates, so run them through a contrast checker before you commit.

- **Page background:** `#FBF6EC` (warm cream, much lighter)
- **Body text:** `#3A3128` (dark warm brown, roughly 11:1)
- **Primary button:** `#1F7A6D` (deep teal) with white text, roughly 5:1
- **Secondary button:** white or cream fill with a teal border and teal text, so it's clearly lower in the hierarchy
- **Links:** the same teal as the primary, underlined
- **Highlight:** a warm amber like `#F2A63B`, used for badges and accents, not for text
- **Error:** `#B3261E` on a light background, paired with an icon so it doesn't rely on color alone

The warmth comes from the cream and brown neutrals, and the friendliness comes from the saturated teal and amber accents. You can swap the teal for a terracotta like `#C2531F` if you want it warmer, but check that white text on it passes 4.5:1.

I can also put together a quick HTML swatch page that previews the old and new palettes on a mock screen.
