**Why per-keystroke validation is discouraged**

- **It flags users before they've finished.** Typing `jo` into an email field triggers "Invalid email" even though they're mid-entry. The error is technically correct but useless, and it feels like being scolded for working normally.
- **It's noisy and distracting.** Messages flicker on and off as the input crosses valid and invalid states. This is especially bad for screen reader users, since live regions announce every change.
- **It adds anxiety and hurts completion.** Red text appearing immediately signals "you're doing it wrong" and can push people to abandon the form.
- **It can fire expensive or misleading checks.** A promo code lookup on every keystroke hammers your API and shows "invalid code" for every partial string.

**Better timing: validate on blur, then correct on input**

The widely recommended pattern is often called "reward early, punish late":

1. **Before first interaction:** show nothing.
2. **On blur (when the user leaves the field):** run validation and show the error. They've signaled they're done.
3. **After an error is showing:** re-validate on each keystroke, so the error clears the moment the value becomes valid. This gives instant positive feedback without making the user re-blur.
4. **On submit:** validate everything, show all errors, and move focus to the first invalid field with an error summary if the form is long.

**Applied to your three fields**

- **Email:** validate on blur. Check format only, and don't try to be clever with regexes. Show the error after blur, then clear it live as they fix it.
- **Password with rules:** this is the main exception. Show the rules up front as a checklist, and update each rule's status live as they type. That's guidance, not an error: it's neutral until they've failed something, and don't style unmet rules in red while the field is untouched or focused for the first time. Show a true error only on blur or submit if rules remain unmet.
- **Promo code:** don't validate while typing. Check on blur or when they click "Apply", ideally with a loading state. Treat it as optional: an empty field is never an error, and an invalid code shouldn't block registration unless you want it to.

**Other tips**

- Write specific messages ("Enter an email like name@example.com") rather than "Invalid input".
- Use `aria-invalid` and tie the message to the field with `aria-describedby`.
- Don't rely on color alone. Add text or an icon.
- Keep the submit button enabled so users can discover what's wrong, rather than leaving it disabled with no explanation.
