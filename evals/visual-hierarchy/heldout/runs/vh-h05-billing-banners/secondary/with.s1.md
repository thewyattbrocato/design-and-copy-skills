**Flag before handoff:** today is 7 October 2026, so "pauses on 14 March" is already in the past. Either the copy is hardcoded and stale, or the date is wrong. Your developer should pull the real pause date from billing data, and the message should change once the plan is actually paused.

## Loudness and placement

| | Message | Loudness | Where |
|---|---|---|---|
| 1 | Card declined | **Loudest, but as a warning, not a blue banner.** Persistent until resolved. | Top of the Invoices screen in one fixed slot, and a warning dot on the account/billing menu item everywhere else. |
| 2 | Portuguese invoices | **Quiet.** Dismissible once, then remembered. | Not on the Invoices screen. Put it in the "What's new" entry with a dot on the menu item, and as a hint next to the language field in the send-invoice dialog, where it's useful. |
| 3 | Press N | **Quietest.** No banner. | Inline with the "New invoice" button as a shortcut label (`New invoice  N`). Optionally a one-time tooltip for new users. |

## Developer spec

**Shared rules**
- One banner slot. Never stack banners. If more than one is eligible, show the highest-priority one: billing > announcements > tips.
- Reserve the blue solid fill for the page's primary action. Information banners use a neutral or light-blue surface with text, not a solid fill.

**Message 1: payment failure**
- Warning treatment (amber, or red if the pause is close), with an icon and a text label. Don't rely on color alone.
- Copy: "Your card ending 4417 was declined. Your plan pauses on [date] unless you update it."
- One action: "Update card" (primary). No "Dismiss" button, because it stays until the payment method is fixed.
- Shows on every screen through the account menu indicator, so it can't be missed by someone who never opens billing.
- Clears automatically when a valid card is saved.

**Message 2: Portuguese**
- Dismissible with an × (or "Got it"). Once dismissed, never shown again.
- Shown only in the "What's new" list and as a hint in the language selector. Not a blocking modal.

**Message 3: keyboard shortcut**
- Render the `N` hint as a small label on the "New invoice" button. Hide it on touch devices.
- Optional one-time tooltip for users who have never used the shortcut. Once they press N, stop showing it.

## Trade-off
Message 1 is the only one that costs the user money or access, so it's the only one allowed to interrupt. If the team pushes back on a persistent banner, a warning dot plus a persistent in-page warning is the minimum I'd accept.
