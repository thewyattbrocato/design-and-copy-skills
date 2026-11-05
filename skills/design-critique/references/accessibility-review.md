# Accessibility review

Load when the ask is whether something is accessible, or an access review or audit of a page, flow or product. A passing mention of contrast in a general critique stays in the Accessibility pass of [checks](checks.md). A short ask still gets a short answer: the proof label can be one word.

## Turn the ask into tasks and people

- "Is it accessible?" becomes: can these people finish these tasks? People: keyboard only, screen reader, magnification, voice control, low vision, color-vision difference, heavy load on attention or memory. Tasks: arrive, sign in, the core task, pay or submit.
- A bare verdict, positive or negative, is not the output. Say what was checked, on which pages, by which method, and what was found.
- Never write "accessible", "compliant" or "meets the standard" from a review. A review finds known faults; it cannot clear a product.
- Name a standard or level only if the person did. Otherwise judge whether the named people can finish the named tasks. Keep law names, versions and dates out.

## Scope line

State the artifact (code, screenshot, live address, description), what was sampled and what was not. Sample the main journeys and one instance of each shared template or component. A fault in a shared part is one finding with a count.

## Proof label on every finding

Mark each finding with one of:

- **read in the code:** an unnamed button, a missing label, a positive tabindex.
- **computed:** a ratio, a size, a count, from what was supplied.
- **needs a person or a device:** focus order as it feels, announcements, voice control, real zoom, forced colors.

A screenshot alone cannot show focus order, names, announcements or traps. Say so instead of guessing, and say what code reading does establish.

## Blockers, defined by task

A blocker means a named group cannot finish the main task on its own. Typical ones: a keyboard trap; the primary action unreachable or unnamed; a timeout that throws away typed input; sound or motion that cannot be stopped; a puzzle or memory test at sign-in with no other route; an error shown only by color.

- A failed check is a defect. A task a named group cannot complete is a barrier. If the goal is use, rank barriers first. If the goal is a claim to a buyer or a regulator, rank by the criteria they named. Say which ranking you used.
- After severity: shared components and templates first (one fix, many pages), then cheap fixes with wide reach, and code about to be retired last unless it sits on a main path. Several minor faults on one path can add up to a barrier; say so when they do.

## What tools show

- A clean scan or a high score means the common machine-detectable faults are absent, not that the page works. Never report the score as the verdict, and give no coverage percentage.
- Name what a scanner cannot judge on this page: whether an alternative means anything, whether the order makes sense, whether a present name is the right one, meaning carried by color or position.
- Where a scanner may be blind (embedded frames, components with their own tree, states behind a click), seed one known fault and see whether the tool reports it before trusting a zero.

## Manual probes, and what each finds

- Keyboard-only walk of the main task: reach, order, traps, visible focus.
- 200% text and a 320px width: clipping, two-way scrolling.
- Forced colors: lost borders, vanished icons and logos.
- Reduced motion: large movement still playing.
- Styles off: source order, headings that are only styled text.
- Screen-reader pass of the main task: names and announcements.

List the probes not run in the limits line as recommendations.

## Third parties and overlays

- Consent banners, chat, embeds and payment frames are reported like first-party findings, each with who owns the fix.
- A one-line overlay widget is neither a fix nor a defence: it cannot judge meaning and can fight the person's own tools. At most a stopgap with an end date while real fixes ship. A separate "accessible version" is not a remedy either.
- A vendor's "fully accessible" is a claim to test: ask what was tested, which version, by whom, and read the rows marked partly supported.

## Order of work for a whole site

1. Template-level common faults: contrast, missing text alternatives, unlabeled fields, empty links and buttons, missing page language.
2. Manual passes on the main journeys.
3. Keep it fixed: checks in the review flow that comment before they block, components that refuse to render without a name.
4. The long tail of old pages; delete what need not exist.
5. Sessions with disabled people on a defined task, once known faults are gone, experienced users first.

## Review is not evaluation

Review findings are not user results. Only people using their own tools on real tasks show whether it works; recommend a small session after the blockers are fixed.

## Tracker-ready findings

When the output feeds a tracker, add to Seen / Why / Change: steps to reproduce, expected versus actual behavior, who is affected with what technology, effort and owner.
