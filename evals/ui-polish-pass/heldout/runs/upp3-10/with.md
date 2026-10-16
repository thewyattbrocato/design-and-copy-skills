The screen has the right content and a clear single action. It feels unfinished because it only covers the happy path. I haven't seen your code, so these are the changes I'd make, ranked by harm. I'd keep your layout, colors, type and wording.

1. **Confirm gives no feedback and can be double-tapped.** This is the biggest gap, because a double tap could book twice.
   - On press, disable Confirm right away, set `aria-busy`, and change the label to "Confirming…".
   - Keep the button the same width so the layout doesn't jump.
   - Ignore further presses until the call returns.
   - Send an idempotency key with the request if the API supports one.

2. **A failed API call has no outcome.** Today it probably fails silently or navigates anyway.
   - Navigate to the thank-you page only after the call succeeds.
   - On failure, show an inline message above the button that stays until the next attempt. Make it a `role="alert"` region and keep the summary card on screen.
   - Re-enable the button as "Try again".
   - Use specific copy for each case:
     - **Offline:** "You're offline. Reconnect and try again."
     - **Slot taken (if the API returns a conflict):** "[Groomer] was just booked at that time. Go back to pick another."
     - **Anything else:** "We couldn't complete your booking. Nothing was charged. Try again." Only say this if it's true.

3. **The summary doesn't help people check their booking.**
   - Use a labeled list (`<dl>`) with "Groomer", "Date", "Time" and "Price", so screen readers announce what each value is.
   - Show the full date with the weekday ("Sat, Oct 24 · 10:00 AM"), not a numeric date.
   - Add the dog's name and the service if you have them. A confirm step is mainly for checking those, and it's the thing that makes the screen feel specific to Pawsworth.
   - Let long groomer names wrap.
   - Right-align the price in the same format everywhere (currency, two decimals).
   - If a cancellation or payment policy applies, add a single line under the card. I'd use the placeholder [policy line] until you supply the wording.

4. **Back is a bare text link and hard to tap or find.**
   - Give it a tap target of at least 44px.
   - Use a visible focus ring. Check that there's no `outline: none` without a replacement.
   - Label it "Back to choose a time", or whatever the previous step actually is.
   - While Confirm is in flight, disable Back or make sure it can't leave the user in a half-submitted state.

5. **Focus and keyboard.**
   - Make the heading the page's `h1` and move focus to it when the screen loads, so screen-reader and keyboard users land at the top.
   - Make Enter on Confirm behave like a tap.
   - Check that the order is heading, summary, Confirm, Back.
   - If a failure message appears, leave focus on the button and let the alert announce it.

6. **Cosmetic polish, only if it matches your existing style.**
   - Give the Confirm button a clear primary treatment: full width on narrow screens, with the price in the label ("Confirm · $65").
   - Check that the card text and the Back link meet contrast (4.5:1).
   - Check the layout at 320px width and at 200% text size.
   - I wouldn't add animation, new illustrations or a dark theme unless you already have them.

The thank-you page should show the same groomer, date and time, so people see that what they confirmed is what got booked. I'd also check that reloading it doesn't re-trigger the booking.

I haven't run any of this or tested it with a screen reader. If you paste the component, I'll make these changes directly, keeping the diff small.
