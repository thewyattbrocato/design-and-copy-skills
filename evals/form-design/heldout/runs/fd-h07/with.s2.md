Neither is fully right, but your designer is closer. I'd go with validate on submit, then re-check live once a field has shown an error. There are two exceptions.

**Why not every keystroke (the developer's approach):**
- The first characters of a valid value aren't valid yet. Someone typing `sam@` gets an "invalid email" error mid-thought. That's noise and it feels like scolding.
- Autofill and tabbing away also fire field-level checks while the person is still working.

**Why not submit-only (the designer's approach):**
- If errors only appear on submit and stay until the next submit, people fix a problem and don't know whether it worked. The fix is to re-check a field live once it has shown an error, so the message disappears the moment it's true.

**What I'd do per field:**

| Field | Behavior |
|---|---|
| **Email** | Check on submit only. If it fails, re-check as they edit. Message: "Enter an email address with an @, like name@example.com". |
| **Username (unique)** | This is the exception where live checking helps. Run an availability check after a short pause in typing (about 400–500 ms), not on every keystroke. Show "Checking…", then "Available" or "Taken. Try another." The server must still enforce uniqueness on submit, because someone else can claim the name in between. |
| **Password (min length)** | The other exception. Show the rule before they type ("At least [N] characters") and let it tick off as they meet it. That's a checklist, not an error. Also allow paste and add a show-password toggle. |

**Submit button:** keep it pressable the whole time. A button that's disabled until the form is valid gives no reason and is often unreachable by keyboard. If there are two or more problems after pressing it, put a summary at the top that links to each field. Keep everything the person typed, including after a server error.

So the developer gets live feedback where it actually helps (username, password), and the designer gets calm, error-free typing everywhere else. I haven't seen your form's code. If you want, point me at it and I can check it against this.
