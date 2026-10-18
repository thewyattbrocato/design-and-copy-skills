I'd fix it in this order. Most of what makes it feel unfinished is missing states and vague copy, not styling.

**1. Handle the states the screen currently skips**
- **Loading:** disable the Confirm button and show a spinner or "Booking…" label while the request runs. Without this, people can tap twice and create duplicate bookings.
- **Error:** if the API fails, stay on this screen, show a specific inline message ("Couldn't reach Pawsworth. Your time slot is still held, try again"), and keep the details visible. Don't dump the user back to a generic page.
- **Slot taken:** if the time was booked by someone else in the meantime, say so and offer a way back to pick another time.

**2. Make the copy say what's happening**
- The heading and button both say "Confirm," which is redundant. Make the heading "Review your booking" and the button specific, like "Confirm for $65" or "Book Bella's bath." Naming the price on the button shows the user what they're agreeing to.
- Change "Back" to "Edit booking" or "Change time." It's clearer about what happens and reads as a deliberate action.

**3. Fix the summary card's hierarchy**
- Lay it out as labeled rows: Groomer (with photo if you have one), Date, Time, Service, and Total. Put the total last, bold and larger, with a divider above it.
- Add the dog's name and the service if you have them. Confirming "Bella · Full groom" reads as more finished than a list of logistics.
- Show the total with any fees or tax broken out, so the price doesn't change on the thank-you page.

**4. Add the trust details near the button**
- A line like "Free cancellation until 24 hours before" or "You'll be charged after the appointment" answers the question people have at this step. Put it just above the button, in small secondary text.
- Tell them what happens next: "You'll get a confirmation text."

**5. Make the visual layer deliberate**
- On mobile, pin the Confirm button to the bottom with a clear primary style. Keep the Edit link as a secondary action above it.
- Use your brand color for the primary button and the total, and keep everything else neutral. Use proper spacing and type sizes so the card doesn't look like a default form.
- Use a small icon or illustration for the groomer or the date. Don't overdo it.

**6. Accessibility basics**
- Make the heading the page's `h1`, and make the button at least 44px tall.
- Announce the loading and error states to screen readers (`aria-live` or `role="alert"` for errors), and move focus to the error message when it appears.

**7. Connect it to the thank-you page**
- The thank-you page should repeat the booking details (groomer, date, time, total) and give a next step, such as adding to calendar or viewing the booking. A plain "Thanks" page makes the flow feel like it ends abruptly.

If you can share the component file and the thank-you page, I can make these changes directly. Tell me your stack (React, SwiftUI, plain HTML, etc.) and whether the API returns a price breakdown and a service name, since those decide what the card can show.
