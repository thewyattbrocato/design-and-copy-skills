Your palette is already restrained and well suited to letterpress. The warm paper, one accent, and cool neutrals read as considered, and I wouldn't change the overall direction. Premium usually comes more from typography, space, and restraint than from the colors themselves, but a few specific tweaks would help.

**Contrast checks** (my hand calculations, roughly WCAG 2.x):

- **Ink on Paper:** about 13:1. Excellent for headings and body.
- **Muted on Paper:** about 4.9:1. Passes AA for body text, but it will drop below 4.5:1 on any darker or tinted background.
- **Rust on Paper:** about 4.8:1. Passes AA for normal text, just barely. Paper text on a Rust button is about the same, so it's fine.
- **Sage on Paper:** about 3:1. Fails for text. Keep it to rules, ornaments, and non-essential decoration.
- **Ink on Sage:** about 4.3:1. Slightly under 4.5:1 for small tag labels.

**Suggested changes**

1. **Never set text in Sage.** Use it only for rules, dividers, and ornaments. If you want Sage tags, either darken the fill a little (roughly 10–15% toward Ink) or use Sage as a 1px outline with Ink text.
2. **Underline your links.** Rust against Ink is distinguished mostly by hue, which doesn't work for everyone. An underline, or an underline that thickens on hover, makes links clear without making the accent louder.
3. **Consider a slightly earthier Rust.** #b4472a is a bit orange-leaning for a premium look. Something like #a44a31 or #9e4530 would feel more like pressed ink on cotton. This is a taste call, so test it next to your actual paper color.
4. **Make sure Ink and Muted separate by more than color.** They're both cool, mid-dark tones, so hierarchy should come from size, weight, or spacing as well. Otherwise captions can look like faded body text.
5. **Keep Paper warm and avoid pure white.** You're already doing this. Don't add pure white or pure black anywhere, including the page background, image borders, and shadows.

**What will matter more than the palette**

- **Typography:** a refined serif for headings (a classic letterpress-style face) with a quiet sans or serif for body text. This is usually the single biggest premium signal.
- **Space:** generous margins and line height. Cramped layouts look cheap regardless of colour.
- **Restraint with effects:** avoid heavy drop shadows, gradients, or obvious "paper texture" images. A subtle, real photograph of your prints will do more than any filter.
- **Photography:** shoot prints on a neutral surface in soft, even light. Your palette will look cohesive if the product photos share the same warmth.

If you want, I can draft a small CSS variable set with these colors, the adjusted tag and link treatments, and a contrast-checked focus style.
