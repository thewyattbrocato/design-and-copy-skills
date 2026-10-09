## Handoff: Invoices screen messages

**Job of the screen:** create, find and send invoices. Anything that competes with that has to earn its place.

**Ranking:** (1) payment failure is the only item with a consequence and a deadline. (2) the Portuguese announcement is informational. (3) the N-key tip is optional. Each gets a different treatment, and only one of them can use the top slot.

### 1. Payment failure: loudest, persistent, top slot

- **Placement:** the only item in the top slot. Full width, above the invoice list.
- **Style:** one warning treatment with an icon and text. It should be the strongest element on the screen, but not a red alarm. Use one solid button, "Update card," as the single primary action. No other buttons.
- **Dismissal:** no close button. It stays until the card is fixed or the plan has paused. If you add "Remind me later," make it a text link, not a second button.
- **Copy:** include the year in the date. Today is 7 October 2026, so "14 March" is already past if it means 2026. Confirm the year, then use something like: "Your card ending 4417 was declined. Update it by 14 March 2027 to keep your plan active."
- **Trigger:** payment failure on the account, cleared automatically when a valid card is saved.

### 2. Portuguese invoices: quiet, dismissible, shown once

- **Placement:** not in the top slot. Put it in the header area as a small "New" badge with a text link, or in the account/help menu as a "What's new" entry.
- **Style:** text-only, same size as body, muted value. No fill, no border, no icon.
- **Dismissal:** an × on the item. Once dismissed, or after the user opens the feature, it doesn't come back.
- **Trigger:** shown to users who have not dismissed it. Remove the badge after about 30 days even if they haven't acted.

### 3. N-key tip: lowest, contextual, retires itself

- **Placement:** next to the "New invoice" button, as a small muted hint ("Press N"). Not on the banner line.
- **Style:** smallest, lowest-contrast element of the three. Plain text, no color.
- **Dismissal:** disappears the first time the user presses N, or after it has been shown about 5 sessions.
- **Trigger:** only when no payment banner is showing.

### Rules that hold across all three

- At most one item in the top slot at a time. The payment message always wins.
- While the payment banner shows, hide the Portuguese item from the header. Keep the N hint, since it sits by the button and doesn't add to the top.
- Do not use the same blue banner for any of them. Each level has a different placement, size, and style.
- Never show an announcement as a stacked banner.

**Assumptions:** the year on the payment date needs confirming, and I've assumed the top slot is the only place for a full-width banner on this screen. If the design already has a "What's new" menu, use it for item 2.
