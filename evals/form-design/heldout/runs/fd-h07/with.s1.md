Your designer is closer to right, but neither of them has it fully.

**Validate on submit, then re-check live.** Don't show errors while someone is still typing their first attempt. "j" and "jane@" aren't valid emails yet, so a keystroke validator shows people red errors for things they're still in the middle of doing. That's the main problem with your developer's approach. Submit-only has a different weakness. Once an error appears, the person needs to see it clear as soon as they fix it, so they aren't left guessing.

**What I'd do for each field**

- **Email:** Validate on submit. After an error has appeared, re-check as they edit so the message disappears the moment it's true. Use `type="email"` and `autocomplete="email"`, and turn off auto-capitalize and spellcheck.
- **Username (unique):** This is where your developer has a point. Uniqueness is something the person can't predict, so run the availability check after a short pause in typing (about 500 ms) rather than on every keystroke. Show "That username is taken. Try another." next to the field. Don't check until they've typed a plausible minimum. The server must check again on submit, because someone else can claim the name in between.
- **Password:** Show the minimum length as a hint above the field before they type, for example "At least [N] characters". Let it tick off as they meet it, so it works as a checklist and not as an error. Allow paste, add a show-password toggle, and use `autocomplete="new-password"`.
- **Submit button:** Keep it clickable at all times. A button that's disabled until the form is valid gives no reason and is hard to reach by keyboard. Label it "Create account", not "Submit". While the request is running, show progress and block double submits.
- **Errors after submit:** Put each message at its field, in words, with an icon or text cue as well as color, and say how to fix it. For example: "Enter an email address with an @, like name@example.com". With two or more problems, add a summary at the top that links to each field. Keep everything they typed.

Also avoid validating on blur. Autofill and tabbing away fire it mid-task, so it shows errors before the person is done.

The result gives your developer the instant feedback where it helps (username availability, the password checklist). It gives your designer a calm form that doesn't flag half-typed input.

I haven't seen your code, so tell me if you want me to implement this in the form.
