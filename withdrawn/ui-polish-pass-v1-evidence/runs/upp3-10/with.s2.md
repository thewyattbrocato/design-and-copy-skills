I haven't seen the code, so this is based on your description. It's ranked by harm, and none of it changes the layout, palette or wording you have now.

**What already works:** the screen is small and has one clear action. The summary card gives people what they need to check before committing.

1. **Confirm does nothing visible while the API call runs.** This is the biggest gap.
   - On tap, disable the button, change its label to "Confirming…", and set `aria-busy`. That stops double-taps, which could create two bookings.
   - Keep Back usable while the call runs, or disable it too. Don't leave it live in a half-submitted state.

2. **A failed call has no handling.**
   - Stay on the screen and show an inline message above the Confirm button, not a toast. Something like: "We couldn't confirm your booking. Your time with [groomer] isn't booked yet. Try again."
   - Announce it with `role="alert"` and keep the summary and the button in place so retry is one tap.
   - Treat a taken slot (a conflict response) separately: "That time was just taken. Pick another time." Make the button take them back to the time picker.
   - Add an offline message too. Don't invent a retry count or a support address. Use a placeholder like [support link] until you have a real one.

3. **The summary card may not read well to screen readers or in edge cases.**
   - Mark it up as a labelled group or a description list (Groomer / Date and time / Price), so it isn't a loose run of text.
   - Include the dog's name if the app knows it. It's the thing people most want to check, and it's missing from your list.
   - Make sure the date and time carry the weekday and the time zone if the salon's zone could differ from the phone's.
   - Check the longest realistic groomer name. It should wrap, not clip.

4. **Focus and keyboard.**
   - Move focus to the heading on arrival, so screen-reader and keyboard users know the page changed.
   - Put a visible focus ring on both Confirm and Back.
   - After a failure, move focus to the error message.
   - Make the Back link a real link or button with enough tap target, at least 44px tall. Text links are often too small.

5. **The handoff to the thank-you page.**
   - Don't navigate until the API succeeds. Then use `replace` rather than `push`, so Back from the thank-you page can't return here and re-confirm.
   - If someone lands on this screen with no pending booking (a refresh or a stale link), show "There's nothing to confirm" with a button to start a booking. Don't show a blank card.

6. **Cosmetic touches that make it feel finished, using your existing style.**
   - Put a one-line reassurance under the price if it's true, such as the cancellation policy. I won't write that line for you, because I don't know your policy.
   - Give the price a clear label ("Total") and align it consistently.
   - Make Confirm full-width on narrow screens. Check the layout at 320px and at 200% text.

I'd leave the motion, the theme and the copy tone alone. They're product decisions, not defects.

**Remaining decisions:** the cancellation policy line, and how conflict errors should route back to the time picker.

**Not checked:** I haven't seen the code or run the screen, so none of this is tested, including with a screen reader.

If you paste the component or tell me the framework, I'll make these changes as a small diff.
