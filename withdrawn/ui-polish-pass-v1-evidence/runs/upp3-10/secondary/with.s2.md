The structure is sound: one summary, one primary action, a way back. What's missing is how it behaves while waiting and when it fails, and that's most of what makes it feel unfinished. I haven't seen the component code, so these are fixes to make in your code, ranked by harm.

1. **Give the Confirm tap immediate feedback.** Within about 100 ms, disable the button, change its label to "Confirming…" with a small spinner, and keep its width fixed so the layout doesn't jump. This stops double bookings and tells the person the tap registered. A silent request is the most common cause of "it feels broken."

2. **Handle failure on this screen.** If the API call fails, stay on the page, keep the summary as it is, and show a message beside the button in plain words, such as "We couldn't book this time. Check your connection and try again." Keep a Try again button. Don't use a toast that disappears, and don't use "Something went wrong." Move focus to the message and announce it to screen readers.

3. **Make the summary a labeled list.** Use a definition list or label/value rows: Groomer, Date, Time, Price. Format the date with the weekday (for example "Thu, Oct 22"), show the time as a range if you have an end time, and wrap long groomer names. Put the price in the largest type on the card, right-aligned with tabular figures, so it reads as the thing to check.

4. **Add a way to fix mistakes.** A small "Change" link beside the date/time and groomer rows lets people correct something without pressing Back and losing their place. If the app already keeps their selections, this costs little.

5. **Name the Back target.** "Back" is vague. "Back to choose a time" says where it goes. Keep it as a text link with a hit area of at least 44 px tall.

6. **Set expectations on the price.** If the total includes anything beyond the base price (tax, deposit, add-ons), show that as a line item. If there's a cancellation policy, put a link next to the button: "Cancellation policy: [link]". Use a placeholder until you have the real text. Don't invent terms.

7. **Make the thank-you transition clean.** Replace the confirm step in history so Back from the thank-you page doesn't re-submit the booking. Pass the booking details, including a reference number if the API returns one, so the next page can confirm specifics instead of a generic "Thanks!"

8. **Keep the look.** The palette, type, and spacing can stay. A groomer photo or an icon next to the groomer's name would add warmth, but it's optional and not a fix.

Not checked: I haven't run the app or tested with a screen reader, and I can't see the code. If you paste the component, I can make these changes directly.
