Neither is fully right. The best approach is a hybrid, and each field gets a different treatment.

**What I'd do**

- **Email:** Validate on blur (when the user leaves the field), not on each keystroke. Keystroke validation flags `jo` and `john@` as errors while the person is still typing, which is annoying and looks broken. Check the format on blur, then re-validate live once an error is showing so it clears the moment it's fixed.
- **Username (unique):** Check availability while typing, but debounce it by about 400–500ms and only after a minimum length. Uniqueness needs a server call, so firing on every keystroke wastes requests and makes the result flicker. Show a neutral "checking…" state, then a clear "taken" or "available." This is the one field where your developer's instinct is clearly right, because the feedback is useful before submit.
- **Password (min length):** Show a live hint like "8+ characters" that ticks off as they type. Don't style it as an error until they leave the field or try to submit. A progress-style hint is helpful. A red error after one character is hostile.
- **Submit:** Always validate everything again here. Client-side checks are a convenience, and the server must enforce all rules, including uniqueness, because the username can be taken between the check and the submit. On failure, focus the first invalid field and show a clear message.

**The general principle**

Validate late, correct early. Don't show an error before the user has had a chance to finish. Once a field has shown an error, update it live so they get instant confirmation of the fix.

**Where each person is right**

- **Developer:** Instant feedback is good, especially for username availability and the password requirement.
- **Designer:** Errors that appear mid-typing are noisy and discouraging, and submit-only validation is the safest baseline.

Submit-only has a real cost for this form. If someone finds out at submit that the username is taken, they have to guess new ones, and the form can feel like a guessing game. That's the strongest argument against the designer's position.

If you can only A/B test one thing, test the username check. It's the biggest friction point and the one where the two approaches differ most.
