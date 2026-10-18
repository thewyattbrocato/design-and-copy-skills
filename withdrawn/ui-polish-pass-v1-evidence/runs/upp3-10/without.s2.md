I'd make it feel like the last step of a commitment instead of a form. In priority order:

**1. Make the summary card say what's being booked**
- Lead with the dog: name, and a photo or breed icon if you have them. "Biscuit's grooming" is warmer than a bare "Confirm booking."
- Show the service (full groom, bath only) and the duration. The user is committing to something, and the card should list what.
- Give the groomer an avatar and rating, not just a name.
- Format the date for people: "Saturday, Oct 18 · 10:00–11:30 AM," not "2026-10-18 10:00." Add the location or an "Add to calendar" option if it's cheap.
- Make the price the visual anchor: larger, right-aligned, with a line-item breakdown if there are add-ons or taxes. Say whether payment happens now or at the salon, because that's the question people have at this step.

**2. Make the heading reassuring and specific**
- Something like "Almost done. Check the details" or "Ready to book Biscuit?" The heading shouldn't just repeat the button.
- Add a progress indicator ("Step 3 of 3") so the screen reads as the final step.

**3. Make the Confirm button earn its place**
- Pin it to the bottom of the screen on mobile, full width, with the price in the label: "Confirm · $65."
- Give it a loading state while the API call runs (spinner, disabled, "Booking…"). This matters most, because double-taps create duplicate bookings.
- Handle failure inline: keep the user on the screen, show a friendly error ("That slot was just taken. Pick another time"), and offer a retry. If slots can be taken by someone else, that case is likely and needs its own message.

**4. Demote and clarify Back**
- Keep it as a secondary action, but label it for what it does: "Change time" or "Edit details." A bare "Back" makes people wonder whether they'll lose their selections.
- Add a small line near the button about the cancellation policy ("Free cancellation up to 24 hours before"). It lowers the stakes of tapping Confirm.

**5. Add some brand and motion**
- Use Pawsworth's palette and rounded, friendly type. Give the card a soft shadow and a small paw or dog illustration so it doesn't look like a default template.
- On success, don't hard-cut to the thank-you page. Run a short button-to-checkmark animation first, then transition. That moment is the one most worth polishing.

**6. Accessibility and edge cases**
- Move focus to the heading on load, announce errors with `aria-live`, keep tap targets at least 44px, and check contrast on the price and secondary text.
- Decide what happens on refresh or direct navigation to this URL when no selection exists. Redirect back with a message rather than showing an empty card.

If you only have time for three things, do the loading and error states, the human-readable summary with dog name and service, and the success transition. Those change both how the screen feels and how reliably it works.

If you share the component code or your stack (React Native, web, SwiftUI), I can draft the changes.
