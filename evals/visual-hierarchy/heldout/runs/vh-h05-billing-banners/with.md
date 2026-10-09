# Invoices screen: message hierarchy

**Job of the screen:** let the freelancer see and act on their invoices. Only the payment failure can stop that work, so it is the only message that gets to interrupt.

## Ranking

| Rank | Message | Loudness | Placement | Dismissible? |
|---|---|---|---|---|
| 1 | Card declined | Loud | Full-width banner at the top of the content area, above the invoice list | No. It clears when the card is fixed. |
| 2 | Portuguese invoices | Quiet | Inline, small, dismissible, below the page header or beside it | Yes, permanently |
| 3 | Press N tip | Almost invisible | Not a banner. Put it in the UI as a hint. | Yes, or it goes away on its own |

## 1. Card declined (primary)

- **Style:** the only element on the screen with a saturated status color (amber or red) and a tinted background. Use a warning icon so color isn't the only cue. A neutral banner with an amber left edge also works. Red fits better if the pause is imminent.
- **Copy:** lead with the consequence and give the button the action.
  - Text: "Your card ending 4417 was declined. Your plan will pause on 14 March unless you update it."
  - Bold "14 March" or "will pause". Don't bold the whole sentence.
- **Action:** one solid primary button, "Update card". It's the only solid button in the banner and the only one competing with the page's own main action ("New invoice"). Keep "New invoice" as the page's primary, but make sure the banner's button doesn't visually beat it. A strong outline or a darker tinted button inside the banner is enough.
- **Behavior:**
  - Persistent, with no close button.
  - Nothing else is stacked above or beside it.
  - If the date gets close (say, within 3 days), escalate the color to red. Don't make it bigger.

## 2. Portuguese invoices (secondary)

- **Style:** no colored background. Use a small line of regular-weight text in the muted text color, with a small "New" label (a pill or plain bold text). Keep it to one line. Add a text link, "Try it", rather than a button.
- **Placement:** under the page title or in the header area, left-aligned to the same edge as the invoice list. It should read as a note about the screen, not an alert.
- **Behavior:**
  - Has a close "×".
  - Once dismissed, it never returns.
  - Don't show it at all while the card banner is visible. That day the user has a more urgent job, and the announcement will still be there later. If you'd rather not add that rule, it's fine to show both, as long as the card banner stays clearly louder.

## 3. Press N tip (tertiary)

- **Don't make this a banner.** It's a hint about a control, so attach it to the control.
- **Best:** show a keyboard-key badge ("N") beside or inside the "New invoice" button, or in its tooltip on hover.
- **Alternative:** a one-line muted hint in the empty state or footer of the list.
- **Behavior:** no close button needed if it lives on the button. If it must be a message, show it only to users who haven't used the shortcut yet, and stop after a few sessions.

## What this does to the screen

- **Squint test:** the eye lands on the card banner, then the invoice list and "New invoice". The other two messages shouldn't register until the user looks for them.
- **Grayscale test:** the banner still wins through its icon, its position, its bold date and its button.
- **Share of emphasis:** one colored element, roughly a tenth of what's visible.

## Notes for the developer

- Build three components, not one banner with a color prop: `AlertBanner` (blocking, persistent), `InlineNotice` (dismissible, stored per user), `ShortcutHint` (attached to the button).
- Store dismissals server-side per user, so they don't come back on another device.
- Give the alert `role="alert"` or `role="status"` depending on urgency. The other two shouldn't be announced by screen readers on load.
- Check text contrast on the tinted banner and on the muted text. "Muted" must still pass the minimum for small text.

**Assumptions:** the screen has a "New invoice" button, and you're free to move the N tip out of the banner area. If there's a design system with existing alert colors, use its warning or error tokens rather than new ones.
