---
name: visual-hierarchy
description: Use whenever a screen or page needs a clear order of importance, in any language and at any length - "nothing stands out", "it looks flat, busy or like a template", "what should be the main thing", "make it pop", "which button should win", "why does everything compete". Covers the focal point and first screen of a landing page, app screen, dashboard, settings page, card, pricing section, empty state, slide or poster; the steps between levels, one primary action, how loud a warning, badge, price or recommended plan is, and whether a shadow, gradient, border or icon earns its place. Not for spacing values, type sizes, palettes and contrast numbers, page grids, chart encodings or logos.
---

# Visual hierarchy

A view works when a stranger can say what it is for, what matters most and what to do next within a few seconds. Left to defaults, a design splits the difference between sizes, emphasizes everything and adds effects to feel finished. Replace that with a ranked order and visible, deliberate steps.

## When to use

Building, restyling or reviewing any composed surface where several things compete for attention.

## When not to use

- Not the numbers: spacing values (spacing-and-grouping), type sizes and ramps (typesetting), palettes and contrast floors (color-palette), page grids (layout-structure), chart encodings (chart-design). Use those skills if installed; otherwise ordinary judgment. For scored critiques use design-critique if installed.
- A one-line fix (a button is too loud, an icon sits low) gets only the matching check, not the whole method.
- Explicit user instructions, an existing design system and platform conventions win over every default here. Standard controls stay familiar; distinctiveness belongs in brand moments.

## Method

1. **Name the job and rank the content.** One sentence for what the view is for, then primary, secondary, tertiary and meta; three or four levels is normal. If two items cannot be ranked, pick one and say so in a line. Ask only when interactive and the answer changes the design.
2. **Order before style.** Picture everything in one size and weight. If position and grouping alone do not show the order, fix the structure; styling will not rescue it.
3. **Pull one lever per step.** Position and room first, then weight, size, value, color (see [contrast levers](references/contrast-levers.md)). The top element may take two; nothing needs four. Size alone gives huge headings over tiny text: use weight and value too.
4. **Make steps visible.** Neighbors differ by roughly 1.25 to 1.5 in size, a two-step weight jump, or a clear value gap. A one-step difference reads as a mistake, not a choice.
5. **Quiet the competition first.** If the main thing will not stand out and cannot get louder, soften what surrounds it: inactive nav, panel fills, secondary buttons, chrome. Subtracting beats adding.
6. **One boss per decision.** One primary action style per view or decision group; secondary quieter (outline or text); tertiary link-like. A destructive action that is not the page's main job gets quiet styling and sits apart; the confirmation step is where it becomes loud.
7. **Spend emphasis sparingly.** About a tenth of what is visible, one technique, used the same way every time. Pair color with a second cue.
8. **Share edges, repeat roles.** Every element shares an edge or axis with something; one primary text edge at the reading start. The same role gets the same treatment everywhere. A deliberate surprise only works against a consistent base. Optical fixes: [alignment](references/alignment-and-optical-fixes.md).
9. **Give every mark a job.** A line, box, shadow, gradient, glow, icon or illustration must organize, emphasize or identify. If removing it loses no information and no identity, remove it. Details: [decoration and depth](references/decoration-and-depth.md).
10. **Check, then hand back.** Run the quick checks below.

## Judgment calls

- **Centering.** Default: flush at the reading start, never a centered heading over flush-left text. Change for short, ceremonial or single-focus pieces (invitation, certificate, short hero, empty state): center everything in the group consistently and keep any paragraph over a couple of lines flush.
- **Drama by context.** Default: marketing, editorial and onboarding take large jumps in scale; dense tools, dashboards and tables use calmer steps and one clear focus per region. In a monitoring view never trade visible rows for bigger headings without a task reason.
- **Section titles in apps.** Default: a clear step up from body. Change when the title is only a label for something self-evident (a settings group): it can stay small, quiet or visually hidden, and the rows below carry the hierarchy.
- **Labels.** Default: drop a label the context already makes obvious, or merge it into the value ("12 left"). When a label stays, quiet it and give the value the weight. Change for spec-style pages where scanning the labels is the task.
- **Peer choices.** Default: one primary per group. For true peers (plan cards) the group shares one treatment, and the single recommended option gets a label plus structural emphasis (position, size, border weight), not color alone.
- **Fading.** Default: rank secondary text by size or weight, or a modest value step. Change only while it still clears the text contrast floor; never use a light weight on small text to quiet it, use a softer value or smaller size.
- **Decoration with identity.** Default: cut what has no job. Change when a device carries the brand or the mood asked for: keep it, quieter than the headline and the action.
- **Position by content.** Default: spend order and space before style. When the order is fixed (table, form, feed), rank with weight and value inside it.

## Do not produce

- A heading a few pixels larger than body, or every label bold, or three colored badges per card.
- Several solid primary buttons; a red destructive button louder than the main action.
- A centered headline over left-aligned paragraphs.
- A hero plus identical bordered cards each topped by an icon in a colored circle: rank the features, drop the boxes, and keep an icon only if it carries meaning.
- Gradient backdrop, glass panel, glow and shadow stacked on one surface; decorative blobs; an illustration louder than the headline.
- Made-up proof to fill a hero or pricing block: customer counts, logos, ratings, testimonials, stats, prices, deadlines, "only N left". Use a visible placeholder such as "[customer count]" or leave the slot out, and still deliver the full design.

## Output discipline

- Deliver the requested thing first: the code, the ranked fix list, or the one pick. When a count, a set or a word limit is given, deliver exactly that, and check the count rather than asserting it.
- After it, at most two one-line notes (an assumption, or the one trade-off that matters), unless more is asked for. No tour of the method.
- Reviews: findings in order of effect on the task, each as what you see, what it costs the viewer and the fix. Name what already works and leave it alone. If the existing design already holds, say so and change only what fails.
- Rewriting a design that works is the common failure of polish requests: touch the parts that break the order, keep the rest, content included.

## Quick checks

- Blur or squint: what remains should be the intended primary, then the secondary group.
- Grayscale: the order should survive; if a status or recommendation vanishes, add a second cue.
- Five seconds: could a stranger say what to do? Point to the element that serves the job.
- Count loud things per group and emphasized share; count distinct left edges.
- Put two neighboring levels side by side; if you must look twice, widen the step.
- Name each decorative mark's job; delete those without one.

## References

- [references/contrast-levers.md](references/contrast-levers.md): load when two levels look alike or you are choosing how to separate them; lever strengths, combining, starting steps, text colors and weights.
- [references/alignment-and-optical-fixes.md](references/alignment-and-optical-fixes.md): load when edges look off, or when centering icons, numerals and bullets.
- [references/decoration-and-depth.md](references/decoration-and-depth.md): load when a design uses shadows, gradients, glass, illustration, icon sets or text over images.
