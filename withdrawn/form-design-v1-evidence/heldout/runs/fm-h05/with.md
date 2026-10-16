**Why per-keystroke validation is discouraged**

- **The first characters of a valid value aren't valid yet.** Someone typing `sam@exa` gets "Enter a valid email" while they're still mid-entry. The error is wrong in context and it's noise. It also makes people feel scolded for something they haven't finished doing.
- **Messages flicker.** An error appears, disappears and reappears as the person types. That's distracting, and screen readers may announce each change.
- **It adds friction.** Red text early makes the form feel hard and can push people to abandon it.

**Better timing: validate on submit, then re-check live**

1. **Show no errors while the first attempt is in progress.**
2. **Check on submit.** Keep the button pressable, and don't disable it until the form is valid. A disabled button gives no reason and is often unreachable by keyboard. Put each message next to its field. If two or more fields fail, also add a summary at the top. The summary links to each field, takes focus, and puts the error count in the page title.
3. **After a field has shown an error, re-check it as the person edits.** The message disappears the moment the value becomes valid.
4. **Be wary of validating on blur.** Autofill and switching windows can trigger blur at odd moments.

**Applying this to your three fields**

- **Email:** validate on submit only. Use `type="email"` and `autocomplete="email"`, and turn off autocapitalize and spellcheck. A message like "Enter an email address with an @, like name@example.com" says how to fix it.
- **Password with rules:** this is the main exception. Show the rules *before* typing, as a checklist that ticks off each rule as it's met. That's guidance rather than an error. Allow paste, add a show-password control, and use `autocomplete="new-password"`. Still run the full check on submit.
- **Promo code:** it's optional, so mark it "optional" in the label. Don't check it while typing. Check it on submit, or through an explicit "Apply" button that shows a result like "That code has expired" or "Code applied". If you validate it asynchronously, wait for a pause in typing before you check.

Run the same checks on the server, and keep everything the person typed if the server rejects the form.
