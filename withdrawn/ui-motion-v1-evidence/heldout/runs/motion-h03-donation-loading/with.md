**Pick A**, with a few adjustments. Put the progress inside the button, because that's where the person is looking and where their finger just was. B and C both have problems.

- **B (top progress bar):** The bar fills over about 3 seconds, but the charge takes 1 to 6. A fixed fill will either finish early and sit there, or lie about progress. It's also far from the button, and a bank wait has no real percentage to show.
- **C (modal):** It's the heaviest option for the most anxious moment. It hides the amount and the page they're about to trust with their card, and for a 1 second charge it flashes on and off. Reserve it for a case that needs it, like a 3-D Secure challenge.

**How to build A**

1. **Acknowledge within 100 ms.** The button shows its pressed state immediately (scale about 0.98, 100 ms).
2. **Swap the label for a spinner in place.** Keep the button's width fixed so nothing shifts. A fast 1 second charge shouldn't flash a spinner, so show it after about 300 ms. By then the pressed state has already confirmed the tap.
3. **Don't leave the label blank.** After about 3 seconds, change the text to "Processing…" or "Still working…". This covers the 6 second bank case, where a bare spinner starts to feel broken.
4. **Block double-submits in code, not just visually.** Use `aria-disabled` plus a handler guard and an idempotency key on the charge request. A double charge is the worst failure on this page. Disabling here is justified because it's a commit that must finish. Also set `aria-busy` and announce "Processing your gift" through a polite live region.
5. **Lock the amount and other fields in place** while the charge is in flight, without graying out the page.
6. **Don't be optimistic.** The charge can fail in ways that matter, so show the total change only after the server confirms.

**When the charge succeeds**

The job is to confirm the gift and show cause and effect, on a path people take rarely. That earns a bit more motion than a normal control, but it should stay calm.

1. **Button (0 to 200 ms):** The spinner crossfades to a checkmark and "Thank you!". Use ease-out with no bounce. Keep the button in this state rather than resetting it.
2. **Total (starting about 150 ms in):**
   - Update "$41,860 raised" to "$41,885". Tick the number from old to new over about 400 to 600 ms, ease-out. It's a 25-dollar change, so the tick is short.
   - Give the progress bar a small fill extension over about 400 ms with transform, not width. The number and the bar should move together, so they read as one change.
   - Briefly highlight the number, for example a soft background tint that fades over about 800 ms.
3. **Message (about 300 ms in):** Show persistent text, such as "Your $25 gift is in. Receipt sent to you@…", with a fade of 200 ms or less. Move focus to it or announce it in a live region. Don't use a toast that disappears, because people want to see the receipt confirmation.
4. **Next step:** After the confirmation, offer one clear action, like sharing or setting up a monthly gift. Don't auto-redirect.

If the page's total also changes from other donors (polling or a live feed), don't animate those updates the same way. Update them quietly, so only the person's own gift gets the highlight.

**Failure case:** The spinner reverts to the label, and plain text appears next to the button, such as "Your bank declined this card. Try another card." Move focus to that message. A small shake is optional, and you can skip it. Keep the entered card details.

**Reduced motion:** Drop the count-up tick, the bar extension and any scale. Keep the spinner (or a static "Processing…"), the checkmark swap, the color highlight and the focus states. The total simply changes, and the text message still confirms it.

**Numbers**

| Moment | Duration | Easing |
|---|---|---|
| Press | 100 ms | ease-out |
| Spinner delay | 300 ms | n/a |
| Spinner → check | 200 ms | ease-out |
| Total tick and bar | 400 to 600 ms | ease-out |
| Highlight fade | 800 ms | linear or ease-out |
| Message fade-in | 200 ms | ease-out |
