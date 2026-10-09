**Welcome modal** (shown once, replaces the wall of text)

> **Welcome to Stackwell**
> Stackwell helps your clinic keep supplies stocked and orders organized.
>
> Let's get your first items in. It takes three steps:
>
> 1. Set your currency and time zone
> 2. Add your locations, like front desk, exam rooms, storage
> 3. Import your item catalog from a spreadsheet
>
> [**Start setup**] [Skip for now]
>
> You can pick this up again anytime from the Setup checklist.

**Setup checklist** (stays visible on the home screen, with progress kept and finished steps checked off)

> **Get Stackwell ready**
>
> **Start here**
> ✓ Set currency and time zone
> ✓ Add locations
> ✓ Import your item catalog
>
> **Next: make ordering easier**
> - Set par levels. *A par level is the amount of an item you want on hand. Stackwell flags items that fall below it.* Start with your most-used items. You can add the rest later.
> - Add vendors and their payment terms
> - Set approval rules for purchase orders
>
> **When you're ready**
> - Invite your team and assign roles
> - Connect your accounting software
> - Schedule weekly cycle counts
>
> Need help? Open the Help Center.

**What I changed**

- **One goal.** After the modal, the admin has their locations and items in the app. The other six tasks are real work they do later, not something to read up front.
- **Fixed the order.** The original had par levels (step 3) before the item import (step 8), but you can't set par levels on items that aren't there yet. Import now comes first.
- **Three steps up front, not nine.** The rest sits in a checklist that tracks progress and can be reopened. Nobody has to remember it.
- **Cut the feature list.** The list of lot tracking, audit logs and the like names things the admin hasn't seen yet. Each can be explained where it appears.
- **Defined "par level" once**, at the moment it's needed. I left "reorder points" out of the setup text. If it's a separate setting, explain it beside that setting.
- **Dropped "your 200+ items."** It made the task sound huge, and the import handles it in one go.

**Assumptions and trade-offs**

- I assumed the grouping and order of the later tasks. Adjust them if, for example, accounting must be connected before the first order.
- "Start setup", "Skip for now" and "Setup checklist" are placeholder labels. Match them to your real UI.
- To see if this works, check how many new admins place a real order within a couple of weeks. That tells you more than whether they finish the modal.
