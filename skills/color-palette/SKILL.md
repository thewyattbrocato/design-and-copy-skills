---
name: color-palette
description: Use whenever color is being chosen, judged or fixed, in any language and at any length - "make it look more professional, premium, calm or bold", "less generic", "the colors feel off, muddy, garish or hard to read", a dark mode, brand or status colors, a palette from nothing or from one given color. Covers lead color, neutrals, accents, tonal ramps, contrast pairs, text on images, gradients, themes, print versus screen, in CSS, HTML, tokens or a description. Not for chart data scales (chart-design), logo design (brand-identity), token plumbing (design-system-builder) or type weight (typesetting).
---

# Color palette

A color is a relationship, not a hex code: the same value reads differently on a tinted card, beside a neighbor, over a photo or on dark. Choose few colors on purpose, give each a job and test every pair where it will sit. Unguided color defaults to a stock indigo, five equal accents, pale gray text and a gradient to feel finished.

## When to use

Choosing a palette for a screen, page, product, deck or graphic; fixing weak contrast, too many accents, muddy ramps, clashing edges or a flat or garish theme; status and interactive colors; dark themes; text over images; color for a given audience or print process. A short request ("make this look less like a template") is not a small one. After any interface build, use it as a last pass on the colors chosen.

## When not to use

- Scales inside charts: chart-design if installed. This skill still covers the interface around the chart.
- Logo and mark color: brand-identity if installed. Token tiers and theming plumbing: design-system-builder if installed. Type weight on dark grounds: typesetting if installed.
- Color-critical tools (photo, video, illustration, print proofing): keep the surround neutral and the brand color to small accents and selection, because surrounding color changes how the work is judged.
- Working color. If the roles, pairs and accents already hold, say so and change nothing, or only the pairs that fail, by the smallest move. A user's palette, brand guide, design system or platform convention wins: keep it and report failing pairs with a fix.
- A fix request changes colors only. Keep the markup, copy and features; do not add elements (status tags, icons, sections) nobody asked for.

## Rules that change the output

- **Lead and structure.** Name the audience and the job, then choose a lead with a reason that is not "it pops". Default for products: tinted neutral base, one lead, a semantic set. Co-equal hues only when roles are co-equal (calendars, departments). A loud multicolor or clash brief (festival, kids, campaign) stays vivid: one dominant color, a few supporting, one action color, readable text on every ground. A category cliché is allowed on purpose.
- **Quantity before hues.** Decide what dominates by area, what repeats, what appears once; white and near-black count. Light saturated colors need less area than dark quiet ones. On a phone one accent button can fill the view, so keep it small.
- **Neutrals.** Lean grays toward the lead's temperature, raising saturation slightly at both ends so the temperature stays even; start from dark gray rather than pure black for large areas. Separate surface levels by small steady lightness steps.
- **Ramps.** Build in a perceptual space, not even HSL or RGB steps; middle steps must look like real colors. Details in [ramps and roles](references/ramps-and-roles.md).
- **Measure pairs, do not eyeball.** Cross-hue lightness judgments are often wrong. Test each text, icon and border pair on the surface it actually sits on (tint, hover, selected, banner, image, footer, disabled), with the ratio stated. The ratio comes from the accessibility standard in force: about 4.5 to 1 body text, 3 to 1 large text, icons, focus rings and control edges; confirm the version.
- **Edges: lightness first.** Strong hue contrast at near-equal lightness makes text vibrate; neighbors at equal lightness lose their edge. Anything read, counted or clicked needs a clear lightness gap. Small, thin or pale items need more separation than large ones.
- **Fix contrast in the family.** Move one or two ramp steps. If white on a mid fill fails, try dark text, or flip to dark text on a pale tint. On a colored panel, make secondary text a hue-matched tint, not translucent white, which looks disabled. Do not retreat to black and white.
- **Roles are separate.** Danger is not the brand color; if the brand is red or pink, differ by shade, icon and words. Hover and selected are different jobs. Meaning never lives in hue alone: add an icon, label, sign or shape, then check grayscale and red-green.
- **Text on images.** Scrim, overlay or a quiet patch, checked at the brightest or busiest spot under the text, not the average.
- **Gradients and glows.** Only with a job (a brand moment, depth, data), narrow in hue, never under body text; no stock purple-to-blue wash.
- **Dark themes are a new ground.** Layered dark gray surfaces, off-white text, accents lighter or calmer so they do not glare, status colors remapped, every pair re-measured. Prove it: a dark token should land on the matching step of the light ramp. Respect the system preference and allow an override.
- **Meaning and medium.** Name the audience; companions and region change what a hue means. Never encode gender. Screen values are not print values, and spot, foil and metallic inks are not a hex. Details in [grounds, dark, meaning and print](references/grounds-dark-and-media.md).

## Missing facts

If no brand color, audience or medium is given, choose, say so in one line ("no brand color given: I chose X because Y") and still deliver the full work. Ask once, with defaults, only when interactive and the build is large; never reply with only questions. Never invent the user's current colors, brand guide, audience or a contrast figure. If you cannot run code, say the ratios are estimates.

## Do not produce

- A framework-default blue or indigo as "the brand", or a purple-to-blue gradient hero.
- Five or more equally loud accents on one screen.
- Pale gray body text, placeholders or labels below the floor.
- The brand color reused as the error color.
- Status by a colored dot, or by red and green numbers, alone.
- A ramp made by even HSL lightening; a dark theme made by inverting values.
- Contrast checked on white when the text sits on a tint or photo.
- Brand color across the panels of a color-critical tool.
- A vivid brief muted into gray plus one blue.
- Made-up proof on a page built to show a palette (customer counts, ratings, quotes, prices, deadlines): use a visible placeholder or leave the slot out, and still deliver the full design.
- A critique that invents problems in colors that work, or a fix with no value ("darken a step" without the hex).

## Output discipline

Deliver the requested thing first (the palette, the CSS, the fixed values, the pick), no preamble and no tour of color theory, because notes and theory bury the values the reader came for. When a count or set is asked for, give exactly that: three palettes differ in lead and structure, not in shade. Honor any length cap; drop the lowest-value point instead of shrinking all of them, and count rather than assert. A palette shows each color with value, role and reason, plus the ratio of the pairs that matter. A critique lists findings by impact, each with the fix as a value and where it applies. After the work, at most two one-line notes (an assumption, the one trade-off), unless more is asked.

## Quick checks

- One reason for the lead; one color dominates by area; the accent stays small.
- Every pair measured on its real ground, including hover, selected, banners and footers.
- Grayscale and red-green simulations still read; status carries an icon or word.
- Ramp steps look even; dark theme layered and re-measured.
- Text on images and gradients readable at the worst spot.
- Given brand color, system and instructions kept; working color left alone and said so.
- Option count and length cap met.

## References

- [references/ramps-and-roles.md](references/ramps-and-roles.md): load when generating tonal scales or neutrals, mapping colors to surfaces, text levels, states and status sets, or computing contrast.
- [references/grounds-dark-and-media.md](references/grounds-dark-and-media.md): load when colors misbehave in place, for dark themes, images, vibration, dense patterns, audience meaning, naming, or screen versus print.
