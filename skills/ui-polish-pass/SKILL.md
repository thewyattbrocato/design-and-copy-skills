---
name: ui-polish-pass
description: Use whenever an interface should be finished, not just functional, however the ask is worded - "final touches", "make it production-ready", "it looks rough or half-done", "before we ship, anything missing", "what did I forget", "handle the edge cases", "empty, loading and error states", "accessibility pass", "less generic", "clean this up", "demo on Monday", "last two days before launch" - and also when the ask is only a short plain description of a screen, form, list, dashboard or panel to build or complete ("a simple order page", "a small settings screen"), where the unstated wish is that it be good. Covers every state (empty, loading, error, success, disabled, focus), forms, keyboard and screen-reader access, contrast, dark theme, long content, narrow screens and motion, in HTML, CSS, components or a described screen. Leaves what works alone. Not for visual redesigns, scored critiques (design-critique) or one named fix.
---

# UI polish pass

Generated interfaces stop at the happy path. Finishing means the unhappy path works: failure, waiting, nothing to show, too much to show, a keyboard, a small screen. The usual mistakes run the other way too: a polish request turned into a redesign, an unrequested dark theme, a rewritten file, a lecture. Fix what is broken, keep what works, stay in proportion to the ask.

## When not to use

- A new design from nothing: build it, with the focused skills if installed. A judged review or score with no changes: design-critique, if installed.
- System-level tokens and component libraries: design-system-builder, if installed.
- One named fix ("change the label", "nothing else"): do exactly that, briefly.

## Scope first

- The existing look is a decision. Keep layout, palette, type, field order and wording unless one is itself the defect. New states and fixes should look like they were always there.
- Add a dark theme, motion, new features, new copy tone or a new component only if the project already has one or the request names it. If a dark theme exists, check it; do not invent one.
- Do not widen a narrow ask into a sweep.
- If the thing is already in good shape, say so in a sentence, name what works, and change at most a few lines. Do not invent problems to look thorough, and do not pad a short list of real ones.
- An explicit instruction, an existing design system or a platform convention beats every default here. Reuse its tokens and components.

## Find the gaps by state

Walk each component in scope through [the states for its type](references/states-and-checks.md) and skip any that cannot occur. Check these first, because generated code misses them most:

- **Submit and async actions:** acknowledged within about a tenth of a second (busy state, no double-submit), a visible result in words, a failure that keeps what the person typed and offers retry. A silent `fetch` is the commonest defect.
- **Empty:** first use says what the place is for and offers the first action; no results says what was searched and offers to clear it; no dead controls on an empty list.
- **Errors:** what happened, why if known, what to do next, in plain words. Beside the field or near the failed action, persistent until fixed, announced to assistive tech, focus on the first problem. Never only a vanishing toast; never "Something went wrong".
- **Disabled:** a visible reason beside the control, or enabled and explaining on press.
- **Undo or confirm:** reversible actions (archive, remove, move) act now and offer undo for several seconds. Confirm only what cannot be taken back, name the consequence, and put verbs on the buttons ("Delete project", "Keep it"). Leaving (cancel, unsubscribe, export) is never harder than joining.
- **Access floor:** every control has an accessible name (repeated "open" links or icon-only buttons name their target); focus is visible on every control and never lost after a deletion or dialog close; the task works by keyboard; meaning never rests on color or hover alone (severity gets a word or icon); text and input borders meet contrast; the layout survives 200% text and a 320-pixel width. Numbers are in the reference.
- **Long and many:** the longest realistic name, long unbroken words and URLs, zero, one and hundreds of items, and a slow or offline network. Wrap or truncate with a route to the full text; never clip a label that names an action.
- **Motion:** keep what has a job (feedback, orientation); frequent paths fast and interruptible; reduced-motion removes movement but keeps the state change visible.

## Fix in order of harm

Blocks a task or excludes people (no name, no focus, trapped, lost input), then misleads (silent failure, false success), then degrades (truncation, layout break), then cosmetic. Fix at the source, a token or shared component, once. Re-walk the states you touched, with real text lengths.

## Missing facts

Never invent a retry count, response time, support address, phone number, limit, policy, deadline or other fact the user did not give. Use a visible placeholder like [support link] or a softer true sentence, and still deliver the work. If the real causes, limits or copy are unknown, infer from the material and proceed; ask once only if the chat is interactive and the answer is cheap and changes the work. Never answer with only questions.

## Do not produce

- A redesign, a new visual style, a theme or feature nobody asked for, or copy rewrites where the existing copy works.
- A checklist, matrix or audit table in place of the fixed code or the ranked findings.
- "Oops", "Error 500", "No data", "Are you sure?", a spinner with no way out, `outline: none` with no replacement, an icon button with no name, a confirm where undo would do.
- Pre-checked consent, shaming decline wording, a harder cancel than sign-up, fake urgency.
- A claim that something is accessible or tested when you only read the code. You cannot run a screen reader, a server or a real device here; say what you did not check.

## Deliver

- Lead with the work: the changed code, the screen or the answer. No preamble, no restating the input.
- Code: return the whole file only when asked for it or when most of it changed; otherwise the changed pieces. Send code only if you changed something. Keep the original's structure, naming and style so the diff stays small.
- Asked what is rough or worth checking: findings ranked by harm, each with a targeted fix and a one-line reason, not a rewrite. Open with what already works, in a line.
- Asked for a count or a set (three fixes, the states, a checklist): give exactly that. Honor any word cap and count rather than assert.
- Then at most two one-line notes: what remains or needs a design decision, and what you did not check.

## Example

Ask: "polish this task list for release". Before: a list that renders items only, an icon-only delete, `outline: none`. After: an empty state with an "Add a task" action; a skeleton while loading and an inline error with Retry that keeps the list; the delete named "Delete: Buy milk" with an Undo bar; focus ring restored; long titles wrapping. Same colors, spacing and type as before. Closing note: "Not tested with a screen reader."

Ask: "change the Submit label on the newsletter form, nothing else". Answer: the new label (for example "Subscribe") and one line of why. No other edits.

For the full state list per component type, thresholds and fast tests, read [references/states-and-checks.md](references/states-and-checks.md). For full procedures use form-design, ui-motion, color-palette, typesetting, spacing-and-grouping, responsive-layout and design-system-builder, each if installed.
