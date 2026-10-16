Neither is fully right. The best approach is a hybrid, and it differs by field.

**Why each side falls short**

- **Validating every keystroke** is hostile. Someone typing "jane@" gets an "invalid email" error before they've had a chance to finish. For the unique username it's worse, because you'd fire a server request on every character. That causes rate-limit problems, flickering results, and race conditions where a slow response for "jan" overwrites the result for "jane".
- **Validating only on submit** means a person fills out everything, hits the button, and then finds out "username taken" and "password too short". That's the most frustrating time to learn it, especially for the username, since they may go through several guesses.

**What I'd do**

1. **Validate on blur** (when the user leaves the field) for email format and password length. The user has finished typing, so the error isn't premature.
2. **Check username uniqueness on blur, or after a debounce of about 400–500ms** once the username meets the basic format rules. Cancel stale requests so old responses can't overwrite new ones. Still treat the server as the final authority on submit, because someone else can claim the name in between.
3. **After a field has shown an error, re-validate on every keystroke** so the error clears as soon as the input is fixed. That gives the developer's instant feedback where it actually helps.
4. **For the password, show the requirement up front** ("At least 8 characters") as helper text. A live checklist or strength hint that updates as they type is fine, since it's guidance rather than an error.
5. **Still validate everything on submit**, and move focus to the first invalid field. This is the safety net, and it's needed for server-side validation anyway.
6. **Make the errors specific and polite.** "Use at least 8 characters" works better than "Invalid password".

**The short version:** the designer is right that you shouldn't nag people mid-typing. The developer is right that people shouldn't have to wait until submit to learn about problems. "Validate on blur, then live-correct once an error has appeared" gives you both.

If you tell me your stack (React, plain HTML, and so on), I can sketch how to implement it.
