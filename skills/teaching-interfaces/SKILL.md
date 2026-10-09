---
name: teaching-interfaces
description: Use whenever a screen, page or flow has to teach someone to do or understand something, in any language and at any length - "design the first screen after sign-up", "nobody finishes our onboarding", "people don't get this feature", "the empty state is useless", "explain how this works with a diagram", "write the help article", "is this tour any good". Covers first-run and guided tasks, tours, coach marks, teaching tooltips, empty states, what's-new notes, explainer cards, in-product video, help articles. Not for quizzes or courses (practice-and-assessment), input fields (form-design), animation timing (ui-motion), data charts (chart-design), marketing pages or general interface strings.
---

# Teaching interfaces

People learn an interface by doing a real task in it, not by being shown it. Unguided, a model teaches by exposure: a coach-mark tour of every toolbar button, a carousel of benefits before the product opens, a "Got it" tooltip on each control, a diagram with a lettered legend, narration plus the same paragraph on screen, an empty state that is a large illustration and "Nothing here yet!", confetti and "You're all set!", streak reminders for a help feature. These feel helpful and teach little.

## When to use

Any surface whose job includes getting someone to do or understand something new: first run, a guided first task, a tour, a tooltip, an empty state, a feature announcement, an explainer card or diagram, an instructional clip, a help article or step list. Also judging an existing one.

## When not to use

- Question banks, scenarios, drills, course or curriculum design: practice-and-assessment if installed.
- A screen that only needs clear labels, such as a settings or preferences page. Do not add tours, overlays or tutorials to it; helper text only where a label cannot carry the meaning.
- Marketing pages, general interface strings, dashboards, animation timing: use ordinary judgment or the matching skill if installed.
- Expert tools: experts pull help when they want it. Offer optional, targeted help (what differs from tools they know) and a short reference; never a mandatory tutorial.
- Text or a flow that already teaches well. Say so and change at most a word.

## Rules that change the output

- **Fix before you teach.** If people struggle with a label, default or control, change the interface. Teach only what cannot be designed away; the best help is a job aid at the moment of action, not a tour before it.
- **Name the one thing.** Write the sentence "afterwards they can ___" and keep every element in service of it. Anything that would become the memory instead (mascot, joke, decoration) is cut or demoted.
- **A few new things at a time.** Introduce about two or three before the person acts. Keep the instruction and their earlier choices on screen while they work, so nothing has to be remembered.
- **Teach by doing.** One sentence of context so the steps make sense, a short worked example or finished sample, then the real task in the real product, then feedback. Prefer a guided first task to a tour. A tour is acceptable only as three to five steps tied to the first real success, never an inventory of controls.
- **Explain the arbitrary, not the universal.** Your icons, terms and concepts need explaining; scrolling and dragging do not. Introduce the names and parts before the process that uses them.
- **Starting points beat blank canvases.** Offer a template, sample content or a partly finished item. Label sample data as sample, make it replaceable in one action, and never show plausible-looking numbers that could be taken for the person's own.
- **Novices guided, experts free.** A default path for newcomers, with an obvious skip and a way back to help later. Important examples and practice default on; people overrate what they know. Let people control pace (continue, back), not the syllabus.
- **Words on the picture.** Label the parts themselves, not a legend; keep each sentence beside the part it explains; use still steps for conceptual sequences and motion only when the motion is the point; split long explanations into short segments the person advances. Details in [words and pictures](references/words-and-pictures.md).
- **Do not double the channel.** Narration over a graphic gets captions as a mode, or a few keywords on screen, not the full script as well. With no audio, text carries the explanation. Captions and transcripts are not optional; nothing essential rides only on animation or hover.
- **Cut what does not teach.** Background music, filler narration, decorative illustration, jokes the audience did not ask for. Warmth belongs on the essential object (a friendly sample, a plain voice), not in a new character. Conversational is good; forced chumminess is not.
- **Feedback updates their model.** Say what happened and why, in their terms ("3 emails moved to Receipts because they came from billing@"), not "Great job!" or "Incorrect". A brief confirmation that states what now works and points to the next step is fine; ceremony that delays the next action is not.
- **Bring it back through real work.** Important actions reappear later as real tasks, ideally with different surface details. A reminder tied to a step the person started is fine; streaks, guilt copy and clock-based drips are not.
- **Empty states explain.** Say what the area is for, give the one action that starts it, optionally show an example. Hide controls that do nothing yet. An illustration may show what the area will hold but is never the largest element.
- **Help for doing.** Task-based title; when and why in a line; numbered steps, one action each, with the expected result; cropped, annotated screenshots; troubleshooting last; reference kept apart from tutorials. Details in [first run and help](references/first-run-and-help.md).
- **Memorize only when it pays.** When a task is time-critical or dangerous, rehearsed recall can beat reading under stress; keep a visible checklist as support and say it is an exception. Otherwise keep the information on screen where the task happens.
- **Judge by later performance.** Success is whether people do the task days later unaided, not whether they finished the tour. Propose that measure instead of asserting a completion or retention number.

## Missing facts

If the product, audience or steps are not given, assume the simplest case, say so in one line and still deliver. Ask once, with a default, only when interactive and cheap; never reply with only questions. Never invent product facts: menu paths, button labels, limits, shortcuts, screenshots, user counts, completion rates, quotes. Use a visible placeholder such as `[menu name]` or `[step 3 result]`, or write the step in a softer true form.

## Do not produce

- A toolbar tour of every control, or a benefits carousel before the product opens.
- A diagram with a lettered or numbered legend away from its parts.
- Narration plus the identical paragraph on screen.
- "Nothing here yet!" with a big illustration and no action.
- Confetti, mascots or "Got it!" gates standing between the person and the task.
- A help article as one wall of text, or steps that hide two actions in one number.
- Streaks, guilt notifications or night-time nudges for a learning feature.
- A mandatory tutorial for experts, or any sequence with no skip.

## Output discipline

Deliver the requested thing first (the screen, the card, the outline, the verdict), no preamble and no tour of learning theory, because the reader came for the work. When a count or set is asked for, give exactly that. Honor any length cap by dropping the lowest-value point, and count instead of asserting. A verdict names its evidence and the next check. After the work, at most two one-line notes (an assumption, the main trade-off) unless more is asked.

## Quick checks

- Could they do the real task in the first minute?
- One sentence says what they can do afterwards; nothing competes with it.
- No more than three new ideas before they act; skip and return paths visible.
- Labels sit on parts; no full script duplicated; captions available.
- Empty state has purpose, one action, no dead controls.
- No invented fact, number or label; count and length cap met.

## References

- [references/words-and-pictures.md](references/words-and-pictures.md): load for explainers, diagrams, instructional video or animation, and narration or caption choices.
- [references/first-run-and-help.md](references/first-run-and-help.md): load for first-run flows, tours, sample data, empty states, what's-new notes, and help articles.
