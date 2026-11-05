# Stackwell setup: rewrite

## Welcome modal (replaces the current one)

> **Welcome to Stackwell**
> Stackwell helps your clinic keep supplies stocked and orders organized.
>
> Let's get your first supply order ready. It takes 4 short steps, and you can stop and pick up again anytime.
>
> **[Start setup]**  ·  Skip for now

The modal does only three jobs: say what Stackwell is for, name the goal, and start the first step. The feature list is cut. Admins will meet those features when they use them.

## Setup checklist (stays visible until done, not a one-time modal)

**Get ready to place your first order**

1. **Set your currency and time zone**
   Used for costs and for order and expiration dates.
2. **Add your locations**
   Places you keep supplies, like front desk, exam rooms, storage.
3. **Import your items from a spreadsheet**
   Start with a few items if you're not sure about all 200+. You can add more later. *[Download sample spreadsheet]*
4. **Add a vendor**
   Just one to start. Payment terms can be added now or later.

When step 4 is done, the checklist updates to say what now works. For example: *"You can now create a purchase order for [vendor name]. [Create order]"*

## "Next, when you're ready" (appears after step 4, each item optional)

- Set par levels, the amount of each item you want on hand. Start with your most-used items. *(Needs your items, so it comes after the import.)*
- Invite your team and assign roles
- Set approval rules for purchase orders
- Connect your accounting software
- Schedule weekly cycle counts

Help Center link sits at the bottom of the checklist, so it's always there.

## What changed and why

- **One goal.** After setup, the admin can place a first order. Nine equal steps became 4 required ones and 5 optional ones.
- **Fixed an ordering problem.** The original had par levels (step 3) before the item import (step 8), but you can't set levels for items that don't exist yet.
- **The checklist persists.** A one-time modal can't be revisited, and nobody finishes nine tasks while a popup is open.
- **No feature inventory.** Terms like "reorder points" and "lot tracking" are better explained where they appear in the product.

**Assumptions:** I haven't seen the product, so the button labels, the "stop and pick up again" behavior, and the sample spreadsheet are my suggestions. Bracketed items are placeholders. To check that it works, look at how many new admins place a real order within their first week without opening the Help Center.
