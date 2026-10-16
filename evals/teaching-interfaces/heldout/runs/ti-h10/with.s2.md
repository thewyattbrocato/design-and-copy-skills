# Stackwell setup: rewrite

**The one thing:** after setup, an admin can place their first purchase order.

The main problem isn't the wording. A nine-step list in a one-time modal can't be learned, because the modal disappears the moment they start. I'd replace it with a short welcome and a setup checklist that stays on screen while they work.

## Welcome modal (shown once, with Skip)

> **Welcome to Stackwell**
> Stackwell helps your clinic keep supplies stocked and orders organized.
>
> Let's get your first order ready. It takes three quick steps:
>
> 1. Add your items
> 2. Add a vendor
> 3. Place an order
>
> The rest can wait.
>
> **[Start]**  ·  Skip for now

## Checklist (a persistent panel, not a modal)

**Get ready to order**
- ☐ **Add your items.** Import a spreadsheet of your supplies, or add a few by hand. *(Start with 5–10 if you like; you can add the rest later.)*
- ☐ **Add a vendor.** Enter who you order from. Payment terms are optional for now.
- ☐ **Place your first order.** Choose a vendor and items, then send it.

When step 3 is done, the panel confirms what now works: *"Your order to [vendor] is sent. When it arrives, open it here to record what you received."*

**Set up when you're ready** (collapsed, each item opens the real screen)
- Set currency and time zone
- Add locations (front desk, exam rooms, storage)
- Set par levels, the stock amount you want on hand. *Do these after items are added; start with your most-used supplies.*
- Set approval rules for orders
- Invite your team and assign roles
- Connect accounting software
- Schedule weekly cycle counts

A **Help Center** link stays at the bottom of the panel, so the panel doubles as the way back.

## What changed and why

- **Nine steps became three.** A first-time admin needs a few new ideas before acting, not nine. The rest is still there, but as optional later work.
- **The order is fixed.** The original had par levels before the item import, but par levels need items to exist.
- **The feature list is gone** (lot tracking, audit logs, cost reports, and so on). Listing features before someone has used the product teaches nothing. Let them discover those in context.
- **"200+ items" no longer reads as homework.** The list says you can start with a handful.
- **Currency and time zone are demoted.** If possible, default them from the clinic's address at sign-up so they aren't a step at all.

## Assumptions

- Items, vendor and order are the true minimum path. If Stackwell requires locations or currency before an order can be placed, move those into the first group.
- I didn't name specific buttons or menu paths, since I don't know them. Tie each checklist row to its real screen.

To judge whether it works, check how many new admins place a second order a week or two later without opening the Help Center. Finishing the checklist isn't the measure.
