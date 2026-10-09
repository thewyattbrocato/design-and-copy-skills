I'd change the structure as well as the wording. A single modal that lists 12 features and 9 steps is too much to take in at once, and nobody can act on it while it's on screen. Here's what I'd do instead.

**1. Welcome modal (shown once)**

> **Welcome to Stackwell**
> Stackwell helps your clinic keep supplies stocked and orders organized.
>
> Setup takes about 15 minutes. Start with the three basics below. You can do the rest whenever you're ready, and your checklist will be waiting on the home screen.
>
> [Start setup] [I'll explore first]

**2. Setup checklist (persistent, on the home screen)**

> **Get started** (about 15 min)
> 1. Set your currency and time zone
> 2. Add your locations (front desk, exam rooms, storage)
> 3. Import your item catalog from a spreadsheet
>
> **Next: set up ordering**
> 4. Add your vendors and payment terms
> 5. Set par levels (the amount you want on hand) for your items
> 6. Set approval rules for purchase orders
>
> **Then: bring in your team**
> 7. Invite your team and assign roles
>
> **When you're ready**
> 8. Connect your accounting software
> 9. Schedule weekly cycle counts
>
> Stuck? Visit the [Help Center].

**What I changed and why**

- **Cut the feature list.** The list of lot tracking, audit logs and so on means nothing to someone who hasn't used the app yet. Features are easier to learn when they show up in context.
- **Split it into a checklist.** Admins can leave and come back, and they can see their progress. A modal only works if they finish in one sitting.
- **Reordered the steps.** The original put par levels (step 3) before the catalog import (step 8), but par levels belong to items, so the items have to exist first. I also grouped the steps by purpose and moved the integration and cycle counts to the end, since they aren't needed on day one.
- **Dropped "Click Finish when done."** The checklist tracks completion itself.
- **Added a way out.** "I'll explore first" respects admins who want to look around before committing.

If you can, make the import template include a par level column. That turns step 5 from "define par levels for 200+ items" into a quick review, which is the most intimidating line in the original.

I made up the "about 15 minutes" estimate, so replace it with a real number or remove it.
