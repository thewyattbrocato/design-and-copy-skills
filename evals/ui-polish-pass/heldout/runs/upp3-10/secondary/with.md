Nothing here is broken on the surface, so I'd leave the layout, colors, and type alone. The gap is in what happens around the button. I haven't seen the code, so these are findings, not diffs. Ranked by harm:

1. **Confirm gives no feedback and allows a double submit.** Tapping Confirm should disable the button and show a busy label within about 100 ms, such as "Booking…", with `aria-busy` on the card. A second tap must not send a second booking. Only navigate to the thank-you page after the API confirms success.

2. **Failure needs a path that keeps the screen.** If the call fails, stay on this page and show the failure in words beside the button: "We couldn't confirm your booking. Your details are still here. Try again." Keep the groomer, date, and time as they were, and make Retry the focused action. If the API gives a reason, show it. If it doesn't, don't invent one. Use a polite live region for the message, and move focus to it.

3. **The button label should name the action.** "Confirm" alone is vague. Use "Confirm booking" for the button and a different heading such as "Review your booking", or put the price in the label ("Confirm booking · $X"). Pick one; don't keep both as the same words.

4. **Make the summary card read like a receipt.** Use labels and values: "Groomer" with the name, "When" with a full date and time such as "Saturday, Oct 17 at 9:00 AM", and "Total" with the price. If the price includes tax or fees, say so next to it. Long groomer names should wrap, not clip. Keep the card's current styling.

5. **The Back link is vague.** "Back" doesn't say what you're going back to. "Edit booking" or "Change time or groomer" is clearer. It should also keep the person's selections.

6. **Set up the access basics.** The heading should be the page's `h1` and receive focus when the page loads. The Confirm button needs a real name, not just an icon. Keep focus visible on both controls.

7. **Replace the history entry on success.** Navigate to the thank-you page with replace, so Back doesn't return to a form that was already submitted. Pass the booking details to the thank-you page so it can show what was booked.

I didn't see any code, so I haven't changed anything and can't test it. I also didn't check how the API fails, what the price includes, or whether there is a cancellation policy to show. Those are facts only you can give me. If you share the component and the API call, I can apply items 1 and 2 first and keep the diff small.
