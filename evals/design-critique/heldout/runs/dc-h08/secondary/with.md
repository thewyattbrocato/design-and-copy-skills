I'd group the toggles by **what they're about**, not by the 14 flat switches, and put channel (push vs. email) in columns. That cuts the visible rows to about nine and makes each group's purpose clear.

**Layout sketch**

```
Notifications

              [ Push ]   [ Email ]          ← master switches live in the column headers

My garden
  Watering reminders         ☑  ☐
  Frost alerts               ☑  ☑
  Harvest windows            ☑  ☐

Community
  Friend requests            ☑  ☑
  Comments on my beds        ☑  ☐
  Shared bed invites         ☑  ☑

Ideas & summaries
  New plant suggestions      ☐  ☐
  Plant of the week          ☐  ☐
  Weekly summary email       —  ☑

Quiet hours                  10pm–7am  >     ← applies to push only; shown under Push

News & offers
  Product news               —  ☐
  Sale announcements         ☐  ☐
```

**Why this works**

- **Column headers replace the two master toggles.** "Push" and "Email" can be switched off as a whole from the header, so people don't have to hunt for a master row or wonder how it relates to the others.
- **Sections carry the meaning.** "My garden" and "Community" describe what someone is opting into, which is easier to scan than a list of identical labels.
- **Separate "News & offers" from everything else.** These are marketing messages with their own consent rules (unsubscribe requirements, and GDPR consent if you have EU users). Keeping them apart lets people turn off all promotions in one tap, and it keeps you from accidentally burying them under a functional setting. Use a "Turn off all news & offers" link there.
- **Quiet hours sits by Push** because it only affects push. Putting it in the general list suggests it governs email too.
- **Use sensible defaults.** Most people will never open this screen, so set the defaults to what a typical gardener would want. Leave discovery and promotions off by default. Ask for sales and news consent explicitly, not through a pre-checked box.

**Smaller decisions**

- If a cell is not applicable, like "Product news" under Push, show a dash instead of a disabled toggle.
- Consider a short line under each section header explaining it ("Reminders for your beds and plants"). That does more for overwhelm than extra spacing.
- Test it with five or so real users by asking them to change one specific setting. Their misses will tell you more than the layout debate will.
