**Don't send it yet.** The biggest problem is that the form doesn't save anything.

**Blocking**

1. **Sign-ups go nowhere.** The form has no `action` and the script only updates the page text. Anyone who clicks "Save my place" sees "You are on the list," but nothing is recorded and no one on the committee gets notified. Connect it to something before sending: a form service such as Google Forms, Formspree, or Tally, or a small backend. Then test it with a real submission.
2. **The page doesn't say what the event is.** It has no date, start and end times, location, parking or access directions, or cost. "Saturday" is ambiguous, especially since it's currently early November. Put the exact date and location on the page.

**Should fix**

3. **Empty name gets through.** `required` alone doesn't stop submission here because `novalidate` is set and the script never checks the name. An empty name produces "You are on the list: , party of 2." Add a name error like the one for the party size.
4. **No contact details.** If the club needs to reach people about a cancellation or a change, the form has no email or phone field.
5. **No cancellation or weather policy.** Star parties are often called off for clouds. Say how people will be told and whether the event is rescheduled.
6. **No deadline, and no way to change or cancel a sign-up.** Say when sign-ups close and how to update one.
7. **The "two parts" advice has no mechanism.** The error tells groups over 8 to sign up in two parts. If that's allowed, the organizer needs a way to link them, or the message should just say "email the organizer if your group is larger than 8."

**Minor**

8. **No fallback without JavaScript.** Without it the form does nothing useful. A plain `action` pointing at your form service covers this.
9. **Error text isn't announced.** The party-size error appears without an announcement. Focus moves to the field and the error is linked to it, which mostly covers this, but an `aria-live` region would be more reliable.

The visual design is fine. Focus rings, dark mode, reduced-motion handling, and color contrast all look correct.

I can fix items 3, 8, and 9 in the HTML now, and add placeholders for the date, location, and policy text. Items 1 and 2 need your input: which form service or backend you're using, and the event details.
