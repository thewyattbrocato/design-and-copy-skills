Here's what I'd change, most important first.

**1. Make the commitment obvious.** Confirm is the last point where someone can back out, so the screen should state exactly what they're agreeing to:
- Show the price as a total, with fees or tax broken out if there are any.
- Say when they pay: "Charged after your appointment" or "Charged now" would each be clear. Ambiguity here causes support tickets and chargebacks.
- Put a short cancellation line near the button, such as "Free cancellation until 24 hours before." It reduces hesitation more than any visual change.

**2. Turn the summary card into a booking, not a list.**
- Lead with the service and the dog: "Full groom for Biscuit." Using the pet's name and photo makes this feel like the user's booking rather than a form.
- Show the groomer with a photo and their name.
- Write the date and time in plain language: "Saturday, Oct 18 · 10:30 AM." Add duration and location if you have them.
- Give each row a small "Change" affordance, so the user can fix one field without hitting Back and losing everything.

**3. Make the button specific and handle its states.**
- Label it with the outcome: "Book for Sat 10:30 AM · $65" beats a generic "Confirm."
- Disable it while the request is in flight and show a spinner. This prevents double bookings from a second tap.
- On failure, keep the screen as it is and show an inline message such as "Couldn't reach us. Your details are saved. Try again." Don't navigate away or clear the form.

**4. Fix the heading and framing.**
- "Confirm booking" reads like a system step. Consider "Review your appointment," with a step indicator ("Step 3 of 3") above it so the user knows they're nearly done.
- Keep the heading as a real heading and move focus to it when the screen loads, for screen readers.

**5. Make Back a clear secondary action.**
- Label it "Edit details" rather than "Back" so it's clear what it returns to, and give it a 44pt tap target. A text link is fine if it's obviously tappable.

**6. Carry the momentum into the thank-you page.** Show the confirmation number, the summary again, and an "Add to calendar" action. A bare thank-you page is where the "unfinished" feeling tends to show up.

**Visual polish, last.** Give the card a clear surface and spacing, use one strong primary color for the button, and add one small brand touch like a paw mark or the groomer's avatar. Skip decorative illustrations; they usually make a checkout screen look less serious.

I don't see the component code in this working directory, so I haven't changed anything. If you paste the screen's component or point me to its file, I can make these changes directly, starting with the summary card, the button states, and the error path, since those affect behavior the most.
