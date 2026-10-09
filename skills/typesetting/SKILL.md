---
name: typesetting
description: Use whenever text is being set, judged or fixed, in any language and at any length - "make it easier to read", "feels cramped", "looks amateur", "more editorial", "the type is too small", "numbers won't line up". Covers body size, line length, line height, size scales, heading and paragraph spacing, prices and figures, all-caps labels, justification, dark-theme text, quotes and dashes, in CSS, pages, documents and designs. Not for choosing typefaces (typeface-selection), ranking a whole view (visual-hierarchy), palettes (color-palette) or logos (brand-identity).
---

# Typesetting

Make text comfortable to read and quick to scan: few sizes with jobs, a line length the eye can follow, room between lines, numbers that stack. Most fixes are small and visible at a glance, so make them and move on. Setting the text well does not mean a plainer page: keep the cards, accents, display faces and atmosphere the task wants, and set the text inside them.

## When to use

- Building or editing any page, card, article, form, document or email where text carries the content: set the text as you build, not as an afterthought.
- Reviewing CSS or a design for size, measure, leading, heading spacing, alignment, capitals or figures.
- Prices, quantities, timers and totals in lists, cards and columns; dark themes; small text; print and ebook text.

A short request ("this looks cramped") is not a small one. Check the whole text setup, then change only what fails.

## When not to use

- Choosing, pairing or loading typefaces: use typeface-selection if installed; otherwise keep the face in play or a system stack. Licensed fonts need fallbacks.
- What the eye sees first across a view: visual-hierarchy if installed. Contrast ratios and palettes: color-palette if installed. Page grids and table structure: layout-structure and data-tables if installed. Type tokens: design-system-builder if installed.
- Logos, wordmarks and display lettering: space them by eye; body rules do not apply.
- Code, logs and fixed-width data: keep them monospace and unwrapped when the job needs it.
- A user's explicit instruction, an existing design system or a platform convention wins. Check around it and report only what fails.

## Do not produce

- Body text in fixed px at 12 to 14, in pale gray, across a container of 900px or more.
- One line height for everything; a heading at 1.0 that wraps to two lines.
- Six to eight sizes stepping evenly from the first heading to the last.
- A heading with equal space above and below, or floating between sections.
- Proportional figures in a column of prices or timers.
- Tiny all-caps labels with no tracking; tracked lowercase body text.
- Justified text in a narrow card or on a phone.
- A blank line and a first-line indent on the same paragraphs.
- Straight quotes, hyphens for ranges, double hyphens for dashes, in copy that is final.
- Pure white on pure black at the light-theme weight.
- Faux bold, italic or small caps (`font-synthesis: none`; use real faces).
- A flatter page than asked for, or a rewrite of text that was already well set.

## Defaults, and when to change them

**Body size.** 1rem for reading text, 1.125 to 1.25rem on long-form reading pages; never fixed px on the root. Dense tools may drop secondary text to about 14px if it stays legible. Anything read to act (errors, prices, instructions, field help) stays at body size; about 12px is for metadata and captions.

**Measure.** 45 to 75 characters for continuous reading, near 60 to 70; 35 to 50 in narrow columns and cards. Cap the text element (`max-width: 65ch`), not the page wrapper. Captions, labels, titles, code, logs and table cells are not prose and are exempt.

**Leading.** Unitless, about 1.5 for screen body text and 1.1 to 1.25 for headings; it falls as size rises and rises with line length, large x-height or heavy faces. If lines run long, shorten the line before adding leading. Keep line space clearly larger than word space.

**Scale.** Name the roles (display, title, section, body, small, label, code), give each one size: four to six in all. Ratio about 1.2 to 1.25 for interfaces, up to about 1.4 for editorial and marketing display only. Round to tidy rem values. Heading levels follow the outline; looks come from classes, so two levels may share a size. On small screens big sizes shrink faster than small ones (`clamp()` with a rem floor).

**One variable per step.** Add emphasis as space, then weight, then size; as size rises, weight may fall. A pull quote, caption or total differs from body by one or two properties, not all of them. One device sets off a quotation: italic, indent or size, not all three. Change for a hero, where a big jump is the point.

**Spacing.** About twice as much space above a heading as below it. Separate paragraphs by a gap of half to one line or a first-line indent of about 1em, never both; no indent after a heading. Print and ebook flip this: indents, no gaps, justified with hyphenation.

**Figures.** Tabular lining (`font-variant-numeric: tabular-nums`) for anything in columns, prices, timers and counters; right-aligned or on the decimal, same decimals on every row. Proportional in prose. Old-style only in long editorial prose with lowercase. Mixed sizes on one line (price and currency, label and value) share a baseline. A total differs by one step.

**Capitals.** Sentence case for buttons, labels, tabs and headings. All caps only for short labels, tracked 0.05 to 0.1em, at 12px or more; capitals read slower, so never for sentences. Tighten large display slightly (about -0.01 to -0.02em); otherwise trust the face's own spacing.

**Alignment.** Flush at the reading start, ragged on screens; center only a few short lines; right-align numbers. Justify only with `hyphens: auto` and `lang` set, a wide enough measure, and a medium that calls for it.

**Dark grounds.** Off-white on soft dark gray, same sizes and measure. Judge weight by eye at the same zoom: if text looks swollen drop a step or use a lighter grade, if thin strokes break up at small sizes raise it. Open small text slightly. Dim secondary text by value, not by opacity.

**Wrapping.** `text-wrap: balance` on short headings, `pretty` on body. Non-breaking space between a number and its unit. Truncate only non-critical text, and give a way to see all of it. Never truncate an amount, an error or the only instruction.

**Details.** Curly quotes, en dash for ranges, one dash style per product, multiplication sign for dimensions, real accents. Follow the locale for number and date formats.

## Working text

If sizes, measure, leading and figures already hold up, say so in a sentence and change nothing, or only the lines that fail. A sound stylesheet gets "this is sound", not a rewrite; at most one clearly labeled optional tweak. Fix what was asked or clearly broken, fully, and make no unrequested changes (unit swaps, restyling).

## Missing information

Do not stall on questions. Assume a screen, a light ground, the face already in play or a system stack, sizes in rem, and deliver. Ask once only if interactive and the answer changes the build (print versus screen, a fixed system). Say at most two assumptions after the work. Content the user gave stays word for word. When you must write sample content, keep it plainly generic, and never add statistics, quotes, reviews, ratings, customer names, deadlines or stock limits the user did not supply: use a visible placeholder or leave the slot out.

## Output discipline

- Deliver the requested thing first, with no preamble or tour of typography: the code, the changed lines, the one pick. Code answers keep the user's selectors; show whichever is shorter and clearer, changed lines or the whole block.
- When a count or set is asked for, deliver exactly that; two scales means two that differ in ratio and role count.
- Honor any word cap. If the answer will not fit, drop the lowest-value point, then count and finish under the limit. Give units on every size.
- A critique names what works, then real failures, each with a fix and a one-line reason.
- After the work, at most two one-line notes unless more are asked for.

## Quick checks

- Body is in rem; no paragraph spans a wide container; lines run about 45 to 75 characters.
- Body leading near 1.5, headings tighter; count the sizes, four to six, each tied to a role.
- Space above each heading is about double the space below.
- Columns of figures align, with tabular figures and one format.
- Caps labels are short, tracked and 12px or more; body is not letterspaced.
- Dark text is off-white and legible small; quotes and dashes are typographic.
- Working text was left alone; the output has the exact count and length asked for.

## References

- [references/reading-text.md](references/reading-text.md): load when setting a reading page, a scale or dark and small text; ranges by context, CSS recipes, ramps, heading mapping, audit routine.
- [references/figures-and-details.md](references/figures-and-details.md): load when text holds numbers, units, dates, quotes, dashes or capitals, or must be truncated.
