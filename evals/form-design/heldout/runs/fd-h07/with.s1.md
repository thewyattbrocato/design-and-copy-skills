Neither of you is fully right. The designer is closer, but the form needs a hybrid. Here's what I'd do.

**Default: validate on submit, then re-check live.** After a field has shown an error, re-check it as the person types, so the message disappears the moment it's fixed. This takes the best part of your developer's idea and drops the worst. Keystroke validation shows errors while someone is still typing a valid value. "j" isn't a valid email yet, and flashing red at it is noise.

**Three exceptions, one per field:**

- **Password:** show the minimum length before they start typing, for example "At least [N] characters" under the label. You can tick it off as they type. It's a hint, not an error, so nothing turns red mid-typing. I've left the length as [N] because you didn't give it.
- **Username uniqueness:** check after a short pause once they stop typing, not on every keystroke. Only the server can answer this question, and finding out "taken" before submitting saves a round trip. Show a neutral "Checking…" state, then "Taken" or "Available". Check again on the server at submit, because two people can claim the same name in between.
- **Email:** submit only, then live re-check after an error. There's nothing useful to say before they finish.

**Other things I'd do:**

- **Keep the button pressable.** Don't disable it until the form is valid. A grayed-out button gives no reason and is often unreachable by keyboard. Show a progress state and block double-submits while the request is in flight.
- **Write fix-it messages at the field.** "Enter an email address with an @, like name@example.com" works. "Invalid email" doesn't. Use an icon or text cue as well as red. If two or more fields fail, add a summary at the top that links to each one.
- **Keep what they typed** if the server rejects the form.
- **Use the right input attributes:**
  - Email: `type=email` and `autocomplete=email`.
  - Username: autocapitalize, autocorrect and spellcheck off.
  - Password: `autocomplete=new-password`, paste allowed, and a show-password toggle.
- **Server-side checks:** run all the same checks there too.

The developer is right that people shouldn't have to wait until submit to learn a username is taken, which is why that field gets live checking. The designer is right about everything else.
