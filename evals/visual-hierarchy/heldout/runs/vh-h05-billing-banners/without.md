# Invoices screen: message hierarchy spec

**Principle:** loudness should match consequence. Only the card problem can cost the user money or work, so it is the only one that gets a persistent banner. The other two shouldn't compete with it.

## 1. Card declined: loudest, top of screen

- **Placement:** full-width banner above everything, pinned at the top of the Invoices screen. It's the only banner on the screen.
- **Style:** error/warning treatment, using a red or amber background tint, a leading warning icon, and text that meets contrast requirements. Don't rely on color alone, because the icon and the wording also carry the severity.
- **Copy:** "Your card ending 4417 was declined. Your plan will pause on 14 March unless you update it."
  - Include the year if the date could be read as past or far off. Better still, add a relative cue: "in 5 days".
  - Bold "14 March" or the relative cue.
- **Action:** a primary button, **Update card**, that goes straight to the payment form. Don't make it a text link.
- **Dismissal:** not dismissible. It disappears only when the card is fixed. If you must allow dismissal, hide it for the session only and bring it back on the next load.
- **Escalation:** at 3 days or fewer before the pause date, make it stronger (solid red fill, "pauses in 2 days"). Also send an email, since people who ignore the in-app banner won't see it.
- **Accessibility:** `role="alert"` or `role="status"`, depending on whether it appears after load. It must be reachable by keyboard, with the button in tab order.

## 2. Portuguese invoices: quiet, one-time, out of the way

- **Placement:** not a banner. Use a small dismissible card or a "What's new" entry. Two good options are a dot or badge on a "What's new" item in the nav, or a small card in the sidebar or below the invoice list.
- **Style:** neutral (gray or white, subtle border) with a small "New" tag. No blue fill.
- **Copy:** "New: you can now send invoices in Portuguese." Add a link, **Try it**, that goes to the language setting or invoice template.
- **Dismissal:** dismissible with an ×. Once dismissed it never returns, and the state is stored per user. Auto-retire it after about 30 days.
- **Suppression:** hide it entirely while the card banner is showing. Announcements can wait until the user's payment is sorted.
- **Optional targeting:** show it only to users who have Portuguese-speaking clients or a Brazil/Portugal locale. For everyone else it's noise.

## 3. Keyboard-shortcut tip: quietest, contextual

- **Placement:** inline, near where it's useful. Put it as muted helper text next to the **New invoice** button (for example, a small `N` key hint on the button or in its tooltip), or in the empty-state area.
- **Style:** secondary text, with `N` rendered as a keycap. No background, no icon, no banner.
- **Copy:** "Tip: press **N** to start a new invoice."
- **Dismissal:** show it at most a few times. Stop once the user has pressed N or clicked **New invoice** a few times. It needs no dismiss control.
- **Suppression:** never show it alongside the card banner.

## Rules for the developer

1. **Priority queue:** define three levels: `critical` (blocking or billing), `announcement`, and `tip`. Only `critical` may render as a banner. Allow one banner at a time.
2. **Precedence:** if a critical message is active, suppress announcements and tips on that screen. Otherwise show at most one announcement. Tips render inline and never queue up.
3. **Persistence:** store dismissals per user, server-side if possible, so they don't reappear on another device. Critical messages have no dismissal state. They derive from account status.
4. **Colors:** reserve red and amber for problems only. Blue is currently doing everything, so it loses meaning. Use it sparingly or not at all for these.
5. **Test cases:**
   - Card failed: only the red banner shows, with no other messages.
   - Card OK, new feature not dismissed: the announcement card shows and no banner.
   - Everything dismissed: only the inline shortcut hint remains until the user has used it.
   - Card fixed: the banner disappears immediately without a reload.

## Summary

| Message | Loudness | Where | Dismissible |
|---|---|---|---|
| Card declined | High | Top banner, red/amber, button | No |
| Portuguese | Low | Sidebar card or "What's new" | Yes, permanently |
| Press N tip | Minimal | Inline by the New invoice button | Fades out after use |
