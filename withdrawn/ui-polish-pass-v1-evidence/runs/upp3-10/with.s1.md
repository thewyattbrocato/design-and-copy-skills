The screen is missing its unhappy paths and some of the information a person needs before committing. I'd keep the layout, look and wording, and fix these in order of harm:

1. **Confirm is silent while the API call runs.**
   - On tap, disable the button right away and change the label to "Confirming…". That stops double-bookings, which matter most here.
   - Keep the button's width fixed so it doesn't jump.

2. **A failed call has no handling.**
   - Show an inline message above the button and move focus to it. Announce it with `role="alert"`.
   - The message should say the booking wasn't made and that nothing was charged, but only if that's true. For example: "We couldn't confirm your booking. Check your connection and try again."
   - Keep the summary on screen and leave Confirm enabled as the retry.
   - Handle "that time was just taken" separately. Say so and send the person back to pick another slot. Don't show a generic retry for it.

3. **The summary card leaves out what the person is committing to.**
   - Add the dog's name and the service (e.g. "Bath & trim"). Without them it's unclear what's being booked.
   - Say what the price is: the total, due when, and whether it's charged now or at the salon. I don't know your payment flow, so confirm which applies.
   - Make the date and time readable ("Sat, Oct 18 · 10:30 AM"), and show the duration if you have it.
   - Add a one-line cancellation or change note only if you have a real policy. Otherwise leave a `[policy link]` placeholder.
   - Mark up the card as a labelled list (`dl`) so a screen reader reads each label with its value.

4. **Back is weak.**
   - It's a bare text link, so give it a larger tap target (at least 44px) and a visible focus ring.
   - Disable or hide it while the request is in flight, so nobody backs out mid-booking.
   - Label it "Back to change time" or similar so it says what it does.

5. **The heading is generic.**
   - Keep "Confirm booking", but add one friendly line under it, such as "Check the details, then we'll save [dog name]'s spot." That adds some Pawsworth voice without a redesign.
   - Don't add mascots, confetti or new illustration unless you want a visual change.

6. **Smaller checks.**
   - Make sure a long groomer or dog name wraps rather than clipping.
   - Give the card and Confirm button a 320px-wide layout check, and check 200% text size.
   - Move focus to the heading when the screen loads.
   - Confirm that the thank-you page shows the same details, so the loop feels finished.
   - Don't add a "Are you sure?" dialog. Confirm is already the confirmation step.

I haven't seen the code, so none of this is tested. I also haven't checked it with a screen reader. If you paste the component, I'll make these changes in it directly. Two things need your input: the payment timing and the cancellation policy.
