---
name: typeface-selection
description: Use whenever a font is being chosen, paired, judged or fixed, in any language and at any length - "what font should I use", "the fonts look generic, off or amateur", "does this pairing work", "make it feel more premium, friendly or technical", "which font for long reading", "it falls back to Times", "fonts for Arabic or Vietnamese". Covers roles, one family versus two, pairing, system font stacks, web-font loading and fallbacks, variable fonts, licensing and script coverage, in CSS, pages, apps, decks and brand work. Not for sizes, leading or line length (typesetting), drawing logos (brand-identity), type tokens (design-system-builder) or palettes (color-palette).
---

# Typeface selection

Choose faces by the job each one does, then prove the choice on real text at the real size. Unguided, the choice is one geometric sans for everything, a stock serif and sans pairing, monospace headings to look technical, and a named web font that never loads so the page quietly falls back to a default serif.

## When to use

- Picking or changing the font for a page, app, document, deck or brand; judging an existing choice; pairing faces; writing or fixing `font-family`.
- Pages that must render with no web font (offline, email, previews, strict privacy or performance): the system stack is the answer, not a fallback.
- Shipping web fonts, variable fonts or several scripts; checking that a face is licensed and complete for the languages used.

A short request ("this font feels off") is not a small one: name the role that fails, then change that role.

## When not to use

- Sizes, line length, leading, figures in use: typesetting if installed. Drawing a logo or custom lettering: brand-identity if installed. Type tokens: design-system-builder if installed. Contrast and palettes: color-palette if installed.
- A brand font or design system already fixes the face: apply it, with its own fallbacks, and only fix what fails around it.
- The text already works: say so in a sentence and change at most one thing. A good stack gets "this is sound", not a swap.

## Do not produce

- One interface sans at one weight for title, body and labels, or a thin geometric sans for long reading.
- Two near-identical sans faces paired; three families plus mono; a second family with no role.
- Monospace for headings, buttons or "tech feel". It is for code, identifiers and columns that must align.
- A script, condensed or decorative face in buttons, labels or body text; a face that mimics the subject (a gear face for software, handwriting for a bakery).
- A named font that is not loaded or installed, with no real fallback after it; a bare generic family as the whole stack.
- Faux bold, italic or small caps. Pick a family that has them, or turn synthesis off and drop the style.
- Hairline weights for text; light-on-dark text with the light-theme weight.
- An invented fact about a font: its license terms, popularity, file size, or script coverage you have not checked. Say "confirm with the foundry" instead.
- A plainer page than asked for. A poster, a brand moment or an expressive brief wants an expressive display face, used big and short, with a plain partner for the small text.

## Choosing

**Write the reading job first.** One line: long reading, scanning interface text, glanceable data, or display voice; the smallest size that occurs; languages and scripts; whether web fonts can load; license budget. Unknowns are assumed, not asked (see Missing information).

**One family by default.** Choose one with real range: regular, a medium or semibold, bold, and a true italic. Hierarchy comes from weight and size inside it. Add a second family only for a role the first cannot play: long reading, a display voice, or code.

**Reading text.** Neither serif nor sans wins by category; the specific face, size and screen decide. What matters is comfort at the size used: moderate contrast, open apertures, a medium to generous x-height, sturdy serifs or terminals that survive small rendering, a drawn italic. Test a real paragraph at the smallest size on the real background, not a headline specimen. For an essay, article, recipe or book-like page a text serif or humanist stack is the stronger default.

**Interface text.** A sturdy grotesque or humanist sans with distinct I, l, 1 and O, 0, tabular figures for money and counts, and a weight range. Round, closed geometric shapes suit headlines better than dense small text.

**Display.** Contrast, width and character are allowed where text is big and short. Keep the voice of the face tied to the brand's actual tone, not its subject. Pair a display face with a calm text face, not another display face.

**Pairing.** Pair faces that share skeleton and proportions (same x-height, similar stroke contrast), or faces that differ plainly in category with roles fixed in advance: serif for reading, sans for interface; display serif over a sturdy sans. Two faces that differ only slightly look like a mistake. Bold and italic stay in the family that owns the text. If a pairing needs a third face to feel right, the first two are wrong.

**Monospace.** Code, inline identifiers, parameter names, terminal output, and columns that must align where no tabular figures exist. Keep prose around them proportional.

**System stacks.** When fonts cannot load, write a stack per role (see references) and check what it renders as. A stack is a design decision: pick the serif stack for reading pages, the system UI stack for tools, and keep the roles separate.

**Variable fonts.** One file for the weight range; map named weights to the roles. Let optical size follow the size automatically; use a grade or a lighter cut on dark grounds when available. Do not animate axes for decoration.

**Scripts.** Choose for the scarcer or harder script first (Arabic, Devanagari, CJK before Latin), confirm Vietnamese stacked diacritics and Greek or Cyrillic coverage, match apparent size by eye not equal points, and leave extra line height for tall marks. Do not force a Latin face to supply glyphs it lacks; the browser will substitute one that does not match.

**Licensing and loading.** Open licenses are the safe default when rights are unclear; check web, app and embedding rights before using a commercial face, and never copy font files without them. Self-hosting needs subsetting, two to four files, a display strategy that never shows invisible text, a preload for the critical file, and fallback metrics tuned to reduce layout shift.

## Missing information

Do not stall on questions. Assume a screen, a Latin-script audience, no installed fonts beyond system ones, and deliver. Ask once only if interactive and the answer changes the pick (print versus screen, a locked brand face, languages). State at most two assumptions after the work. Never invent fonts the user did not name as installed, license terms, or claims such as "used by" or "most popular". If a face you would like cannot be verified, name the stack that works now and the one upgrade.

## Output discipline

- Deliver the requested thing first: the stack, the pairing, the `font-family` lines, the verdict. A reason is one line per choice.
- When a count is asked for (three pairings, two options), deliver exactly that many, each with a role and a one-line reason.
- Honor any word cap. Count the words and cut the lowest-value point instead of asserting that it fits.
- A critique names what works, then what fails, each with a fix.
- After the work, at most two one-line notes unless asked for more.

## Quick checks

- Every role (reading, interface, display, code) has a named face or stack, and each stack ends in a real fallback.
- No more than two families plus mono; no pair that is nearly the same.
- Bold and italic exist in the family; no synthesis.
- Digits and I, l, 1, O, 0 can be told apart where it matters; money has tabular figures.
- Offline, the page still looks as intended: the fallback was checked, not assumed.
- Languages, license and loading are stated, or the open question is.

## References

- [references/judging-and-pairing.md](references/judging-and-pairing.md): load when shortlisting from several faces, comparing candidates or building a pair; the structure checklist and pairing table.
- [references/stacks-loading-scripts.md](references/stacks-loading-scripts.md): load when fonts cannot load, or when shipping web fonts, variable fonts or several scripts; stacks by role, loading recipe, script notes.
