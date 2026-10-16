I'd pick **A**, with a few additions.

**Why A**

- **It puts feedback where the person is looking.** They just tapped the button, so the spinner shows up in the same spot. They know the tap registered, and nothing else on the page moves.
- **Disabling the button prevents double charges.** On a payment form this matters more than anything else here. A person who sees nothing happen for 4 seconds will tap again. Disable the button, and also send an idempotency key with the charge request so a retry or double-submit can't bill them twice.
- **It handles the 1–6 second range well.** A spinner is open-ended, so it works whether the bank answers in 1 second or 6.
- **It matches the moment.** The person is giving money, so you want calm. A spinner on the button is quiet, and a gray-out modal can feel like something is wrong.

**Why not B or C**

- **B (progress bar):** It fills over a fixed 3 seconds, but the charge takes 1 to 6. The bar will either finish early and sit there looking stuck, or hit 100% while the charge is still running. A fake progress bar also makes a bank delay look like a bug. It's also at the top of the page, away from the button, and on mobile that part may be off-screen.
- **C (modal):** It's the heaviest option. It blocks the whole page for a task that is usually short, and a flash of modal on a 1-second charge feels jarring. It also adds focus-trap and accessibility work. It does make it obvious not to tap again, but disabling the button already handles that.

**Small improvements to A**

- **Keep the button width fixed** so it doesn't shrink when the label becomes a spinner.
- **Change the label instead of removing it.** "Giving…" with a spinner is better than a bare spinner. It's clearer and works better for screen readers.
- **Set `aria-busy` and use an `aria-live` region** so assistive tech announces that the payment is processing.
- **After about 6–8 seconds, show a quiet line under the button.** Something like "Still working. Please don't refresh." covers slow banks. Set a hard timeout too, with a clear message that says whether the card was charged or not.
- **Disable the amount fields too**, so the amount can't change mid-charge.

**When the charge succeeds**

Do these things in order:

1. **Confirm the gift first.** Replace the button, or the whole form, with a success state: a checkmark and "Thank you! Your $25 gift went through." This is the main event, and it should come before the total updates.
2. **Then update the total, with some animation.** Count the number up from $41,860 to $41,885 over about 600–800ms, and grow the progress bar to match. This lets the person see their own gift move the number. Make sure the number shown is the real server-confirmed total and not a guess. If other donors gave at the same time, the total may rise by more than $25. That's fine, so just show the server's number.
3. **Say what the gift does,** if you have the data. For example, "Your $25 helps remove about X pounds of trash from the river." That connects the money to the mission, and it's the best thing you can put on this screen.
4. **Tell them about the receipt.** For example, "A receipt is on its way to you@email.com."
5. **Move focus and announce it.** Move keyboard focus to the success message and put it in an `aria-live` region. Respect `prefers-reduced-motion` by skipping the count-up and just swapping the number.
6. **Offer one next step,** such as share, give monthly, or done. Don't show the same "Give $25" button again, because it invites an accidental second gift.

**When the charge fails**

Re-enable the button and show an error next to it. Say what happened ("Your bank declined the card") and what to do. Keep the amount and the card details filled in. Don't touch the total.
