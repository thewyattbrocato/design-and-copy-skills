# Undo, recovery, defaults and memory

Load when an action can destroy or overwrite something, when work can be lost, or when the product asks questions it might answer itself.

## Pick the recovery by the action

| Action | Default recovery | Confirmation only if |
|---|---|---|
| Delete, archive, move, rename | Act at once, toast with Undo, item stays in a trash for a stated period | Permanent deletion from the trash: ask once, name the item and what goes with it |
| Overwrite, bulk edit, import | Keep the previous version or a snapshot; offer revert | Nothing can restore the prior state |
| Send, publish, share | A short delay with Undo, or a clear separate publish step | The message reaches other people and cannot be recalled |
| Money, legal records, anything audited | Reversal as a new recorded entry, not an erased one | Always a specific review, since the effect is real |
| Settings and layout | Apply at once, offer Undo and Reset | Changes that affect other people |

Rules that make undo trustworthy:
- Undo covers every kind of change, including ones made in dialogs, and is reachable from the keyboard.
- Name what will be undone ("Undo move of 3 items"), and never style it as an error.
- The toast stays at least about 6 to 10 seconds, longer for bulk actions, and pauses on hover and focus; the action stays reachable afterwards (history, trash).
- Soft-deleted data is really recoverable and the retention period is shown where people look for it.
- Choose the simplest shape that covers real regret: one step for small things, a stack for editors, a browsable trash for objects, named versions for documents people return to. Redo exists because stacks overshoot.
- An optimistic update needs a visible rollback and a visible sync state, not silence.

## Confirmations that work

A confirmation works when it is rare and specific. If people see one every day they answer it the same way every time and it protects no one. Write the title as the verb plus the object, use the same button labels as the title ("Delete 12 files", "Keep files"), never "OK/Cancel", and put the cheaper choice in focus.

## Saving and losing work

- Autosave after a pause or at natural boundaries; show a quiet state ("Saving", "Saved", "Offline, will sync") in place.
- Persist before acknowledging. On failure keep everything typed and say what was kept.
- Restore drafts after a crash or a closed tab; offer the history, not a lecture.
- Never discard valid parts because one part failed.

## Tolerating bad input

Accept the odd record, flag it where the person is looking, let them continue and fix later, and keep a trail of what changed; never rewrite typed input silently. For a bulk import, process the good rows, hold the bad ones in a list with the reason for each and a way to download or fix them, and report counts at the end. Hard gates stay for money, safety and legal records. Field-level validation timing follows `form-design` if installed: check on submit, then re-check live after the first error; a live check after a short pause suits availability and format rules people cannot guess.

## Defaults and memory

- Test every question: could the product have known? Use last choice, most common choice, or a value derived from context (a shipping speed that follows order size).
- Remember per kind of thing, not globally: last export format per report type, last view per list, a currency that follows the selected store.
- When a choice flips between two values, last-used is often wrong; condition on context or offer both.
- When a guess is right most of the time and undo is cheap, act and show what was assumed beside the control. Below that, or when undo is impossible, ask. Do not make up the hit rate; say "assumed" if unknown.
- Start from a plausible draft or template, not a blank page or an interview. Very expert users may want blank: let them choose it.
- Keep a visible reset. Remember interface state on the device; personal profiles need a stated purpose and an off switch. Defaults that serve the business at the person's expense (pre-ticked upsells, auto-renewal) are `fair-persuasion` territory if installed.
