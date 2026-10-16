---
name: interface-behavior
description: Use when deciding how a product acts rather than how it looks or reads, in any words or language - "people lose work", "too many are-you-sure popups", "nobody trusts autosave", "settings are a mess", "too many clicks", "can't find anything", "make it feel less annoying", "how should delete, save, import, search, undo or bulk select work", "who is this for and how dense should it be". Covers defaults and memory, undo and recovery, how state and progress show, modes, navigation and search, selection and bulk actions, settings, and a short behavior spec. Not for page grids, field mechanics, copy, motion timing, table styling or charts.
---

# Interface behavior

Most interfaces mirror how they were built: a screen per backend step, a question per database column, a warning wherever something could go wrong. Design from what the person is trying to get done instead. Act on a sensible guess, show state where they are already looking, and make mistakes cheap to undo rather than hard to make.

## Do not produce

- "Are you sure?" before a reversible action, or a "Saved successfully" dialog for normal operation.
- A wizard or an interview for something the product could infer, remember or default.
- A mode (editing, selecting, filtering) with no visible indicator and no obvious exit.
- Actions that appear only on hover, drag with no keyboard route, color as the only selection cue.
- A settings page standing in for good defaults, or a setting for every internal option.
- Invented numbers: hit rates, retention windows, usage stats or support-ticket counts nobody gave you. Say "assumed" or leave a placeholder; numbers below are starting values.

## When to use

- Specifying or reviewing how an action, flow or screen behaves: delete, save, import, share, search, filter, reorder, bulk edit, settings, first run.
- Fixing data loss, annoyance, confusion about state, or too many clicks.
- Choosing density, navigation structure and shortcuts for a given audience.

## When not to use

- Fields, validation timing and error wording: `form-design` if installed. Table appearance and sorting display: `data-tables`. Motion timing: `ui-motion`. Controls and save model on a settings screen: `form-design`; this skill owns what should be a setting at all. Page structure and grids: `layout-structure`. Judging a finished screen: `design-critique`. Defaults that favor the business over the person, and cancel flows: `fair-persuasion`. All if installed.
- A fix that touches one behavior needs only that decision plus the checks.
- An explicit instruction, an existing design system, a platform convention or a regulatory duty beats every default here. If the product already behaves well, say so and change at most one thing.

## When facts are missing

Infer audience, device and frequency from the brief and state the assumption in one line. Ask once only if the chat is interactive and one answer would change the design. Otherwise deliver on stated assumptions and mark unknowns as placeholders. Never invent usage data, quotes or limits.

## Decisions, in order

A small task starts at the decision it touches.

1. **Who and how often.** Name the user, device, input and session length. Default: serve people past their first week but short of expert: visible labels, shortcuts as an extra route, newcomers helped by the first task, not a tour. Change to first-time design for one-off or public contexts (checkout, kiosk, glance on a phone). Long-session tools earn density and keyboard routes; one-job tools get one view, large labeled controls and remembered settings. See [who it is for and feedback](references/who-and-feedback.md).
2. **Default, remember, or ask.** Default: if the product could know, act. Reuse the last choice per kind of thing, show what was assumed beside the control, and keep a reset. Change to asking when a wrong guess is costly and cannot be undone, or the choice is a one-time decision. Remember interface state on the device; store personal data only with a purpose and an off switch; never remember secrets or payment details unasked. See [undo and defaults](references/undo-and-defaults.md).
3. **Mistakes: prevent, then recover, then ask.** Default: constrain input (pickers, ranges, autofill), accept odd input and flag it in place, then make the action undoable (a toast with Undo for about 6 to 10 seconds, trash with retention, version history, a short send delay). Change to an explicit, specific confirmation only when nothing can restore it: money moved, a message sent to others, a legal record, data with no backup. Name the object and what else goes with it, and keep these rare so people still read them.
4. **Save versus publish.** Default: save continuously and quietly, keep drafts through errors and crashes, and make publish, send or share a separate deliberate act. Failures say so; success stays silent.
5. **How state shows.** Default: in place, in the main view (a badge, count, progress ring or sync status), readable at a glance, detail on demand. Never a modal for success. Toasts only for an event that has an action or link; keep a place to review missed notices. Change to an interruption only for something unexpected that blocks the person. Latency ladder and modes: [who it is for and feedback](references/who-and-feedback.md).
6. **Modes.** Default: avoid. When needed (a tool, a selection, a "viewing as" state), show the mode where the eyes are, make Esc or one control exit, and never let one gesture mean two things silently. Keep tool sets to a handful.
7. **Moving around.** Default: three to five visible primary destinations, location always shown, back and Esc preserve scroll, filters and selection, every view has a link, search beyond a few dozen items. Change to a command palette plus a sidebar for dense work tools. Hidden drawers only for secondary destinations. See [navigation and collections](references/navigation-and-collections.md).
8. **Collections.** Default: visible checkboxes when a list can scroll, a bar with the count and actions on selection, undo after a bulk action, edit in place, order and sort remembered. Every pointer feature has a keyboard and touch route. See [navigation and collections](references/navigation-and-collections.md).
9. **Settings.** Default: good defaults first; separate running a command from configuring it (the button uses remembered options, a sibling link opens them); apply reversible settings immediately with undo; group by how often people touch them; search when there are many; say whether a setting is per device or per account; offer reset. Change to an explicit Apply for settings that disrupt others or cannot be reversed. Hold costly features out of the everyday area rather than deleting them.

## Accessibility pairing

Every action reachable by keyboard with a visible focus; undo toasts and status changes announced to screen readers (a polite live region) and not removed before they can be read, with the time limit extendable; modals trap and return focus; hover-only functions get a focusable route; no meaning by color alone. Follow standard accessible component practice.

## Output: a short behavior spec

Unless asked for something else, deliver the assumption line (who, device, how often), then only the rules that apply, each as "when X, do Y, because Z". Add a recovery table or edge cases only when the request is about recovery or failure. Build tasks get the working UI with those states present. A stated length cap or count beats this format: give exactly that and drop the rest.

## Quick checks

- Every destructive action is undoable, or has one specific confirmation with a reason it cannot be undone.
- Nothing asks what the product could remember or infer; the assumption is visible and resettable.
- Every mode has an indicator and an exit; normal success makes no popup.
- Waits are classed by length and the long ones show progress, allow cancel and keep working in the background.
- Selection, drag, hover and shortcut features each have a keyboard and touch route.
- No invented figures; unknowns are placeholders.

## References

- [undo-and-defaults.md](references/undo-and-defaults.md): load when designing delete, save, drafts, import errors, version history, defaults or memory.
- [navigation-and-collections.md](references/navigation-and-collections.md): load for navigation structure, search, filters, selection, bulk actions, reorder and drag.
- [who-and-feedback.md](references/who-and-feedback.md): load for density and device choices, modes, progress and wait handling, notifications, and device-specific contexts.
