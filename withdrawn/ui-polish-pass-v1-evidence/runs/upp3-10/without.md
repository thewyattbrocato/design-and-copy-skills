Here's what I'd do, roughly in priority order. The first three changes matter most.

**1. Make the summary card feel like the booking, not a form readout**
- Put the groomer first: avatar or photo, name, and a small rating or "Your groomer" label.
- Give the date and time real visual weight. Use "Saturday, Oct 18 · 10:30 AM" as the card's main line, with small calendar and clock icons, not three plain label/value rows.
- Show the dog if you have it (name, breed, service). "Biscuit's full groom" is much warmer than a bare price.
- Break the price into service and total, even if there's only one line. Put the total in the card's footer, set off by a divider.

**2. Reassure the user at the moment of commitment**
- Add one line near the button about what happens next and what it costs. Examples: "You won't be charged until your appointment" or "Free cancellation up to 24 hours before." This is the biggest trust gain for the least work.
- Change the heading from "Confirm booking" to something with a bit of voice, like "Almost done, does this look right?". Keep the button label specific, such as "Confirm booking · $65" or "Book Biscuit's groom".

**3. Handle the Confirm tap properly**
- Disable the button on tap and show a spinner with "Booking…". This prevents double submits, which matter here because they'd create duplicate appointments.
- Show an inline error with a retry if the API fails or the slot was just taken. In the slot-taken case, link back to time selection.
- Move focus and announce errors for screen readers.

**4. Polish and brand**
- Use your brand color for the primary button: full width, rounded, and pinned to the bottom of the viewport on mobile so it's always reachable.
- Make Back a clear secondary action with a chevron ("‹ Change time"). The label should say what it does.
- Use a consistent spacing scale and soft card elevation, and keep the card's radius in line with the button's.
- Add a small paw or grooming illustration near the top. Keep it modest so it doesn't push the card down.

**5. Small touches**
- Fade or slide the card in on load.
- Run a short success animation, like a checkmark or paw, before navigating to the thank-you page. Keep it to about 600ms.
- Add an "Edit" affordance on individual rows (time, groomer) so Back isn't the only way to fix a mistake.

If you share the component file (or tell me the stack: React Native, web, SwiftUI, etc.), I can implement these. I'd start with the card hierarchy, the reassurance line, and the loading and error states, since those change how the screen feels and behaves the most.
