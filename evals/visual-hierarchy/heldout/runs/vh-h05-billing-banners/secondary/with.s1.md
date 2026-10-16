**Job of the Invoices screen:** create and send invoices. Only the card problem can stop that, so it's the only message that gets a banner. The other two are secondary and tertiary, and the tip isn't a banner at all.

## Spec

| | 1. Card declined | 2. Portuguese announcement | 3. Press N tip |
|---|---|---|---|
| **Rank** | Primary (blocking) | Secondary (news) | Tertiary (hint) |
| **Where** | Top banner slot, full width, above the page header | Dismissible card in the page's side or empty area, or inside the Send dialog's language field | Inline on the "New invoice" button as a small `N` key badge; optional one-time tooltip on first visit |
| **Tone** | Warning or error color (not blue), warning icon, bold text | Neutral surface, info icon, regular weight | No surface; `N` badge in muted text |
| **Copy** | "Your card ending 4417 was declined. Your plan pauses on [date] unless you update it." | "New: send invoices in Portuguese." | None beyond the badge |
| **Action** | One solid button: "Update card" | Text link: "Try it" (opens language setting) | None |
| **Dismiss** | Not dismissible until the card is fixed; it returns if the problem recurs | Close button; stays dismissed; auto-retires after ~30 days | Hide after N is used a few times or the user dismisses the tooltip |
| **Shows** | Until resolved | Once per user, then retires | Badge always visible; tooltip once |

## Rules for developers

- **One banner slot, priority order:** account-critical > news. Never stack banners. If news is queued while the card banner is up, news waits.
- **Blue is reserved for the main action,** so the banner is not blue. Keep the card banner's color distinct from the announcement's neutral surface.
- **Do not add emphasis to the tip.** It should be the quietest thing on screen.
- **Persist dismissals** per user, so an announcement is never shown twice.

## Notes

- **Check the date.** Today is 15 October 2026, so "14 March" is either next year or a stale date. Show the year in the copy and pull the date from billing rather than hardcoding it.
- **Pick one primary action for the card banner.** If you also want a "Dismiss" option, make it a text link so "Update card" stays the only solid button.
