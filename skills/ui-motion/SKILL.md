---
name: ui-motion
description: Use when someone wants an interface to feel smooth, responsive, alive, polished, premium or less janky, or asks to add, fix, cut, time, specify or review animation - transitions, hover and press feedback, modals, sheets, menus, page and state changes, list reordering, scroll effects, loaders and skeletons, stagger, easing, springs, shake on error, micro-interactions - in a product UI, web app or interface-like page. Also reduced-motion handling and motion handoff specs, in any language or request length. Not for video, film or character animation, detailed chart animation, print or static deliverables, or carousel semantics.
---

# UI motion

Motion in an interface is a tool for telling people where things went, what changed and whether their action worked. The right default is less, faster and always interruptible. Spend motion where it has a job, and make everything else instant.

## Do not produce

These are the usual defaults. Skip them unless the brief asks for them by name.

- Every section fading up on scroll, or a parallax hero.
- `transition: all` with a long duration, or animating width, height, top or left on large elements.
- Modals, menus and sheets that take 500 ms or more, or ease-in-out in both directions.
- Bounce or overshoot on frequent controls; a call-to-action that pulses forever.
- Controls disabled while an animation plays; input ignored until a transition ends.
- Stagger that makes the last item late; count-ups on load; a spinner flashing for a near-instant wait.
- A reduced-motion answer of "delete all transitions" (it removes focus and state feedback too), or no answer at all.

## When to use

- Adding motion to a screen, component or flow, or deciding whether it needs any.
- Fixing animation that feels slow, heavy, janky, blocking, nauseating or "too much".
- Writing a motion spec, a handoff note, a motion vocabulary or tokens as numbers.
- Reviewing animation code or a described animation, including its reduced-motion behavior.
- Loading, progress, success and error feedback; shared-element and page transitions.
- Vague asks such as "make it feel premium", "more delightful", "it feels laggy". A short request is not a low-stakes one.

## When not to use

- Video, social clips, title sequences, character or frame-by-frame animation. Only the reduced-motion and readability parts of this skill apply there.
- Charts and data graphics: use `chart-design` if installed for transitions inside a chart; static charts and print need no motion at all.
- Carousel and widget semantics, focus order and keyboard behavior: detailed component accessibility work, outside this skill; follow standard practice.
- Motion token naming inside a design system: `design-system-builder` if installed. Whole-screen finishing passes: outside this skill. Instructional animation that teaches a concept: `teaching-interfaces` if installed; a still diagram often teaches better.
- Games, playful toys and media players, where movement is the content: keep these rules for the surrounding interface and let the content move as the design wants. Keep input responsive, offer a way to reduce it, and avoid flashing.
- User-started media (they pressed play) is not interface motion. It needs controls, captions and no autoplay, not removal.

An explicit instruction, an existing design system's motion rules or a platform convention beats every default here. Motion that already serves a job, is fast, can be interrupted and respects reduced motion is working: leave it alone and say so rather than retuning it. Do not add motion to work that did not ask for it.

## Inputs (ask first, never stall)

Ask once, in one short message, only for what you cannot infer: the platform and stack, how often people hit this path, the brand's temperament in a word or two, and any existing durations, curves or tokens. If the person declines or the request is a one-line fix, proceed with these defaults and state them in one line: a web product UI, a frequent path, a calm and decisive tone, CSS transitions, system reduced-motion honored.

Deliver the thing asked for first, with no preamble. If they ask for a number of options, give exactly that many and count them before sending. If they set a length, stay inside it; cut material before going over. A fix gets the fixed code; a spec gets the spec; a critique gets the findings.

## Procedure

1. **Name the job.** Each motion must do one of: orient (where did this come from or go), focus attention on a change, show cause and effect, confirm an action, demonstrate a gesture, express a stated brand trait. "Delight" alone is not a job. No job, no motion.
2. **Charge by frequency.** Duration times how often it is paid is the real cost. Frequent actions get the fastest, simplest motion or none; a rare or first-run moment can carry more.
3. **Pick a duration by size of change.** Press and hover feedback about 100 to 150 ms; small local changes about 150 to 250; menus, toasts and panels about 200 to 300; large travel or whole-screen changes about 300 to 500. Exits run about a fifth to a third shorter than entrances. Over half a second only for loaders and deliberate demonstrations. See [timing and easing](references/timing-and-easing.md).
4. **Pick an easing by direction.** Arriving things decelerate (ease-out). Leaving things accelerate or simply fade quickly. Things that move between two on-screen places use ease-in-out. Linear only for continuous progress and looping opacity. Direct manipulation can use a spring with little overshoot.
5. **Make it interruptible.** New input retargets or reverses from the current state. Never disable controls during motion. Reserve uninterruptible motion for commits that must finish, and show status then.
6. **Tell the truth about space.** Things enter from where they live and leave toward where they go; the same object persists across states instead of fading out and a different one fading in. See [transitions and continuity](references/transitions-and-continuity.md).
7. **Choreograph sparingly.** One primary motion at a time; related items share easing; stagger offsets about 20 to 40 ms with the total capped near 200 to 300 ms.
8. **Cover waits and results.** Acknowledge input within about 100 ms; show progress only after about a second of waiting; put it inside the control that started it. See [feedback and loading](references/feedback-and-loading.md).
9. **Make it safe.** Provide reduced-motion behavior, keep flashing under the limit, give anything self-moving a pause. See [reduced motion and safety](references/reduced-motion-and-safety.md).
10. **Keep it cheap, then write it down.** Animate transform and opacity first. Record the result as numbers: duration, easing, delay, trigger, interruption, reduced-motion variant.

Scale to the task. A single hover state needs steps 1, 3, 4 and 9. A fix to one stylesheet needs only what that stylesheet breaks.

**Big builds (a motion system, a whole app, a full redesign pass).** Before writing code, give a short plan: the five to ten moments that earn motion, each with its job, and the shared vocabulary (see below). Then build one representative slice, such as one overlay with its enter, exit, interruption and reduced-motion variant, and let the person redirect before extending it everywhere.

**One anchor.** Pick one feel to match and say it in a line ("calm and decisive, like a quiet productivity tool"). Use it everywhere in the work. Depart from it only where the brief, the brand or a platform convention says to, and name the departure.

## Judgment calls

**Whether to animate at all.** Default: a state change that is obvious in place needs nothing; a change that could confuse, such as an item moving, a panel appearing from elsewhere or content replacing content, gets short motion that explains it. Change when the brand brief names a motion trait, or the moment is rare and meant to be remembered. See [purpose and budget](references/purpose-and-budget.md).

**Springs or curves.** Default: cubic-bezier curves for enter, exit and state changes; a critically damped or lightly bouncy spring only for drag release, sheets and anything that follows a finger. Change to springs everywhere when the platform already does so; keep overshoot small and rare in product UI.

**Brand temperament.** Default: calm means shorter travel and opacity over position; decisive means arrive and stop with no overshoot; energetic allows a slight overshoot; playful allows a little squash where it cannot hurt a hit target. Apply one temperament everywhere. Change when the brand has measured values already; use those.

**Page-load choreography.** Default: render the content immediately and animate only the one change that tells people where to look. Change for a first-run or marketing moment, with one subtle reveal and a total under about half a second.

**Stagger.** Default: groups of up to about eight items may offset a little, with the total capped. Change to no stagger for long lists, frequent updates, or anything people act on at once.

**Scroll effects.** Default: none beyond sticky headers and anchored position changes. Change for a single editorial or marketing moment where scroll position is the content, and keep it off under reduced motion.

**Error motion.** Default: a brief small shake or highlight only as a secondary cue, plus persistent text near the problem, no layout jump and no forced scroll, and focus moved to the message. Change to no motion when the form already shows an obvious message in place.

**Optimistic updates.** Default: show the result immediately only when the action can be rolled back, and show the rollback. Change to a visible pending state when the action can fail in ways that matter, such as payment.

**Platform and library conventions.** Default: use the framework's own transition and layout-animation tools and existing tokens. Change only to fix a measured problem.

## Common failures

- **Scroll reveals on every section** → cut them, or keep one subtle reveal for a key moment.
- **Modal in 700 ms with bounce** → about 250 to 300 ms ease-out in, faster out, no bounce.
- **Pulsing or looping call to action** → static emphasis; motion on first appearance only.
- **Parallax hero** → static, or a minimal effect that is off under reduced motion.
- **`transition: all 600ms`** → list the properties; transform and opacity; 150 to 300 ms.
- **Button disabled during its own animation** → keep input live; the motion retargets.
- **Fifteen-item list at 100 ms per item** → 20 to 40 ms offsets, total capped, or no stagger.
- **Spinner flashes for a near-instant action** → no loader under about a second; a short delay before showing one.
- **No reduced-motion handling, or every transition removed including focus** → remove movement, keep opacity, color and focus feedback.
- **Label, icon and position all change in one fast move** → change one thing at a time, or slow the move; never move a target someone is aiming at.
- **Same element different curve on every screen** → three durations, three curves, one stagger value, used everywhere.
- **Screen "feels slow" and the fix is more motion** → measure first: input latency and long tasks cause more lag than long durations.
- **A written answer past a length the person set** → keep to it; cut material before the limit.

## Quick checks

- Every motion names its job; frequent paths are the fastest and simplest.
- Durations fall in the ranges above; exits are shorter than entrances.
- Enter eases out, exit eases in or fades; nothing uses ease-in-out by habit.
- New input interrupts or reverses any motion; no control is disabled to wait for it.
- Reduced motion is handled: movement removed, feedback and focus kept.
- Nothing flashes more than three times in a second; anything self-moving for over about five seconds can be paused.
- Only transform and opacity animate on large elements; no `transition: all`.
- The result is written as numbers (duration, easing, delay, trigger, interruption), not adjectives.
- Counts, such as option or item totals, were verified, and any stated length cap holds.
- Existing design system, platform and brief constraints are followed; working motion was left alone.

## References

- [purpose-and-budget.md](references/purpose-and-budget.md): load before adding motion; the jobs list, the frequency rule and motion to cut.
- [timing-and-easing.md](references/timing-and-easing.md): load when choosing values; duration ranges, starting curves, springs, exits and stagger arithmetic.
- [transitions-and-continuity.md](references/transitions-and-continuity.md): load for state, overlay and page transitions; directions, shared elements, interruption.
- [feedback-and-loading.md](references/feedback-and-loading.md): load for waits and confirmations; press states, progress, placeholders, optimistic updates, errors, toasts.
- [reduced-motion-and-safety.md](references/reduced-motion-and-safety.md): load whenever motion ships; what to remove and keep, pause controls, flashing, performance, handoff specs.
