# Invoices screen: message hierarchy

Rank the three messages by consequence. Only one of them risks something the user cares about, so only that one should look different from the rest.

| # | Message | Level | Placement | Dismissible? |
|---|---|---|---|---|
| 1 | Card declined | **Critical** | Persistent banner at the top of the screen, above the page content | No. It clears when the card is fixed. |
| 2 | Portuguese invoices | **Informational** | Small, quiet card or inline row, below the invoice list header or in a sidebar | Yes, and the dismissal is remembered |
| 3 | Press N tip | **Passive hint** | Not a banner. Put it in the empty state, the "New invoice" button tooltip, or a small footer hint. | Yes, and it disappears for good once the user has pressed N |

## 1. Card declined (loud)

- **Style:** Red or amber, with a warning icon. It should be the only strongly colored element on the page. Use a solid tinted background, not the shared blue.
- **Copy:** "Your card ending 4417 was declined. Your plan will pause on 14 March unless you update it."
- **Action:** A primary button, **Update card**, that goes straight to the payment form. The banner shouldn't only describe the problem.
- **Position:** Pinned at the top. It stays visible when the invoice list scrolls, or sticks to the top of the viewport.
- **Persistence:** It shows on every visit until the payment succeeds. Don't offer an X. If you want a release valve, offer "Remind me later" that hides it for 24 hours. Make it come back as more urgent as the date nears, for example in the last 3 days.
- **Accessibility:** Use `role="alert"` or `aria-live="assertive"`. Don't rely on color alone, because the icon and the text carry the meaning too.
- **Also:** Send this by email as well. Someone who doesn't open the app before 14 March shouldn't lose their plan.

## 2. Portuguese invoices (medium-quiet)

- **Style:** Neutral or very light tint, with a small "New" badge. No saturated color, so it doesn't compete with the card warning.
- **Copy:** "New: you can now send invoices in Portuguese." Add a link, **Try it**, to the language setting or invoice template.
- **Position:** Below the main action area, not above the invoices. It must never push the invoice list down.
- **Persistence:** Dismissible with an X. Store the dismissal per user and never show it again. Auto-expire it after about 30 days even if it wasn't dismissed.
- **Accessibility:** `role="status"` (polite).
- **Rule:** While the card banner is showing, **hide this message entirely**. Never show it at the same time as a critical message.

## 3. Press N tip (almost invisible)

- **Style:** Plain gray text with a keyboard-key glyph (`N`). No box, no banner.
- **Position:** Pick one of these:
  - Next to the **New invoice** button, as a tooltip or label ("New invoice `N`").
  - In the empty state when the user has no invoices.
  - As a small hint at the bottom of the list.
- **Persistence:** Stop showing it permanently after the user presses N once, or after about 3 sessions.
- **Rule:** Don't show it while any other message is showing. Tips only appear on a clear screen.

## Rules for the developer

1. **Three severity levels, not one banner component.** The levels are `critical`, `info` and `hint`, and each has its own styles and behavior.
2. **At most one banner-style message at a time**, chosen by priority: critical, then info. The hint is never a banner.
3. **Never stack more than one message above the invoice list.** The invoices are the main content.
4. **Colors:** Reserve red or amber for billing and account-risk messages only. If feature announcements ever use it, the warning stops standing out.
5. **Dismissal state is stored server-side per user**, not in local storage, so dismissals survive across devices.

## One thing to check

I assumed the 14 March date appears as-is. Consider showing "in 5 days" or "in 5 months" next to it, or include the year, so the urgency is clear at a glance. Escalate the styling as the date gets closer.
