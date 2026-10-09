The main problem is that one modal asks a new admin to read about 12 features and 9 tasks at once, and almost nobody will absorb that. I'd split it into a short welcome and a persistent checklist, and cut the feature list entirely, since people learn the features by doing the steps.

## Welcome modal (shown once)

> **Welcome to Stackwell**
> Let's get your clinic ready to order supplies. Setup takes about 4 steps to start, and you can do the rest later.
>
> [Start setup] [Skip for now]

## Setup checklist (stays on the dashboard until done)

**Get started (required)**
1. **Set your basics.** Choose your clinic's currency and time zone.
2. **Add your locations.** For example: front desk, exam rooms, storage.
3. **Import your items.** Upload your catalog from a spreadsheet. [Download template]
4. **Add your vendors.** Include payment terms for each.

**Set up your team**
5. **Invite your team.** Assign each person a role.
6. **Set approval rules.** Choose who must approve purchase orders.

**Optional, when you're ready**
7. **Set par levels.** Start with your most-used items. You can add the rest over time.
8. **Connect your accounting software.**
9. **Schedule weekly cycle counts.**

> Need help? Visit the [Help Center].

## What changed and why

- **Cut the feature list.** "Lot tracking, expiration alerts, audit logs…" is jargon that means nothing before the user has any data. Introduce those features in context, when they become relevant.
- **Reordered the steps.** Your original order had par levels (step 3) before items were imported (step 8). You can't set par levels for items that don't exist yet. Import now comes before par levels.
- **Grouped the steps and marked some optional.** Four required steps feel manageable. Accounting integration and cycle counts aren't needed on day one.
- **Made par levels incremental.** "Define par levels for each of your 200+ items" sounds like a wall of work. Starting with the most-used items is more realistic.
- **Replaced "Click Finish when done."** A checklist tracks progress and lets people leave and come back. A one-time modal can't do that, and new admins will likely get interrupted partway through.

Two things to check on your side. I assumed a spreadsheet template exists, so drop that link if it doesn't. I also assumed the "about 4 steps" claim holds, so adjust it if the required steps take longer.
