# Invoices screen: message hierarchy spec

**Job of the screen:** let the freelancer see and act on their invoices. Only the card problem threatens that, because the plan pauses on 14 March. The other two are optional.

## Ranking

| Rank | Message | Loudness | Placement |
|---|---|---|---|
| 1 | Card declined | Loud. The only message that interrupts. | Full-width banner at the top of the Invoices screen, above the page title and list. |
| 2 | Portuguese invoices | Quiet. Dismissible. | Not a banner. Put it where the feature is used (see below). |
| 3 | Press N tip | Quietest. | Inline hint next to the "New invoice" button. No container. |

## 1. Card declined (the only banner)

- **Style:** use the app's warning/error treatment, not blue. Blue is the "info" color and all three currently use it. Use a tinted red or amber background with a solid left edge or border, and dark text that meets contrast requirements. Add a warning icon so the message doesn't rely on color alone.
- **Copy:** keep the text. Make "Your card ending 4417 was declined" bold, and leave the rest ("Your plan will pause on 14 March unless you update it.") regular weight.
- **Action:** one solid primary button in the banner, "Update card", which opens the payment form directly. This is the only solid primary button in the banner area.
- **Dismissal:** no dismiss (×) button. It disappears when the card is fixed. If you must allow dismissal, hide it for the current session only and bring it back on the next load.
- **Escalation:** if you want to go further, make it stronger when the deadline is near. Within 3 days of the pause date, use the full error color. Before that, use amber. Check the date handling with your developer. This is optional.
- **Also show it elsewhere:** put a small warning dot or badge on the Billing or Settings nav item, so the problem is visible when the user leaves this screen.

## 2. Portuguese invoices (announcement)

- **Don't make it a banner.** A feature announcement gets in the way of work and has no deadline.
- **Preferred:** show it as a small "New" badge plus a one-line text link, next to the language selector in the new-invoice form (or wherever the invoice language is set). That's where someone who wants Portuguese will look for it.
- **If you also want it on the Invoices screen:** use one slim, neutral-gray line (no colored fill) below the list header or at the bottom of the page, with a text link ("Try it") and a dismiss ×. Show it once, and when dismissed never show it again.
- **Never show it at the same time as the card banner.** If the card banner is visible, hide the announcement. Payment comes first.

## 3. "Press N" tip

- **Don't make it a banner either.** It's a hint, not a message.
- Show it as small, muted-gray text next to or under the "New invoice" button, with the key rendered as a keyboard-key chip: `New invoice  [N]`. Alternatively, show it only in the button's tooltip.
- It needs no dismiss button and no container, and it is permanent, not tied to any state.
- If you prefer to keep it as a tip, show it only to users who haven't used the shortcut yet, and stop showing it after they do.

## Rules for the developer

1. **One banner slot, one message.** If several messages compete, show only the highest-priority one. Priority: payment problem > anything else.
2. **Severity decides the color.** Error/warning for billing, neutral gray for announcements and tips. Reserve blue/info for anything that remains.
3. **Persistence:** billing stays until fixed. The announcement is dismissed once and stays dismissed. The tip is permanent but quiet.
4. **Accessibility:** mark the billing banner `role="alert"` (or `role="status"` if it's present on load and not injected later). Don't rely on color alone. Keep text contrast at 4.5:1 or better.
5. **Result when all three apply:** the screen shows one loud red/amber banner at the top, a muted "[N]" hint by the New invoice button, and the Portuguese note only in the language setting. The top of the screen now has one thing to read.

**Notes:**
- I assumed the app has a Billing or Settings nav item and a language setting in the invoice form. If it doesn't, put the Portuguese note in the slim gray line described above.
- I haven't seen your actual screen or design system. If you have defined warning and error colors, use those instead of the colors described here.
