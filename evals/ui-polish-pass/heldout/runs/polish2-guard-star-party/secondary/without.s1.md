**Don't send it yet.** The biggest problem is that the page doesn't record sign-ups at all.

**Blocking**

1. **Nothing is saved.** The submit handler only changes the text on the page. No data goes to a server, spreadsheet, or email, so the club's chair and torch count would be based on nothing. Point the form at a backend (Google Forms, Formspree, a mailing-list tool, or your club's server) or swap in a Google Form link.
2. **The page has no event details.** It never says the date, start and end times, location, parking or entrance, what to bring, or who to contact. Add those above the form.
3. **The link needs to be hosted.** If you attach the HTML file, most people will see raw code or a download. Host it, or use one of the options above, and test the link on a phone.

**Bugs in the form**

4. **Blank names get through.** `novalidate` turns off the browser's `required` check, and the script never checks the name. An empty name shows "You are on the list: , party of 2." Add a check that trims the name and asks for it when it's empty.
5. **Fractional party sizes are accepted.** Entering 2.5 passes the check. Add `step="1"` to the number input and check that the value is a whole number.
6. **The confirmation is misleading.** "You are on the list" appears even though nothing was saved. This goes away once the form is connected to a real destination.

**Worth adding**

7. **A response deadline**, so you know the numbers before the day.
8. **Cancellation or weather info**, such as a rain date or where to check for updates. Also collect an email or phone number so you can reach people.
9. **A clearer error message.** "If your group is bigger, sign up in two parts" is awkward. Something like "For groups larger than 8, submit a second form for the rest of your party" is clearer. You could also raise the limit if the field's real purpose is headcount.
10. **Optional notes**, such as a field for arrival time or a request for a red-light torch.

The colors, dark mode, focus outlines, and live status message are fine.

Once you tell me where the responses should go (a form service, your own server, or an email address) and what the event details are, I can update the page to handle the name check, the whole-number check, the event info, and the saving.
