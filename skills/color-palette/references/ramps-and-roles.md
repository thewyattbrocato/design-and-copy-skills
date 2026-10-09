# Ramps and roles

Load this when generating tonal scales or neutrals, mapping colors to jobs, or computing contrast.

## Ramps

- Work in a perceptual space (OKLCH or similar), not HSL or RGB: equal numeric steps there are not equal to the eye. If only HSL is available, tune by hand.
- Eight to twelve steps for a hue that carries a product, five or six for one accent. Steps that look equal change in proportion, not by equal amounts: small moves near the light end, larger ones toward the dark end.
- Ease chroma toward both ends. Keep it too high and the top looks neon and the bottom sooty; drop it too far and the shades look washed out.
- To lighten a saturated color, rotate its hue slightly toward a brighter neighbor (toward yellow, cyan or magenta); to darken, toward a darker one (red, green, blue). Stay within about 20 to 30 degrees. Darkening yellow toward orange keeps it warm; straight darkening turns it to mud.
- Keep the same step number at the same lightness across hues, so a step-600 green and a step-600 red carry equal weight.
- Generate, then tune by eye, then freeze. Adding a shade should be rare; if you add many, the scale has dissolved.
- Neutrals are a ramp too: eight to ten steps, a trace of the lead's hue, saturation slightly higher at both ends.
- Check evenness in grayscale: adjacent steps should differ by a similar visible amount, with no two nearly the same.

## Surfaces, text and borders

- Four or fewer surface levels (page, card, raised, overlay), each a small lightness step. A white card on a slightly tinted page is often enough; add a hairline only where the step is too subtle.
- Three text levels: primary near-black, secondary clearly lighter but still at the body floor, tertiary for metadata that still clears the floor when it informs. Pale gray "because it looks quiet" fails first; quiet text with a smaller size or a softer value, not a thinner weight.
- Borders that only decorate may sit below the text floor; borders that mark an input or control need about 3 to 1 against the neighboring ground. Strengthen a faint border by thickening it, not by darkening it harshly.
- Links differ from body text by more than hue (underline, or a clear lightness step plus weight) and are measured on the real surface.

## The accent

Reserve it for the primary action, the current selection and a few emphasis points. Check text on the accent fill both ways: white on a mid-tone often fails and dark text may pass. If the accent is also the link color, confirm it on the page and on tinted surfaces. To highlight within a set, mute everything else and let one color speak.

## States

- Hover: one step darker or lighter, same hue. Pressed: two steps. Focus: a ring at about 3 to 1 against both the element and the ground, not a fading shadow.
- Selected: a tint plus a marker (bar, check, heavier border). If hover and selected are both a pale accent tint, people cannot tell which row they are on.
- Disabled: lower contrast but legible, with a non-color cue; never the same look as selected.

## Status sets

Five roles: success, warning, danger, information, neutral. Per role keep a fill for badges and large areas, a text color for light surfaces and a text color for use on its own tint. Use nameable hues, one icon or word each, and the same ramp step for every fill so none is louder by accident. The failure state is the most salient in a mixed list; waiting and canceled stay neutral and quiet; in-progress can use motion or a shape. Amber and yellow text on white is rarely readable: use a darker amber for text, bright yellow for fills with dark text on top.

## Contrast

Floors (re-check the standard your product must meet): body text about 4.5 to 1; large text (about 24px, or 19px bold), meaningful icons, focus rings and control boundaries about 3 to 1; text on a tinted banner 4.5 to 1 measured on the tint; placeholders that carry instructions at the body floor.

Compute, do not eyeball. Per channel c in 0 to 1: linear = c / 12.92 if c is about 0.04 or less, else ((c + 0.055) / 1.055) ^ 2.4. Luminance L = 0.2126 R + 0.7152 G + 0.0722 B. Ratio = (lighter L + 0.05) / (darker L + 0.05). Flatten any transparent color onto its real ground first. Measure on every surface the pair meets. When fixing, report before and after values.
