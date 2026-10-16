# Invoices screen: message hierarchy (spec for dev)

**Job of the screen:** manage and send invoices. The card problem is the only message that threatens that job, so it gets the only loud treatment. The other two must not compete with it.

**Rank:** 1. Card declined. 2. Portuguese. 3. Keyboard tip.

## 1. Card declined: loud, top of page

- **Placement:** full-width banner pinned above the invoice list, below the app header. Always the topmost thing on the screen. It is not dismissible and stays until the card is fixed.
- **Style:** the only red/error-toned element on the screen. Use a solid tinted background with a strong left border or an error icon. The icon and the "Update card" button are the second cue, so it still reads without color.
- **Copy:** keep the content but lead with the consequence.
  - Bold line: **Your card ending 4417 was declined**
  - Regular line: Your plan will pause on 14 March unless you update it.
  - Button: **Update payment method**
- **Action:** one solid primary button, right-aligned in the banner or under the text on narrow screens. It's the only solid primary button on the screen besides the app's own "New invoice" button. If those two collide, make the banner button the filled one and keep "New invoice" as it is. Don't change the button that exists today without checking with me.
- **Escalation (optional, cheap):** from 3 days before the pause date, add "in N days" to the text. Don't add a modal.

## 2. Portuguese: quiet, one-time, dismissible

- **Placement:** not in the banner stack. Show it as a slim, single-line notice below the card banner (or at the top of the list if the card banner is absent), or as a dot or "New" badge on the language picker in the invoice editor, where it's actually useful.
- **Style:** neutral. Grey or very light background, regular-weight text, no icon colour. A small text link, "Try it", is the action. Nothing blue-filled and no button.
- **Behaviour:** has an ✕ and never returns once dismissed. Auto-retire after about 30 days. **Hide it entirely while the card banner is showing.** Two messages at once is plenty, and a launch note should never sit next to a billing problem.

## 3. Keyboard tip: quietest, out of the banner area

- **Placement:** remove it from the top of the page. Put it where the action lives, as a small muted hint next to or inside the "New invoice" button (a `N` key badge, or a tooltip on hover). Or show it in the empty state of the list.
- **Style:** small, secondary-grey text, no background, no border.
- **Behaviour:** no dismiss needed since it's not a banner. If it must be a message, show it once and never again after the user has pressed N or dismissed it.

## Rules for the dev

- Maximum **one banner** at a time in the top slot, chosen by priority: billing > feature news > tips. Tips never use the banner slot.
- Only the card message uses the error colour. Don't reuse it anywhere else on this screen.
- Blue stops being the default for all three. Blue/neutral is for informational content only.
- Expected result: on a squint test you see one red block with one button. Everything else is calm.

**Assumptions:** the card banner is shown only to the account owner (others can't fix it), and the 14 March date is real data from billing, not hard-coded.
