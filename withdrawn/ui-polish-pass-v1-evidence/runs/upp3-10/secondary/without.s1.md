I'd focus on three things: make the card read like a clear receipt, make the commitment explicit, and make the button and its states feel finished. I'm working from your description, not the code, so I haven't checked your components or design tokens.

**1. Make the summary a receipt the user can scan**
- Show the dog's name, service, groomer, and date/time as labeled rows with small icons. Right now the card is only a list of values.
- Format the time as a range ("Sat, Oct 18 · 10:00–11:30 AM") and add a relative cue like "in 3 days." Users check this line more than anything else.
- Show the groomer's photo or initial next to their name. A person feels more concrete than a text field.
- Split the price into service, add-ons, and fees, with a bold total underneath. A single price feels unfinished and makes people wonder what's included.

**2. State what happens when they tap**
- Add a line above the button such as "You'll pay $65 at your appointment" or "Payment is taken now." Users hesitate most when they don't know whether money moves.
- Put the cancellation policy right under the button in small text: "Free cancellation until 24h before." This reduces anxiety more than almost anything else on the screen.

**3. Make the button and its states specific**
- Label the button with the outcome, like "Book for $65" or "Confirm Sat 10:00 AM," not a generic "Confirm." Keep it full-width, and pin it to the bottom on mobile.
- On tap, disable it and show a spinner so people can't double-book. Keep the card visible during the request.
- Handle failure inline. If the slot was taken or the request failed, stay on the screen with a clear message and a retry, not a silent error. Use `aria-live` so screen readers announce it.
- Make the Back link an explicit "Edit booking" or "Change time" link that returns to the right step. Make sure its tap target is at least 44pt.

**Smaller polish**
- Rename the heading to "Review your booking" and add a short subline like "Almost done. Check the details below."
- Use brand color sparingly, for the total and button only, and add a small pet-friendly touch such as an icon or illustration at the top.
- On the thank-you page, carry over the booking reference and offer "Add to calendar."

If you share the component file, I can make these changes directly, starting with the summary card and button states. Tell me if you'd rather I stop at a written spec.
