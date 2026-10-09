# Stackwell setup rewrite

**The one thing:** after setup, a new admin can send their first purchase order.

The original modal lists 9 steps and a dozen features, then disappears after one viewing. I'd replace it with a short welcome and a checklist that stays on the home screen. That way nobody has to memorize steps.

## 1. Welcome modal (shown once, skippable)

> **Welcome to Stackwell**
> Stackwell helps your clinic keep supplies stocked and orders organized.
>
> Let's get you to your first purchase order. It takes 4 short steps.
>
> **[Start setup]**  ·  Skip for now

Below the buttons: "Your setup checklist stays on the home screen."

## 2. Setup checklist (persistent, one step open at a time)

**Get to your first purchase order**

1. **Set your currency and time zone.** *Used on every order and report.*
2. **Add your locations.** *Places where you keep supplies, like front desk, exam rooms, storage.*
3. **Import your items.** *Upload a spreadsheet of what you stock. [Download a sample spreadsheet]*
4. **Add a vendor.** *Who you order from, and their payment terms.*

When step 4 is done, the checklist becomes:

> **You're ready to order.** [Create a purchase order]

Each step opens the real screen for that task. The checklist stays visible while they work. When a step finishes, it confirms what now works. For example: "214 items imported into 3 locations. Next: add a vendor." The counts come from the actual import.

## 3. "Later" section (collapsed under the checklist)

Show these only after the first order, or whenever someone opens the section. Each is one line stating what it does for them:

- **Set par levels**: so Stackwell can tell you when to reorder. *Start with your 10 most-used items, not all 200+.*
- **Set approval rules**: require sign-off on orders over an amount you choose.
- **Invite your team and assign roles**
- **Connect your accounting software**
- **Schedule weekly cycle counts**

## What changed and why

- **Cut from 9 steps to 4.** Everything else is a real task, but not one needed to place an order. Moving it to "Later" keeps new admins from facing it all at once.
- **Dropped the feature list.** Lot tracking, audit logs and the rest will make sense when they meet them in use. Listing them up front taught nothing.
- **Reordered by dependency.** You need locations and items before vendors, and all three before an order. The original order had par levels before vendors, and a spreadsheet import after hand-defining items.
- **Replaced "define par levels for each of your 200+ items"** with a spreadsheet import. The original contradicted itself, since step 8 imports the catalog that step 3 asks you to build by hand.
- **Removed "Click Finish" and the Help Center line.** Done is now defined by the first order. Help should sit as a persistent link on each step.

**Assumptions:**
- Button and screen names in brackets are placeholders, so use your real labels.
- I assumed a spreadsheet import and sample file exist. If not, step 3 should be "Add your first items."

**How to measure it:** check how many new admins send a purchase order on their own a week or two after setup. Completion of the checklist itself is the weaker signal.
