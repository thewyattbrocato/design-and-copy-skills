**The dispatchers are mostly right, but the GM has noticed a real problem. The fix for it isn't the three things the GM proposed.**

Assumptions: dispatchers are on desktop with a keyboard, working all shift. That's about 300 calls a shift on a handful of job types, so they're experts. I haven't seen your console, so I'm taking the double-assignment cause from your description. Please check it against the actual code.

## Why each proposal fails

- **Wizard for every new job:** For repeat experts, a wizard adds a click for every field they already know. At 300 calls a shift, even a few extra seconds per call adds up to a large share of the shift. Dispatchers are on the phone with a stranded caller, so the delay lands on the customer.
- **Tooltips on everything:** They help someone in their first week. After that they only get in the way. They also can't be reached by keyboard.
- **"Are you sure?" before assigning:** People get through 300 of these by pressing Enter without reading. It would be confirmed 300 times a shift and still miss the double-booking. It also doesn't tell them anything, because the dispatcher already believes the truck is free. That belief is why they assigned it.

## What caused the double assignments

A confirm dialog can only ask "are you sure?". The console already has the information that the truck is busy, or it should have. The fix belongs in the system, not in the dialog.

## What to do

1. **Block the double-booking at the source.**
   - When a truck is already on an active job, disable it in the assign list and show "On job #1234, clear ~3:40pm" next to it. Don't hide it, so dispatchers can see why it's unavailable.
   - Enforce the same rule on the server. If two dispatchers assign the same truck at the same moment, the second one fails with a clear message: "Truck 7 was just assigned to #1234 by Sam. Pick another?" Offer the next-nearest free trucks in that message. Check whether this race is what caused your two incidents. It's the most likely cause if the console doesn't refresh live.
   - Keep truck status live on every screen. Stale lists cause this kind of error.
2. **Allow a deliberate override.** Sometimes a truck really can take a second job, such as a nearby tow that finishes first. Make that a separate, explicit action ("Assign anyway") that is logged. It should be the only place a confirmation appears, because it's the only risky case.
3. **Make assignment undoable instead of confirmed.** After assigning, show "Truck 7 → #1234. Undo" for a few seconds. It's one keystroke to reverse, and nobody has to click through it.
4. **Speed up the common job types.**
   - Offer a one-key template for each of the handful of job types that pre-fills the usual fields.
   - Remember the last choice per field.
   - Make the whole new-job flow keyboard-only: Tab order, shortcuts, type-to-search for trucks and customers.
   - Show what was assumed beside each field, with a reset.
5. **Give newcomers help without slowing experts.**
   - Use one short onboarding path for new dispatchers, such as a "training mode" toggle that turns on hints.
   - Add an optional "?" help link per screen, and a wizard for rare job types only.
   - Keep the default screen dense.

## How to settle it with the GM

The GM's goal is fewer mistakes and an easier console, and that's a good goal. Don't argue wizard versus no wizard. Ask for two numbers instead: double-assignments per quarter (currently 2, which would be the target to bring to 0), and average time to create a job. If the fixes in item 1 drive the first to zero without raising the second, the GM has their result.

I can look at the dispatch console code and check how truck availability is calculated and whether assignment is protected against two dispatchers acting at once. Point me at the repo.
