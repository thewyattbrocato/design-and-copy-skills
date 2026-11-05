**Neither is fully right, but your designer is closer.** I'd validate on submit by default, then re-check live once a field has shown an error. Two fields get exceptions.

**Why per-keystroke validation fails:** The first characters of a valid value aren't valid yet. Someone typing `jo` on the way to `jo@example.com` gets an error for doing nothing wrong. That's noise, and it makes the form feel like it's scolding them.

**Why submit-only falls short:** If errors only appear on submit, a person who fixes a mistake still sees the old error until they press the button again. Live re-checking after the first error fixes that.

**What I'd do, field by field:**

- **Email:** Check on submit. If it fails, re-check as they edit so the message clears as soon as it's true. Use `type="email"`, `autocomplete="email"`, and turn off autocapitalize and autocorrect.
- **Password:** Show the rule before they type ("At least [N] characters"). Tick it off live as they meet it. This is the one place where per-keystroke feedback helps, because it's a checklist and not an error. Allow paste and add a show-password control.
- **Username (unique):** Check availability after a short pause once they stop typing, not on every keystroke. Show "Checking…", then "Available" or "Taken". Also check on the server at submit, because the live check can go stale.
- **Submit button:** Keep it pressable at all times, with a label like "Create account". A button that's disabled until the form is valid gives no reason and is hard to reach by keyboard.
- **After a failed submit:** Put the message next to each field, in words, with an icon or text cue as well as color. For example: "Enter an email address with an @, like name@example.com". With two or more errors, add a summary at the top that links to each field. Keep everything the person typed.

**For the developer:** Their goal of fast feedback is right. It belongs on the password checklist and the username availability check, where the person benefits from it as they type.

**For the designer:** Pure submit-only leaves stale errors on screen. Live re-checking after the first error fixes that.

Whichever way you go, the server has to run the same checks again.
