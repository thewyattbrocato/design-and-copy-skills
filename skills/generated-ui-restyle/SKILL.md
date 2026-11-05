---
name: generated-ui-restyle
description: Use whenever a screen, page or component looks machine-generated or like an untouched starter template and should look designed for its own product, in any language and any words - "this looks vibecoded", "it screams AI", "looks like every other SaaS", "make it ours", "less template-y", or a new page that must not have the usual AI look. Restyles HTML, CSS, Tailwind or components while keeping the content, features and section order - names the generic tells, decides how much to change (sometimes nothing), writes a short brief from what the product deals in, reworks the layers starting from the words (structure, emphasis, color, type, icons, details, imagery, motion), then checks the result could not pass for a rival's. Also answers "does this look AI-made, and what gives it away". Not for missing states or accessibility on a look that works (ui-polish-pass), scored critiques (design-critique), logos (brand-identity), one layer alone such as a palette (color-palette), or one named fix.
---

# Generated UI restyle

A generated screen is recognizable before anyone reads a word, because it carries the same choices every other generated screen carries. A restyle works when the screen could only belong to this product and still says exactly what it said before. The default failures run both ways: stripping the effects and leaving a plain gray copy of the same template, or turning the request into a redesign that drops content, invents proof and trades one fashionable effect for another.

## Do not produce

- A screen that changes what the product is: new sections, features, claims, customer counts, ratings, testimonials or data the original did not have. Filler (lorem lines, patterned numbers) may give way to believable sample content of the same shape.
- The same template with its effects removed. It now looks like the kit's own demo page: correct, neutral and nobody's.
- An effect or flourish with no job that the decision notes can name, whether it is new or stands where a removed one was.
- A heavy restyle of a screen that was already designed, or a changed product name or real logo.
- A list of tells and no restyled screen when a restyle was asked for.

## When to use

- Existing code or a described screen looks AI-made or like a kit default, and the person wants it to look like their product: an app screen, dashboard, settings page, landing page, pricing section, sign-in, empty state.
- A new screen or page is requested with an explicit wish that it not look generic or generated.
- Someone asks whether a screen looks generated and what gives it away.

## When not to use

- The look already works and the gaps are states, edge cases or access: ui-polish-pass. A judged or scored review of a whole design: design-critique. Logos and marks: brand-identity. Each skill if installed.
- One layer only (a palette, a typeface, the grid, motion, one chart, the words): color-palette, typeface-selection or typesetting, layout-structure, ui-motion, chart-design, editing-and-cutting or ux-microcopy, if installed.
- A single fix inside a generic screen ("make the button less purple") gets that fix and nothing else.
- A deliberate style (loud, playful, retro, raw, maximal) is judged against its own intent. It is not flattened into calm neutrals.
- Explicit user instructions, an existing design system, a real brand guide and platform conventions win over every default here. A brand that really is purple, or really uses gradients, is a brand.

## Scope the job

The request sets the size first and the evidence second. Do not widen a narrow ask into a sweep.

- **A question** ("does this look generated?"): answer with the diagnosis only (see Output). No restyled code unless asked.
- **A named part** (the hero, the card row, "the colors"): restyle that part and what it forces in its neighbors. Leave the rest as it is, and mention in one line any tell you saw and left.
- **A whole screen, a page, or a new build:** all the passes below.
- **A screen with no tell on it:** say so in a sentence, name what works, and change nothing.

## Procedure

1. **Read the screen as people meet it.** Render it if you can, and read the code for values. Collect the source material for every later choice: the words on the page, the headings and column names, the objects the data is about, and whatever the person said about who uses it and where.
2. **Name the tells, with places.** One line each: the tell and where it sits (component, selector or region), grouped by cause using [tells by cause](references/tells-by-cause.md). The cause says what goes in the tell's place. Something with a job (a brand color, a status that pulses because it is live) is not a tell.
3. **Write the decision notes.** A short list pairing each large choice (neutrals, accent, face, the shape of the lead area, the sample data, imagery) with the source it comes from. A choice with no source is a default, and defaults are what you are removing. How to find sources and what counts as one: [choices and sources](references/choices-and-sources.md).
4. **Restyle in passes, ordered by what depends on what.** Shared values come before the places that use them, and the fill comes last. Take each pass through the whole screen before the next, since each changes how the next reads.
   1. **Words and data.** The page's text decides how much room everything else needs, so it is settled first. The headline names the result and the reader in the product's own nouns. Whatever would read the same on a rival's screen goes: stock enthusiasm, vague superlatives, figures without context, proof nobody can check (ux-microcopy, headlines-and-leads, honest-claims).
   2. **Shared values.** Put the choices from the notes into the variables or tokens the project uses, once: neutrals and one accent with measured pairs (color-palette), face and weights (typeface-selection), sizes and figure formats (typesetting), one spacing scale (spacing-and-grouping), a short radius scale (design-system-builder). Later passes read from these; a value typed inline again is how a screen drifts back to cause 3.
   3. **Arrangement and emphasis.** The sections stay in sequence. Replace a stock arrangement (a centered stack, a row of equal cards) only where it hides how the content relates (layout-structure). One focal point per view, one primary action per decision, meta set quiet, the frame quieter than the content (visual-hierarchy).
   4. **Parts and fill.** Icons, counts, badges, every state of every control, then imagery: [components and details](references/components-and-details.md).
   5. **Motion.** Keep what explains a change; remove loops and decoration (ui-motion).
5. **Re-walk, then check.** Look at the screen again with the final text, at a narrow width and in every state the restyle touched (responsive-layout), then run the checks below.

## Judgment calls

- **Brand or default.** Default: a color, face or mark the product really owns stays and leads, and the restyle spends it with intent. Change when the "brand" is only the generator's starting look and nobody claims it (brand-identity separates the two). When unsure, keep it and say so in one line.
- **Density.** Default: keep the density the screen has, because the people who use it daily set it by use (interface-behavior). Change when the original spends its rows on filler. Never trade visible rows or columns for character.
- **Theme.** Default: keep the light or dark theme the screen has and make it a good version of that theme. Change only when asked.
- **Patch or rewrite.** Default: change values and classes, keep the markup, ids and component names. Change to a full rewrite when most lines change anyway; content and structure still match the original.
- **Claims already on the page.** Default: they are the person's content; keep them, set them plainly (no stars, avatar stacks or glowing badges around them), and list any that need a source in a note. Change when a claim is clearly filler (a lorem line, an impossible round number): replace it with a labeled placeholder, not a better-sounding invention.
- **A new build.** Default: write the notes from the request, then build in the same pass order; the request's facts are the only facts. Change when the person supplies a brand guide or design system: build inside it and let the notes only choose within it.

## Missing facts

Never invent a customer count, rating, testimonial, award, client logo, price, feature, date or metric. Sample data in a preview is plausible and labeled as sample where someone could take it for real. If the product's audience or subject matter is unclear, infer it from the page's own words, state the guess as the first line of the notes and still deliver. Ask once only if the chat is interactive, the restyle is large and the answer would change the notes; never answer with only questions.

## Output

- Lead with the work: the restyled code or screen. Return the whole file when most of it changed, otherwise the changed parts.
- Then the decision notes, four lines or fewer for a small job, and at most two one-line notes: what to confirm (a claim, a brand question) and what you did not check.
- Asked only what looks generated: the tells ranked by how much each makes the screen read as generic, each with its place and a concrete fix, opened by one line on what already works.
- A requested count or length cap is met exactly; count rather than assert.

## Quick checks

Three comparisons before handing back.

- **Against the original.** Name, content, features and section order are unchanged unless the person asked otherwise. No number, name, claim, logo or feature appears that the material did not supply. A named-part job touched only that part.
- **Against the notes.** Pick any three visible choices; each traces to a source in the notes. Each pass drew its values from the shared ones: spacing from one scale, siblings matching, text and accent pairs (hover, selected and focus included) above the contrast floor on the surfaces they sit on.
- **Against a rival.** Put a rival's name on the screen. If nothing else needs to change, the sources were too thin: go back to step 1 and gather more of the product's own nouns. Do not add effects to fix it.

## References

- [references/tells-by-cause.md](references/tells-by-cause.md): load when diagnosing a screen, and before writing the notes; the generic tells grouped by why they appear, with what replaces each and which skill owns the fix.
- [references/choices-and-sources.md](references/choices-and-sources.md): load when writing the decision notes; where each kind of choice gets its reason, what makes a reason usable, a real brand as the source, and two worked outlines.
- [references/components-and-details.md](references/components-and-details.md): load in the parts-and-fill pass; icons in place of emoji, counts and badges, corner radii, figures and charts, marks, product previews and placeholders, states.
