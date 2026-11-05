**Don't send it yet.** The biggest problem is that sign-ups go nowhere.

**Blocking**

1. **Nothing is saved.** The form has no `action` and the script only updates the page. Anyone who clicks "Save my place" sees "You are on the list," but the organizer receives nothing. Connect it to something that stores responses, such as a Google Form, Formspree, or a spreadsheet-backed endpoint, or change the button to a mailto link.
2. **The confirmation message is misleading.** Because nothing is stored, "You are on the list" is false. It should match whatever the backend actually does.
3. **No event details.** The page never says which Saturday, the start time, the location, what to bring, or the deadline to sign up. Add them above the form. Since it's currently November 4, 2026, the next Saturday is November 7, so make sure the date is explicit.
4. **No way to reach people.** Only a name is collected. Add an email or phone number so you can send weather cancellations or changes.

**Should fix**

5. **Empty name passes validation.** `required` is ignored because of `novalidate`, and the script never checks the name. Submitting a blank name produces "You are on the list: , party of 2."
6. **Fractional party sizes are accepted.** `2.5` passes the `1–8` check. Use `Number.isInteger(v)`, or `step="1"` plus a check.
7. **Errors may not be announced.** The error paragraph is toggled with `hidden` but has no `role="alert"` or live region, so screen-reader users may miss it. Add `role="alert"` to `#n-err`, or put it in the live region.
8. **The error text is confusing.** "Sign up in two parts" won't make sense to most people, and it invites duplicate entries. Say something like "For a larger group, email [contact]."
9. **Confirm the 8-person cap.** It may be right, but check that it's what the club intends.
10. **No protection against double submits.** Disable the button while sending, or clear the form after success so people don't submit twice.

**Minor**

11. **Set expectations for changes.** Tell people how to cancel or change their count, since the form doesn't allow it.
12. **Add a meta description** if the link might be shared outside email.

What already works: the labels, the hint text, the dark-mode colors, the focus outline, and the reduced-motion handling are fine.

If you tell me where responses should go (a form service, a spreadsheet, or your email), I can wire it up and add the event details and the fixes above.
