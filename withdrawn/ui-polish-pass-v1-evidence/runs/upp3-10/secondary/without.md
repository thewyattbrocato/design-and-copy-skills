I'd fix the summary and the button first, since that's where a confirm screen earns trust or loses it. I haven't seen your code, so these are design recommendations, not changes to the app.

**1. Make the summary a complete record.** Right now it shows only groomer, date/time, and price. Add:
- **Service and duration**, such as "Bath & haircut · about 90 min." Without it, the user can't tell what they're paying for.
- **Dog's name**, if you have it. Seeing "Biscuit" on the summary makes it feel like *their* booking.
- **Full date with weekday** ("Tue, Oct 20 · 10:00 AM"), not a numeric date.
- **Location**, if the groomer has more than one.
- **Groomer's photo or avatar** next to the name. It's a small change that makes the card feel less like a form.

**2. Turn the price into an itemized total.** Show the service line, any add-ons or fees, then a bold total with a divider above it. Use tabular numbers so the amounts align. Users look for surprises here, so the total should be the most prominent figure on the card.

**3. Make the button say what happens.** "Confirm booking" is generic. Try "Book for Tue 10:00 · $65" or "Confirm appointment." Then:
- Show a loading state and disable the button on tap so a double-tap can't create two bookings.
- If the API fails, show an inline error near the button with a retry option. Don't leave the user stranded.
- On mobile, pin the button to the bottom of the screen so it's always reachable.

**4. Give the policy its own line.** Put one short line above the button, such as the cancellation window, deposit, or vaccination requirement. Link to the full policy. For grooming this is where most support tickets come from, and it protects both you and the customer. Only include terms you actually enforce.

**5. Reconsider the Back link.** A bare "Back" makes users guess what they can change. Try a secondary button labeled "Change time" or "Edit booking," or small "Edit" links on each summary row. Keep the touch target at least 44pt.

**6. Warm up the heading and copy.** "Review your appointment" with a short subline like "Biscuit's spot with Maya is almost ready" feels more personal. Keep it short, and use the brand's voice.

**7. Smooth the handoff to the thank-you page.** Carry the booking details forward, and offer "Add to calendar" there. A confirm screen that ends on a useful next step feels finished.

**Smaller polish:**
- Use your brand color for the button and a subtle accent on the card, such as a top border or a paw icon.
- Use a 16px card radius with consistent padding, and let the spacing between sections do the grouping rather than extra borders.
- Set focus to the heading on load, and announce errors through an `aria-live` region so screen readers pick them up.

If you want, point me at the confirm component and the booking data shape, and I'll implement the summary card and button changes. I'd start with items 1 to 3, since they need the least new content.
