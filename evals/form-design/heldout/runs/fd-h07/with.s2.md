Neither is fully right. I'd use the designer's approach as the base, with two exceptions for the developer's instinct.

**Default: validate on submit, then re-check live.**
- Don't show errors while someone is still typing. The first characters of a valid value aren't valid yet. "Enter an email with an @" appearing after the first letter is noise, and it feels like being scolded mid-sentence.
- Once a field has shown an error, re-check it on every keystroke. The message then disappears the moment the problem is fixed. This keeps most of what the developer wants, which is instant feedback, without the premature errors.
- Don't validate on blur. Autofill and tabbing away fire it mid-task.

**Two exceptions where live feedback is better than the designer's rule:**
1. **Password:** show the rule before they type ("At least [N] characters") and tick it off as it's met. It's guidance, not an error, so nothing red appears.
2. **Username uniqueness:** check after a short pause in typing (about 400–500 ms), not on every keystroke, and show "Checking…", then "Available" or "Taken, try another". This is the one check the person can't predict, so waiting until submit would send them back to redo work. It also avoids a server request per keystroke.

**Other details:**
- Keep the "Create account" button pressable at all times. A button that's disabled until the form is valid gives no reason and is often unreachable by keyboard. After a press with problems, put the message at each field and, if there are two or more, a summary at the top that links to each one.
- Run every check on the server too. The availability check can go stale between typing and submit.
- Keep what they typed after any error.
- Email: use `type="email"` and `autocomplete="email"`. Turn off autocapitalize and autocorrect on email and username. Password gets `autocomplete="new-password"`, allow paste, and add a show-password control.

**Settling the disagreement:** the developer is right that feedback should be immediate once it's useful (during a fix, for the password rule, for username availability). The designer is right that it shouldn't come before the person has had a chance to finish. If you want to test it, A/B the error timing on completion rate and time to submit.

I haven't seen your code, so this is based on the field list you gave. I left the minimum password length as [N] because you didn't say what it is.
