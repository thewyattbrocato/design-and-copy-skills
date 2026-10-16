Neither extreme is right. I'd validate on blur (when the user leaves a field), and for a few fields add live feedback while typing.

**Why per-keystroke fails**
- Showing "invalid email" after the first character is hostile. The user hasn't had a chance to finish.
- A uniqueness check on every keystroke fires a server request per character. That's wasteful, it flickers, and responses can arrive out of order and show a stale result.

**Why submit-only fails**
- The user fills three fields, hits submit, and learns the username is taken. Uniqueness is the error they're most likely to hit, and they can't predict it.
- Errors far from where the user was looking are harder to fix.

**What I'd do, field by field**
- **Email:** Validate on blur, with a loose format check only (something like `@` and a dot). Real verification happens via confirmation email. Once an error is showing, clear it as soon as the input becomes valid.
- **Username:** Run the uniqueness check debounced, about 400–500 ms after typing stops. Also enforce a minimum length before you query. Show a small "checking…" state, and ignore responses for stale input. Always re-check on the server at submit, because the name can be taken between the check and the submit.
- **Password:** This is the one place live feedback helps. Show the requirement ("8+ characters") as a hint from the start and tick it off as the user types. Don't show it as an error. Add a show/hide toggle.
- **Submit:** Validate everything again. Focus the first invalid field and show an inline message next to it. Server-side validation is the real authority either way. Client-side checks are only for convenience.

**The rule behind it**
Don't show an error for a field until the user has left it once ("touched"). After that, re-validate as they type so the error disappears the moment they fix it. This is sometimes called "reward early, punish late." It gives your developer the instant feedback they want without scolding people mid-word. It also gives your designer the calm form they want, with no errors flashing while someone is still typing.

If you have to pick one of the two positions as stated, the designer's is closer to right for most fields. The developer is right about the username and password, where early feedback saves a failed submit.

I'm assuming a standard web form. If this is a mobile app, the same approach applies, but the keyboard covering the form makes blur-time errors a bit more important.
